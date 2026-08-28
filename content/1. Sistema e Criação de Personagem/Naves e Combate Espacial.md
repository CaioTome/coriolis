---
title: Combate Espacial & Naves (Dual-Engine)
---

# Naves Espaciais e o Modelo "Dual-Engine"

A interação com naves espaciais é o coração da aventura. A versão unificada usa a lógica **Dual-Engine** para lidar com isso:

* **No Espaço (Camada Espacial):** Adota as regras clássicas de O Terceiro Horizonte para manutenção, dívida da nave, posições da tripulação e combate tático.
* **Nas Ruínas (Camada Terrestre):** Quando desembarcados, entra em cena o sistema de exploração (veja [[Coriolis/Exploração de Ruínas]]).

---

## 1. A Nave como Personagem

Toda tripulação começa com uma nave espacial em dívida. Ela possui Atributos Básicos:
* **Casco:** Integridade estrutural (Pontos de Casco - PC). Zere-o e a nave sofre Dano Crítico.
* **Energia:** Pontos de Energia (PE) gerados pelo reator a cada turno.
* **Manobrabilidade:** Bônus (ou redutor) aplicados ao Piloto.
* **Assinatura:** Quão fácil é travar a mira na nave pelos Sensores inimigos.
* **Blindagem:** O equivalente da Armadura; reduz o dano sofrido por cada '6' rolado.

---

## 2. As Fases Táticas e a Tripulação

O combate espacial exige cooperação. Cada jogador assume uma estação de comando. A ordem do turno é dividida em 5 fases sequenciais:

### Fase 1: O Capitão (Liderança)
O Capitão dita as ordens. Ele não gasta Energia.
* **Ordem de Comando (Liderança):** Rolagem de Liderança. Cada sucesso gera **1 Dado de Comando** que qualquer membro da tripulação pode usar como bônus neste turno.

### Fase 2: O Engenheiro (Tecnologia)
O Engenheiro gerencia a refrigeração do Reator e aloca a Energia.
* **Alocar Energia:** O Reator gera X Pontos de Energia por turno. O Engenheiro os distribui para Escudos, Armas e Motores.
* **Sobrecarga (Tecnologia):** Rola Tecnologia. Sucessos geram PE adicionais temporários, mas falhar gera Estresse e pode causar falha mecânica.
* **Reparos em Combate:** Gasta seu turno para consertar Dano Crítico em um subsistema.

### Fase 3: O Operador de Sensores (Investigação)
Sem Sensores, o atirador está cego.
* **Travar Mira (Investigação):** Rola Investigação contra a Assinatura inimiga. Se tiver sucesso, a nave inimiga está "Travada". O Atirador recebe +1d6 para disparar Torpedos.
* **Guerra Eletrônica (Investigação):** Destrói a trava de mira do inimigo na sua nave, forçando-os a rolar de novo ou atirar às cegas (-3d6).

### Fase 4: O Piloto (Pilotagem)
Controla os propulsores e a posição tática. Exige Energia nos motores.
* **Manobra de Aproximação/Fuga (Pilotagem):** Tenta mudar a faixa de distância (Curto, Médio, Longo Alcance).
* **Ação Evasiva (Pilotagem):** Cada sucesso gera penalidade de -1d6 para todos os ataques inimigos contra a nave nesta rodada. Consome muita energia.

### Fase 5: O Atirador (Combate a Distância)
Opera as baterias de armas. Requer Energia nas Armas.
* **Disparar Canhões:** Rola Combate a Distância (modificado pela trava dos Sensores e Manobrabilidade do alvo). Se o dano passar da Blindagem, atinge os Pontos de Casco.

---

## 3. Armamento Naval

| Arma de Nave | Custo de Energia | Dano Base | Crítico | Alcance | Traços / Efeitos |
| :--- | :---: | :---: | :---: | :--- | :--- |
| Canhão Acelerador Leve | 1 PE | 1 | 3 | Curto | - |
| Bateria de Torpedos | 2 PE | 3 | 1 | Longo | O alvo precisa estar Travado. Destrói Blindagem permanentemente. |
| Canhão de Íons | 3 PE | 1 | 2 | Médio | Dano diretamente na Energia do inimigo, não no Casco. |
| Feixe Térmico | 2 PE | 2 | 2 | Curto | Perfurante (Ignora 2 pontos de Blindagem). |

---

## 4. Tabela de Lesões Críticas em Naves (d66)

Quando o Casco (PC) chega a 0, ou uma arma com Valor de Crítico obtém sucessos suficientes, rola-se o Dano Crítico da Nave. Se a nave sofrer mais de 3 danos críticos não reparados, ela explode.

| d66 | Subsistema Atingido | Efeito Mecânico | Reparo Necessário |
| :---: | :--- | :--- | :--- |
| 11-16 | Vazamento de Gás | A Manobrabilidade da nave cai -1. | Tecnologia (Fácil) |
| 21-25 | Pane de Sensores | Operador de Sensores perde a tela. Não pode travar mira. | Tecnologia (Normal) |
| 26-33 | Curto-Circuito nas Armas | Uma arma aleatória pifa e não pode disparar. | Tecnologia (Difícil) |
| 34-42 | Falha nos Suportes de Vida | Descompressão lenta. Tripulação tem d6 Turnos para vestir os Exo-Shells. | Tecnologia (Normal) |
| 43-52 | Sobrecarga do Reator | A geração de Pontos de Energia cai pela metade. A nave pisca no escuro. | Engenheiro no local |
| 53-62 | Incêndio no Convés | Tripulantes sofrem 1 de Dano físico por rodada até apagar o fogo. | Rolar Vigor |
| 63-65 | Brecha no Casco | Sugados para o vácuo. Rolagem de Vigor ou Mobilidade ou **morte imediata**. | Tecnologia (Difícil) |
| 66 | Colapso do Reator Módulo Zero | A nave vira poeira estelar instantaneamente. Fim de jogo. | - |

---

## 5. Combate Simplificado via Dados de Recurso (Regra Opcional)

Para combates menores ou mesas mais focadas na exploração (A Grande Escuridão), use o modo "Cinemático":
* A nave possui apenas um **Dado de Casco** (d8) e um **Dado de Energia** (d10).
* Manobras difíceis forçam rolagem do Dado de Energia. Se cair 1-2, o dado degrada (d10 vira d8).
* Ao tomar tiros, rola-se o Dado de Casco. Quando ele chegar a d4 e degradar, a nave sofre Dano Crítico letal direto (Rola 66).
