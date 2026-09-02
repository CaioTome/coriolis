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
* **Capítulo 6 (Naves Espaciais):** Concluído e modularizado na pasta `6. Naves Espaciais/` (8 arquivos: introdução e etapas de construção, chassis e tipos de naves, encaixes, defesas e armas, naves e estações de exemplo, customização e modificação, viagem espacial/sensores/reparos, e combate espacial com ações e crises).
* **Capítulo 7 (A História do Espaço):** Concluído e modularizado na pasta `7. A História do Espaço/` (4 arquivos: introdução e temas centrais, expansão humana e o Mandato, o Grito/Silêncio/Renascimento, e placeholder para Linha do Tempo do Futuro).
* **Capítulo 9 (Criação de Aventuras):** Concluído e modularizado na pasta `9. Criação de Aventuras/` (7 arquivos: introdução/metodologia de design, recompensas de aventura e sistemas de XP, gerador matricial de conflitos com 80 opções e restrições/reviravoltas, gerador de PNJs com postura e desfecho de acordos, gerador de locais com matriz de perigos e recompensas, 100 sementes de aventura oficiais completas, e exemplo prático de criação no planeta Delaine).
* **Capítulo 10 (Xenobestiário):** Concluído e modularizado na pasta `10. Xenobestiário/` (6 arquivos: hub do capítulo/condução de combate/rolagem de reação, humanidade e compêndio de 19 PNJs, robôs/sistemas especialistas/IVs e robótica na campanha, fauna alienígena/enxames/venenos e bestas, xenocivilizações/Semelhantes vs Outros/compêndio das 20 Lentes/sociedades, e regras completas para PJs sintéticos e alienígenas).
* **Capítulo 11 (Facções):** Concluído e modularizado na pasta `11. Facções/` (8 arquivos: hub do capítulo/regras centrais/renda/manutenção/combate, objetivos e evolução de facções/XP/PV/fusão, compêndio dos 25 ativos de Astúcia A-Z, compêndio dos 27 ativos de Força A-Z, compêndio dos 25 ativos de Economia A-Z, compêndio das 20 Tags de Facção oficiais, facções na campanha/facções de PJs/8 facções prontas, e exemplo prático de jogo de 3 turnos com notícias).
* **Ponto de Parada Atual:** Paramos no **Capítulo 12 (Recursos do Mestre)**. As próximas tarefas de estruturação e revisão devem iniciar a partir deste capítulo.

---

## 4. Regras Obrigatórias para Links e Renderização

* **Links Internos (Obsidian):** Todos os links entre arquivos e capítulos devem utilizar a sintaxe `[[Nome da Pasta/Nome do Arquivo|Texto Alternativo]]`.
* **Proibição de Emojis:** É terminantemente proibido o uso de emojis em qualquer título, marcador ou corpo de texto.
* **Proibição de ASCII Art:** Tabelas devem ser feitas exclusivamente em Markdown padrão GFM.
