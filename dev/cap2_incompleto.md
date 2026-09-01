Listed directory coriolis
Listed directory livros
Listed directory dev
Listed directory 2.%20Cria%C3%A7%C3%A3o%20de%20Personagem
Ran command: `python3 -c "
import pypdf
print('pypdf installed')
" 2>/dev/null || python3 -c "
import fitz
print('PyMuPDF installed')
" 2>/dev/null || which pdftotext || echo "no direct pdf tool"`
Ran command: `python3 -c "
for mod in ['pypdf', 'pypdf2', 'fitz', 'pdfplumber', 'pypdf4']:
    try:
        __import__(mod)
        print(f'{mod}: available')
    except ImportError:
        pass
"`
Viewed 2.%20Cria%C3%A7%C3%A3o%20de%20Personagens.md:1-75
Viewed 2.1.%20Profiss%C3%B5es.md:1-364
Viewed 2.2.%20Classes.md:1-49
Viewed 2.3.%20Focos.md:1-100
Viewed 2.4.%20Per%C3%ADcias.md:1-76
Viewed 2.5.%20Estat%C3%ADsticas%20e%20Equipamento.md:1-69
Ran command: `python3 -c "
import subprocess

# Let's check page count and search for Chapter 1 / Character creation in the PDF using pdftotext
# Let's extract first 40 pages to text
subprocess.run(['pdftotext', '-f', '1', '-l', '40', 'livros/pdfcoffee.com_stars-without-number-revised-deluxe-edition-pdf-free.pdf', 'dev/pdf_pages_1_40.txt'])
with open('dev/pdf_pages_1_40.txt') as f:
    text = f.read()

print('Length of extracted text:', len(text))
# print table of contents or first occurrences of Chapter / Character Creation
for line in text.split('\n')[:80]:
    print(line)
"`
Ran command: `python3 -c "
import subprocess

# Let's extract pages 1 to 32 to dev/swn_char_creation.txt with pdftotext
subprocess.run(['pdftotext', '-f', '5', '-l', '32', 'livros/pdfcoffee.com_stars-without-number-revised-deluxe-edition-pdf-free.pdf', 'dev/swn_char_creation.txt'])

with open('dev/swn_char_creation.txt') as f:
    text = f.read()

print('Length:', len(text))
lines = text.split('\n')
for i, line in enumerate(lines):
    if line.strip().isupper() and len(line.strip()) > 3:
        print(f'Line {i}: {line.strip()}')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print(f'Total pages extracted: {len(pages)}')
for idx, page in enumerate(pages):
    first_lines = [l.strip() for l in page.split('\n') if l.strip()][:3]
    print(f'Page {idx+5}:', ' | '.join(first_lines))
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    text = f.read()

pages = text.split('\x0c')

for i, p in enumerate(pages):
    print(f'=== PAGE {i+1} (Book page {i+3}) ===')
    print(p[:300].strip())
    print('...')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

# Let's inspect pages 1 to 27
for i in range(len(pages)):
    lines = [l for l in pages[i].split('\n') if l.strip()]
    header = lines[0] if lines else 'EMPTY'
    print(f'=== Page index {i} (PDF page {i+5}, Book page {i+1 if i < 2 else i}) : {header} (Lines: {len(lines)}) ===')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

# Let's inspect Page index 2, 3, 4, 5 (Pages 2-6 in book)
print('=================== PAGE 2 & 3 & 4 & 5: INTRO, SUMMARY, ATTRIBUTES ===================')
for p_idx in [2, 3, 4, 5]:
    print(f'--- Page index {p_idx} ---')
    print(pages[p_idx])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== PAGE 3 (Book page 4) ===================')
print(pages[3])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== PAGE 6 & 7 (Book pages 7-8: Skills) ===================')
print(pages[6])
print('-----------------------------------------')
print(pages[7])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== PAGE 8 (Book page 9: Choosing a Background) ===================')
print(pages[8])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

# Pages 9 to 14 of PDF extraction are Book pages 10 to 15
for p in range(9, 15):
    print(f'=== Page index {p} (Book page {p+1}) ===')
    print(pages[p])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

for p in range(9, 15):
    text = pages[p]
    print(f'=== PAGE {p+1} ===')
    for line in text.split('\n'):
        if line.strip() in ['Barbarian', 'Clergy', 'Courtesan', 'Criminal', 'Dilettante', 'Entertainer', 'Merchant', 'Noble', 'Official', 'Peasant', 'Physician', 'Pilot', 'Politician', 'Scholar', 'Soldier', 'Spacer', 'Technician', 'Thug', 'Vagabond', 'Worker']:
            print('-> Background:', line.strip())
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

import re

# Let's extract each background block from book pages 10 to 15 (page index 9 to 14)
full_bg_text = '\n'.join(pages[9:15])

# Print all background names found
bg_matches = re.findall(r'(Barbarian|Clergy|Courtesan|Criminal|Dilettante|Entertainer|Merchant|Noble|Official|Peasant|Physician|Pilot|Politician|Scholar|Soldier|Spacer|Technician|Thug|Vagabond|Worker)', full_bg_text)
print('Backgrounds found in PDF:', set(bg_matches), 'Total count:', len(bg_matches))
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

bg_pages = '\n'.join(pages[9:15])

# Let's write a parser to extract each of the 20 backgrounds cleanly
# We know the 20 backgrounds in order from page 9 table:
order = ['Barbarian', 'Clergy', 'Courtesan', 'Criminal', 'Dilettante', 'Entertainer', 'Merchant', 'Noble', 'Official', 'Peasant', 'Physician', 'Pilot', 'Politician', 'Scholar', 'Soldier', 'Spacer', 'Technician', 'Thug', 'Vagabond', 'Worker']

for name in order:
    pos = bg_pages.find(name + '\n\n')
    if pos == -1:
        pos = bg_pages.find(name + '\n')
    print(f'=== {name} (found at {pos}) ===')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== BOOK PAGES 16-18: CHARACTER CLASSES ===================')
for p in [15, 16, 17]:
    print(f'--- Book Page {p+1} ---')
    print(pages[p])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== BOOK PAGES 19-23: FOCI ===================')
for p in range(18, 23):
    print(f'--- Book Page {p+1} ---')
    print(pages[p])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

foci_text = '\n'.join(pages[18:23])

# List all Foci in the book
import re
foci_names = ['Alert', 'Armsmaster', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat', 'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Origin Focus', 'Psychic Training', 'Savage Fray', 'Shocking Assault', 'Sniper', 'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Unique Gift', 'Wanderer', 'Wild Psychic Talent']

for f in foci_names:
    found = f in foci_text
    print(f'{f}: {found}')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

foci_text = '\n'.join(pages[18:23])

# Let's find all focus names
lines = foci_text.split('\n')
for i, l in enumerate(lines):
    if l.startswith('Level 1:') or l.startswith('Level 1 :'):
        # The focus name is the previous non-empty line
        for k in range(i-1, -1, -1):
            if lines[k].strip() and not lines[k].strip().startswith('Foci') and not lines[k].strip().startswith('The Focus List'):
                # find the header
                # let's look further up until previous focus
                name = lines[k].strip()
                # print
                print(f'Focus detected: {name}')
                break
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

foci_text = '\n'.join(pages[18:23])

# Let's inspect some of the foci mechanics in the book vs markdown
# E.g. Assassin, Die Hard, Hacker, Specialist, Armsman, Close Combatant
for f_name in ['Alert', 'Armsman', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat', 'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Psychic Training', 'Savage Fray', 'Shocking Assault', 'Sniper', 'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Unique Gift', 'Wanderer', 'Wild Psychic Talent']:
    pos = foci_text.find(f_name)
    if pos != -1:
        # print next 300 chars
        snippet = foci_text[pos:pos+350].replace('\n', ' ')
        print(f'*** {f_name} ***:\n{snippet}\n')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

foci_text = '\n'.join(pages[18:24])

import re

# Let's see all focus names and level 1 / level 2 descriptions in the original text
foci_list = ['Alert', 'Armsman', 'Assassin', 'Authority', 'Close Combatant', 'Connected', 'Die Hard', 'Diplomat', 'Gunslinger', 'Hacker', 'Healer', 'Henchkeeper', 'Ironhide', 'Psychic Training', 'Savage Fray', 'Shocking Assault', 'Sniper', 'Specialist', 'Star Captain', 'Starfarer', 'Tinker', 'Unarmed Combatant', 'Unique Gift', 'Wanderer', 'Wild Psychic Talent']

for f in foci_list:
    # find where f is on a line by itself
    match = re.search(r'\n(' + f + r')\s*\n', foci_text)
    if match:
        idx = match.start()
        print(f'=== FOCUS: {f} ===')
        print(foci_text[idx:idx+700].strip())
        print('-'*40)
    else:
        print(f'=== FOCUS: {f} NOT FOUND DIRECTLY ===')
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== BOOK PAGES 24-25: FINAL TOUCHES & EQUIPMENT PACKAGES ===================')
print(pages[23])
print('-----------------------------------------')
print(pages[24])
"`
Ran command: `python3 -c "
with open('dev/swn_char_creation.txt') as f:
    pages = f.read().split('\x0c')

print('=================== BOOK PAGES 26-27: QUICK CHARACTER CREATION ===================')
print(pages[25])
print('-----------------------------------------')
print(pages[26])
"`

Apresento a revisão minuciosa e exaustiva de cada arquivo presente no diretório `content/1. Estrelas Incontáveis/2. Criação de Personagem/`, comparando o conteúdo atual com o texto integral do livro original (*Stars Without Number: Revised Edition*, páginas 3 a 27).

---

## 1. Visão Geral da Auditoria

A estrutura atual contém resumos, omissões de parágrafos narrativos/exemplos de jogo, adulterações em regras mecânicas fundamentais e a ausência de seções inteiras presentes no livro original.

Abaixo está o detalhamento arquivo por arquivo de todo o conteúdo faltante, incompleto ou incorreto.

---

## 2. Revisão Detalhada por Arquivo

### Arquivo 1: `2. Criação de Personagens.md`
*(Correspondente às páginas 3 a 6 do livro original: Introdução, Resumo do Processo e Atributos)*

* **Passo a Passo Incompleto (Livro original pp. 4-5):**
  * O livro original estabelece **18 passos detalhados**, acompanhados de anotações do diagrama da ficha de personagem.
  * O arquivo atual resume o processo em apenas 8 passos rápidos, omitindo regras como:
    * Regra de acumulação de perícias na criação (1ª escolha = Nível 0, 2ª escolha = Nível 1, 3ª escolha = permite trocar por qualquer outra perícia não-psíquica, com teto máximo de Nível 1 no 1º nível).
    * Focos de Origem para alienígenas, IVs (Inteligências Virtuais) e IAs Verdadeiras (Passo 8 original).
    * Cálculo detalhado de BBA, CA base (10 + Modificador de Destreza), bônus de armas de energia (+1 no ataque) e determinação de metas e motivações iniciais do herói (Passo 18 original).
* **Ausência do Exemplo Narrativo Completo ("Simon's Example" - Livro p. 6):**
  * Falta toda a narrativa de exemplo do jogador Simon rolando seus atributos (rolagens 10, 4, 13, 16, 8, 7), a substituição do valor 4 por 14 em Destreza, o cálculo dos modificadores e as implicações de interpretação (como uma Sabedoria 8).
* **Explicações Complementares de Atributos:**
  * Falta a explicação sobre variações e alterações de atributos durante o jogo (por ferimentos incapacitantes, avanço de nível ou foco).

---

### Arquivo 2: `2.1. Profissões.md`
*(Correspondente às páginas 9 a 15 do livro original: Escolhendo um Antecedente e os 20 Antecedentes)*

* **Ausência dos Textos Introdutórios e Normas de Antecedentes (Livro p. 9):**
  * Falta o texto de introdução sobre a origem dos aventureiros, escolha de mundo natal e a regra para antecedentes customizados com o Mestre.
  * Falta a seção **"Treinamento de Perícias e Atributos"** (*Training Skills and Attributes*), que explica como funcionam as entradas "Qualquer Perícia", "Qualquer Perícia de Combate" e o teto de valor 18 nos atributos.
  * Falta a seção **"Antecedentes, Perícias e Crescimento"** (*Backgrounds, Skills, and Growth*), detalhando a escolha entre Perícias Rápidas, 2 perícias da tabela de Aprendizado ou 3 rolagens divididas entre Crescimento e Aprendizado.
  * Falta a **Tabela d20 de Antecedentes** para rolagem aleatória.
* **Dois Antecedentes Originais Estão Faltando:**
  * **Vagabundo / Andarilho (*Vagabond*):** Não consta no arquivo. Possui Perícia Gratuita: Sobreviver-0; Perícias Rápidas: Sobreviver-0, Furtividade-0, Perceber-0; Tabelas de Crescimento (1d6) e Aprendizado (1d8).
  * **Trabalhador / Operário (*Worker*):** Não consta no arquivo. Possui Perícia Gratuita: Trabalho-0; Perícias Rápidas: Conectar-0, Exercitar-0, Trabalho-0; Tabelas de Crescimento (com +1 em Qualquer Atributo de 1 a 4) e Aprendizado (com regra especial permitindo substituir Trabalho por outra perícia como Administrar ou Programar de acordo com a função do operário).
* **Antecedentes Inventados / Não-Oficiais Presentes no Arquivo:**
  * O antecedente **"Aristocrata"** (inserido no início) e o antecedente **"Sucateiro"** (inserido na posição 16) não existem no livro original de *Stars Without Number* (os conceitos originais correspondentes são *Noble*, *Dilettante*, *Vagabond* e *Worker*).
* **Adulteração Grave nas Tabelas de Crescimento (1d6):**
  * No livro oficial, as tabelas de crescimento possuem resultados flexíveis: **`+2 Físico`** (permite somar +2 em FOR, DES ou CON, ou dividir +1/+1 entre dois atributos físicos) e **`+2 Mental`** (permite somar +2 em INT, SAB ou CAR, ou dividir +1/+1 entre dois atributos mentais).
  * No arquivo markdown, esses resultados foram substituídos por atributos fixos e arbitrários (como `+2 em Força`, `+2 em Sabedoria`, `+2 em Destreza`), eliminando a liberdade de escolha do jogador e alterando as regras originais.
* **Divergências nas Perícias Rápidas e Tabelas de Aprendizado:**
  * Há divergências nas listas de perícias de antecedentes como Clérigo, Cortesã, Soldado, Espacialista, Técnico e Capanga.

---

### Arquivo 3: `2.2. Classes.md`
*(Correspondente às páginas 16 a 18 do livro original: Classes de Personagem)*

* **Texto Introdutório Geral Ausente (Livro p. 16):**
  * O texto de introdução do capítulo sobre as vocações dos aventureiros não foi incluído.
* **Erros e Omissões no Especialista (Livro p. 17):**
  * Falta a regra que permite ao Especialista aplicar seus dois focos iniciais de 1º nível no mesmo foco não-combatente para começar o jogo com o Nível 2 desse foco.
  * Falta a especificação de que o ponto de perícia bônus recebido ao subir de nível só pode ser gasto em perícias não-combatentes e não-psíquicas (ou guardado para uso futuro).
* **Erros Mecânicos Críticos no Psíquico (Livro p. 17):**
  * **Fórmula de Esforço Incorreta:** O arquivo traz `1 + Maior Modificador de INT ou SAB + Maior Nível de Perícia Psíquica`. No livro original, a fórmula oficial é:
    $$\text{Esforço Máximo} = 1 + \text{Maior Nível de Perícia Psíquica} + \text{Maior Modificador entre Sabedoria ou Constituição}$$
    *(Inteligência não faz parte do cálculo de Esforço; usa-se Sabedoria ou Constituição).*
  * Falta a regra de que o Esforço Máximo nunca pode ser inferior a 1, mesmo com modificadores negativos.
  * O arquivo afirma incorretamente que o Psíquico ganha 1 ponto de perícia bônus exclusivo para psionismo por nível (essa regra não existe no livro básico; houve confusão com a habilidade de Especialista).
  * Falta o texto descritivo sobre a Síndrome de Extroversão Metadimensional (SEM), os perigos do uso sem treinamento e as consequências históricas do Grito.
* **Omissões no Guerreiro (Livro p. 18):**
  * Na habilidade *Sorte do Veterano*, foram omitidas as restrições obrigatórias: ela não pode ser usada contra danos ambientais, efeitos que não exigem jogada de ataque ou ataques direcionados a veículos ocupados pelo guerreiro.
  * Falta a regra permitindo gastar os dois focos iniciais de 1º nível para iniciar com Nível 2 em um foco de combate.
* **Erros Mecânicos Críticos no Aventureiro (Livro p. 18):**
  * **Parcial Especialista:** O arquivo afirma que ganha *Mestre de Perícia* 1x/dia. No livro original, a classe parcial **não recebe** a habilidade *Mestre de Perícia*; recebe 1 foco não-combatente gratuito e +1 ponto de perícia extra por nível.
  * **Parcial Guerreiro:** O arquivo afirma que ganha *Sorte do Veterano* 1x/dia e que seu BBA é `Nível - 1`. No livro original, a classe parcial **não recebe** *Sorte do Veterano*; seu BBA é de meio nível padrão, recebendo **+1 bônus fixo no BBA no 1º nível e no 5º nível**, além de 1 foco de combate gratuito e +2 PV por nível.
  * **Parcial Psíquico:** Falta a restrição explícita de que um Parcial Psíquico só pode escolher uma única disciplina psíquica e **nunca** poderá aprender ou evoluir outras disciplinas psíquicas durante toda a campanha.

---

### Arquivo 4: `2.3. Focos.md`
*(Correspondente às páginas 19 a 23 do livro original: Escolhendo um Foco e Lista de Focos)*

* **Ausência do Texto Introdutório e Exemplo Narrativo (Livro pp. 19-20):**
  * Falta a explicação sobre aquisição de focos durante a progressão de níveis (ganhos nos níveis 2, 5, 7 e 10).
  * Falta o exemplo narrativo de criação do personagem Basil escolhendo os focos Franco-atirador e Pistoleiro.
* **7 Focos Oficiais Completamente Ausentes do Arquivo:**
  O livro original contém 25 focos. O arquivo atual lista apenas 18. Faltam os seguintes 7 focos:
  1. **Combate Feroz (*Savage Fray*):** Causa Dano de Choque a todos os oponentes adjacentes não atacados no final do turno (Nível 1); no Nível 2 o choque afeta qualquer CA e o primeiro ataque corpo a corpo contra você na rodada erra automaticamente.
  2. **Investida Agressiva / Ataque Chocante (*Shocking Assault*):** Trata todos os alvos como CA 10 para fins de Dano de Choque (Nível 1); no Nível 2 adiciona +2 ao Dano de Choque de todas as armas corpo a corpo e acertos normais nunca causam menos dano do que o valor de Choque.
  3. **Capitão Estelar (*Star Captain*):** Concede Liderar e +2 Pontos de Comando por turno à nave (Nível 1); no Nível 2 adiciona +20% de PV temporários à nave no início do combate e permite resolver uma Crise de nave como Ação Instantânea.
  4. **Combatente Desarmado (*Unarmed Combatant*):** Concede Soco, dano desarmado escala com o nível de Soco (1d6 a 1d12+1) com Dano de Choque (Nível 1); no Nível 2 ataques contam como TL4 contra armaduras avançadas e causam 1d6 mesmo em caso de erro.
  5. **Dom Único (*Unique Gift*):** Regra e diretrizes para criar poderes e traços exóticos cibernéticos, transumanos ou mutantes.
  6. **Andarilho (*Wanderer*):** Concede Sobreviver, comunicação básica em qualquer idioma e facilidade para obter transporte interestelar gratuito (Nível 1); no Nível 2 permite forjar autorizações e documentos de viagem com 1d6 horas de trabalho.
  7. **Talento Psíquico Selvagem (*Wild Psychic Talent*):** Regras completas para personagens não-psíquicos que manifestam uma única habilidade psíquica inata com 1 ou 2 pontos de Esforço máximo.
* **Mecânicas Incompletas/Alteradas nos Focos Existentes:**
  * **Especialista em Perícia (*Specialist*):** No Nível 2, o livro original determina rolar **4d6 e descartar os dois menores dados** (o arquivo afirmava incorretamente que elevava o nível numérico da perícia).
  * **Pele de Ferro (*Ironhide*):** O livro original estabelece CA natural base de **15 + metade do nível** (Nível 1) e **17 + metade do nível** (Nível 2).
  * **Combatente Próximo (*Close Combatant*):** Omitida a imunidade a Dano de Choque corporal no Nível 2.
  * **Franco-atirador (*Sniper*):** Omitida a aplicação estrita a Ataques de Execução com armas de disparo/arcos.
  * **Engenhoqueiro (*Tinker*):** Omitidas as regras de pontuação de Manutenção (*Maintenance score*) e redução de peças de salvamento pré-tecnologia (*pretech salvage*).

---

### Arquivo 5: `2.4. Perícias.md`
*(Correspondente às páginas 7 e 8 do livro original: Perícias e Lista de Perícias)*

* **Ausência da Seção "Testes de Perícia" (*Skill Checks* - Livro p. 7):**
  * Falta o texto que detalha a competência inerente dos personagens (atividades rotineiras do histórico do herói nunca exigem teste, como um fazendeiro operando condensadores de umidade ou a herdeira corporativa analisando relatórios).
  * Falta a explicação formal da fórmula de rolagem de perícia: $2d6 + \text{Modificador de Atributo} + \text{Nível de Perícia}$ contra a Dificuldade estipulada pelo Mestre.
  * Falta o detalhamento sobre tarefas que exigem treinamento obrigatório (Nível 0 mínimo).
* **Ausência da Seção de Sobreposição de Perícias (Livro p. 8):**
  * Falta a explicação sobre o escopo amplo das perícias e situações de sobreposição (exemplo de destravar um canhão disruptor emperrado usando *Consertar* ou *Atirar*).
* **Ausência Completa das Perícias Psíquicas (*Psychic Skills* - Livro p. 8):**
  * O arquivo contém apenas as 19 perícias mundanas, omitindo totalmente a lista e a descrição das **6 Perícias Psíquicas**:
    1. *Biopsionismo* (*Biopsionics*)
    2. *Metapsionismo* (*Metapsionics*)
    3. *Precognição* (*Precognition*)
    4. *Telecinese* (*Telekinesis*)
    5. *Telepatia* (*Telepathy*)
    6. *Teletransporte* (*Teleportation*)
  * Falta a regra de restrição de compra e avanço dessas perícias durante a criação de personagem.

---

### Arquivo 6: `2.5. Estatísticas e Equipamento.md`
*(Correspondente às páginas 24 e 25 do livro original: Toques Finais e Pacotes de Equipamento)*

* **Ausência da Regra de Perícia Livre de Interesse Pessoal (Livro p. 24):**
  * Falta a regra do passo final que concede **1 escolha livre de perícia não-psíquica** no Nível 0 (ou elevação para Nível 1) representando hobbies, estudos particulares ou talentos secundários.
* **Ausência da Caixa de Texto: "Personagens e Idiomas" (*PCs and Languages* - Livro p. 24):**
  * Toda a seção de regras de idiomas foi omitida:
    * Idioma Mandato (*Mandate*) como língua franca padrão.
    * Idiomas nativos do mundo natal e histórico.
    * Idiomas adicionais baseados em *Conhecimento* (*Know*) ou *Conectar* (*Connect*): +1 no Nível 0, +3 no Nível 1, +6 no Nível 2, +10 no Nível 3 e todos os idiomas conhecidos do setor no Nível 4.
* **Créditos Iniciais Incorretos:**
  * O arquivo indica rolar `3d6 x 100` Créditos. O livro oficial determina rolar **`2d6 x 100` Créditos** (200 a 1.200 créditos).
* **Regras de Combate de Armas de Energia e Dano de Choque:**
  * Falta a regra que concede **+1 bônus nas jogadas de ataque** para armas de energia a distância (lasers/plasma) devido à ausência de recuo e balística de vento.
* **Pacotes de Equipamento Incompletos e Adulterados (Livro p. 25):**
  * O livro original possui **10 pacotes prontos**:
    1. Bárbaro (*Barbarian*)
    2. Espadachim / Duelista (*Blade*)
    3. Ladrão (*Thief*)
    4. Hacker (*Hacker*)
    5. Pistoleiro (*Gunslinger*)
    6. Soldado (*Soldier*)
    7. Batedor (*Scout*)
    8. Médico (*Medic*)
    9. Civil (*Civilian*)
    10. Técnico (*Technician*)
  * O arquivo atual possui apenas 6 pacotes, omitindo os pacotes de *Batedor*, *Civil*, *Espadachim* e alterando os itens e créditos dos pacotes existentes.

---

## 3. Conteúdo do Livro Original Não Criado no Diretório

* **Criação Rápida de Personagens (*Quick Character Creation* - Livro pp. 26-27):**
  * Trata-se de um sistema completo de 2 páginas no livro original para criação imediata de personagens através de tabelas aleatórias e matrizes pré-calculadas para arquétipos de Especialistas (*Smart*, *Smooth*, *Nimble*), Guerreiros (*Melee*, *Ranged*, *Leader*) e Psíquicos (*Seer*, *Adept*), com matrizes de atributos, histórico d20, disciplinas d6, focos 1d6 e perícia bônus d20.
  * Esse sistema não possui arquivo próprio e não consta em nenhum ponto da pasta atual.

---

## 4. Síntese dos Erros Mecânicos e Ações Necessárias

| Arquivo | Problema Crítico Identificado | Correção Obrigatória |
| :--- | :--- | :--- |
| `2. Criação de Personagens.md` | Processo resumido (8 passos em vez de 18); omissão de exemplos narrativos. | Expandir para os 18 passos integrais e traduzir o exemplo narrativo de Simon. |
| `2.1. Profissões.md` | Falta *Vagabond* e *Worker*; inclusão indevida de *Aristocrata* e *Sucateiro*; tabelas de crescimento adulteradas. | Restaurar os 20 antecedentes oficiais, corrigir as opções flexíveis `+2 Físico` e `+2 Mental` e incluir textos introdutórios/tabela d20. |
| `2.2. Classes.md` | Esforço Psíquico calculado com INT (em vez de SAB/CON); Aventureiros parciais com habilidades inexistentes no original. | Corrigir fórmulas de Esforço e restaurar as regras autênticas de Especialista Parcial e Guerreiro Parcial. |
| `2.3. Focos.md` | 7 focos ausentes; mecânicas de Nível 2 alteradas em Especialista, Pele de Ferro, etc. | Traduzir e incluir os 7 focos faltantes e ajustar as descrições mecânicas exatas de Nível 1 e Nível 2. |
| `2.4. Perícias.md` | Omissão das 6 Perícias Psíquicas e do sistema de testes de perícia (2d6). | Incluir regras de testes de perícia, casos de sobreposição e a lista completa de Perícias Psíquicas. |
| `2.5. Estatísticas e Equipamento.md` | Omissão de Idiomas e da perícia livre de hobby; apenas 6 pacotes de itens; créditos iniciais incorretos (`3d6` em vez de `2d6`). | Inserir a seção de Idiomas, corrigir a rolagem de créditos para `2d6 x 100` e restaurar os 10 pacotes originais. |