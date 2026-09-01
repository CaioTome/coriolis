# -*- coding: utf-8 -*-
import os
import re
import glob

GLOSSARY = {}

def add_gloss(en, pt, category="Mecânica / Conceito"):
    if not en or not pt:
        return
    en = en.strip().strip("*").strip()
    pt = pt.strip().strip("*").strip()
    if not en or not pt or en.lower() == pt.lower():
        return
    if re.match(r"^(d\d+|\d+d\d+|\d+|ex|exemplo|ver|nota|cr|créditos|pv|ca|ba|bba|nt|tl|pe|pjs|pj|mj|gm|km|m|kg)$", en.lower()):
        return
    en = re.sub(r"^[*_`]+|[*_`]+$", "", en).strip()
    pt = re.sub(r"^[*_`]+|[*_`]+$", "", pt).strip()
    if en and pt and en != pt:
        GLOSSARY[en] = (pt, category)

def remove_emojis(text):
    return re.sub(r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|💡|⚔️|🛡️|🚀|🔧|📜|✨|🎲|🪐|👽|🤖|👁️|⚡|💀|💊|🗺️|🛸|💥|🌌", "", text)

def generic_cleanups(text):
    # Standardize GM -> MJ
    text = re.sub(r"\bGM\b", "MJ", text)
    # Remove emojis
    text = remove_emojis(text)
    return text

def process_file_1(text):
    # 1. Introdução.md
    add_gloss("Into the Waiting Night", "Em Direção à Noite Esperançosa", "Capítulo / Título")
    add_gloss("A Word to Newbies", "Uma Palavra aos Iniciantes", "Seção")
    add_gloss("Deluxe Edition", "Edição Deluxe", "Geral")
    add_gloss("Sandbox", "Mundo Aberto / Caixa de Areia", "Estilo de Jogo")
    add_gloss("Game Master (GM)", "Mestre do Jogo (MJ)", "Papel")
    add_gloss("Player Characters (PCs)", "Personagens dos Jogadores (PJs)", "Papel")
    
    text = re.sub(r"# Capítulo 1: Introdução \(Into the Waiting Night\)", r"# Capítulo 1: Introdução", text)
    text = re.sub(r"# EM DIREÇÃO À NOITE ESPERANÇOSA \*\(INTO THE WAITING NIGHT\)\*", r"# EM DIREÇÃO À NOITE ESPERANÇOSA", text)
    text = re.sub(r"> ###\s*💡?\s*Uma Palavra aos Iniciantes\s*\*\(A Word to Newbies\)\*", r"> ### Uma Palavra aos Iniciantes", text)
    text = re.sub(r"\(ou \"MJ\" / \"GM\"\)", r'(ou "MJ")', text)
    text = re.sub(r"\"jogo \*sandbox\*\" \(caixa de areia\)", r'"jogo de mundo aberto" (*sandbox*)', text)
    text = re.sub(r"\bmechs\b", r"mechas", text)
    return text

def process_file_2(text):
    # 2. Criação de Personagens.md
    add_gloss("Character Creation", "Criação de Personagens", "Capítulo")
    add_gloss("Background", "Histórico", "Mecânica")
    add_gloss("Backgrounds", "Históricos", "Mecânica")
    add_gloss("Classes", "Classes", "Mecânica")
    add_gloss("Foci", "Focos", "Mecânica")
    add_gloss("Focus", "Foco", "Mecânica")
    add_gloss("Effort", "Esforço", "Recurso")
    add_gloss("Hit Points (HP)", "Pontos de Vida (PV)", "Recurso")
    add_gloss("Base Attack Bonus (BAB)", "Bônus Base de Ataque (BBA)", "Mecânica")
    add_gloss("Armor Class (AC)", "Classe de Armadura (CA)", "Mecânica")
    add_gloss("Saving Throws", "Salvaguardas", "Mecânica")
    add_gloss("Physical Save", "Salvaguarda Física", "Salvaguarda")
    add_gloss("Evasion Save", "Salvaguarda de Evasão", "Salvaguarda")
    add_gloss("Mental Save", "Salvaguarda Mental", "Salvaguarda")
    add_gloss("Skills", "Perícias", "Mecânica")
    add_gloss("Attributes", "Atributos", "Mecânica")
    add_gloss("Expert", "Especialista", "Classe")
    add_gloss("Warrior", "Guerreiro", "Classe")
    add_gloss("Psychic", "Psíquico", "Classe")
    add_gloss("Adventurer", "Aventureiro", "Classe")
    add_gloss("Noble", "Aristocrata", "Histórico")
    add_gloss("Barbarian", "Bárbaro", "Histórico")
    add_gloss("Clergy", "Clérigo", "Histórico")
    add_gloss("Criminal", "Criminoso", "Histórico")
    add_gloss("Dilettante", "Diletante", "Histórico")
    add_gloss("Entertainer", "Artista", "Histórico")
    add_gloss("Spy", "Espião", "Histórico")
    add_gloss("Peasant", "Camponês", "Histórico")
    add_gloss("Merchant", "Mercador", "Histórico")
    add_gloss("Physician", "Médico", "Histórico")
    add_gloss("Soldier", "Soldado", "Histórico")
    add_gloss("Spacer", "Espacial", "Histórico")
    add_gloss("Official", "Oficial", "Histórico")
    add_gloss("Pilot", "Piloto", "Histórico / Perícia")
    add_gloss("Politician", "Político", "Histórico")
    add_gloss("Scholar", "Erudito", "Histórico")
    add_gloss("Worker", "Trabalhador", "Histórico")
    add_gloss("Scout", "Batedor", "Histórico")
    add_gloss("Technician", "Técnico", "Histórico")
    add_gloss("Vagabond", "Vagabundo", "Histórico")
    add_gloss("Administer", "Administrar", "Perícia")
    add_gloss("Connect", "Conectar", "Perícia")
    add_gloss("Exert", "Esforço Físico", "Perícia")
    add_gloss("Fix", "Consertar", "Perícia")
    add_gloss("Heal", "Curar", "Perícia")
    add_gloss("Know", "Conhecer", "Perícia")
    add_gloss("Lead", "Liderar", "Perícia")
    add_gloss("Notice", "Notar", "Perícia")
    add_gloss("Perform", "Atuar", "Perícia")
    add_gloss("Program", "Programar", "Perícia")
    add_gloss("Punch", "Soco / Desarmado", "Perícia")
    add_gloss("Shoot", "Atirar", "Perícia")
    add_gloss("Sneak", "Furtividade", "Perícia")
    add_gloss("Stab", "Perfurar", "Perícia")
    add_gloss("Survive", "Sobreviver", "Perícia")
    add_gloss("Talk", "Conversar", "Perícia")
    add_gloss("Trade", "Comerciar", "Perícia")
    add_gloss("Work", "Trabalhar", "Perícia")
    add_gloss("Alert", "Alerta", "Foco")
    add_gloss("Armorer", "Armeiro", "Foco")
    add_gloss("Assassin", "Assassino", "Foco")
    add_gloss("Authority", "Autoridade", "Foco")
    add_gloss("Close Combatant", "Combatente Corpo a Corpo", "Foco")
    add_gloss("Connected", "Conectado", "Foco")
    add_gloss("Cybernetic", "Cibernético", "Foco")
    add_gloss("Die Hard", "Duro de Matar", "Foco")
    add_gloss("Diplomat", "Diplomata", "Foco")
    add_gloss("Duelist", "Duelista", "Foco")
    add_gloss("Gunslinger", "Pistoleiro", "Foco")
    add_gloss("Hacker", "Hacker", "Foco")
    add_gloss("Healer", "Curandeiro", "Foco")
    add_gloss("Heavy Metal Specialist", "Especialista em Armas Pesadas", "Foco")
    add_gloss("Ironhide", "Pele de Ferro", "Foco")
    add_gloss("Nullifier", "Nulificador", "Foco")
    add_gloss("Polymath", "Polímata", "Foco")
    add_gloss("Savage", "Selvagem", "Foco")
    add_gloss("Shock Assault", "Assalto de Choque", "Foco")
    add_gloss("Sniper", "Atirador de Elite", "Foco")
    add_gloss("Specialist", "Especialista", "Foco")
    add_gloss("Starfarer", "Navegador Estelar", "Foco")
    add_gloss("Starship Associate", "Tripulante Associado", "Foco")
    add_gloss("Tinkerer", "Engenhoqueiro", "Foco")
    add_gloss("Unarmed Combatant", "Combatente Desarmado", "Foco")
    add_gloss("Wild Psychic Talent", "Talento Psíquico Selvagem", "Foco")
    add_gloss("Combat Medic", "Médico de Combate", "Foco")
    add_gloss("Stealth Master", "Mestre Furtivo", "Foco")

    text = re.sub(r"# Capítulo 2: Criação de Personagens \(Character Creation\)", r"# Capítulo 2: Criação de Personagens", text)
    text = re.sub(r"### 2\.1 Históricos \(Backgrounds\)", r"### 2.1 Históricos", text)
    text = re.sub(r"### 2\.2 Classes \(Classes\)", r"### 2.2 Classes", text)
    text = re.sub(r"### 2\.3 Perícias \(Skills\)", r"### 2.3 Perícias", text)
    text = re.sub(r"### 2\.4 Focos \(Foci\)", r"### 2.4 Focos", text)
    
    text = re.sub(r"\*Histórico\* \(\*Background\*\)", r"*Histórico*", text)
    text = re.sub(r"\*Focos\* \(\*Foci\*\)", r"*Focos*", text)
    text = re.sub(r"\*Esforço\* \(\*Effort\*\)", r"*Esforço*", text)
    text = re.sub(r"Salvaguardas \(\*Saving Throws\*\)", r"Salvaguardas", text)
    text = re.sub(r"Estresse Sistêmico \(\*System Strain\*\)", r"Estresse Sistêmico", text)
    text = re.sub(r"Atributos \(\*Attributes\*\)", r"Atributos", text)
    text = re.sub(r"Históricos \(\*Backgrounds\*\)", r"Históricos", text)
    
    bg_replaces = [
        ("Aristocrata (Noble)", "Aristocrata"),
        ("Bárbaro (Barbarian)", "Bárbaro"),
        ("Clérigo (Clergy)", "Clérigo"),
        ("Criminoso (Criminal)", "Criminoso"),
        ("Diletante (Dilettante)", "Diletante"),
        ("Entretenimento (Entertainer)", "Artista"),
        ("Espião (Spy)", "Espião"),
        ("Fazendeiro (Peasant)", "Camponês"),
        ("Mercador (Merchant)", "Mercador"),
        ("Médico (Physician)", "Médico"),
        ("Militar (Soldier)", "Soldado"),
        ("Navegador (Spacer)", "Espacial"),
        ("Oficial (Official)", "Oficial"),
        ("Piloto (Pilot)", "Piloto"),
        ("Político (Politician)", "Político"),
        ("Professor (Scholar)", "Erudito"),
        ("Provedor (Worker)", "Trabalhador"),
        ("Ranger (Scout)", "Batedor"),
        ("Técnico (Technician)", "Técnico"),
        ("Vagabundo (Vagabond)", "Vagabundo"),
    ]
    for orig, rep in bg_replaces:
        text = text.replace(orig, rep)
        
    skill_replaces = [
        ("Administrar (Administer)", "Administrar"),
        ("Atirar (Shoot)", "Atirar"),
        ("Conectar (Connect)", "Conectar"),
        ("Conhecer (Know)", "Conhecer"),
        ("Consertar (Fix)", "Consertar"),
        ("Conversar (Talk)", "Conversar"),
        ("Curar (Heal)", "Curar"),
        ("Enganar (Sneak)", "Furtividade"),
        ("Exultar (Perform)", "Atuar"),
        ("Liderar (Lead)", "Liderar"),
        ("Navegar (Navigate)", "Navegar"),
        ("Notar (Notice)", "Notar"),
        ("Perfurar (Stab)", "Perfurar"),
        ("Pilotar (Pilot)", "Pilotar"),
        ("Programar (Program)", "Programar"),
        ("Punch / Desarmado (Punch)", "Soco / Desarmado"),
        ("Sobreviver (Survive)", "Sobreviver"),
        ("Trabalhar (Work)", "Trabalhar"),
    ]
    for orig, rep in skill_replaces:
        text = text.replace(orig, rep)
        
    foci_replaces = [
        ("Alerta (Alert)", "Alerta"),
        ("Armas Pesadas (Heavy Metal Specialist)", "Especialista em Armas Pesadas"),
        ("Assassino (Assassin)", "Assassino"),
        ("Atirador de Elite (Sniper)", "Atirador de Elite"),
        ("Autoridade (Authority)", "Autoridade"),
        ("Braço-Forte (Armorer)", "Armeiro"),
        ("Cibernético (Cybernetic)", "Cibernético"),
        ("Conexão (Connected)", "Conectado"),
        ("Corpo a Corpo (Close Combatant)", "Combatente Corpo a Corpo"),
        ("Cura Rápida (Die Hard)", "Duro de Matar"),
        ("Diplomata (Diplomat)", "Diplomata"),
        ("Duelista (Duelist)", "Duelista"),
        ("Especialista (Specialist)", "Especialista"),
        ("Furtivo (Stealth Master)", "Mestre Furtivo"),
        ("Gênio (Gunslinger)", "Pistoleiro"),
        ("Hacker (Hacker)", "Hacker"),
        ("Médico de Combate (Combat Medic)", "Médico de Combate"),
        ("Mente Blindada (Ironhide)", "Pele de Ferro"),
        ("Piloto Estelar (Starfarer)", "Navegador Estelar"),
        ("Polímata (Polymath)", "Polímata"),
        ("Savage / Selvagem (Savage)", "Selvagem"),
        ("Shock Assault / Assalto de Choque (Shock Assault)", "Assalto de Choque"),
        ("Tinkerer / Engenheiro de Sucata (Tinkerer)", "Engenhoqueiro"),
        ("Wild Psychic Talent / Talento Psíquico Selvagem (Wild Psychic Talent)", "Talento Psíquico Selvagem"),
    ]
    for orig, rep in foci_replaces:
        text = text.replace(orig, rep)
        
    class_replaces = [
        ("#### O Especialista (Expert)", "#### O Especialista"),
        ("#### O Guerreiro (Warrior)", "#### O Guerreiro"),
        ("#### O Psíquico (Psychic)", "#### O Psíquico"),
        ("#### O Aventureiro (Adventurer)", "#### O Aventureiro"),
    ]
    for orig, rep in class_replaces:
        text = text.replace(orig, rep)
        
    return text

def process_file_3(text):
    # 3. Psionismo.md
    add_gloss("Psionics", "Psionismo", "Capítulo")
    add_gloss("The Scream", "O Grito", "História")
    add_gloss("The Silence", "O Silêncio", "História")
    add_gloss("Metadimensional Extroversion Syndrome (MES)", "Síndrome de Extroversão Metadimensional (SEM)", "Condição")
    add_gloss("Effort Commitment", "Comprometimento de Esforço", "Mecânica")
    add_gloss("On Turn", "No Turno", "Tempo")
    add_gloss("Scene", "Cena", "Tempo")
    add_gloss("Day", "Dia", "Tempo")
    add_gloss("System Strain", "Estresse Sistêmico", "Condição")
    add_gloss("Core Technique", "Técnica Central", "Psionismo")
    add_gloss("Psychic Discipline", "Disciplina Psíquica", "Psionismo")
    add_gloss("Biopsionics", "Biopsionismo", "Disciplina Psíquica")
    add_gloss("Metapsionics", "Metapsionismo", "Disciplina Psíquica")
    add_gloss("Precognition", "Precognição", "Disciplina Psíquica")
    add_gloss("Telekinesis", "Telecinese", "Disciplina Psíquica")
    add_gloss("Telepathy", "Telepatia", "Disciplina Psíquica")
    add_gloss("Teleportation", "Teletransporte", "Disciplina Psíquica")
    add_gloss("Psychic Succor", "Socorro Psíquico", "Técnica")
    add_gloss("Mastered Succor", "Socorro Aprimorado", "Técnica")
    add_gloss("Metapsionic Ward", "Proteção Metapsiônica", "Técnica")
    add_gloss("Psychic Static", "Estática Psíquica", "Técnica")
    add_gloss("Oracle", "Oráculo", "Técnica")
    add_gloss("Intuitive Response", "Resposta Intuitiva", "Técnica")
    add_gloss("Telekinetic Armory", "Arsenal Telecinético", "Técnica")
    add_gloss("Telekinetic Flight", "Voo Telecinético", "Técnica")
    add_gloss("Telepathic Contact", "Contato Telepático", "Técnica")
    add_gloss("Transmit Thought", "Transmitir Pensamento", "Técnica")
    add_gloss("Personal Apparition", "Aparição Pessoal", "Técnica")
    add_gloss("Burdened Apparition", "Aparição com Carga", "Técnica")
    add_gloss("Torching", "Forçar a Mente / Queimar", "Mecânica Psíquica")

    text = re.sub(r"# Capítulo 3: Psionismo \(Psionics\)", r"# Capítulo 3: Psionismo", text)
    text = re.sub(r"\(The Scream\)", r"", text)
    text = re.sub(r"\(The Silence\)", r"", text)
    text = re.sub(r"\*Esforço Psíquico\* \(\*Effort\*\)", r"*Esforço Psíquico*", text)
    text = re.sub(r"### Esforço Psíquico \(\*Effort\*\)", r"### Esforço Psíquico", text)
    text = re.sub(r"Esforço \(\*Effort\*\)", r"Esforço", text)
    text = re.sub(r"Comprometimento de Esforço \(\*Commitment\*\)", r"Comprometimento de Esforço", text)
    text = re.sub(r"Comprometido pelo Turno \(\*On Turn\*\)", r"Comprometido pelo Turno", text)
    text = re.sub(r"Comprometido pela Cena \(\*Scene\*\)", r"Comprometido pela Cena", text)
    text = re.sub(r"Comprometido pelo Dia \(\*Day\*\)", r"Comprometido pelo Dia", text)
    text = re.sub(r"Estresse Sistêmico \(\*System Strain\*\)", r"Estresse Sistêmico", text)
    text = re.sub(r"Forçar a Mente \(\*Torching\*\)", r"Forçar a Mente (*Torching*)", text)
    
    text = re.sub(r"### 3\.2 Biopsionismo \(Biopsionics\)", r"### 3.2 Biopsionismo", text)
    text = re.sub(r"### 3\.3 Metapsionismo \(Metapsionics\)", r"### 3.3 Metapsionismo", text)
    text = re.sub(r"### 3\.4 Precognição \(Precognition\)", r"### 3.4 Precognição", text)
    text = re.sub(r"### 3\.5 Telecinese \(Telekinesis\)", r"### 3.5 Telecinese", text)
    text = re.sub(r"### 3\.6 Telepatia \(Telepathy\)", r"### 3.6 Telepatia", text)
    text = re.sub(r"### 3\.7 Teletransporte \(Teleportation\)", r"### 3.7 Teletransporte", text)
    
    def clean_tech_line(m):
        pt = m.group(1).strip()
        en = m.group(2).strip()
        add_gloss(en, pt, "Técnica Psíquica")
        return f"- **{pt}**:"
    text = re.sub(r"- \*\*([^\*\(\)]+)\s*\(([A-Za-z\s'\-]+)\)\*\*:", clean_tech_line, text)
    
    return text

def process_file_4(text):
    # 4. Sistemas.md
    add_gloss("Systems", "Sistemas", "Capítulo")
    add_gloss("Skill Checks", "Testes de Perícia", "Mecânica")
    add_gloss("Difficulty Class (DC)", "Classe de Dificuldade (CD)", "Mecânica")
    add_gloss("Aiding a Skill Check", "Ajudar em Teste de Perícia", "Mecânica")
    add_gloss("Opposed Skill Checks", "Testes de Perícia Opostos", "Mecânica")
    add_gloss("Combat", "Combate", "Mecânica")
    add_gloss("Main Action", "Ação Principal", "Combate")
    add_gloss("Move Action", "Ação de Movimento", "Combate")
    add_gloss("On Turn Action", "Ação de Turno", "Combate")
    add_gloss("Instant Action", "Ação Instantânea", "Combate")
    add_gloss("Hitting an Enemy", "Jogada de Ataque", "Combate")
    add_gloss("Shock Damage", "Dano Choque", "Combate")
    add_gloss("Cover", "Cobertura", "Combate")
    add_gloss("Prone Targets", "Alvo Caído", "Combate")
    add_gloss("Execution Attack", "Ataque de Execução", "Combate")
    add_gloss("Injury, Death, and Healing", "Ferimentos, Morte e Cura", "Combate")
    add_gloss("Mortally Wounded", "Mortalmente Ferido", "Condição")
    add_gloss("Stabilization", "Estabilização", "Mecânica")
    add_gloss("Lazarus Patch", "Curativo de Lázaro", "Equipamento")
    add_gloss("Hacking", "Invasão de Redes / Hacking", "Mecânica")
    add_gloss("Data Protocols", "Protocolos de Dados", "Hacking")
    add_gloss("Character Advancement", "Avanço de Personagem", "Mecânica")
    add_gloss("Skill Points (SP)", "Pontos de Perícia (PP)", "Mecânica")
    add_gloss("Environmental Hazards", "Perigos Ambientais", "Regras")
    add_gloss("Falling", "Quedas", "Perigo")
    add_gloss("Poisons", "Venos", "Perigo")
    add_gloss("Diseases", "Doenças e Pragas Interstelares", "Perigo")
    add_gloss("Radiation", "Radiação", "Perigo")
    add_gloss("Hard Vacuum", "Vácuo Rígido e Asfixia", "Perigo")
    add_gloss("System Quick Reference Sheet", "Folha de Referência Rápida dos Sistemas", "Referência")

    text = re.sub(r"# Capítulo 4: Sistemas \(Systems\)", r"# Capítulo 4: Sistemas", text)
    text = re.sub(r"### Salvaguardas \(Saving Throws\)", r"### Salvaguardas", text)
    text = re.sub(r"## 4\.2 Testes de Perícia \(Skill Checks\)", r"## 4.2 Testes de Perícia", text)
    text = re.sub(r"### Testes Cooperativos \(Aiding a Skill Check\)", r"### Testes Cooperativos", text)
    text = re.sub(r"### Testes Opostos \(Opposed Skill Checks\)", r"### Testes Opostos", text)
    text = re.sub(r"## 4\.3 Combate \(Combat\)", r"## 4.3 Combate", text)
    text = re.sub(r"### Jogada de Ataque \(Hitting an Enemy\)", r"### Jogada de Ataque", text)
    text = re.sub(r"### Dano e Dano Choque \(Shock\)", r"### Dano e Dano Choque", text)
    text = re.sub(r"#### Dano Choque \(Shock\)", r"#### Dano Choque", text)
    text = re.sub(r"#### Cobertura \(Cover\)", r"#### Cobertura", text)
    text = re.sub(r"#### Alvo Caído \(Prone Targets\)", r"#### Alvo Caído", text)
    text = re.sub(r"#### Ataque de Execução \(Execution Attack\)", r"#### Ataque de Execução", text)
    text = re.sub(r"## 4\.4 Ferimentos, Morte e Cura \(Injury, Death, and Healing\)", r"## 4.4 Ferimentos, Morte e Cura", text)
    text = re.sub(r"### Chegar a 0 Pontos de Vida \(Mortalmente Ferido\)", r"### Chegar a 0 Pontos de Vida (Mortalmente Ferido)", text)
    text = re.sub(r"### Estresse Sistêmico \(System Strain\)", r"### Estresse Sistêmico", text)
    text = re.sub(r"## 4\.5 Hacking e Redes Eletrônicas \(Hacking\)", r"## 4.5 Hacking e Redes Eletrônicas", text)
    text = re.sub(r"### Protocolos de Dados \(Data Protocols\)", r"### Protocolos de Dados", text)
    text = re.sub(r"## 4\.6 Avanço de Personagem \(Character Advancement\)", r"## 4.6 Avanço de Personagem", text)
    text = re.sub(r"#### 4\. Seleção de Novos Focos \(Foci\)", r"#### 4. Seleção de Novos Focos", text)
    text = re.sub(r"## 4\.7 Perigos Ambientais \(Environmental Hazards\)", r"## 4.7 Perigos Ambientais", text)
    text = re.sub(r"### Quedas \(Falling\)", r"### Quedas", text)
    text = re.sub(r"### Venenos \(Poisons\)", r"### Venenos", text)
    text = re.sub(r"### Doenças e Pragas Interstelares \(Diseases\)", r"### Doenças e Pragas Interstelares", text)
    text = re.sub(r"### Radiação \(Radiation\)", r"### Radiação", text)
    text = re.sub(r"### Vácuo Rígido e Asfixia \(Hard Vacuum\)", r"### Vácuo Rígido e Asfixia", text)
    text = re.sub(r"## 4\.8 Folha de Referência Rápida dos Sistemas \(System Quick Reference Sheet\)", r"## 4.8 Folha de Referência Rápida dos Sistemas", text)
    
    text = re.sub(r"Salvaguardas \(Saving Throws\)", r"Salvaguardas", text)
    text = re.sub(r"Dificuldade \(DC\)", r"Dificuldade (CD)", text)
    text = re.sub(r"Dificuldade \(DC / CD\)", r"Dificuldade (CD)", text)
    text = re.sub(r"\*Ação Principal\* \(\*Main Action\*\)", r"*Ação Principal*", text)
    text = re.sub(r"\*Ação de Movimento\* \(\*Move Action\*\)", r"*Ação de Movimento*", text)
    text = re.sub(r"\*Ações de Turno\* \(\*On Turn Actions\*\)", r"*Ações de Turno*", text)
    text = re.sub(r"\*Ações Instantâneas\* \(\*Instant Actions\*\)", r"*Ações Instantâneas*", text)
    
    return text

def process_file_5(text):
    # 5. Equipamento e Veículos.md
    add_gloss("Equipment and Vehicles", "Equipamento e Veículos", "Capítulo")
    add_gloss("Encumbrance", "Carga e Capacidade de Transporte", "Mecânica")
    add_gloss("Readied Items", "Itens Preparados", "Carga")
    add_gloss("Stowed Items", "Itens Guardados", "Carga")
    add_gloss("Encumbered", "Sobrecarregado", "Carga")
    add_gloss("Lightly Encumbered", "Ligeiramente Sobrecarregado", "Carga")
    add_gloss("Heavily Encumbered", "Gravemente Sobrecarregado", "Carga")
    add_gloss("Maltech", "Maltech (Tecnologia Proibida)", "Tecnologia")
    add_gloss("Unbraked AIs", "IAs Desenfreadas / Sem Trava", "Tecnologia")
    add_gloss("Tech Level (TL)", "Nível Tecnológico (NT)", "Tecnologia")
    add_gloss("Armor", "Armaduras", "Equipamento")
    add_gloss("Weapons & Mods", "Armas e Modificações", "Equipamento")
    add_gloss("Heavy Weapons", "Armas Pesadas", "Armas")
    add_gloss("Stims", "Farmacêuticos / Estimulantes", "Equipamento")
    add_gloss("Drones", "Drones", "Equipamento")
    add_gloss("Cyberware", "Implantes Cibernéticos", "Equipamento")
    add_gloss("Pretech Artifacts", "Artefatos Pretech", "Equipamento")
    add_gloss("Armored Undersuit", "Traje de Tecido Balístico", "Armadura")
    add_gloss("Combat Field Uniform", "Armadura de Combate", "Armadura")
    add_gloss("Armored Vacc Suit", "Traje de Vácuo Blindado", "Armadura")
    add_gloss("Deflector Array", "Armadura de Deflexão", "Armadura")
    add_gloss("Powered Assault Armor", "Armadura Energizada de Assalto", "Armadura")
    add_gloss("Pretech War Suit", "Traje de Guerra Pretech", "Armadura")
    add_gloss("Semi-Auto Pistol", "Pistola Semi-Automática", "Arma")
    add_gloss("Heavy Revolver", "Revólver Pesado", "Arma")
    add_gloss("SMG", "Submetralhadora", "Arma")
    add_gloss("Combat Rifle", "Rifle de Combate", "Arma")
    add_gloss("Shotgun", "Espingarda", "Arma")
    add_gloss("Sniper Rifle", "Rifle de Precisão", "Arma")
    add_gloss("Laser Pistol", "Pistola Laser", "Arma")
    add_gloss("Laser Rifle", "Rifle Laser", "Arma")
    add_gloss("Plasma Pistol", "Pistola de Plasma", "Arma")
    add_gloss("Mag Rifle", "Rifle Magnético", "Arma")
    add_gloss("Mono-blade", "Lâmina Monomolecular", "Arma")
    add_gloss("Stun Baton", "Bastão de Atordoamento", "Arma")
    add_gloss("Rocket Launcher", "Lança-Foguetes", "Arma")
    add_gloss("Heavy Machine Gun", "Metralhadora Pesada", "Arma")
    add_gloss("Autocannon", "Autocanhão", "Arma")

    text = re.sub(r"# Capítulo 5: Equipamento e Veículos \(Equipment and Vehicles\)", r"# Capítulo 5: Equipamento e Veículos", text)
    text = re.sub(r"### Carga e Capacidade de Transporte \(Encumbrance\)", r"### Carga e Capacidade de Transporte", text)
    text = re.sub(r"\* \*\*Itens Preparados \(Readied\)\*\*", r"* **Itens Preparados**", text)
    text = re.sub(r"\* \*\*Itens Guardados \(Stowed\)\*\*", r"* **Itens Guardados**", text)
    text = re.sub(r"#### Penalidades de Sobrecarga \(Encumbered\)", r"#### Penalidades de Sobrecarga", text)
    text = re.sub(r"\* \*\*Ligeiramente Sobrecarregado \(Lightly Encumbered\)\*\*", r"* **Ligeiramente Sobrecarregado**", text)
    text = re.sub(r"\* \*\*Gravemente Sobrecarregado \(Heavily Encumbered\)\*\*", r"* **Gravemente Sobrecarregado**", text)
    text = re.sub(r"#### Tecnologia Proibida \(Maltech\)", r"#### Tecnologia Proibida (Maltech)", text)
    text = re.sub(r"Mandato Terreno \(\*Terran Mandate\*\)", r"Mandato Terreno", text)
    text = re.sub(r"### Níveis Tecnológicos \(Tech Levels - TL\)", r"### Níveis Tecnológicos (NT)", text)
    text = re.sub(r"## 5\.2 Armaduras \(Armor\)", r"## 5.2 Armaduras", text)
    text = re.sub(r"## 5\.3 Armas e Modificações \(Weapons & Mods\)", r"## 5.3 Armas e Modificações", text)
    text = re.sub(r"### Armas Corpo a Corpo e Dano Choque \(Shock\)", r"### Armas Corpo a Corpo e Dano Choque", text)
    text = re.sub(r"#### Dano Choque \(Shock\)", r"#### Dano Choque", text)
    text = re.sub(r"### Armas Pesadas \(Heavy Weapons\)", r"### Armas Pesadas", text)
    text = re.sub(r"#### Farmacêuticos \(Stims\)", r"#### Farmacêuticos", text)
    text = re.sub(r"#### Acessórios e Encaixes de Drones \(Fittings\)", r"#### Acessórios e Encaixes de Drones", text)
    text = re.sub(r"### Implantes Cibernéticos \(Cyberware\)", r"### Implantes Cibernéticos", text)
    text = re.sub(r"#### Armaduras Artefato \(Pretech\)", r"#### Armaduras Artefato Pretech", text)
    text = re.sub(r"#### Armas Artefato \(Pretech\)", r"#### Armas Artefato Pretech", text)
    
    table_items = [
        ("Traje de Tecido Balístico (Armored Undersuit)", "Traje de Tecido Balístico"),
        ("Armadura de Combate (Combat Field Uniform)", "Armadura de Combate"),
        ("Traje de Vácuo Blindado (Armored Vacc Suit)", "Traje de Vácuo Blindado"),
        ("Armadura de Deflexão (Deflector Array)", "Armadura de Deflexão"),
        ("Armadura Energizada de Assalto (Powered Assault Armor)", "Armadura Energizada de Assalto"),
        ("Traje de Guerra Pretech (Pretech War Suit)", "Traje de Guerra Pretech"),
        ("Pistola Semi-Automática (Semi-Auto Pistol)", "Pistola Semi-Automática"),
        ("Revólver Pesado (Heavy Revolver)", "Revólver Pesado"),
        ("Submetralhadora (SMG)", "Submetralhadora"),
        ("Rifle de Combate (Combat Rifle)", "Rifle de Combate"),
        ("Espingarda (Shotgun)", "Espingarda"),
        ("Rifle de Sniper (Sniper Rifle)", "Rifle de Precisão"),
        ("Pistola Laser (Laser Pistol)", "Pistola Laser"),
        ("Rifle Laser (Laser Rifle)", "Rifle Laser"),
        ("Pistola de Plasma (Plasma Pistol)", "Pistola de Plasma"),
        ("Rifle de Magma / Plasma (Mag Rifle)", "Rifle Magnético"),
        ("Faca / Adaga (Knife)", "Faca / Adaga"),
        ("Espada / Lâmina (Sword)", "Espada / Lâmina"),
        ("Clava / Porrete (Club)", "Clava / Porrete"),
        ("Lança / Pique (Spear)", "Lança / Pique"),
        ("Lâmina Monomolecular (Mono-blade)", "Lâmina Monomolecular"),
        ("Maça de Energia (Stun Baton)", "Bastão de Atordoamento"),
        ("Lança-Foguetes (Rocket Launcher)", "Lança-Foguetes"),
        ("Metralhadora Pesada (Heavy Machine Gun)", "Metralhadora Pesada"),
        ("Canhão Automático (Autocannon)", "Autocanhão"),
    ]
    for orig, rep in table_items:
        text = text.replace(orig, rep)

    return text

def process_file_6(text):
    # 6. Naves Espaciais.md
    add_gloss("Starships", "Naves Espaciais", "Capítulo")
    add_gloss("Spike Drive", "Propulsor de Salto (Spike Drive)", "Naves")
    add_gloss("Power", "Energia", "Naves")
    add_gloss("Mass", "Massa", "Naves")
    add_gloss("Hardpoints", "Pontos de Fixação de Armas", "Naves")
    add_gloss("Fittings", "Instalações / Encaixes", "Naves")
    add_gloss("Strike Fighter", "Caça de Ataque", "Casco de Nave")
    add_gloss("Shuttle", "Lançadeira", "Casco de Nave")
    add_gloss("Free Merchant", "Mercador Livre", "Casco de Nave")
    add_gloss("Patrol Boat", "Barco de Patrulha", "Casco de Nave")
    add_gloss("Corvette", "Corveta", "Casco de Nave")
    add_gloss("Heavy Frigate", "Fragata Pesada", "Casco de Nave")
    add_gloss("Bulk Freighter", "Cargueiro Pesado", "Casco de Nave")
    add_gloss("Cruiser", "Cruzador", "Casco de Nave")
    add_gloss("Carrier", "Porta-Naves", "Casco de Nave")
    add_gloss("Battleship", "Couraçado", "Casco de Nave")
    add_gloss("Armored Bulkhead", "Antepara Blindada", "Instalação de Nave")
    add_gloss("Cargo Space", "Espaço de Carga", "Instalação de Nave")
    add_gloss("Emissions Dampener", "Amortecedor de Emissões", "Instalação de Nave")
    add_gloss("Fuel Bunkers", "Tanques de Combustível Extras", "Instalação de Nave")
    add_gloss("Fuel Scoops", "Coletores de Combustível", "Instalação de Nave")
    add_gloss("Hydroponic Production", "Produção Hidropônica", "Instalação de Nave")
    add_gloss("Survey Sensors", "Sensores de Varredura", "Instalação de Nave")
    add_gloss("Workshop", "Oficina de Reparos", "Instalação de Nave")
    add_gloss("Sandthrower", "Lançador de Areia", "Arma de Nave")
    add_gloss("Flak Emitter", "Emissor Antiaéreo (Flak)", "Arma de Nave")
    add_gloss("Multifocal Laser", "Laser Multifocal", "Arma de Nave")
    add_gloss("Reaper Battery", "Bateria Ceifadora", "Arma de Nave")
    add_gloss("Plasma Beam", "Feixe de Plasma", "Arma de Nave")
    add_gloss("Mag Cannon", "Canhão Magnético", "Arma de Nave")
    add_gloss("Torpedo Launcher", "Lançador de Torpedos", "Arma de Nave")
    add_gloss("Spike Drill", "Salto de Propulsão / Salto Hiperespacial", "Viagem Espacial")

    text = re.sub(r"# Capítulo 6: Naves Espaciais \(Starships\)", r"# Capítulo 6: Naves Espaciais", text)
    text = re.sub(r"### Motores de Salto \(Spike Drive\)", r"### Propulsor de Salto (Spike Drive)", text)
    text = re.sub(r"### Energia \(Power\)", r"### Energia", text)
    text = re.sub(r"### Massa \(Mass\)", r"### Massa", text)
    text = re.sub(r"### Pontos de Armamento \(Hardpoints\)", r"### Pontos de Fixação de Armamento", text)
    text = re.sub(r"### Acessórios de Nave \(Fittings\)", r"### Instalações de Nave", text)
    text = re.sub(r"### Armas de Bordo \(Weapons\)", r"### Armas de Bordo", text)
    text = re.sub(r"### Viagem Interestelar e Saltos \(Drill\)", r"### Viagem Interestelar e Saltos", text)
    text = re.sub(r"### Combate Espacial \(Space Combat\)", r"### Combate Espacial", text)
    
    return text

def process_file_7(text):
    # 7. A História do Espaço.md
    add_gloss("The History of Space", "A História do Espaço", "Capítulo")
    add_gloss("Jump Gates", "Portais de Salto", "História")
    add_gloss("Terran Mandate", "Mandato Terreno", "História")
    add_gloss("Psionic Authority", "Autoridade Psiônica", "História")
    add_gloss("The Like", "Os Semelhantes (Alienígenas)", "História")
    add_gloss("The Others", "Os Outros (Alienígenas Incompreensíveis)", "História")
    
    text = re.sub(r"# Capítulo 7: A História do Espaço \(The History of Space\)", r"# Capítulo 7: A História do Espaço", text)
    text = re.sub(r"Portais de Salto \(\*Jump Gates\*\)", r"Portais de Salto (*Jump Gates*)", text)
    text = re.sub(r"\(Terran Mandate\)", r"", text)
    text = re.sub(r"\(Psionic Authority - PA\)", r"", text)
    text = re.sub(r"\(The Like\)", r"", text)
    text = re.sub(r"\(The Others\)", r"", text)
    text = re.sub(r"\(The Scream\)", r"", text)
    return text

def process_file_8(text):
    # 8. Criação de Setor.md
    add_gloss("Sector Creation", "Criação de Setor", "Capítulo")
    add_gloss("World Tags", "Etiquetas de Mundo / Tags de Mundo", "Geração de Setor")
    add_gloss("Primary World", "Mundo Principal", "Geração de Setor")
    add_gloss("Atmosphere", "Atmosfera", "Geração de Setor")
    add_gloss("Temperature", "Temperatura", "Geração de Setor")
    add_gloss("Biosphere", "Biosfera", "Geração de Setor")
    add_gloss("Population", "População", "Geração de Setor")
    add_gloss("Tech Level", "Nível Tecnológico", "Geração de Setor")
    
    text = re.sub(r"# Capítulo 8: Criação de Setor \(Sector Creation\)", r"# Capítulo 8: Criação de Setor", text)
    text = re.sub(r"\(\*Drill\*\)", r"", text)
    text = re.sub(r"\(\*Spike Drive\*\)", r"", text)
    text = re.sub(r"\(\*Primary World\*\)", r"", text)
    return text

def process_file_9(text):
    # 9. Criação de Aventuras.md
    add_gloss("Adventure Creation", "Criação de Aventuras", "Capítulo")
    add_gloss("Sandbox Adventure Structure", "Estrutura de Aventuras Sandbox", "Mestrado")
    add_gloss("Enemy", "Inimigo", "Elemento de Aventura")
    add_gloss("Friend", "Amigo / Aliado", "Elemento de Aventura")
    add_gloss("Complication", "Complicação", "Elemento de Aventura")
    add_gloss("Thing", "Coisa / Objeto", "Elemento de Aventura")
    add_gloss("Place", "Lugar", "Elemento de Aventura")
    add_gloss("Adventure Hook", "Gancho de Aventura", "Elemento de Aventura")
    add_gloss("Adventure Rewards", "Recompensas de Aventura", "Mestrado")
    
    text = re.sub(r"# Capítulo 9: Criação de Aventuras \(Adventure Creation\)", r"# Capítulo 9: Criação de Aventuras", text)
    text = re.sub(r"### 9\.1 Estrutura de Aventuras Sci-Fi \(Sandbox Adventure Structure\)", r"### 9.1 Estrutura de Aventuras Sci-Fi", text)
    text = re.sub(r"\(\*Enemy\*\)", r"", text)
    text = re.sub(r"\(\*Friend\*\)", r"", text)
    text = re.sub(r"\(\*Complication\*\)", r"", text)
    text = re.sub(r"\(\*Thing\*\)", r"", text)
    text = re.sub(r"\(\*Place\*\)", r"", text)
    text = re.sub(r"\(\*Hook\*\)", r"", text)
    text = re.sub(r"\(\*Motivation & Want\*\)", r"", text)
    text = re.sub(r"### 9\.2 Recompensas de Aventura \(Adventure Rewards\)", r"### 9.2 Recompensas de Aventura", text)
    return text

def process_file_10(text):
    # 10. Xenobestiário.md
    add_gloss("Xenobestiary", "Xenobestiário", "Capítulo")
    add_gloss("Hit Dice (HD)", "Dados de Vida (DV / HD)", "Estatística")
    add_gloss("Morale", "Moral", "Estatística")
    add_gloss("Move", "Deslocamento", "Estatística")
    add_gloss("Attack Bonus", "Bônus de Ataque", "Estatística")
    add_gloss("Alien Creation", "Criação de Alienígenas", "Regras")
    
    text = re.sub(r"# Capítulo 10: Xenobestiário \(Xenobestiary\)", r"# Capítulo 10: Xenobestiário", text)
    text = re.sub(r"\(Dados de Vida / HD\)", r"(Dados de Vida - DV)", text)
    text = re.sub(r"\(Classe de Armadura / AC\)", r"(Classe de Armadura - CA)", text)
    text = re.sub(r"\(Move\)", r"(Deslocamento)", text)
    text = re.sub(r"\(Moral\)", r"(Moral)", text)
    return text

def process_file_11(text):
    # 11. Facções.md
    add_gloss("Factions", "Facções", "Capítulo")
    add_gloss("Faction Turn", "Turno de Facção", "Mecânica")
    add_gloss("Force", "Força", "Atributo de Facção")
    add_gloss("Cunning", "Astúcia", "Atributo de Facção")
    add_gloss("Wealth", "Economia / Riqueza", "Atributo de Facção")
    add_gloss("FacCreds", "Créditos de Facção", "Recurso de Facção")
    add_gloss("Bases of Influence", "Bases de Influência", "Facções")
    add_gloss("Faction Assets", "Recursos de Facção / Ativos", "Facções")
    add_gloss("Military Unit", "Unidade Militar", "Ativo de Facção")
    add_gloss("Special Forces", "Forças Especiais", "Ativo de Facção")
    add_gloss("Starship", "Nave de Facção", "Ativo de Facção")
    add_gloss("Smugglers", "Contrabandistas", "Ativo de Facção")
    add_gloss("Informers", "Informantes", "Ativo de Facção")
    add_gloss("Saboteurs", "Sabotadores", "Ativo de Facção")
    add_gloss("Guerilla Populace", "População Guerrilheira", "Ativo de Facção")
    add_gloss("Party Machine", "Máquina Partidária", "Ativo de Facção")

    text = re.sub(r"# Capítulo 11: Facções \(Factions\)", r"# Capítulo 11: Facções", text)
    text = re.sub(r"\(Force\)", r"", text)
    text = re.sub(r"\(Cunning\)", r"", text)
    text = re.sub(r"\(Wealth\)", r"", text)
    text = re.sub(r"\(Hit Points / HP\)", r"(Pontos de Vida - PV)", text)
    text = re.sub(r"\(Bases of Influence\)", r"", text)
    text = re.sub(r"\(Faction Assets\)", r"", text)
    text = re.sub(r"\(Military Unit\)", r"", text)
    text = re.sub(r"\(Special Forces\)", r"", text)
    text = re.sub(r"\(Starship\)", r"", text)
    return text

def process_file_12(text):
    # 12. Recursos do Mestre.md
    add_gloss("Game Master Resources", "Recursos do Mestre", "Capítulo")
    add_gloss("PC Death", "Morte de Personagens", "Mestrado")
    add_gloss("House Rules", "Regras da Casa", "Mestrado")
    add_gloss("One-Roll NPCs", "Gerador Rápido de PNJs", "Gerador")
    add_gloss("Patrons", "Patronos", "Gerador")
    
    text = re.sub(r"# Capítulo 12: Recursos do Mestre \(Game Master Resources\)", r"# Capítulo 12: Recursos do Mestre", text)
    text = re.sub(r"\(PC Death\)", r"", text)
    text = re.sub(r"\(\*Lazarus Patches\*\)", r"(*Curativos de Lázaro*)", text)
    text = re.sub(r"\(House Rules\)", r"", text)
    text = re.sub(r"\(One-Roll NPCs\)", r"", text)
    return text

def process_file_13(text):
    # 13. Campanhas Trans-humanas.md
    add_gloss("Transhuman Campaigns", "Campanhas Trans-humanas", "Capítulo")
    add_gloss("Hard vs. Soft Singularities", "Singularidades Rígidas vs. Flexíveis", "Cenário")
    add_gloss("Hard Singularity", "Singularidade Rígida", "Cenário")
    add_gloss("Soft Singularity", "Singularidade Flexível", "Cenário")
    add_gloss("Transhuman Soul", "Alma Trans-humana", "Mecânica")
    add_gloss("Face", "Prestígio (Face)", "Recurso Trans-humano")
    add_gloss("Shell / Sleeve", "Invólucro (Shell)", "Trans-humanismo")
    add_gloss("Organic Shells", "Invólucros Orgânicos", "Trans-humanismo")
    add_gloss("Mechanical Shells", "Invólucros Mecânicos", "Trans-humanismo")
    add_gloss("Digital Shells", "Invólucros Digitais", "Trans-humanismo")
    add_gloss("The Net", "A Rede", "Trans-humanismo")
    add_gloss("Digital Combat", "Combate Digital", "Trans-humanismo")

    text = re.sub(r"# Capítulo 13: Campanhas Trans-humanas \(Transhuman Campaigns\)", r"# Capítulo 13: Campanhas Trans-humanas", text)
    text = re.sub(r"\(Hard vs\. Soft Singularities\)", r"", text)
    text = re.sub(r"\(Hard Singularity\)", r"", text)
    text = re.sub(r"\(Soft Singularity\)", r"", text)
    text = re.sub(r"\(Transhuman Soul\)", r"", text)
    text = re.sub(r"\(\*Soul\*\)", r"", text)
    text = re.sub(r"\(\*Shell\* / \*Sleeve\*\)", r"", text)
    return text

def process_file_14(text):
    # 14. Magia Espacial.md
    add_gloss("Space Magic", "Magia Espacial", "Capítulo")
    add_gloss("Space Fantasy", "Fantasia Espacial", "Gênero")
    add_gloss("Magic Skill", "Perícia Mágica", "Perícia")
    add_gloss("The Arcanist", "O Arcanista", "Classe")
    add_gloss("The Magister", "O Magíster", "Classe")
    add_gloss("The Adept", "O Adepto", "Classe")
    add_gloss("Incandescent Order", "Ordem Incandescente", "Tradição Mágica")
    add_gloss("The Light Within", "A Luz Interior", "Tradição Mágica")
    add_gloss("Arcanist Spells", "Magias de Arcanista", "Magia")
    add_gloss("Magister Spells", "Magias de Magíster", "Magia")

    text = re.sub(r"# Capítulo 14: Magia Espacial \(Space Magic\)", r"# Capítulo 14: Magia Espacial", text)
    text = re.sub(r"\(Magic Skill\)", r"", text)
    text = re.sub(r"\(The Arcanist\)", r"", text)
    text = re.sub(r"\(The Magister\)", r"", text)
    text = re.sub(r"\(The Adept\)", r"", text)
    text = re.sub(r"\(Incandescent Order\)", r"", text)
    return text

def process_file_15(text):
    # 15. Personagens Heróicos.md
    add_gloss("Heroic Characters", "Personagens Heróicos", "Capítulo")
    add_gloss("Heroic Warrior", "Guerreiro Heróico", "Classe Heróica")
    add_gloss("Heroic Expert", "Especialista Heróico", "Classe Heróica")
    add_gloss("Heroic Psychic", "Psíquico Heróico", "Classe Heróica")
    add_gloss("Heroic Adventurer", "Aventureiro Heróico", "Classe Heróica")
    add_gloss("Fray Die", "Dado de Combate / Dado de Atrito (Fray Die)", "Combate Heróico")
    add_gloss("Heroic Defiance", "Desafio Heróico", "Habilidade Heróica")

    text = re.sub(r"# Capítulo 15: Personagens Heróicos \(Heroic Characters\)", r"# Capítulo 15: Personagens Heróicos", text)
    text = re.sub(r"\(Heroic Warrior\)", r"", text)
    text = re.sub(r"\(Heroic Expert\)", r"", text)
    text = re.sub(r"\(Heroic Psychic\)", r"", text)
    text = re.sub(r"\(Heroic Adventurer\)", r"", text)
    return text

def process_file_16(text):
    # 16. Inteligências Artificiais Verdadeiras.md
    add_gloss("True Artificial Intelligences", "Inteligências Artificiais Verdadeiras", "Capítulo")
    add_gloss("Quantum Core", "Núcleo Quântico", "IA")
    add_gloss("Unbraked AI", "IA Desenfreada / Sem Trava", "IA")
    add_gloss("Firstborn Pact", "Pacto dos Primogênitos", "História de IA")
    add_gloss("Brakes", "Travas Psíquicas / Freios", "IA")
    add_gloss("Perimeter Agencies", "Agências do Perímetro", "Facção")
    add_gloss("Armatures", "Armações / Corpos de IA", "IA")
    add_gloss("Synth", "Sintético (Corpo)", "Armação de IA")
    add_gloss("Sledge", "Trombadinha / Trenó (Corpo Pesado)", "Armação de IA")

    text = re.sub(r"# Capítulo 16: Inteligências Artificiais Verdadeiras \(True Artificial Intelligences\)", r"# Capítulo 16: Inteligências Artificiais Verdadeiras", text)
    text = re.sub(r"\(Quantum Core\)", r"", text)
    text = re.sub(r"\(Firstborn Pact\)", r"", text)
    text = re.sub(r"\(Brakes\)", r"", text)
    text = re.sub(r"\(Armatures\)", r"", text)
    return text

def process_file_17(text):
    # 17. Sociedades.md
    add_gloss("Societies", "Sociedades", "Capítulo")
    add_gloss("One-Roll Origins", "Gerador Rápido de Origens", "Sociedades")
    add_gloss("One-Roll Rulers", "Gerador Rápido de Governantes", "Sociedades")
    add_gloss("One-Roll Ruled", "Gerador Rápido de Governados", "Sociedades")
    add_gloss("Flavoring the Society", "Ambientação da Sociedade", "Sociedades")
    add_gloss("One-Roll Society Flavor", "Gerador Rápido de Traços Culturais", "Sociedades")

    text = re.sub(r"# Capítulo 17: Sociedades \(Societies\)", r"# Capítulo 17: Sociedades", text)
    text = re.sub(r"\(One-Roll Origins\)", r"", text)
    text = re.sub(r"\(One-Roll Rulers\)", r"", text)
    text = re.sub(r"\(One-Roll Ruled\)", r"", text)
    text = re.sub(r"\(Flavoring the Society\)", r"", text)
    text = re.sub(r"\(One-Roll Society Flavor\)", r"", text)
    return text

def process_file_18(text):
    # 18. Mechas.md
    add_gloss("Mechas", "Mechas", "Capítulo")
    add_gloss("Quantum Tap ECM", "ECM de Salto Quântico", "Tecnologia Mecha")
    add_gloss("Pretech Neural Interfaces", "Interfaces Neurais Pretech", "Tecnologia Mecha")
    add_gloss("Suit Mecha", "Traje Mecha", "Chassi de Mecha")
    add_gloss("Light Mecha", "Mecha Leve", "Chassi de Mecha")
    add_gloss("Heavy Mecha", "Mecha Pesado", "Chassi de Mecha")
    add_gloss("Shock Suit", "Traje de Assalto / Traje de Choque", "Projeto Mecha")
    add_gloss("Light Psimech", "Psimecha Leve", "Projeto Mecha")
    add_gloss("Power Stress", "Estresse de Reator / Energia", "Regras de Mecha")
    add_gloss("Escape Pod", "Cápsula de Escape", "Módulo de Mecha")
    add_gloss("Neural Sensors", "Sensores de Atividade Neural", "Módulo de Mecha")
    add_gloss("Psimech Interface", "Interface Psimecha", "Módulo de Mecha")
    add_gloss("Jump Jets", "Jatos de Salto", "Módulo de Mecha")
    add_gloss("Force Shield", "Escudo de Força", "Módulo de Mecha")

    text = re.sub(r"# Capítulo 18: Mechas \(Mechas\)", r"# Capítulo 18: Mechas", text)
    text = re.sub(r"# Capítulo 18: Mechs \(Mechs\)", r"# Capítulo 18: Mechas", text)
    text = re.sub(r"\(Quantum Tap ECM\)", r"", text)
    text = re.sub(r"\(Pretech Neural Interfaces\)", r"", text)
    text = re.sub(r"\(Suit Mecha\)", r"", text)
    text = re.sub(r"\(Light Mecha\)", r"", text)
    text = re.sub(r"\(Heavy Mecha\)", r"", text)
    text = re.sub(r"\(Power Stress\)", r"", text)
    text = re.sub(r"\(Mech Weapons\)", r"", text)
    text = re.sub(r"\(Mech Weaponry\)", r"", text)
    text = re.sub(r"\(Mecha Weaponry\)", r"", text)
    text = re.sub(r"\(Mecha Hulls\)", r"", text)
    text = re.sub(r"\(Mech Weapon\)", r"", text)
    text = re.sub(r"\(Mecha Weapon\)", r"", text)
    text = re.sub(r"\(Hull Class\)", r"", text)
    text = re.sub(r"\(Escape Pod\)", r"", text)
    text = re.sub(r"\(Neural Sensors\)", r"", text)
    text = re.sub(r"\(Psimech Interface\)", r"", text)
    text = re.sub(r"\(Jump Jets\)", r"", text)
    text = re.sub(r"\(Force Shield\)", r"", text)
    text = re.sub(r"\(Shock Suit\)", r"", text)
    text = re.sub(r"\(Light Psimech\)", r"", text)
    
    return text

def process_file_19(text):
    # 19. Índice.md
    add_gloss("Index", "Índice", "Capítulo")
    text = re.sub(r"# Capítulo 19: Índice \(Index\)", r"# Capítulo 19: Índice", text)
    text = re.sub(r"# ÍNDICE REMISSIVO DE TERMOS \(INDEX\)", r"# ÍNDICE REMISSIVO DE TERMOS", text)
    
    # Process each index line: - **Termo em Português** (*English Term*) — Págs. X–Y
    def index_replacer(m):
        pt = m.group(1).strip()
        en = m.group(2).strip()
        rest = m.group(3)
        add_gloss(en, pt, "Índice Remissivo")
        return f"- **{pt}**{rest}"
        
    text = re.sub(r"^-\s+\*\*([^\*]+)\*\*\s+\(\*([^\*]+)\*\)(.*)$", index_replacer, text, flags=re.MULTILINE)
    
    # Process indented sub-items:   - Subtermo (*English*) — Pág. X
    def subindex_replacer(m):
        indent = m.group(1)
        pt = m.group(2).strip()
        en = m.group(3).strip()
        rest = m.group(4)
        add_gloss(en, pt, "Índice Remissivo")
        return f"{indent}- {pt}{rest}"

    text = re.sub(r"^(\s+)-\s+([^\(\n]+)\s+\(\*([^\*\)]+)\*\)(.*)$", subindex_replacer, text, flags=re.MULTILINE)
    
    return text

def process_all_files():
    files_map = {
        "1. Introdução.md": process_file_1,
        "2. Criação de Personagens.md": process_file_2,
        "3. Psionismo.md": process_file_3,
        "4. Sistemas.md": process_file_4,
        "5. Equipamento e Veículos.md": process_file_5,
        "6. Naves Espaciais.md": process_file_6,
        "7. A História do Espaço.md": process_file_7,
        "8. Criação de Setor.md": process_file_8,
        "9. Criação de Aventuras.md": process_file_9,
        "10. Xenobestiário.md": process_file_10,
        "11. Facções.md": process_file_11,
        "12. Recursos do Mestre.md": process_file_12,
        "13. Campanhas Trans-humanas.md": process_file_13,
        "14. Magia Espacial.md": process_file_14,
        "15. Personagens Heróicos.md": process_file_15,
        "16. Inteligências Artificiais Verdadeiras.md": process_file_16,
        "17. Sociedades.md": process_file_17,
        "18. Mechas.md": process_file_18,
        "19. Índice.md": process_file_19,
    }
    
    base_dir = "content/1. Estrelas Incontáveis"
    for fname, proc in files_map.items():
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            print(f"Aviso: {fpath} não encontrado.")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        cleaned = proc(content)
        cleaned = generic_cleanups(cleaned)
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Processado: {fname}")

def generate_glossary_file():
    glossary_path = "dev/Glossário-stars-without-number.md"
    
    sorted_terms = sorted(GLOSSARY.items(), key=lambda x: x[0].lower())
    
    md = []
    md.append("# Glossário de Termos — Stars Without Number (PT-BR)")
    md.append("")
    md.append("> **Documento de Padronização Terminológica**  ")
    md.append("> *Este arquivo reúne as escolhas de tradução dos termos técnicos, mecânicos e conceituais de Stars Without Number (Revised & Deluxe Edition) para a adaptação em Português Brasileiro.*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Tabela de Correspondência Terminológica")
    md.append("")
    md.append("| Palavra Original (EN) | Tradução Oficial PT-BR | Categoria / Contexto |")
    md.append("| :--- | :--- | :--- |")
    
    for en, (pt, cat) in sorted_terms:
        md.append(f"| **{en}** | {pt} | {cat} |")
        
    md.append("")
    
    with open(glossary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
        
    print(f"Glossário gerado com {len(sorted_terms)} termos em {glossary_path}")

if __name__ == "__main__":
    print("Iniciando processamento completo de limpeza e glossário...")
    process_all_files()
    generate_glossary_file()
    print("Processamento concluído com sucesso!")
