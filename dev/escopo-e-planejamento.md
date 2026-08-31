# Escopo e Planejamento: Coriolis (Sistema Base v2)

> **Documento de Visão e Arquitetura**  
> *Referência rápida sobre os objetivos do projeto: a integração do cenário de O Terceiro Horizonte (v1) com as mecânicas modernas de A Grande Escuridão (v2).*

---

## 1. Visão Geral do Projeto

O objetivo central é criar um compêndio digital em português (PT-BR), combinando a rica ambientação e rotas estelares de **Coriolis: O Terceiro Horizonte (v1)** com as mecânicas refinadas e visceral de **A Grande Escuridão (v2)**.

O resultado será um compêndio digital navegável (Wiki) gerado através do **Quartz / Obsidian**.

A estrutura e escopo do projeto baseiam-se em:
* **Mecânicas v2 Pura (A Grande Escuridão):** Uso da Ficha Oficial v2, motor de Dados de Estágio (d6, d8, d10, d12), Estresse, Esperança e Escavação de Ruínas.
* **Adaptação Espacial v2:** As viagens e combates navais serão resolvidos pelas perícias nativas da v2 + Dados de Recurso da nave.
* **Cenário Expandido:** O cenário engloba as tensões políticas das Facções no Terceiro Horizonte, os novos setores (Odacon e Quadrante do Pilar) e a exploração de ruínas alienígenas.
* **Infraestrutura Web:** O diretório `/content/` é a fonte oficial da Wiki de onde o Quartz extrai os arquivos Markdown para renderizar o site estático.

> **Nota de Histórico:** A ideia original de realizar uma tradução literal e integral do livro base da v1 foi **abandonada**. Todo o esforço atual está focado em estruturar o Mod Unificado Híbrido.

---

## 2. Estratégia e Padronização

1. **Glossário Base (`dev/glossario-termos.md`):** É obrigatório consultar este arquivo para manter o alinhamento perfeito entre termos em Inglês e a Tradução Oficial (PT-BR) adotada no projeto.
2. **Matriz de Decisões (`dev/conflitos-e-solucoes-mecanicas.md`):** Onde as resoluções de conflitos mecânicos entre as duas edições estão documentadas. As caixas marcadas com `[x]` ditam as regras oficiais do Mod e devem ser sempre consultadas antes de escrever mecânicas novas em `content/`.

---

---

## 3. Estrutura de Capítulos e Cronograma (Milestones)

Conforme decidido, a prioridade máxima é o desenvolvimento do **Cenário** e da **Campanha**, deixando a especificação detalhada das regras mecânicas para o **último bloco do cronograma**.

### Milestone 1: O Universo e Cenário Expandido (Prioridade Atual)
* **O Terceiro Horizonte:** Rotas estelares (Miran, Sadaal, Algol, Dabaran, Estação Coriolis).
* **As Novas Fronteiras (PDF):** Sistema de Odacon e o Quadrante do Pilar (Altai, Ordana, Sivas, Zhau).
* **Sociedade e Fé:** As 10 Facções e a devoção correta aos Nove Ícones.

### Milestone 2: A Campanha e Ferramentas do Mestre
* **A Campanha Viva:** Organização dos Diários de Bordo, PJs, NPCs e Missões.
* **A Nave:** Ficha, histórico de dívidas e gerenciamento de recursos.
* **Templates em `dev/templates/`:** Modelos rápidos para criação dinâmica de conteúdo durante o jogo.

### Milestone 3: O Sistema e Mecânicas Base v2 (Por Último no Cronograma)
* **O Motor v2 (A Grande Escuridão):** Dados de Estágio (d6, d8, d10, d12), Ficha Oficial v2, Estresse e Esperança.
* **Exploração Terrestre:** Regras de Escavação de Ruínas (Delving) e Dados de Recurso (oxigênio/luz).
* **Adaptação Espacial v2:** Resolução de funções da tripulação e combate de naves usando as perícias nativas da v2 e Dados de Recurso para a fuselagem da nave.
