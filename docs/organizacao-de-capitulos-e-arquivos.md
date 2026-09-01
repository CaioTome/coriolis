# Diretriz de Organização Modular de Capítulos e Assuntos

## 1. Visão Geral da Estrutura

Para otimizar a navegação na engine Quartz, facilitar a manutenção do texto e permitir a tradução integral e exaustiva sem perda de detalhes, os capítulos extensos do sistema (*Stars Without Number* e suplementos) passam a adotar uma **estrutura modular por pastas de capítulos**.

---

## 2. Padrão de Organização

1. **Pastas por Capítulo (Capítulos Extensos):**
   * Cada capítulo extenso deve possuir uma pasta própria dentro de sua respectiva seção em `content/` (por exemplo: `content/1. Estrelas Incontáveis/2. Criação de Personagem/`, `content/1. Estrelas Incontáveis/3. Psionismo/`, `content/1. Estrelas Incontáveis/4. Sistemas/`).
   * **Nomenclatura (Quartz):** Nunca utilize hífens para separar palavras no nome das pastas. Utilize a grafia oficial com acentos e espaços (ex: `content/1. Estrelas Incontáveis/4. Como Jogar/`).

2. **Arquivos Modulares por Assunto:**
   * Dentro da pasta do capítulo, cada arquivo `.md` é dedicado a um **assunto específico ou subseção principal** do capítulo.
   * O primeiro arquivo da pasta atua como introdução geral e sumário de navegação (exemplo: `3. Psionismo.md` reúne a introdução, histórico do Grito, regras gerais de Esforço, Estresse Sistêmico e Incêndio Psíquico, além de links para cada disciplina).
   * Os arquivos subsequentes aprofundam cada tópico sem resumos (exemplo: `3.1. Biopsionismo.md`, `3.2. Metapsionismo.md`, etc.).

3. **Critério de Aplicação (Apenas Capítulos Extensos):**
   * **NÃO** é necessário criar pastas modulares para todos os capítulos.
   * Capítulos curtos, concisos ou de leitura direta (como introduções de poucas páginas ou tópicos pontuais) podem permanecer como arquivos individuais `.md` na raiz da seção.
   * A divisão em pastas com múltiplos arquivos `.md` deve ser aplicada prioritariamente aos capítulos densos e com muitas tabelas/regras mecânicas (ex.: *Criação de Personagem*, *Psionismo*, *Como Jogar / Sistemas*, *Equipamentos*, *Naves Espaciais*, *Criação de Setor*).

---

## 3. Estado Atual do Projeto e Ponto de Parada

* **Capítulo 1 (Introdução):** Concluído como arquivo individual `1. Introdução.md`.
* **Capítulo 2 (Criação de Personagem):** Concluído e modularizado na pasta `2. Criação de Personagem/` (7 arquivos: introdução, profissões, classes, focos, perícias, equipamento/estatísticas e criação rápida).
* **Capítulo 3 (Psionismo):** Concluído e modularizado na pasta `3. Psionismo/` (7 arquivos: regras gerais e 6 disciplinas psíquicas).
* **Capítulo 4 (Sistemas):** Concluído e modularizado na pasta `4. Sistemas/` (9 arquivos: introdução, testes e salvaguardas, combate, manobras e táticas, ferimentos e cura, hacking, avanço de personagem, perigos ambientais e folha de referência rápida).
* **Capítulo 5 (Equipamento e Veículos):** Concluído e modularizado na pasta `5. Equipamento e Veículos/` (7 arquivos: introdução/regras fundamentais, armaduras, armas, equipamento geral e serviços, veículos e drones, cibernéticos, e artefatos pretech).
* **Ponto de Parada Atual:** Paramos no **Capítulo 6 (Naves Espaciais)**. As próximas tarefas de estruturação e revisão devem iniciar a partir deste capítulo.

---

## 4. Regras Obrigatórias para Links e Renderização

* **Links Internos (Obsidian):** Todos os links entre arquivos e capítulos devem utilizar a sintaxe `[[Nome da Pasta/Nome do Arquivo|Texto Alternativo]]`.
* **Proibição de Emojis:** É terminantemente proibido o uso de emojis em qualquer título, marcador ou corpo de texto.
* **Proibição de ASCII Art:** Tabelas devem ser feitas exclusivamente em Markdown padrão GFM.
