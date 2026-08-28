# Análise Mecânica: O Terceiro Horizonte (Coriolis v1)

> **Relatório Técnico do Agente Analista 1**  
> *Este documento detalha as regras de criação de personagem, mecânicas fundamentais, economia de jogo e balanceamento da edição clássica "Coriolis: O Terceiro Horizonte".*

---

## 1. Criação de Personagens & Atributos

### 1.1. Conceito e Origem
* **Conceitos (11):** Divididos em 3 categorias sociais (Alta Estação, Decks Inferiores, Fronteira):
  * *Artista, Comerciante, Pregador, Oficial, Engenheiro, Cientista, Piloto, Batedor, Mercenário, Operativo, Agente.*
  * Cada conceito define a Perícia Principal, Opções de Talentos de Conceito, Equipamento Inicial e Relacionamento com o Grupo.
* **Origem Cultural:** 
  * **Primeiros (*Firstcome*):** Foco em tradição, religiosidade nos Ícones e adaptação ao Horizonte.
  * **Zenitianos (*Zenithian*):** Foco em tecnologia, mercantilismo, pragmatismo e liderança corporativa.
  * *Impacto:* Afeta a Reputação inicial e os bônus/interações sociopolíticas.

### 1.2. Atributos (4)
* **Força (*Strength*):** Resistência física, esforço bruto.
* **Agilidade (*Agility*):** Reflexos, coordenação, pontaria.
* **Raciocínio (*Wits*):** Inteligência, percepção, acuidade mental.
* **Empatia (*Empathy*):** Carisma, persuasão, conexão com os Ícones e intuição social.
* *Distribuição:* 13 a 15 pontos dependendo da faixa etária (Jovem, Adulto, Veterano). Limite inicial de atributo entre 4 e 5.

### 1.3. Perícias (16)
O jogo divide estritamente as perícias em 8 Gerais (podem ser roladas mesmo com nível 0) e 8 Avançadas (requerem ao menos nível 1 para rolar):

| Atributo | Perícias Gerais (Sem Treino OK) | Perícias Avançadas (Requer Nível 1+) |
| :--- | :--- | :--- |
| **Força** | Combate Corpo a Corpo (*Melee*) | Força Bruta (*Force*) |
| **Agilidade** | Combate a Distância (*Ranged*), Destreza (*Dexterity*) | Infiltração (*Infiltration*), Pilotagem (*Pilot*) |
| **Raciocínio** | Percepção (*Observation*) | Tecnologia (*Datacraft*), Medicina (*Medical*), Ciência (*Science*) |
| **Empatia** | Manipulação (*Command*), Intuição (*Empathy*) | Comando (*Leadership*), Cultura (*Culture*) |

### 1.4. Resustência & Recursos Derivados
* **Pontos de Vida (HP / Health):** $\text{Força} + \text{Agilidade}$
* **Pontos de Mente (MP / Mind):** $\text{Raciocínio} + \text{Empatia}$
* **Reputação:** Determinada pelo Conceito, Origem e Idade.

### 1.5. Talentos
* **Talento de Conceito:** 1 escolhido a partir da lista do conceito.
* **Talento de Ícone:** Determinado pelo Ícone sob o qual o personagem nasceu (concede habilidade especial única utilizável uma vez por sessão via oração).
* **Talentos Gerais & Cibernéticos:** Habilidades passivas ou ativas de combate, sobrevivência ou implantes tecnológicos.

---

## 2. Espinha Dorsal Mecânica & Rolagens

### 2.1. O Teste de Dados ($d6$)
* **Pilha de Dados:** $\text{Atributo} + \text{Perícia} + \text{Bônus de Equipamento} + \text{Modificadores de Situação}$.
* **Sucesso:** Pelo menos um dado mostrando **6**.
* **Sucessos Múltiplos (*Stunts*):**
  * 1 seis (6) = Sucesso Limitado / Normal.
  * 2 seis (66) = Sucesso Crítico.
  * 3+ seis (666+) = Sucesso Extraordinário (permite comprar efeitos extras de bônus, como dano adicional, desarmar, ação rápida ou sigilo).

### 2.2. Empurrar a Rolagem (Orações aos Ícones)
* Se a rolagem falhar ou não obtiver seis suficientes, o jogador pode **Empurrar a Rolagem** fazendo uma oração ao seu Ícone.
* **Mecânica:** Todos os dados que não deram 6 são rerolados.
* **Custo/Consequência:** O jogador **NÃO** sofre dano de atributo ao empurrar. Em vez disso, **concede 1 Ponto de Escuridão (DP) ao Mestre**.

---

## 3. Economia de Jogo: Pontos de Escuridão (Darkness Points / DP)

A mecânica central de tensão do *Terceiro Horizonte* é a gestão de **DP** na mão do Mestre.

* **Como o Mestre ganha DP:**
  1. Sempre que um jogador empurra uma rolagem (+1 DP).
  2. Ao viajar entre sistemas através de Pontos de Salto (*Jump Points*).
  3. Quando os personagens entram em locais profanos, ruínas tomadas pela Ressoa da Escuridão ou violam tabus dos Ícones.
* **Como o Mestre gasta DP:**
  * **Falha de Equipamento / Armas:** Causar emperramento ou esgotamento de munição.
  * **Ataques de Criaturas:** Ativar habilidades sobrenaturais da Ressoa da Escuridão (*Darkbound*).
  * **Complicações Ambientais:** Ativar vácuo repentino, falha de suporte de vida, radiação.
  * **Iniciativa & Reforços:** Fazer inimigos agirem primeiro ou trazer reforços narrativos.

---

## 4. Combate, Dano e Lesões Críticas

### 4.1. Estrutura do Turno
* Teste de Iniciativa ($1d6$ + Agilidade).
* Cada personagem recebe **3 Pontos de Ação (AP)** por turno para distribuir entre Ações Rápidas (1 AP), Ações Normais (2 AP) e Reações/Defesa (1 AP).

### 4.2. Dano e Estado Quebrado (*Broken*)
* **Dano Físico:** Reduz o HP. Se HP chegar a **0**, o personagem fica **Quebrado (*Broken*)**.
  * Um personagem Quebrado não pode agir e deve rolar imediatamente na **Tabela de Lesões Críticas ($d66$)**.
  * Lesões variam de concussões leves a sangramento mortal com cronômetro de minutos/horas para morrer se não receber socorro médico (*Medical*).
* **Dano Mental:** Reduz o MP. Se MP chegar a **0**, o personagem sofre um colapso de estresse/pânico (delírio, paralisia, fuga).

---

## 5. Naves Espaciais & Grupo

* **A Nave da Tripulação:** O grupo começa com uma nave espacial compartilhada de Classe III (ex: Mercante, Exploradora, Patrulha) e uma **Dívida (*Debt*)** substancial com um patrono/banco.
* **Funções na Nave:**
  1. *Capitão:* Concede dados de bônus à equipe via liderança.
  2. *Piloto:* Executa manobras e esquivas.
  3. *Engenheiro:* Distribui energia da pilha de combustível para escudos, armas ou motores.
  4. *Atirador (*Gunner*):* Opera as baterias de armas.
  5. *Operador de Sensores:* Detecta alvos e trava sistemas de travamento de mísseis/mira.
* **Combate Espacial:** Estruturado em fases de Ordens, Manobras, Sensores e Ataque.

---

## 6. Resumo dos Pontos Fortes e Fragilidades Balanceadas (v1)

* **Pontos Fortes:** Rico em ambientação sociopolítica e religiosa; combate espacial excelente; excelente sensação de pertencer a uma tripulação com dívidas reais.
* **Fragilidades / Rigidez:**
  * A divisão entre 8 Perícias Gerais e 8 Avançadas pode engessar certas ações básicas.
  * Falta um sistema granular para exploração a pé / escavação de ruínas (*dungeon crawl*).
  * A economia de DP é 100% focada no Mestre, sem um recurso pessoal direto de Estresse ou Esperança para o jogador além dos pontos de mente.
