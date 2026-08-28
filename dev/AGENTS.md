# Diretrizes para Agentes de IA (`dev/AGENTS.md`)

> **Guia de Execução e Protocolo de Trabalho**  
> *Este documento define o fluxo de trabalho, a divisão de papéis e as normas para qualquer agente de IA que atuar nesta pasta e no projeto Coriolis PT-BR.*

---

## 1. O Papel das Pastas `dev/` e `content/`

* **Pasta `dev/` (Espaço de Rascunho & Decisão do Agente):**
  - Utilizada para análises mecânicas, fichamentos, listas de conflitos e registros de decisões aprovadas pelo usuário.
* **Pasta `content/` (Diretório Oficial de Conteúdo & Publicação Quartz):**
  - **DIRETRIZ PRINCIPAL DE CONTEÚDO:** Todos os conteúdos finais do Mod (regras do sistema unificado, regras de naves, expedições, criação de personagens) e do Cenário (O Terceiro Horizonte, O Horizonte Perdido, Facções, Ícones) devem ser escritos **diretamente na pasta `content/`**.
  - **REGRA DE NOMENCLATURA DE PASTAS (QUARTZ):** Como o nome das pastas é exibido no menu/navegação do site, **NUNCA use hífens (`-`) para separar nomes de pastas**. Sempre utilize o nome oficial acentuado e com espaços (ex: `content/Coriolis/`, `content/O Terceiro Horizonte/`, `content/O Horizonte Perdido/`).
  - **REGRA DE LINKS E TABELAS:** Utilize a sintaxe de links do Obsidian/Quartz `[[Nome da Pasta/Nome do Arquivo|Texto]]`. NUNCA utilize arte ASCII / tabelas em blocos de código (`┌──┐`/`│  │`), pois quebram na renderização do Quartz.
  - **REGRA DO ARQUIVO INDEX:** O arquivo `content/index.md` é o único arquivo `index.md` permitido e deve iniciar obrigatoriamente com o cabeçalho YAML `title: Introdução`.
  - **PROIBIDO O USO DE EMOJIS:** NUNCA utilize emojis em títulos, marcadores ou textos em qualquer arquivo do projeto.
  - **TRADUÇÃO E TERMINOLOGIA ESTRITA EM PORTUGUÊS (PT-BR):** NENHUM termo técnico ou de cenário deve ser mantido em Inglês nos textos finais. Utilize exclusivamente a tradução oficial definida:
    - *Dark Between the Stars* -> **Escuridão Entre as Estrelas**
    - *Darkbound* -> **A Escuridão**
    - *Firstcome* -> **Pioneiros**
    - *Pontos de Escuridão / DP* -> **PE** (Pontos de Escuridão)

---

## 2. Divisão de Papéis dos Agentes (Especialização)

Para evitar mistura de contexto e garantir máxima precisão, o trabalho de unificação é dividido em três papéis de agentes:

* **Papel 1: Agente Analista - O Terceiro Horizonte:** Analisa o livro *O Terceiro Horizonte* (`livros/o-terceiro-horizonte.pdf`). Saída: `dev/analise-terceiro-horizonte.md`.
* **Papel 2: Agente Analista - A Grande Escuridão:** Analisa o livro *A Grande Escuridão* (`livros/a-grande-escuridao.pdf`). Saída: `dev/analise-grande-escuridao.md`.
* **Papel 3: Agente Sintetizador & Arquiteto do Mod:** Mapeia divergências mecânicas e propõe soluções com caixas de seleção `[ ]`. Saída: `dev/conflitos-e-solucoes-mecanicas.md`.

---

## 3. Diretrizes de Formatação e Registro

1. **Glossário:** Sempre consulte e atualize `dev/glossario-termos.md` ao traduzir ou padronizar um termo técnico.
2. **Checkboxes Interativos:** No documento de conflitos, use a sintaxe Markdown:
   - `- [ ] Opção A: ...`
   - `- [ ] Opção B: ...`
3. **Persistência de Decisão:** Quando o usuário marcar uma caixa `- [x]`, esse caminho se torna a **regra oficial do projeto** para a redação do Mod Unificado.

---

> *Qualquer agente iniciando uma tarefa neste repositório DEVE ler este documento e o `escopo-e-planejamento.md` antes de gerar novos arquivos.*
