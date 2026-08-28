# Visão Geral do Projeto: Tradução Integral (O Terceiro Horizonte)

> **Documento de Escopo, Arquitetura e Planejamento**  
> *Este documento serve como referência rápida para o agente de IA e colaboradores compreenderem a visão do projeto, que agora é a tradução literal e integral do livro básico de Coriolis (v1).*

---

## 1. Visão Geral e Estrutura Fundamental

O objetivo principal deste projeto é criar uma tradução completa (PT-BR) do Core Rulebook de **Coriolis: O Terceiro Horizonte**, gerando um site enciclopédico e navegável usando a engine **Quartz / Obsidian**.

A estrutura do projeto foi simplificada para refletir o livro original:
* **Mecânicas Puras (v1):** Preservando Pontos de Escuridão, Pontos de Mente (sem Estresse/Esperança) e as 16 Perícias.
* **O Terceiro Horizonte (Cenário):** Space Opera Clássica, Facções, Ícones.
* **Quartz:** Geração estática do site em Markdown.

> **Nota Histórica:** As tentativas anteriores de criar um "Mod Unificado" (focando em A Grande Escuridão) foram movidas para a pasta `/content/Mod Híbrido Alternativo/` para preservação, não fazendo mais parte do escopo principal.

---

## 2. Estratégia de Tradução e Glossário PT-BR

1. **Glossário Base Flexível (`dev/glossario-termos.md`):**
   * Tabela de equivalência entre os termos em Inglês, a Tradução Oficial PT-BR e a Tradução Oficial Tria Editora.
2. **Separação de Capítulos (O Cronograma):**
   * O livro original será traduzido em ordem modular e publicado diretamente em `content/`.

---

## 3. Cronograma Oficial de Tradução por Marcos (Milestones)

A tradução das quase 400 páginas foi dividida em entregas lógicas:

### Milestone 1: Mecânicas do Jogador (Capítulos 1 a 4)
* **Cap 1. Introdução:** O que é Coriolis, mecânica básica de d6 e empurrar rolagens.
* **Cap 2. Seu Personagem:** Criação de personagem pura v1 (Origens, Reputação, os 11 Conceitos exatos).
* **Cap 3. Perícias:** Lista exata das 8 Perícias Gerais e 8 Perícias Avançadas.
* **Cap 4. Talentos:** A gigantesca lista de talentos, convertida para os custos clássicos (sem Esperança).

### Milestone 2: Combate e Economia (Capítulos 5 a 7)
* **Cap 5. Combate:** Iniciativa, Pontos de Ação (PA), cobertura e a Tabela de Lesões Críticas.
* **Cap 6. Armas e Equipamentos:** Lista de todos os itens do livro, incluindo peso e bônus tecnológico.
* **Cap 7. Naves e Combate Espacial:** Criação da nave, sistema de dívidas e o combate em 5 Fases.

### Milestone 3: O Cenário e o Lore (Capítulos 8 a 10)
* **Cap 8. O Terceiro Horizonte:** História das Facções, as Guerras do Portal, os 9 Ícones.
* **Cap 9. Pessoas e Lugares:** Detalhamento massivo da Estação Coriolis (Anel, Núcleo, Porão).
* **Cap 10. O Sistema Kua e os Portais:** Mapa geopolítico e viagens no hiperespaço.

### Milestone 4: O Mestre de Jogo (Capítulos 11 a 13)
* **Cap 11. Bestiário (Feras e Djinns):** Blocos de estatísticas de inimigos e da Escuridão Entre as Estrelas.
* **Cap 12. A Campanha:** Ferramentas do Mestre e missões aleatórias.
* **Cap 13. O Cenário Inicial:** Tradução da aventura "O Oásis das Sombras".

---

## 4. Setup do Site (Quartz)

A infraestrutura de geração do site Wiki foi inicializada na raiz do repositório. O diretório `/content/` é a fonte da verdade de onde o Quartz puxa os artigos renderizados.
