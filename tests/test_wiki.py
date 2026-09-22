import json
import os
import sys
import tempfile
import unittest
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lint_wiki import lint
from tools.wiki_core import extract_wikilinks, parse_frontmatter


class WikiCoreTests(unittest.TestCase):
    def _write_backlink_concept(self, root, where_appears, aulas="[1]", updated="2026-09-21"):
        concept_dir = root / "conceitos" / "teste"
        concept_dir.mkdir(parents=True, exist_ok=True)
        (root / "conceitos" / "index.md").write_text("# Índice\n", encoding="utf-8")
        concept = (
            "---\n"
            "conceito: Primeiro\n"
            "slug: primeiro\n"
            "disciplina: teste\n"
            "tipo: conceito\n"
            "aka: []\n"
            "status: vivo\n"
            "fontes: [https://example.com/fonte]\n"
            f"aulas: {aulas}\n"
            f"atualizado_em: {updated}\n"
            "---\n\n"
            "Definição.\n\n"
            "## Em uma frase\n\n"
            "Frase.\n\n"
            "## O que precisa saber\n\n"
            "Conteúdo.\n\n"
            "## Erros comuns\n\n"
            "Nenhum.\n\n"
            "## Onde aparece\n\n"
            f"{where_appears}\n\n"
            "## Fontes\n\n"
            "Fonte externa.\n"
        )
        (concept_dir / "primeiro.md").write_text(concept, encoding="utf-8")

    def _write_backlink_lesson(self, root, track, folder, order, body):
        lesson_dir = root / "aulas" / "teste" / track / folder
        lesson_dir.mkdir(parents=True, exist_ok=True)
        lesson = (
            "---\n"
            f"titulo: {folder}\n"
            "disciplina: teste\n"
            f"trilha: {track}\n"
            f"ordem: {order}\n"
            f"slug: {folder[3:]}\n"
            "status: aprovada\n"
            "versao: 1\n"
            "atualizado_em: 2026-09-21\n"
            "---\n\n"
            f"{body}\n"
        )
        lesson_path = lesson_dir / "canonica.md"
        lesson_path.write_text(lesson, encoding="utf-8")
        return lesson_path.relative_to(root).as_posix()

    def test_frontmatter_lists_and_accented_values(self):
        text = "---\nconceito: Relação\nslug: relacao\ndisciplina: teste\ntipo: conceito\naka: [relação, relationship]\nstatus: vivo\nfontes:\n  - lake/teste/fonte com espaço.pdf\naulas: [1, 12]\natualizado_em: 2026-09-21\n---\n\nDefinição.\n"
        frontmatter = parse_frontmatter(text)
        self.assertEqual(frontmatter.errors, [])
        self.assertEqual(frontmatter.data["aka"], ["relação", "relationship"])
        self.assertEqual(frontmatter.data["aulas"], [1, 12])
        self.assertEqual(frontmatter.data["fontes"], ["lake/teste/fonte com espaço.pdf"])

    def test_wikilinks_ignore_fenced_code_and_keep_labels(self):
        lines = [
            "Texto [[conceito|rótulo]] e [[outro#secao]].",
            "```markdown",
            "Exemplo [[nao-e-link]].",
            "```",
        ]
        self.assertEqual(list(extract_wikilinks(lines, 10)), [("conceito", 10), ("outro", 10)])

    def test_clean_fixture_has_no_lint_findings(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            concept_dir = root / "conceitos" / "teste"
            lesson_dir = root / "aulas" / "teste" / "trilha" / "01-primeira"
            concept_dir.mkdir(parents=True)
            lesson_dir.mkdir(parents=True)
            concept = "---\nconceito: Primeiro\nslug: primeiro\ndisciplina: teste\ntipo: conceito\naka: []\nstatus: vivo\nfontes:\n  - https://example.com/fonte\naulas: [1]\natualizado_em: 2026-09-21\n---\n\nUma definição própria.\n\n## Em uma frase\n\nUma frase.\n\n## O que precisa saber\n\nO conteúdo.\n\n## Erros comuns\n\nNenhum.\n\n## Onde aparece\n\n`aulas/teste/trilha/01-primeira/canonica.md`\n\n## Fontes\n\nFonte externa.\n"
            (concept_dir / "primeiro.md").write_text(concept, encoding="utf-8")
            (root / "conceitos" / "index.md").write_text("# Índice\n", encoding="utf-8")
            lesson = "---\ntitulo: Primeira\ndisciplina: teste\ntrilha: trilha\nordem: 1\nslug: primeira\nstatus: aprovada\nversao: 1\natualizado_em: 2026-09-21\n---\n\nAula sobre [[primeiro]].\n"
            (lesson_dir / "canonica.md").write_text(lesson, encoding="utf-8")
            self.assertEqual(lint(root), [])

    def test_future_concept_date_reports_warning_without_crashing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            tomorrow = dt.date.today() + dt.timedelta(days=1)
            self._write_backlink_concept(root, "Ainda não aparece.", aulas="[]", updated=tomorrow.isoformat())

            diagnostics = lint(root)

            future_dates = [item for item in diagnostics if item.code == "future-date"]
            self.assertEqual(len(future_dates), 1)
            self.assertEqual(future_dates[0].severity, "warning")
            self.assertIn("atualizado_em está no futuro", future_dates[0].message)

    def test_duplicate_orders_in_distinct_tracks_are_ambiguous_without_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._write_backlink_concept(root, "Aula 1.")
            first = self._write_backlink_lesson(
                root, "trilha-a", "01-primeira", 1, "Conteúdo sobre [[primeiro]]."
            )
            self._write_backlink_lesson(
                root, "trilha-b", "01-segunda", 1, "Conteúdo de outra trilha."
            )

            diagnostics = lint(root)

            ambiguous = [
                item
                for item in diagnostics
                if item.code == "backlink-ambiguous" and item.path == first
            ]
            self.assertEqual(len(ambiguous), 1)
            self.assertIn("2 canônicas", ambiguous[0].message)

    def test_unique_order_without_path_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            lesson = self._write_backlink_lesson(
                root, "trilha", "01-primeira", 1, "Conteúdo sobre [[primeiro]]."
            )
            self._write_backlink_concept(root, "Aula 1.")

            diagnostics = lint(root)

            missing = [
                item
                for item in diagnostics
                if item.code == "backlink-missing" and item.path == lesson
            ]
            self.assertEqual(len(missing), 1)
            self.assertIn("caminho exato", missing[0].message)
            self.assertIn(lesson, missing[0].message)

    def test_path_qualified_backlink_resolves_duplicate_orders(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = self._write_backlink_lesson(
                root, "trilha-a", "01-primeira", 1, "Conteúdo sobre [[primeiro]]."
            )
            self._write_backlink_lesson(
                root, "trilha-b", "01-segunda", 1, "Conteúdo de outra trilha."
            )
            self._write_backlink_concept(root, f"`{first}`")

            diagnostics = lint(root)

            backlink_findings = [
                item
                for item in diagnostics
                if item.code.startswith("backlink-")
            ]
            self.assertEqual(backlink_findings, [])

    def test_missing_path_in_where_appears_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._write_backlink_concept(
                root,
                "`aulas/teste/trilha/01-inexistente/canonica.md`",
            )
            self._write_backlink_lesson(
                root, "trilha", "01-primeira", 1, "Conteúdo sobre [[primeiro]]."
            )

            diagnostics = lint(root)

            missing = [item for item in diagnostics if item.code == "backlink-path-missing"]
            self.assertEqual(len(missing), 1)
            self.assertEqual(
                missing[0].target,
                "aulas/teste/trilha/01-inexistente/canonica.md",
            )

    def test_invalid_path_in_where_appears_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._write_backlink_concept(root, "`aulas/teste/trilha/canonica.md`")
            self._write_backlink_lesson(
                root, "trilha", "01-primeira", 1, "Conteúdo sobre [[primeiro]]."
            )

            diagnostics = lint(root)

            invalid = [item for item in diagnostics if item.code == "backlink-path-invalid"]
            self.assertEqual(len(invalid), 1)
            self.assertEqual(invalid[0].target, "aulas/teste/trilha/canonica.md")

    def _write_missing_source_fixture(self, root, cache_text):
        source = "lake/desenvolvimento-full-stack-e-cloud-computing/modulo/fonte.pdf"
        concept_dir = root / "conceitos" / "teste"
        graphify_dir = (
            root
            / "lake"
            / "desenvolvimento-full-stack-e-cloud-computing"
            / "graphify-out"
        )
        concept_dir.mkdir(parents=True)
        (graphify_dir / "txtcache").mkdir(parents=True)
        concept = "\n".join(
            [
                "---",
                "conceito: Fonte ausente",
                "slug: fonte-ausente",
                "disciplina: teste",
                "tipo: conceito",
                "aka: []",
                "status: vivo",
                "fontes:",
                f"  - {source}",
                "aulas: []",
                "atualizado_em: 2026-09-21",
                "---",
                "",
                "Uma definição própria.",
                "",
                "## Em uma frase",
                "",
                "Uma frase.",
                "",
                "## O que precisa saber",
                "",
                "O conteúdo.",
                "",
                "## Erros comuns",
                "",
                "Nenhum.",
                "",
                "## Onde aparece",
                "",
                "Ainda não aparece.",
                "",
                "## Fontes",
                "",
                "Fonte derivada para teste.",
                "",
            ]
        )
        (concept_dir / "fonte-ausente.md").write_text(concept, encoding="utf-8")
        (root / "conceitos" / "index.md").write_text("# Índice\n", encoding="utf-8")
        cache_name = "fixture.txt"
        (graphify_dir / "txtcache" / cache_name).write_text(cache_text, encoding="utf-8")
        mapping = [
            {
                "pdf": r"C:\PROJETOS\PROF-TONI\lake\desenvolvimento-full-stack-e-cloud-computing\modulo\fonte.pdf",
                "txt": rf"C:\PROJETOS\PROF-TONI\lake\desenvolvimento-full-stack-e-cloud-computing\graphify-out\txtcache\{cache_name}",
                "chars": len(cache_text),
            }
        ]
        (graphify_dir / ".full_mapping.json").write_text(
            json.dumps(mapping), encoding="utf-8"
        )

    def test_missing_source_with_valid_graphify_cache_keeps_source_missing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._write_missing_source_fixture(root, "texto extraído do Graphify\n")
            diagnostics = lint(root)
            source_missing = [item for item in diagnostics if item.code == "source-missing"]
            cache_hits = [item for item in diagnostics if item.code == "source-cache-hit"]
            self.assertEqual(len(source_missing), 1)
            self.assertEqual(len(cache_hits), 1)
            self.assertEqual(source_missing[0].severity, "warning")
            self.assertEqual(cache_hits[0].severity, "info")

    def test_missing_source_with_empty_graphify_cache_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._write_missing_source_fixture(root, "  \n")
            diagnostics = lint(root)
            source_missing = [item for item in diagnostics if item.code == "source-missing"]
            cache_empty = [item for item in diagnostics if item.code == "source-cache-empty"]
            self.assertEqual(len(source_missing), 1)
            self.assertEqual(len(cache_empty), 1)
            self.assertEqual(cache_empty[0].severity, "info")

    def test_source_newer_than_concept_is_reported_stale(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            concept_dir = root / "conceitos" / "teste"
            lake_dir = root / "lake" / "teste"
            concept_dir.mkdir(parents=True)
            lake_dir.mkdir(parents=True)
            (root / "conceitos" / "index.md").write_text("# Índice\n", encoding="utf-8")
            (lake_dir / "fonte.md").write_text("Fonte alterada.\n", encoding="utf-8")
            concept = "---\nconceito: Fonte\nslug: fonte\ndisciplina: teste\ntipo: conceito\naka: []\nstatus: vivo\nfontes:\n  - lake/teste/fonte.md\naulas: []\natualizado_em: 2000-01-01\n---\n\nDefinição.\n\n## Em uma frase\n\nFrase.\n\n## O que precisa saber\n\nConteúdo.\n\n## Erros comuns\n\nNenhum.\n\n## Onde aparece\n\nAinda não aparece.\n\n## Fontes\n\nFonte local.\n"
            (concept_dir / "fonte.md").write_text(concept, encoding="utf-8")

            diagnostics = lint(root)
            stale = [item for item in diagnostics if item.code == "stale"]
            self.assertEqual(len(stale), 1)
            self.assertEqual(stale[0].target, "lake/teste/fonte.md")

    def test_sources_same_day_or_older_than_concept_are_not_stale(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            concept_dir = root / "conceitos" / "teste"
            lake_dir = root / "lake" / "teste"
            concept_dir.mkdir(parents=True)
            lake_dir.mkdir(parents=True)
            (root / "conceitos" / "index.md").write_text("# Índice\n", encoding="utf-8")

            concept_date = dt.date(2020, 1, 10)
            source_dates = {
                lake_dir / "mesma-data.md": concept_date,
                lake_dir / "data-anterior.md": concept_date - dt.timedelta(days=1),
            }
            for source_path, source_date in source_dates.items():
                source_path.write_text("Fonte de teste.\n", encoding="utf-8")
                timestamp = dt.datetime.combine(source_date, dt.time(12, 0)).timestamp()
                os.utime(source_path, (timestamp, timestamp))
                self.assertEqual(
                    dt.date.fromtimestamp(source_path.stat().st_mtime), source_date
                )

            concept = (
                "---\n"
                "conceito: Fontes com datas não posteriores\n"
                "slug: fontes-nao-posteriores\n"
                "disciplina: teste\n"
                "tipo: conceito\n"
                "aka: []\n"
                "status: vivo\n"
                "fontes:\n"
                "  - lake/teste/mesma-data.md\n"
                "  - lake/teste/data-anterior.md\n"
                "aulas: []\n"
                f"atualizado_em: {concept_date.isoformat()}\n"
                "---\n\n"
                "Definição.\n\n"
                "## Em uma frase\n\n"
                "Frase.\n\n"
                "## O que precisa saber\n\n"
                "Conteúdo.\n\n"
                "## Erros comuns\n\n"
                "Nenhum.\n\n"
                "## Onde aparece\n\n"
                "Ainda não aparece.\n\n"
                "## Fontes\n\n"
                "Fontes locais de teste.\n"
            )
            (concept_dir / "fontes-nao-posteriores.md").write_text(
                concept, encoding="utf-8"
            )

            diagnostics = lint(root)

            stale = [item for item in diagnostics if item.code == "stale"]
            self.assertEqual(stale, [])

    def test_concept_listing_order_without_lesson_backlink_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            concept_dir = root / "conceitos" / "teste"
            lesson_dir = root / "aulas" / "teste" / "trilha" / "02-primeira"
            concept_dir.mkdir(parents=True)
            lesson_dir.mkdir(parents=True)
            (root / "conceitos" / "index.md").write_text("# Índice\n", encoding="utf-8")
            concept = "---\nconceito: Primeiro\nslug: primeiro\ndisciplina: teste\ntipo: conceito\naka: []\nstatus: vivo\nfontes: [https://example.com/fonte]\naulas: [2]\natualizado_em: 2026-09-21\n---\n\nDefinição.\n\n## Em uma frase\n\nFrase.\n\n## O que precisa saber\n\nConteúdo.\n\n## Erros comuns\n\nNenhum.\n\n## Onde aparece\n\nAula 2.\n\n## Fontes\n\nFonte externa.\n"
            (concept_dir / "primeiro.md").write_text(concept, encoding="utf-8")
            lesson = "---\ntitulo: Segunda\ndisciplina: teste\ntrilha: trilha\nordem: 2\nslug: segunda\nstatus: aprovada\nversao: 1\natualizado_em: 2026-09-21\n---\n\nAula sem conceito vinculado.\n"
            (lesson_dir / "canonica.md").write_text(lesson, encoding="utf-8")

            diagnostics = lint(root)
            backlinks = [
                item
                for item in diagnostics
                if item.code == "backlink-missing" and item.path == "conceitos/teste/primeiro.md"
            ]
            self.assertEqual(len(backlinks), 1)
            self.assertIn("nenhuma aula aprovada", backlinks[0].message)


if __name__ == "__main__":
    unittest.main()
