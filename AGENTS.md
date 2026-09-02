# Diretrizes para Agentes de IA (`AGENTS.md`)

> **Guia de Execução e Protocolo de Trabalho**  
> *Este documento define o fluxo de trabalho, a divisão de papéis e as normas obrigatórias para qualquer agente de IA que atuar nesta pasta e no projeto Coriolis PT-BR.*

---

## 1. Estrutura de Diretórios

### Pasta `dev/` (Rascunhos e Análises)
* **Objetivo:** Espaço de trabalho temporário e registro de decisões.
* **Uso:** Armazena análises mecânicas, fichamentos, mapeamento de conflitos de regras e decisões validadas pelo usuário.
* **Execução de Scripts Python:** Sempre que for necessário rodar códigos ou automações em Python, crie/salve o arquivo de script dentro da pasta `dev/` e execute-o a partir de lá (evitando comandos inline complexos ou interativos diretamente no terminal que possam causar travamentos).

### Pasta `content/` (Conteúdo Oficial - Quartz)
* **Objetivo:** Diretório base para a publicação do site/wiki.
* **Uso:** Todos os textos finais do sistema (regras, naves, criação de personagens) e do cenário devem ser escritos **diretamente nesta pasta**.
* **Organização Modular por Capítulos:**
  * Capítulos densos e extensos são organizados em **pastas próprias de capítulo** contendo arquivos `.md` individuais para cada assunto/subseção temática.
  * Capítulos curtos e concisos permanecem como arquivos únicos `.md`.
  * Diretriz completa e status de progresso (parado no Capítulo 4): consulte [docs/organizacao-de-capitulos-e-arquivos.md](file:///home/caio/Documentos/github/coriolis/docs/organizacao-de-capitulos-e-arquivos.md).
* **Regras Estritas para `content/`:**
  * **Nomenclatura (Quartz):** NUNCA use hífens (`-`) para separar palavras no nome das pastas. Utilize a grafia oficial com acentos e espaços (ex: `content/1. Estrelas Incontáveis/2. Criação de Personagem/`).
  * **Links Internos:** Utilize obrigatoriamente a sintaxe do Obsidian: `[[Nome da Pasta/Nome do Arquivo|Texto Alternativo]]`.
  * **Proibido ASCII Art:** NUNCA crie tabelas usando caracteres (como `┌──┐`), pois elas quebram a renderização da engine Quartz.
  * **Arquivo Index Exclusivo:** O único arquivo chamado `index.md` deve estar na raiz de `content/` (`content/index.md`) e precisa iniciar com o cabeçalho YAML `title: Introdução`.

---

## 2. Regras de Estilo, Terminologia e Tradução Integral

* **PROIBIDO USO DE EMOJIS:** É estritamente proibido o uso de emojis em títulos, marcadores de lista ou no meio do texto em **qualquer arquivo** deste projeto.
* **TRADUÇÃO INTEGRAL E SEM RESUMOS (OBRIGATÓRIO):** 
  * É expressamente proibido resumir, abreviar, sintetizar ou omitir parágrafos de prosa, descrições narrativas, caixas de texto, exemplos de jogo, tabelas completas, notas explicativas ou regras detalhadas dos livros originais.
  * A tradução deve ser completa e exaustiva, traduzindo fielmente todo o conteúdo parágrafo por parágrafo, detalhe por detalhe, mantendo a profundidade do material original.
* **Uso do Glossário:** Sempre consulte e atualize o arquivo `dev/glossario-termos.md` ao traduzir conceitos novos.
* **Tradução Exclusiva para Português (PT-BR):** Nenhum termo de regras ou de história deve permanecer em inglês no texto final. Use **apenas** a tradução oficial, com **exceção de palavras em árabe**, que devem ser mantidas no original para preservar o misticismo da campanha:
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

### Controle de Versão (Git)
* **Commit ao Finalizar Tarefas:** Sempre faça commit das alterações locais no Git ao concluir com sucesso uma tarefa. Não faça push automático para o servidor remoto a menos que seja explicitamente solicitado pelo usuário.

---

> **AVISO CRÍTICO:** Qualquer agente que iniciar uma tarefa neste repositório **DEVE** ler este documento (`AGENTS.md`), o arquivo `dev/escopo-e-planejamento.md` e a diretriz `docs/organizacao-de-capitulos-e-arquivos.md` antes de criar ou modificar qualquer coisa.
