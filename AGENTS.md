# Diretrizes para Agentes de IA (`AGENTS.md`)

> **Guia de Execução e Protocolo de Trabalho**  
> *Este documento define o fluxo de trabalho, as normas obrigatórias e os padrões de qualidade para qualquer agente de IA que atuar nesta base de código, dedicada exclusivamente à tradução, modularização e publicação oficial de **Stars Without Number: Edição Revisada (Deluxe)** em Português do Brasil.*

---

## 1. Estrutura de Diretórios e Documentação

### Pasta `dev/` (Rascunhos, Scripts e Glossário)
* **Objetivo:** Espaço de trabalho temporário, extração de PDFs e ferramentas auxiliares.
* **Glossário Oficial:** Sempre consulte e atualize o arquivo [dev/glossario-termos.md](file:///home/caio/Documentos/github/coriolis/dev/glossario-termos.md) ao traduzir novos termos mecânicos ou de cenário.
* **Execução de Scripts Python:** Sempre que for necessário rodar automações, extrações ou validações em Python, crie/salve o arquivo dentro da pasta `dev/` e execute-o a partir de lá (evitando comandos inline complexos no terminal).

### Pasta `docs/` (Diretrizes e Auditoria)
* **Painel de Auditoria de Completude:** Consulte o arquivo [docs/auditoria.md](file:///home/caio/Documentos/github/coriolis/docs/auditoria.md) para verificar a contagem de palavras, quantidade de arquivos e o status de revisão exaustiva de cada capítulo.
* **Organização de Capítulos:** Consulte [docs/organizacao-de-capitulos-e-arquivos.md](file:///home/caio/Documentos/github/coriolis/docs/organizacao-de-capitulos-e-arquivos.md) para diretrizes de divisão temática e nomenclatura de pastas.

### Pasta `content/` (Conteúdo Oficial - Quartz)
* **Objetivo:** Diretório base para a publicação do site/wiki via Quartz.
* **Uso:** Todos os textos finais do sistema (regras, naves, criação de personagens, psionismo, mestrado e suplementos) devem ser escritos **diretamente nesta pasta**.
* **Regras Estritas para `content/`:**
  * **Nomenclatura (Quartz):** NUNCA use hífens (`-`) para separar palavras no nome das pastas. Utilize a grafia oficial com acentos e espaços (ex: `content/1. Inúmeras Estrelas/1.1. Conteúdo do Jogador/2. Criação de Personagem/`).
  * **Links Internos:** Utilize obrigatoriamente a sintaxe do Obsidian: `[[Nome da Pasta/Nome do Arquivo|Texto Alternativo]]`.
  * **Proibido ASCII Art:** NUNCA crie tabelas usando caracteres decorativos (como `┌──┐`), pois elas quebram a renderização da engine Quartz. Utilize exclusivamente tabelas em Markdown padrão GFM (`| Coluna |`).
  * **Arquivo Index Exclusivo:** O único arquivo chamado `index.md` deve estar na raiz de `content/` (`content/index.md`) e precisa iniciar com o cabeçalho YAML `title: Introdução`.

---

## 2. Regras de Estilo, Terminologia e Tradução Integral

* **PROIBIDO USO DE EMOJIS:** É estritamente proibido o uso de emojis em títulos, marcadores de lista, tabelas ou no meio do texto em **qualquer arquivo** deste projeto.
* **TRADUÇÃO INTEGRAL E SEM RESUMOS (PADRÃO OBRIGATÓRIO E INEGOCIÁVEL):** 
  * É expressamente proibido resumir, abreviar, sintetizar, parafrasear ou omitir parágrafos de prosa, descrições narrativas, caixas de texto, exemplos de jogo, tabelas completas, notas explicativas ou regras detalhadas do livro original *Stars Without Number Revised Edition*.
  * A tradução deve ser **100% completa e exaustiva**, traduzindo fielmente todo o conteúdo parágrafo por parágrafo, detalhe por detalhe, tabela por tabela, mantendo toda a profundidade e extensão do material original.
  * **Padrão de Referência (Benchmark):** O modelo absoluto de execução para todo o projeto é o **Capítulo 13 (Campanhas Trans-humanas)**, seguido pelos Capítulos 14 a 18, que foram traduzidos integralmente e de forma exaustiva sem nenhum resumo. Todos os capítulos devem seguir rigorosamente esse mesmo padrão.
* **Plano de Revisão Geral:** Todos os capítulos anteriores do livro básico (Capítulos 1 a 12) passarão por uma rodada de revisão e expansão exaustiva para garantir que nenhum deles contenha resumos e que todos atinjam a completude de 100% demonstrada no bloco Deluxe (Capítulos 13 a 18).
* **Tradução Exclusiva para Português (PT-BR):** Todos os termos de regras, classes, perícias, armas e história devem ser traduzidos para o português formal brasileiro de acordo com o padrão do glossário oficial, preservando apenas termos técnicos em inglês entre parênteses em sua primeira menção para facilitar referência.

---

## 3. Protocolo de Execução e Controle de Versão

1. **Extração Direta da Fonte:** Antes de criar ou revisar qualquer capítulo, extraia as páginas correspondentes diretamente do PDF original (`livros/pdfcoffee.com_stars-without-number-revised-deluxe-edition-pdf-free.pdf`) para a pasta `dev/`.
2. **Modularização Temática:** Capítulos extensos devem ser divididos em uma pasta própria de capítulo com um arquivo Hub e subarquivos numerados (ex: `14. Magia Espacial.md`, `14.1. Classes Arcanas e Conjuração.md`, etc.).
3. **Auditoria e Validação:** Ao concluir a escrita, valide a contagem de palavras, verifique a ausência de emojis/ASCII art e atualize [docs/auditoria.md](file:///home/caio/Documentos/github/coriolis/docs/auditoria.md) e [docs/organizacao-de-capitulos-e-arquivos.md](file:///home/caio/Documentos/github/coriolis/docs/organizacao-de-capitulos-e-arquivos.md).
4. **Controle de Versão (Git):** Sempre faça commit das alterações locais no Git ao concluir com sucesso uma tarefa. Não faça push automático para o servidor remoto a menos que seja explicitamente solicitado pelo usuário.

---

> **AVISO CRÍTICO:** Qualquer agente que iniciar uma tarefa neste repositório **DEVE** ler este documento (`AGENTS.md`) e consultar o painel [docs/auditoria.md](file:///home/caio/Documentos/github/coriolis/docs/auditoria.md) antes de criar ou modificar qualquer arquivo.
