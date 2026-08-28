# Escopo e Planejamento: Mod Unificado Coriolis (v1 + v2)

> **Documento de Visão e Arquitetura**  
> *Referência rápida sobre os objetivos do projeto: a criação de um Mod Híbrido que unifica o melhor do Terceiro Horizonte (v1) com as mecânicas modernas de A Grande Escuridão (v2).*

---

## 1. Visão Geral do Projeto

O objetivo central é criar um **Mod Unificado** em português (PT-BR), combinando a rica ambientação e a gestão de naves de **Coriolis: O Terceiro Horizonte (v1)** com as mecânicas refinadas de sobrevivência e exploração da engine moderna de **A Grande Escuridão (v2)**.

O resultado será um compêndio digital navegável (Wiki) gerado através do **Quartz / Obsidian**.

A estrutura e escopo do projeto baseiam-se na fusão dos dois sistemas:
* **Mecânicas Híbridas (v1 + v2):** Integração do sistema de Estresse, Esperança e Escavação de Ruínas (v2) com o combate de Naves e o impacto narrativo dos Ícones (v1).
* **Cenário Expandido:** O cenário englobará tanto as tensões políticas das Facções no Terceiro Horizonte quanto a exploração hostil de ruínas alienígenas.
* **Infraestrutura Web:** O diretório `/content/` é a fonte oficial do Mod de onde o Quartz extrai os arquivos Markdown para renderizar o site estático.

> **Nota de Histórico:** A ideia original de realizar uma tradução literal e integral do livro base da v1 foi **abandonada**. Todo o esforço atual está focado em estruturar o Mod Unificado Híbrido.

---

## 2. Estratégia e Padronização

1. **Glossário Base (`dev/glossario-termos.md`):** É obrigatório consultar este arquivo para manter o alinhamento perfeito entre termos em Inglês e a Tradução Oficial (PT-BR) adotada no projeto.
2. **Matriz de Decisões (`dev/conflitos-e-solucoes-mecanicas.md`):** Onde as resoluções de conflitos mecânicos entre as duas edições estão documentadas. As caixas marcadas com `[x]` ditam as regras oficiais do Mod e devem ser sempre consultadas antes de escrever mecânicas novas em `content/`.

---

## 3. Estrutura de Capítulos do Mod (Milestones)

As tarefas de redação do Mod Híbrido estão divididas nos seguintes blocos lógicos:

### Milestone 1: Mecânicas do Jogador
* **Introdução:** Premissa do jogo e rolagem da Year Zero Engine (empurrar rolagens gerando Estresse para o jogador e PE para o mestre).
* **Personagem:** Os conceitos clássicos adaptados para o sistema de Esperança.
* **Perícias (14 Unificadas):** A lista enxuta baseada na v2 (sem restrição entre Gerais/Avançadas), resgatando Pilotagem e Tecnologia da v1.

### Milestone 2: Ação, Combate e Sobrevivência
* **Dano e Sanidade:** Tríade com HP (dano físico e lesões críticas), MP/Estresse (dano mental e pânico) e Ruína (contaminação por artefatos).
* **Naves e Viagem Espacial (v1):** Regras de gestão de nave, posições da tripulação (Capitão, Piloto, etc) e combate de naves.
* **Escavação de Ruínas (v2):** Subsistema terrestre para turnos de exploração de mapas, uso de dados de recursos (oxigênio/baterias) e perigos ambientais.

### Milestone 3: O Universo e Mestre de Jogo
* **O Lore Combinado:** Facções e Ícones do Terceiro Horizonte interagindo com o mistério insondável dos Construtores e da Grande Escuridão.
* **Economia do Mestre:** Regras para o Mestre utilizar os Pontos de Escuridão (PE) gerados e ativar perigos, biomorfos e armadilhas.
