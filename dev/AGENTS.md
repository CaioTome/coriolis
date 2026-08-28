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
  - O histórico de decisões tomadas em `dev/conflitos-e-solucoes-mecanicas.md` deve ser rigorosamente respeitado durante a redação dos arquivos em `content/`.

---

## 2. Divisão de Papéis dos Agentes (Especialização)

Para evitar mistura de contexto e garantir máxima precisão, o trabalho de unificação é dividido em três papéis de agentes:

```
  ┌─────────────────────────────────┐        ┌─────────────────────────────────┐
  │      Agente Analista 1          │        │      Agente Analista 2          │
  │    (O Terceiro Horizonte)       │        │     (A Grande Escuridão)        │
  └────────────────┬────────────────┘        └────────────────┬────────────────┘
                   │                                          │
                   │  Gera:                                   │  Gera:
                   │  dev/analise-terceiro-horizonte.md       │  dev/analise-grande-escuridao.md
                   │                                          │
                   └────────────────────┬─────────────────────┘
                                        │
                                        ▼
                       ┌─────────────────────────────────┐
                       │     Agente Sintetizador 3       │
                       │    (Arquiteto do Mod/Regras)    │
                       └────────────────┬────────────────┘
                                        │
                                        │  Gera:
                                        │  dev/conflitos-e-solucoes-mecanicas.md
                                        ▼
                       ┌─────────────────────────────────┐
                       │       Usuário (Decisão)         │
                       │   Marca as caixas [x] no .md    │
                       └─────────────────────────────────┘
```

---

###  Papel 1: Agente Analista - O Terceiro Horizonte
* **Objetivo:** Analisar exclusivamente o livro *O Terceiro Horizonte* (`livros/o-terceiro-horizonte.pdf`).
* **Foco de Análise:**
  1. **Criação de Personagens:** Atributos (4), Perícias (16), Talentos (Gerais, de Conceito, de Ícone), Conceitos e Origens.
  2. **Mecânicas Principais:** Pilha de $d6$, empurrar rolagens, orações aos Ícones.
  3. **Economia do Mestre:** Pontos de Escuridão (DP) e como são gerados/gastos.
  4. **Combate & Naves Espaciais:** Sistema de dano/saúde/empatia, lesões críticas e combate de naves.
* **Saída Obrigatória:** Arquivo `dev/analise-terceiro-horizonte.md`.

---

### 🛡️ Papel 2: Agente Analista - A Grande Escuridão
* **Objetivo:** Analisar exclusivamente o livro *A Grande Escuridão* (`livros/a-grande-escuridao.pdf`).
* **Foco de Análise:**
  1. **Criação de Personagens:** Atributos, lista reduzida/atualizada de Perícias, Talentos e Traços de Sobrevivência.
  2. **Mecânicas Principais:** Atualizações da *Year Zero Engine* (YZE v2).
  3. **Economia de Tensão:** Sistema de Esperança, Estresse, Desespero e Ruína/Contaminação.
  4. **Mecânica de Exploração (*Delving*):** Regras de expedição, ambientes hostis, hazards, recursos e exploração de ruínas dos Construtores.
* **Saída Obrigatória:** Arquivo `dev/analise-grande-escuridao.md`.

---

### ⚖️ Papel 3: Agente Sintetizador & Arquiteto do Mod
* **Objetivo:** Comparar ambos os relatórios de análise, identificar atritos mecânicos e propor soluções modulares.
* **Foco de Análise:**
  1. Mapear divergências de Atributos e Perícias entre as versões.
  2. Comparar Pontos de Escuridão (TH) vs. Estresse/Esperança (GE) e propor modelo de harmonização.
  3. Mapear como integrar o Combate de Naves (TH) com as regras de Expedição e Ruínas (GE).
  4. Oferecer opções claras com caixas de seleção `[ ]` para o usuário decidir o rumo do Mod.
* **Saída Obrigatória:** Arquivo `dev/conflitos-e-solucoes-mecanicas.md`.

---

## 3. Diretrizes de Formatação e Registro

1. **Glossário:** Sempre consulte e atualize `dev/glossario-termos.md` ao traduzir ou propor um novo termo técnico.
2. **Checkboxes Interativos:** No documento de conflitos, use a sintaxe Markdown:
   - `- [ ] Opção A: ...`
   - `- [ ] Opção B: ...`
3. **Persistência de Decisão:** Quando o usuário marcar uma caixa `- [x]`, esse caminho se torna a **regra oficial do projeto** para a redação do Mod Unificado.

---

> *Qualquer agente iniciando uma tarefa neste repositório DEVE ler este documento e o `escopo-e-planejamento.md` antes de gerar novos arquivos.*
