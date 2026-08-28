# Análise Mecânica: A Grande Escuridão (Coriolis v2)

> **Relatório Técnico do Agente Analista 2**  
> *Este documento detalha as regras de criação de personagem, mecânicas modernizadas da YZE, sistema de Esperança/Estresse e a arquitetura de Delving/Expedição de "Coriolis: A Grande Escuridão".*

---

## 1. Criação de Personagens & Atributos (YZE v2)

### 1.1. Filosofia do Design
* *A Grande Escuridão* redireciona a escala do jogo: sai a tripulação de nave mercantil navegando por rotas comerciais e entra a **Companhia de Exploradores/Escavadores (*Delvers*)** adentrando ruínas alienígenas dos Construtores em um horizonte hostil, congelado ou escuro.

### 1.2. Atributos (4)
Mantém os 4 pilares fundamentais da Year Zero Engine:
* **Força (*Might / Strength*):** Vigor físico, resistência a ambientes extremos e capacidade de carga.
* **Agilidade (*Agility*):** Mobilidade em ruínas, esquiva, combate e manipulação de ferramentas de precisão.
* **Raciocínio (*Wits*):** Análise de tecnologia ancestral, decifração de glifos, orientação e astúcia.
* **Empatia / Vontade (*Empathy / Will*):** Força de vontade, liderança, coesão da expedição e resistência ao desespero.

### 1.3. Lista de Perícias Enxugada (12 Perícias)
Diferente da v1, a v2 elimina a separação rígida entre "Gerais" e "Avançadas". Todas as perícias usam a mesma mecânica direta e qualquer personagem pode tentar qualquer ação (embora sem treino use apenas o Atributo):

| Atributo Base | Perícias Enxugadas (v2) | Função na Expedição |
| :--- | :--- | :--- |
| **Força** | Combate Melee, Vigor/Resistência (*Endurance*) | Luta corporal, suportar fadiga e cargas pesadas |
| **Agilidade** | Combate Distância, Mobilidade (*Mobility*), Furtividade (*Stealth*) | Escalada, esquiva, uso de armas de longo alcance, sigilo |
| **Raciocínio** | Percepção (*Awareness*), Sobrevivência/Orientação, Investigação/Tecnologia | Detecção de armadilhas/biomorfos, uso de scanners, decifração |
| **Empatia** | Persuasão/Liderança, Medicina/Socorro, Intuição | Manter o moral do grupo, tratar ferimentos, sentir ameaças |

### 1.4. Traços de Sobrevivência & Talentos
* **Talentos de Expedição:** Habilidades voltadas para a exploração de ruínas, uso avançado de relíquias, gestão de recursos e suporte em combate.
* **Pontos de Esperança (*Hope*):** Um recurso individual ganho durante os descansos ou momentos de forte determinação/conexão. Pode ser gasto para:
  * Adicionar dados bônus a rolagens cruciais.
  * Ativar talentos de sobrevivência avançados.
  * Negar efeitos de medo ou desespero na expedição.

---

## 2. Espinha Dorsal Mecânica & Economia de Tensão

### 2.1. O Teste de Dados & Empurrar Rolagens (YZE Moderna)
* **Pilha Base:** $\text{Atributo} + \text{Perícia} + \text{Equipamento}$.
* **Empurrar a Rolagem:** 
  * O jogador pode empurrar a rolagem re-rolando os dados que não deram 6.
  * **Consequência Directa:** Empurrar **NÃO** concede Pontos de Escuridão ao Mestre imediatamente. Em vez disso, acumula **Estresse (*Strain / Stress*)** diretamente no personagem ou adiciona **Dados de Estresse** à pilha.

### 2.2. A Tríade de Tensão: Estresse, Desespero e Ruína

```
  ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
  │    Estresse     │ ────► │    Desespero    │ ────► │     Ruína       │
  │ (Acúmulo Pessoal│       │ (Testes Pânico/ │       │ (Contaminação   │
  │  ao empurrar)   │       │  Perca Moral)   │       │  Alien/Morte)   │
  └─────────────────┘       └─────────────────┘       └─────────────────┘
```

1. **Estresse (*Stress*):** Aumenta o risco de testes subsequentes. Se o jogador rolar um **1** nos dados de estresse durante um teste empurrado, ocorre um **Surto de Pânico / Complicação de Expedição**.
2. **Desespero (*Despair*):** Quando o estresse atinge o limite ou a expedição sofre traumas graves (perda de luz, colapso de estrutura).
3. **Ruína (*Ruin / Contamination*):** Ao explorar estruturas mais profundas dos Construtores ou interagir com artefatos instáveis, o personagem acumula Ruína, podendo sofrer mutações, insanidade permanente ou degeneração biológica.

---

## 3. O Sistema de *Delving* (Exploração de Ruínas & Expedição)

Esta é a principal adição mecânica de *A Grande Escuridão*, inexistente na versão 1:

### 3.1. Turnos de Escavação (*Delve Turns*)
* A exploração dentro de ruínas alienígenas é dividida em **Turnos de Exploração** (cada turno dura ~10 a 15 minutos de tempo narrativo).
* Em cada turno, a expedição declara uma **Ação de Exploração**:
  * *Avançar / Mapear* (abrir novo setor da ruína).
  * *Procurar / Escavar* (buscar relíquias, suprimentos ou saídas).
  * *Analisar Glifos / Relíquias* (decifrar tecnologia dos Construtores).
  * *Descansar / Forcar Ponto de Apoio* (recuperar estresse e estabilizar trajes).

### 3.2. A Escala da Escuridão & Recursos Consumíveis (*Resource Dice*)
* **Dados de Recursos ($d6, d8, d10, d12$):** Suprimentos (Oxigênio, Luz/Energia, Rações, Baterias) são gerenciados via Dados de Recurso.
  * Após um uso prolongado ou turno de exploração, rola-se o Dado de Recurso. Se sair **1 ou 2**, o dado decai para um tamanho menor (ex: $d10 \to d8 \to d6 \to \text{Esgotado}$).
* **Hazards Ambientais:** Regras explícitas para frio extremo, atmosferas tóxicas, vácuo, gravidade anômala e colapsos estruturais.

---

## 4. Combate & Criaturas (Biomorfos)

* **Combate Dinâmico:** Estrutura de iniciativa por cartas ou dados rápidos, sem a contagem rígida de 3 AP da v1, priorizando fluidez e perigo iminente.
* **Biomorfos & Abominações:** Inimigos em *A Grande Escuridão* possuem tabelas de ataques aleatórios e imprevisíveis. Ataques alienígenas frequentemente causam **Ruína** ou **Estresse** direto além de dano físico.

---

## 5. Resumo dos Pontos Fortes e Fragilidades Balanceadas (v2)

* **Pontos Fortes:**
  * Sistema de exploração de ruínas (*Delving*) brilhante e tenso.
  * Regras de Estresse/Esperança e Dados de Recursos tornam a gestão de sobrevivência muito envolvente.
  * Lista de Perícias mais enxuga e ágil.
* **Fragilidades / Lacunas em Relação à v1:**
  * Menos foco e suporte para intrigas geopolíticas amplas entre Facções no Terceiro Horizonte.
  * Regras de Naves Espaciais e Viagem Intersetorial reduzidas (foco é nas expedições terrestres/fronteira).
