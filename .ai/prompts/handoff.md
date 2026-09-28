# Handoff de sessão

Vou encerrar esta sessão e outro agente (possivelmente outro modelo, sem acesso
a esta conversa) vai continuar. Ele só terá acesso aos arquivos do repositório.

1. Se existir um `.ai/handoff.md` anterior com conteúdo relevante, copie-o para
   `.ai/sessions/AAAA-MM-DD-HHMM.md` antes de sobrescrever.
2. Reescreva `.ai/handoff.md` seguindo o template, com base em TUDO o que
   aconteceu nesta conversa:
   - Seja específico: nomes de arquivos, funções, comandos, mensagens de erro.
   - Em "Em andamento", descreva o raciocínio que estava em curso, não só o que
     foi feito.
   - Em "Armadilhas", registre tentativas que falharam e o motivo.
   - Em "Fatos verificados vs. hipóteses", nunca registre suspeita como causa
     confirmada; cite a evidência de cada fato.
   - Os próximos passos devem ser acionáveis por alguém sem nenhum contexto.
3. Se houve decisão técnica nesta sessão, registre em `.ai/decisions.md`.
4. Se a arquitetura, as dependências ou os módulos mudaram, atualize `.ai/context.md`.
5. Rode `git status` e preencha "Estado do repositório".
6. NÃO faça commit. O arquivo salvo em disco basta para o próximo agente
   continuar nesta pasta.
7. Mostre o handoff final para eu revisar.
