# Diretrizes para Agentes de IA (`AGENTS.md`)

> **Guia de Execução e Protocolo de Trabalho**  
> *Este documento define o fluxo de trabalho, a divisão de papéis e as normas obrigatórias para qualquer agente de IA que atuar nesta pasta e no projeto Coriolis PT-BR.*

---

## 1. Estrutura de Diretórios

### Pasta `dev/` (Rascunhos e Análises)
* **Objetivo:** Espaço de trabalho temporário e registro de decisões.
* **Uso:** Armazena análises mecânicas, fichamentos, mapeamento de conflitos de regras e decisões validadas pelo usuário.

### Pasta `content/` (Conteúdo Oficial - Quartz)
* **Objetivo:** Diretório base para a publicação do site/wiki.
* **Uso:** Todos os textos finais do sistema (regras, naves, criação de personagens) e do cenário devem ser escritos **diretamente nesta pasta**.
* **Regras Estritas para `content/`:**
  * **Nomenclatura (Quartz):** NUNCA use hífens (`-`) para separar palavras no nome das pastas. Utilize a grafia oficial com acentos e espaços (ex: `content/O Terceiro Horizonte/`).
  * **Links Internos:** Utilize obrigatoriamente a sintaxe do Obsidian: `[[Nome da Pasta/Nome do Arquivo|Texto Alternativo]]`.
  * **Proibido ASCII Art:** NUNCA crie tabelas usando caracteres (como `┌──┐`), pois elas quebram a renderização da engine Quartz.
  * **Arquivo Index Exclusivo:** O único arquivo chamado `index.md` deve estar na raiz de `content/` (`content/index.md`) e precisa iniciar com o cabeçalho YAML `title: Introdução`.

---

## 2. Regras de Estilo e Terminologia

* **PROIBIDO USO DE EMOJIS:** É estritamente proibido o uso de emojis em títulos, marcadores de lista ou no meio do texto em **qualquer arquivo** deste projeto.
* **Uso do Glossário:** Sempre consulte e atualize o arquivo `dev/glossario-termos.md` ao traduzir conceitos novos.
* **Tradução Exclusiva para Português (PT-BR):** Nenhum termo de regras ou de história deve permanecer em inglês no texto final. Use **apenas** a tradução oficial:
  * *Dark Between the Stars* ➔ **Escuridão Entre as Estrelas**
  * *Darkbound* ➔ **A Escuridão**
  * *Firstcome* ➔ **Pioneiros**
  * *Darkness Points (DP)* ➔ **PE (Pontos de Escuridão)**

---

## 3. Decisões e Papéis dos Agentes

### Persistência de Decisões Mecânicas
* No documento de conflitos (`dev/conflitos-e-solucoes-mecanicas.md`), as propostas de regras são listadas com checkboxes (`- [ ]`).
* Quando o usuário marca uma opção com `- [x]`, essa decisão torna-se a **regra oficial** definitiva para a redação dos textos finais.

### Especialização (Evitando Mistura de Contexto)
O trabalho de análise é dividido em três papéis principais:
1. **Agente Analista (O Terceiro Horizonte):** Extrai regras do livro original (v1) e compila no arquivo `dev/analise-terceiro-horizonte.md`.
2. **Agente Analista (A Grande Escuridão):** Extrai regras da nova edição (v2) e compila no arquivo `dev/analise-grande-escuridao.md`.
3. **Agente Sintetizador & Arquiteto:** Compara as duas versões, mapeia as diferenças mecânicas e propõe soluções no arquivo `dev/conflitos-e-solucoes-mecanicas.md`.

---

> **AVISO CRÍTICO:** Qualquer agente que iniciar uma tarefa neste repositório **DEVE** ler este documento (`AGENTS.md`) e o arquivo `dev/escopo-e-planejamento.md` antes de criar ou modificar qualquer coisa.
