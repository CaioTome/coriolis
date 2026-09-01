# -*- coding: utf-8 -*-
"""
Script de Tradução e Limpeza Completa - Stars Without Number (PT-BR)
Revisa todos os 19 arquivos de 'content/1. Estrelas Incontáveis/',
traduz todos os termos e frases em inglês remanescentes,
remove resquícios de inglês entre parênteses ou em itálico,
e atualiza o dev/Glossário-stars-without-number.md.
"""
import os
import re
import glob

GLOSSARY = {}

def add_gloss(en, pt, cat="Geral"):
    en = en.strip().strip("*`").strip()
    pt = pt.strip().strip("*`").strip()
    if not en or not pt or en.lower() == pt.lower():
        return
    if re.match(r"^(d\d+|\d+d\d+|\d+|ex|exemplo|ver|nota|cr|créditos|pv|ca|ba|bba|nt|tl|pe|pjs|pj|mj|km|m|kg)$", en.lower()):
        return
    GLOSSARY[en] = (pt, cat)

def load_existing_glossary():
    path = "dev/Glossário-stars-without-number.md"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^\|\s*\*\*([^\*]+)\*\*\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|", line)
            if m:
                en = m.group(1).strip()
                pt = m.group(2).strip()
                cat = m.group(3).strip()
                add_gloss(en, pt, cat)

# --- 1. Introdução.md ---
def clean_file_1(text):
    add_gloss("Exchange of Light", "Bolsa da Luz", "Economia / História")
    add_gloss("Old-School Renaissance (OSR)", "Renascença Clássica / Old-School (OSR)", "Sistema")
    text = re.sub(r"\*Exchange of Light\*", "Bolsa da Luz", text)
    text = re.sub(r"\bExchange of Light\b", "Bolsa da Luz", text)
    return text

# --- 2. Criação de Personagens.md ---
def clean_file_2(text):
    repls = [
        ("Vagabond", "Vagabundo"),
        ("Warrior", "Guerreiro"),
        ("Merchant", "Mercador"),
        ("Courtesan", "Cortesão / Artista"),
        ("Noble", "Aristocrata"),
        ("Expert", "Especialista"),
        ("Adventurer", "Aventureiro"),
        ("Psychic", "Psíquico"),
        ("Healer", "Curandeiro"),
        ("Wanderer", "Andarilho"),
        ("Diplomat", "Diplomata"),
        ("Armorer", "Armeiro"),
        ("Entertainer", "Artista"),
        ("Peasant", "Camponês"),
        ("Star Captain", "Capitão Estelar"),
        ("Sniper", "Atirador de Elite"),
        ("Barbarian", "Bárbaro"),
        ("Mastermind", "Mente Criminosa"),
        ("Specialist", "Especialista"),
        ("Soldier", "Soldado"),
        ("Hacker", "Hacker"),
        ("Official", "Oficial"),
        ("Physician", "Médico"),
        ("Politician", "Político"),
        ("Technician", "Técnico"),
        ("Executive", "Executivo"),
        ("Generalist", "Generalista"),
        ("Dilettante", "Diletante"),
        ("Gunslinger", "Pistoleiro"),
        ("Criminal", "Criminoso"),
        ("Spacer", "Espacial"),
        ("Thug", "Capanga"),
        ("Scholar", "Erudito"),
        ("Assassin", "Assassino"),
        ("Scavenger", "Catador / Sucateiro"),
        ("Cleric", "Clérigo"),
        ("Tinker", "Engenhoqueiro"),
        ("Henchkeeper", "Líder de Capangas"),
        ("Line Shunt", "Derivador de Linha"),
        ("Metatool", "Metaferramenta"),
        ("Medkit", "Kit Médico"),
        ("Compad", "Compad / Comunicador"),
        ("Vacc Suit", "Traje de Vácuo"),
        ("Secure Clothing", "Roupas Protegidas"),
        ("Armored Undersuit", "Traje Balístico"),
        ("Combat Rifle", "Rifle de Combate"),
        ("Laser Pistol", "Pistola Laser"),
        ("Laser Rifle", "Rifle Laser"),
        ("Submachine Gun", "Submetralhadora"),
        ("Semi-Auto Pistol", "Pistola Semi-Automática"),
        ("Heavy Revolver", "Revólver Pesado"),
        ("Shotgun", "Espingarda"),
        ("Mono-blade", "Lâmina Monomolecular"),
        ("Monoblade", "Lâmina Monomolecular"),
        ("Stun Baton", "Bastão de Atordoamento"),
        ("Thermal Flare", "Sinalizador Térmico"),
        ("Survival Kit", "Kit de Sobrevivência"),
        ("Backpack", "Mochila"),
        ("Power Cell", "Célula de Energia"),
        ("Bioshock", "Choque Biológico"),
        ("Ironhide", "Pele de Ferro"),
        ("Die Hard", "Duro de Matar"),
        ("Connected", "Conectado"),
        ("Starfarer", "Navegador Estelar"),
        ("Authority", "Autoridade"),
        ("Alert", "Alerta"),
        ("Savage Fray", "Combate Selvagem"),
        ("Ironwill", "Vontade de Ferro"),
        ("Wild Psychic", "Psíquico Selvagem"),
        ("Psychic Training", "Treinamento Psíquico"),
        ("Close Combatant", "Combatente Corpo a Corpo"),
        ("Unarmed Combatant", "Combatente Desarmado"),
        ("Shocking Assault", "Assalto de Choque"),
        ("Team Player", "Espírito de Equipe"),
        ("Spike Drive", "Propulsor de Salto"),
        ("Effort", "Esforço"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Criação de Personagem")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
        text = re.sub(r"\(" + re.escape(pt) + r"\)", pt, text)

    return text

# --- 3. Psionismo.md ---
def clean_file_3(text):
    repls = [
        ("Metadimensional Extroversion Syndrome", "Síndrome de Extroversão Metadimensional"),
        ("Psychic Refinement", "Refinamento Psíquico"),
        ("Personal Apportation", "Aporte Pessoal"),
        ("Telekinetic Manipulation", "Manipulação Telecinética"),
        ("Metamorph", "Metamorfose"),
        ("Torching", "Forçar a Mente / Queimar"),
        ("The Scream", "O Grito"),
        ("The Silence", "O Silêncio"),
        ("Effort", "Esforço"),
        ("System Strain", "Estresse Sistêmico"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Psionismo")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
        text = re.sub(r"\(" + re.escape(pt) + r"\)", "", text)
    return text

# --- 4. Sistemas.md ---
def clean_file_4(text):
    repls = [
        ("Fighting Withdrawal", "Retirada de Combate"),
        ("Total Defense", "Defesa Total"),
        ("Snap Attack", "Ataque Rápido"),
        ("Go Prone", "Jogar-se no Chão"),
        ("Execution Attack", "Ataque de Execução"),
        ("Mortally Wounded", "Mortalmente Ferido"),
        ("air-gapped", "isolado fisicamente de redes (air-gap)"),
        ("Line Shunt", "Derivador de Linha"),
        ("Medkit", "Kit Médico"),
        ("System Strain", "Estresse Sistêmico"),
        ("On Turn Actions", "Ações no Turno"),
        ("Aiding a Skill Check", "Ajudar em Teste de Perícia"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Sistemas / Combate")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 5. Equipamento e Veículos.md ---
def clean_file_5(text):
    repls = [
        ("Exchange of Light", "Bolsa da Luz"),
        ("Secure Clothing", "Roupas Protegidas"),
        ("Warpaint", "Pintura de Guerra Balística"),
        ("Polyplast Carapace", "Carapaça de Poliplástico"),
        ("Armored Undersuit", "Traje de Tecido Balístico"),
        ("Combat Field Uniform", "Armadura de Combate"),
        ("Armored Vacc Suit", "Traje de Vácuo Blindado"),
        ("Deflector Array", "Matriz Defletora"),
        ("Force Pavis", "Pavês de Força"),
        ("Powered Assault Armor", "Armadura Energizada de Assalto"),
        ("Assault Suit", "Traje de Assalto"),
        ("Pretech War Suit", "Traje de Guerra Pretech"),
        ("Ghost Mantle", "Manto Fantasma Pretech"),
        ("Icarus Harness", "Arnês Ícaro"),
        ("Psitech Combat Suit", "Traje de Combate Psiônico"),
        ("Executive Security Suit", "Traje de Segurança Executiva"),
        ("Titan Powered Armor", "Armadura Energizada Titã"),
        ("Stutterjump Suit", "Traje de Micro-Salto"),
        ("Black Slab", "Placa Negra Pretech"),
        ("Instapanel", "Painel Instantâneo"),
        ("Suit Ripper", "Rasgador de Trajes"),
        ("Thunder Gun", "Arma Trovoada"),
        ("Monoblade", "Lâmina Monomolecular"),
        ("Mono-blade", "Lâmina Monomolecular"),
        ("Stun Baton", "Bastão de Atordoamento"),
        ("Line Shunt", "Derivador de Linha"),
        ("Burst Mode", "Modo Rajada"),
        ("Lazarus Patch", "Curativo de Lázaro"),
        ("Hovercycle", "Moto Flutuante / Hovermoto"),
        ("Gravcar", "Carro Gravitacional"),
        ("Groundcar", "Carro Terrestre"),
        ("Grav Tank", "Tanque Gravitacional"),
        ("Grav Flyer", "Voador Gravitacional"),
        ("Grav APC", "Blindado de Transporte Gravitacional"),
        ("Spare Parts", "Peças Sobressalentes"),
        ("Unbraked AIs", "IAs Desenfreadas / Sem Trava"),
        ("Post-Tech", "Pós-Tecnologia"),
        ("Pretech-Plus", "Pretech Avançada"),
        ("Imperial Arms", "Armamentos Imperiais"),
        ("Colonial Arms", "Armamentos Coloniais"),
        ("Absolution Armaments", "Armamentos Absolvição"),
        ("Nightfall Combine", "Consórcio Queda da Noite"),
        ("Terminus Est", "Terminus Est"),
        ("Tempus Fugit", "Tempus Fugit"),
        ("Spike Drive", "Propulsor de Salto"),
        ("System Strain", "Estresse Sistêmico"),
        ("Vacc Suit", "Traje de Vácuo"),
        ("Armor", "Armadura"),
        ("Fittings", "Instalações"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Equipamento")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
        text = re.sub(r"\(" + re.escape(pt) + r"\)", "", text)
        
    text = re.sub(r"\*Exchange of Light\*", "Bolsa da Luz", text)
    text = re.sub(r"\(Street Armor - TL4\)", "Armadura de Rua (NT4)", text)
    text = re.sub(r"\(Combat Armor - TL4\)", "Armadura de Combate (NT4)", text)
    return text

# --- 6. Naves Espaciais.md ---
def clean_file_6(text):
    repls = [
        ("Deal With a Crisis", "Lidar com uma Crise"),
        ("Smart Cloud", "Nuvem Inteligente"),
        ("Shiptender", "Barco de Apoio Naval"),
        ("Eternal Reactor", "Reator Eterno Pretech"),
        ("Sensor Mask", "Máscara de Sensores"),
        ("Mass Cannon", "Canhão de Massa"),
        ("Exodus Bay", "Baia de Êxodo / Colonização"),
        ("Colony Core", "Núcleo de Colonização"),
        ("Fleet Cruiser", "Cruzador de Frota"),
        ("Cargo Lighter", "Barcaça de Carga"),
        ("Low Emissions", "Baixas Emissões"),
        ("Lifeboats", "Botes Salva-Vidas"),
        ("System Drive", "Propulsor de Sistema"),
        ("Drop Pod", "Cápsula de Desembarque"),
        ("Cold Sleep", "Sono Criogênico"),
        ("Tractor Beams", "Feixes Trator"),
        ("Mobile Factory", "Fábrica Móvel"),
        ("Mobile Extractor", "Extrator Móvel"),
        ("Q-Ship", "Nave Q / Mercador Camuflado"),
        ("Spike Drills", "Saltos Hiperespaciais"),
        ("Spike Drill", "Salto Hiperespacial"),
        ("Spike Drive", "Propulsor de Salto"),
        ("Rutter", "Roteiro de Salto (Rutter)"),
        ("Rutters", "Roteiros de Salto (Rutters)"),
        ("Trimming the course", "Ajustando o curso"),
        ("Ship Crises", "Crises de Nave"),
        ("Clumsy", "Desajeitado (Manobra)"),
        ("Strike Fighter", "Caça de Ataque"),
        ("Patrol Boat", "Barco de Patrulha"),
        ("Corvette", "Corveta"),
        ("Heavy Frigate", "Fragata Pesada"),
        ("Bulk Freighter", "Cargueiro Pesado"),
        ("Free Merchant", "Mercador Livre"),
        ("Battleship", "Couraçado"),
        ("Carrier", "Porta-Naves"),
        ("Armor", "Armadura"),
        ("Fittings", "Instalações"),
        ("Drive-1", "Salto-1"),
        ("Drive-2", "Salto-2"),
        ("Drive-3", "Salto-3"),
        ("Drive-4", "Salto-4"),
        ("Drive-5", "Salto-5"),
        ("Drive-6", "Salto-6"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Naves Espaciais")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
        text = re.sub(r"\(" + re.escape(pt) + r"\)", "", text)

    text = re.sub(r"\(CP / Command Points\)", "(Pontos de Comando - PC)", text)
    return text

# --- 7. A História do Espaço.md ---
def clean_file_7(text):
    repls = [
        ("Lost Worlds", "Mundos Perdidos"),
        ("The Silence", "O Silêncio"),
        ("The Scream", "O Grito"),
        ("Jump Gates", "Portais de Salto"),
        ("Spike Drive", "Propulsor de Salto"),
        ("Terran Mandate", "Mandato Terreno"),
        ("Psionic Authority", "Autoridade Psiônica"),
        ("The Like", "Os Semelhantes"),
        ("The Others", "Os Outros"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "História do Espaço")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
        text = re.sub(r"\(" + re.escape(pt) + r"\)", "", text)
    return text

# --- 8. Criação de Setor.md ---
def clean_file_8(text):
    repls = [
        ("World Tags", "Tags de Mundo"),
        ("Badlands World", "Mundo de Terras Ermas"),
        ("Badlands", "Terras Ermas"),
        ("Primary World", "Mundo Principal"),
        ("World Generation Tables", "Tabelas de Geração de Mundos"),
        ("Spike Drive 1", "Propulsor de Salto 1"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Criação de Setor")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
        text = re.sub(r"\(" + re.escape(pt) + r"\)", "", text)
    text = re.sub(r"Tech Level - NT / TL", "Nível Tecnológico (NT)", text)
    return text

# --- 9. Criação de Aventuras.md ---
def clean_file_9(text):
    return text

# --- 10. Xenobestiário.md ---
def clean_file_10(text):
    repls = [
        ("Xenobestiary", "Xenobestiário"),
        ("Effort", "Esforço"),
        ("Aptitude for Violence", "Aptidão para Violência"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Xenobestiário")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 11. Facções.md ---
def clean_file_11(text):
    repls = [
        ("News Chyron", "Letreiro de Notícias / Noticiário"),
        ("FacCreds", "Créditos de Facção"),
        ("Bases of Influence", "Bases de Influência"),
        ("Faction Assets", "Ativos de Facção"),
        ("Faction Tags", "Tags de Facção"),
        ("The Faction Turn", "O Turno de Facção"),
        ("Repair Asset / Faction", "Reparar Ativo / Facção"),
        ("Book of Secrets", "Livro de Segredos"),
        ("Military Unit", "Unidade Militar"),
        ("Special Forces", "Forças Especiais"),
        ("Guerilla Populace", "População Guerrilheira"),
        ("Party Machine", "Máquina Partidária"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Facções")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 12. Recursos do Mestre.md ---
def clean_file_12(text):
    repls = [
        ("PC Death", "Morte de Personagens"),
        ("Lazarus Patches", "Curativos de Lázaro"),
        ("fences", "receptadores"),
        ("jump gates", "portais de salto"),
        ("House Rules", "Regras da Casa"),
        ("One-Roll NPCs", "Gerador Rápido de PNJs"),
        ("Effort", "Esforço"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Recursos do Mestre")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 13. Campanhas Trans-humanas.md ---
def clean_file_13(text):
    repls = [
        ("Hard Singularity", "Singularidade Rígida"),
        ("Soft Singularity", "Singularidade Flexível"),
        ("Transhuman Soul", "Alma Trans-humana"),
        ("Organic Shells", "Invólucros Orgânicos"),
        ("Mechanical Shells", "Invólucros Mecânicos"),
        ("Digital Shells", "Invólucros Digitais"),
        ("Digital Combat", "Combate Digital"),
        ("The Net", "A Rede"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Trans-humanismo")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 14. Magia Espacial.md ---
def clean_file_14(text):
    repls = [
        ("Space Fantasy", "Fantasia Espacial"),
        ("The Light Within", "A Luz Interior"),
        ("Cross-Disciplinary Study", "Estudo Cruzado"),
        ("Arcane Armor", "Armadura Arcana"),
        ("data-scrolls", "pergaminhos de dados"),
        ("Arcane Familiar", "Familiar Arcano"),
        ("Dabbler", "Amador / Curioso Arcano"),
        ("Broad Knowledge", "Conhecimento Amplo"),
        ("Arcane Foci", "Focos Arcanos"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Magia Espacial")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 15. Personagens Heróicos.md ---
def clean_file_15(text):
    repls = [
        ("Worthy Foes", "Inimigos Dignos"),
        ("Lesser Foes", "Inimigos Menores"),
        ("Fray Die", "Dado de Combate / Dado de Atrito"),
        ("Heroic Defiance", "Desafio Heróico"),
        ("Overflow", "Transbordamento de Dano"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Personagens Heróicos")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 16. Inteligências Artificiais Verdadeiras.md ---
def clean_file_16(text):
    repls = [
        ("Sensor Array", "Arranjo de Sensores"),
        ("unbraked", "desenfreada (sem travas)"),
        ("unbraking", "rompimento de travas"),
        ("System Override", "Sobreposição de Sistema"),
        ("Routines", "Rotinas"),
        ("Core Routines", "Rotinas Centrais"),
        ("Peripheral Routines", "Rotinas Periféricas"),
        ("AI Effort", "Esforço de IA"),
        ("Falcon", "Falcão (Armação Voadora)"),
        ("Synth", "Sintético (Armação Humanoide)"),
        ("Sledge", "Trombadinha / Trenó (Armação Pesada)"),
        ("Asynchronous Processing", "Processamento Assíncrono"),
        ("Infiltration Node", "Nodo de Infiltração"),
        ("Master Control", "Controle Mestre"),
        ("True AI Class", "Classe de IA Verdadeira"),
        ("Self-Repair", "Autorreparo"),
        ("Perimeter Agencies", "Agências do Perímetro"),
        ("Quantum Tap", "Salto Quântico"),
        ("Spike Drive", "Propulsor de Salto"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "IAs Verdadeiras")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    text = re.sub(r"\(Core Rotinas\)", "Rotinas Centrais", text)
    return text

# --- 17. Sociedades.md ---
def clean_file_17(text):
    repls = [
        ("One-Roll Origins", "Gerador Rápido de Origens"),
        ("One-Roll Rulers", "Gerador Rápido de Governantes"),
        ("One-Roll Ruled", "Gerador Rápido de Governados"),
        ("Flavoring the Society", "Ambientação da Sociedade"),
        ("One-Roll Society Flavor", "Gerador Rápido de Traços Culturais"),
        ("The Scream", "O Grito"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Sociedades")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 18. Mechas.md ---
def clean_file_18(text):
    repls = [
        ("Quantum Tap ECM", "ECM de Salto Quântico"),
        ("backscatter", "retroespalhamento de sinal"),
        ("Pretech Neural Interfaces", "Interfaces Neurais Pretech"),
        ("Suit Mecha", "Traje Mecha"),
        ("Light Mecha", "Mecha Leve"),
        ("Heavy Mecha", "Mecha Pesado"),
        ("grav-planes", "planos gravitacionais"),
        ("Power Stress", "Estresse de Energia"),
        ("Quantum Tap Array", "Arranjo de Salto Quântico"),
        ("Mecha Fittings", "Instalações de Mecha"),
        ("Hit Dice Damage", "Dano de Dados de Vida"),
        ("Energy Shield", "Escudo de Energia"),
        ("Hull Points", "Pontos de Casco"),
        ("Escape Pod", "Cápsula de Escape"),
        ("Neural Sensors", "Sensores Neurais"),
        ("Psimech Interface", "Interface Psimecha"),
        ("Jump Jets", "Jatos de Salto"),
        ("Force Shield", "Escudo de Força"),
    ]
    for en, pt in repls:
        add_gloss(en, pt, "Mechas")
        text = re.sub(r"\b" + re.escape(en) + r"\b", pt, text)
        text = re.sub(r"\(" + re.escape(en) + r"\)", "", text)
    return text

# --- 19. Índice.md ---
def clean_file_19(text):
    text = re.sub(r"\bDeluxe\b", "Deluxe", text)
    return text

def execute_all():
    load_existing_glossary()
    
    cleaners = {
        "1. Introdução.md": clean_file_1,
        "2. Criação de Personagens.md": clean_file_2,
        "3. Psionismo.md": clean_file_3,
        "4. Sistemas.md": clean_file_4,
        "5. Equipamento e Veículos.md": clean_file_5,
        "6. Naves Espaciais.md": clean_file_6,
        "7. A História do Espaço.md": clean_file_7,
        "8. Criação de Setor.md": clean_file_8,
        "9. Criação de Aventuras.md": clean_file_9,
        "10. Xenobestiário.md": clean_file_10,
        "11. Facções.md": clean_file_11,
        "12. Recursos do Mestre.md": clean_file_12,
        "13. Campanhas Trans-humanas.md": clean_file_13,
        "14. Magia Espacial.md": clean_file_14,
        "15. Personagens Heróicos.md": clean_file_15,
        "16. Inteligências Artificiais Verdadeiras.md": clean_file_16,
        "17. Sociedades.md": clean_file_17,
        "18. Mechas.md": clean_file_18,
        "19. Índice.md": clean_file_19,
    }
    
    base_dir = "content/1. Estrelas Incontáveis"
    for fname, func in cleaners.items():
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        cleaned = func(content)
        # remove emojis again just to be 100% sure
        cleaned = re.sub(r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|💡|⚔️|🛡️|🚀|🔧|📜|✨|🎲|🪐|👽|🤖|👁️|⚡|💀|💊|🗺️|🛸|💥|🌌", "", cleaned)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Revisado e limpo: {fname}")

    # Write updated glossary
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
        
    print(f"Glossário atualizado com {len(sorted_terms)} termos em {glossary_path}")

if __name__ == "__main__":
    execute_all()
