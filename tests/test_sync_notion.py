import contextlib
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import sync_notion


class SyncNotionCliTests(unittest.TestCase):
    def _patch_plan(self):
        return (
            patch.object(sync_notion, "coletar_aulas", return_value=([], [])),
            patch.object(sync_notion, "planejar", return_value=([], [], [], [])),
        )

    def test_unknown_option_fails_before_any_api_call(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with patch.object(sync_notion, "consultar_base", side_effect=AssertionError):
                with self.assertRaises(SystemExit) as raised:
                    sync_notion.main(["--typo"])
        self.assertEqual(raised.exception.code, 2)

    def test_help_is_read_only(self):
        with contextlib.redirect_stdout(io.StringIO()):
            with patch.object(sync_notion, "consultar_base", side_effect=AssertionError):
                with self.assertRaises(SystemExit) as raised:
                    sync_notion.main(["--help"])
        self.assertEqual(raised.exception.code, 0)

    def test_default_plan_never_applies(self):
        coleta, plano = self._patch_plan()
        with coleta, plano, patch.object(sync_notion, "aplicar") as aplicar:
            with contextlib.redirect_stdout(io.StringIO()) as output:
                result = sync_notion.main([])

        self.assertEqual(result, 0)
        aplicar.assert_not_called()
        self.assertIn("[plan] nada foi escrito", output.getvalue())

    def test_prune_without_apply_only_displays_plan(self):
        coleta, plano = self._patch_plan()
        with coleta, plano, patch.object(sync_notion, "aplicar") as aplicar:
            with contextlib.redirect_stdout(io.StringIO()) as output:
                result = sync_notion.main(["--prune"])

        self.assertEqual(result, 0)
        aplicar.assert_not_called()
        self.assertIn("[plan] nada foi escrito", output.getvalue())

    def test_apply_calls_aplicar_with_prune(self):
        coleta, plano = self._patch_plan()
        with coleta, plano, patch.object(sync_notion, "aplicar") as aplicar:
            result = sync_notion.main(["--apply", "--prune"])

        self.assertEqual(result, 0)
        aplicar.assert_called_once_with([], [], [], True)

    def test_apply_cannot_be_combined_with_read_only_modes(self):
        for option in ("--check", "--dry-run"):
            with self.subTest(option=option):
                with contextlib.redirect_stderr(io.StringIO()):
                    with patch.object(sync_notion, "coletar_aulas", side_effect=AssertionError):
                        with self.assertRaises(SystemExit) as raised:
                            sync_notion.main(["--apply", option])
                self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
