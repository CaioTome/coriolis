# -*- coding: utf-8 -*-
"""
Traduz todas as 100 Sementes de Aventura do Capítulo 9 para Português Fluente.
"""
import re

SEEDS_PT = [
    "Um **Inimigo** tenta roubar de um **Amigo** uma **Coisa** preciosa que ele deseja há muito tempo.",
    "Uma **Coisa** foi descoberta na propriedade de um **Amigo**, mas uma **Complicação** ameaça destruí-la.",
    "Uma **Complicação** atinge repentinamente o grupo enquanto realizavam uma atividade rotineira e inocente.",
    "Os jogadores involuntariamente ofendem ou prejudicam um **Inimigo**, atraindo sua fúria. Um **Amigo** oferece ajuda para escapar das consequências.",
    "Rumores falam da descoberta de uma valiosa **Coisa** em um **Lugar** distante. O grupo precisa alcançá-la antes de um **Inimigo**.",
    "Um **Inimigo** possui conexões com piratas espaciais ou escravagistas, e um **Amigo** foi capturado por eles.",
    "Um **Lugar** foi tomado por rebeldes ou revolucionários violentos, e um **Amigo** está sendo mantido como refém.",
    "Um **Amigo** está apaixonado por alguém proibido pelas convenções sociais locais, e os dois precisam de ajuda para fugir juntos.",
    "Um **Inimigo** exerce poder tirânico sobre um **Amigo**, contando com o suborno de autoridades corruptas para escapar impune.",
    "Um **Amigo** se perdeu em uma região selvagem e hostil, e o grupo precisa alcançar um **Lugar** para resgatá-lo em meio a uma perigosa **Complicação**.",
    "Um **Inimigo** cometeu uma grave ofensa contra um PJ ou sua família no passado. Um **Amigo** revela ao grupo uma fraqueza nas defesas do **Inimigo**.",
    "O grupo é subitamente apanhado no meio de um violento conflito entre duas famílias rivais ou facções políticas em guerra.",
    "O grupo é incriminado injustamente por um **Inimigo** e precisa alcançar o santuário de um **Lugar** antes de poder se reorganizar e encontrar a **Coisa** que provará sua inocência e a perfídia do **Inimigo**.",
    "Um **Amigo** é ameaçado por uma tragédia (doença grave, calamidade judicial ou humilhação pública), e a única pessoa capaz de salvá-lo parece ser um **Inimigo**.",
    "Um desastre natural ou **Complicação** semelhante atinge um **Lugar** onde o grupo está presente, causando grande devastação a menos que os PJs ajudem imediatamente os feridos e soterrados.",
    "Um **Amigo** com um negócio recém-aberto encontrou um depósito de tecnologia Pretech, minerais raros ou destroços valiosos. Ele precisa da ajuda do grupo para alcançar o **Lugar** onde os bens estão.",
    "Um segmento oprimido da sociedade inicia uma revolta repentina no **Lugar** onde o grupo se encontra. Um **Inimigo** simplesmente rotula os PJs como rebeldes e tenta sufocar o levante pela força. Um **Amigo** oferece uma saída para ajudar os rebeldes ou limpar seus nomes.",
    "Um **Amigo** vulnerável virou alvo de sequestro e precisa de guarda-costas. Uma **Complicação** repentina torna a proteção contra o **Inimigo** muito mais difícil. Se o **Amigo** for capturado, o grupo deve resgatá-lo em um **Lugar**.",
    "Um **Lugar** misterioso promete conter uma valiosa **Coisa**, mas o acesso é extremamente perigoso devido à fauna local, nativos hostis ou condições ambientais letais.",
    "Um **Inimigo** e um **Amigo** reivindicam legalmente a posse de uma **Coisa** e tentam minar o caso um do outro. O **Inimigo** está disposto a cometer assassinato se achar que sairá impune.",
    "Um **Inimigo** planeja a morte de seu irmão, um **Amigo**, sabotando seu veículo gravitacional ou lançadeira em terreno inóspito enquanto os PJs coincidem de estar a bordo. O grupo deve sobreviver e trazer provas do crime.",
    "Um **Amigo** quer enviar uma mensagem secreta a um amante, que também está sendo cortejado pelo irmão do **Amigo** (um **Inimigo**). Uma **Complicação** ameaça desgraçar ou matar o amante a menos que o grupo intervenha.",
    "Um **Inimigo** está convencido de que um dos PJs teve um caso com seu cônjuge. Ele planeja atrair o grupo para um **Lugar**, prendê-los lá e deixá-los morrer para os perigos locais.",
    "Um **Inimigo** enlouqueceu pelo uso excessivo de drogas exóticas ou pelo abuso de queima psíquica. Ele elege um PJ como seu arqui-inimigo e planeja mortes elaboradas disfarçadas de **Complicação**.",
    "Um **Amigo** roubou uma preciosa **Coisa** de um **Inimigo** e fugiu para um **Lugar** perigoso e inacessível. O grupo precisa resgatá-lo e decidir o que fazer com a **Coisa** e com o furioso **Inimigo**.",
    "Um **Inimigo** descobre que seu irmão ou irmã mantém um caso amoroso socialmente inaceitável com um **Amigo** e decide matar ambos a menos que o grupo os impeça.",
    "Um **Amigo** causou acidentalmente a morte de um parente e pede ajuda ao grupo para ocultar o corpo ou forjar um acidente antes que a família descubra. Uma **Complicação** torna a tarefa arriscada.",
    "Um **Amigo** é seguidor de um ideólogo fanático que planeja uma manifestação violenta, gerando uma grave **Complicação** social. O **Amigo** morrerá nas retaliações se não for resgatado pelo grupo.",
    "O irmão de um **Amigo** será enviado para uma missão suicida sem chances de sobrevivência. O **Amigo** toma seu lugar no último instante e morrerá a menos que o grupo intervenha.",
    "Homens-bomba detonam explosivos químicos ou biológicos em um **Lugar** ocupado pelo grupo onde uma **Coisa** preciosa está guardada. Os PJs precisam escapar do desabamento e salvar a **Coisa** em meio ao pânico.",
    "Um **Inimigo** que controla permissões de pouso, rações de oxigênio ou recursos vitais tem preconceito contra os PJs. Ele exige que tragam uma **Coisa** de um **Lugar** perigoso antes de liberar o suprimento.",
    "Um **Amigo** descobre que uma grande corporação ou nobreza cometeu um terrível crime ecológico ou massacre no passado, ocultando tudo em um **Lugar**. Um **Inimigo** envia assassinos para silenciá-lo.",
    "Uma **Coisa** misteriosa em posse do grupo começa a emitir sinais estranhos ou manifestar efeitos paranormais, atraindo a atenção indesejada de um **Inimigo** perigoso.",
    "O grupo é contratado por um **Amigo** para escoltar uma carga até um **Lugar**, mas a carga é na verdade uma **Coisa** ilegal ou perigosa cobiçada por um **Inimigo**.",
    "Um **Inimigo** espalha mentiras e boatos difamatórios sobre o grupo, fazendo com que a população local e autoridades se recusem a negociar ou prestar auxílio.",
    "Um **Amigo** cientista descobre uma anomalia em um **Lugar** que contradiz os dogmas da religião ou regime político dominante. Um **Inimigo** inquisidor quer destruí-lo antes que publique a verdade.",
    "Um **Amigo** perdeu tudo em um jogo de azar viciado contra um **Inimigo** trapaceiro. Ele pede ajuda aos PJs para recuperar sua dignidade e uma **Coisa** que pertencia à sua família.",
    "Um vírus alienígena ou toxina bioengenheirada atinge o grupo ou um **Amigo**. A única cura conhecida exige uma substância encontrada exclusivamente em um **Lugar** hostil.",
    "Um **Inimigo** financia piratas para atacar naves de uma rota específica. Um **Amigo** comerciante pede aos PJs que sirvam de escolta armada sem saber que a emboscada é iminente.",
    "Um **Amigo** herda uma propriedade em ruínas em um **Lugar** remoto. Ao chegarem lá para inspecionar, descobrem que o local é usado como esconderijo por capangas de um **Inimigo**.",
    "Um **Inimigo** sequestra uma pessoa querida de um **Amigo** e exige como resgate uma **Coisa** protegida em um complexo de alta segurança.",
    "O grupo intercepta uma transmissão de socorro vinda de uma nave à deriva perto de um **Lugar**. Ao chegarem, descobrem uma armadilha montada por um **Inimigo**.",
    "Um **Amigo** líder de trabalhadores é preso arbitrariamente antes de uma greve pacífica. O grupo é solicitado a libertá-lo ou intermediar a crise com o intransigente **Inimigo** patronal.",
    "Uma inteligência artificial insana ou sistema automatizado de defesa desperta em um **Lugar** e tranca todos os presentes, iniciando um protocolo de extermínio.",
    "Um **Amigo** descobre um segredo militar vergonhoso de um **Inimigo** general. O general mobiliza tropas para cercar o bairro e queimar as provas.",
    "Um **Inimigo** compra todas as fontes de água ou combustível de uma colônia, impondo preços extorsivos. Um **Amigo** lidera um plano audacioso para sabotar o monopólio.",
    "Durante uma celebração cultural em um **Lugar**, uma **Complicação** violenta irrompe quando extremistas detonam bombas de pulso eletromagnético, apagando toda a tecnologia moderna.",
    "Um **Amigo** é acusado de assassinar um nobre ou diplomata influente. As evidências foram forjadas por um **Inimigo** que quer tomar o patrimônio da vítima.",
    "Um **Inimigo** descobre uma falha nos escudos ou sistemas de suporte de vida de uma colônia e planeja usá-la como chantagem política contra um **Amigo** governante.",
    "Uma tempestade de radiação ou clima extremo força o grupo a se abrigar em um **Lugar** onde encontram criminosos perigosos leais a um **Inimigo** também encurralados pela tempestade.",
    "Um **Amigo** desenvolve uma tecnologia revolucionária (ou técnica médica inovadora). Um **Inimigo** corporativo tenta sequestrá-lo e destruir suas anotações.",
    "Uma antiga arma Pretech em um **Lugar** começa a acumular energia instável. O grupo precisa desativá-la antes que cause uma catástrofe planetária.",
    "Um **Inimigo** suborna a tripulação de uma estação orbital para cortar a gravidade e suporte de vida em setores específicos, visando assassinar um **Amigo** dissidente.",
    "O grupo descobre que a água ou suprimentos alimentares de uma cidade estão sendo envenenados por um culto fanático leal a um **Inimigo**.",
    "Um **Amigo** pede ajuda para resgatar escravos genéticos ou clones mantidos em cativeiro em um laboratório clandestino controlado por um **Inimigo**.",
    "Um **Inimigo** desafia abertamente o grupo para um duelo judicial ou combate público de honra, mas prepara emboscadas covardes pelas costas.",
    "Um **Amigo** arqueólogo desaparece em ruínas alienígenas em um **Lugar**. Seus diários indicam que ele encontrou uma **Coisa** capaz de alterar o equilíbrio de poder do setor.",
    "Um nobre local contrata o grupo para recuperar uma joia de família (uma **Coisa**), mas na verdade quer que os PJs matem o atual detentor inocente da peça.",
    "Uma rebelião armada em uma prisão de segurança máxima em um **Lugar** permite que vários criminosos perigosos jurem vingança contra o grupo ou seus aliados.",
    "Um **Inimigo** utiliza drones espiões invisíveis para monitorar cada passo dos PJs e antecipar todos os seus movimentos em uma negociação delicada.",
    "Um **Amigo** é chantageado com gravações íntimas comprometedoras feitas por espiões cibernéticos a serviço de um **Inimigo**.",
    "Um culto apocalíptico planeja colidir um asteroide contra uma colônia rica. O grupo precisa infiltrar a base do asteroide e desviar sua trajetória.",
    "Um **Inimigo** rouba um protótipo militar de combate e o testa impiedosamente contra aldeias indefesas em um **Lugar** isolado.",
    "Um **Amigo** descobre que seu sócio comercial na verdade trabalha como agente duplo para uma facção rival liderada por um **Inimigo**.",
    "Uma tempestade metadimensional afeta temporariamente as mentes psíquicas locais, causando alucinações e surtos de violência em um **Lugar**.",
    "Um **Inimigo** tenta comprar a fidelidade da polícia local para declarar o grupo como foragidos perigosos e colocar recompensa por suas cabeças.",
    "Um **Amigo** pede ajuda para infiltrar uma festa exclusiva da alta sociedade em um **Lugar** luxuoso a fim de recuperar documentos cruciais guardados em um cofre.",
    "Uma cápsula de estase Pretech é encontrada intacta em um **Lugar**, contendo um indivíduo histórico importante ou um criminoso de guerra preservado por séculos.",
    "Um **Inimigo** manipula os mercados financeiros locais para quebrar propositalmente as pequenas empresas do setor e forçar a falência de um **Amigo**.",
    "Um grupo de contrabandistas engana o grupo, escondendo contrabando militar na nave dos PJs pouco antes de uma inspeção aduaneira rigorosa.",
    "Um **Amigo** pede que o grupo proteja um templo ou museu histórico contra saqueadores armados enviados por um colecionador inescrupuloso (um **Inimigo**).",
    "Um **Inimigo** planta uma bomba de fissão ou ogiva química na estação orbital principal e exige resgate milionário sob ameaça de destruição total.",
    "Um **Amigo** psíquico é caçado por caçadores de recompensas contratados por fanáticos que querem erradicar todos os manipuladores de esforço mental.",
    "O grupo é contratado para realizar o reconhecimento de um planeta inexplorado, mas ao pousar encontra sobreviventes de uma expedição esquecida vivendo em estado tribal.",
    "Um **Amigo** tenta desesperadamente ocultar provas de um crime passado que arruinará sua vida caso venha à tona. Um **Inimigo** possui a **Coisa** incriminadora e o chantageia sem piedade.",
    "Um mensageiro confunde o grupo com outros forasteiros e entrega silenciosamente uma **Coisa** perturbadora (como órgãos humanos preservados ou catálogo de escravos). O chefe do mensageiro, um **Inimigo**, tenta silenciar os PJs.",
    "Um cargueiro de navegação lenta é sequestrado por separatistas violentos leais a um **Inimigo**, ao mesmo tempo em que as defesas planetárias são desligadas por sabotagem interna. O cargueiro está em rota de colisão contra o espaçoporto.",
    "Artefatos alienígenas na superfície começam a emitir sinais para o cinturão de asteroides, causando pânico social generalizado. Um **Inimigo** tenta aproveitar o caos para tomar o governo.",
    "Um embaixador alienígena (um **Amigo**) é alvo de assassinos xenófobos a mando de um **Inimigo**. As relações diplomáticas são tão frágeis que uma tentativa de homicídio pode desencadear guerra total.",
    "Uma nova fé espiritual pacífica é pregada por um **Amigo**. O clero tradicional não tolera a concorrência e um **Inimigo** na hierarquia incita a população a perseguir os novos crentes.",
    "Um **Inimigo** já foi o patrono generoso de um **Amigo** antes de traí-lo cruelmente. Agora o **Amigo** busca vingança e possui as informações necessárias para furar as defesas do vilão.",
    "Equipamentos vitais de suporte de vida foram sabotados por fanáticos e precisam de conserto imediato. A única fonte de peças sobressalentes está em um **Lugar** perigoso.",
    "Um **Amigo** importa tecnologia espacial avançada que ameaça desbancar o negócio obsoleto de um empresário local (um **Inimigo**). O rival tenta sabotar o carregamento para difamar o concorrente.",
    "Um diplomata da Bolsa da Luz negocia a abertura de uma agência bancária interestelar no planeta. Um banqueiro local (um **Inimigo**) financia protestos violentos e tumultos ao redor do diplomata.",
    "Um **Inimigo** aristocrata fica furioso com o sucesso e ambição de um **Amigo** de casta inferior e tenta culpá-lo por uma **Complicação** recente na cidade.",
    "Um **Amigo** gerencia uma fábrica corporativa e ignora tradições locais que privilegiavam certas elites étnicas, contratando os operários mais qualificados. Um **Inimigo** enfurecido planeja sabotar as máquinas.",
    "Um músico excêntrico vindo de outro mundo, tratado quase como divindade em seu planeta natal, contrata os PJs como guarda-costas. Seu comportamento desregrado cria inimigos imediatos na cidade.",
    "Tempestades de poeira e distúrbios atmosféricos cobrem o assentamento de escuridão total. Um **Inimigo** comete um homicídio nas sombras e tenta incriminar os PJs como bodes expiatórios.",
    "Um **Inimigo** contamina o suprimento de oxigênio de uma estação espacial com alucinógenos para encobrir um grande roubo. Várias pessoas entram em delírio violento, mas o suprimento do grupo não foi afetado.",
    "Por coincidência, um membro do grupo veste roupas com as cores de um grupo político radical, e um **Inimigo** local passa a tratá-los como aliados em um crime terrível antes que o grupo entenda o que está acontecendo.",
    "Um tirano local exige que estrangeiros avaliem a qualidade de suas poesias horrendas — e reage com violência a qualquer crítica que não seja bajulação efusiva. O descontentamento do líder pode jogar o grupo em uma masmorra.",
    "Um morador local (um **Amigo**) tem fé cega de que a tecnologia dos PJs pode consertar qualquer coisa e promete levianamente a um poderoso **Inimigo** que o grupo consertará uma relíquia Pretech quebrada.",
    "O comunicador da nave dos PJs capta uma transmissão oficial criptografada e decodifica a mensagem, revelando que um governante corrupto planeja um massacre em uma vila para roubar uma relíquia.",
    "Um **Amigo** pertence a uma minoria religiosa ou étnica perseguida e implora para que o grupo ajude uma célula de refugiados a fugir do planeta antes que a polícia secreta os capture.",
    "Uma peça vital da nave dos PJs quebra e precisa de substituição imediata. A única peça no setor está nas mãos de um **Inimigo**, que só a entrega em troca de uma **Coisa** pertencente a um **Amigo** inocente.",
    "Cultistas eugenistas estão criando clones e escravos modificados a partir de material genético roubado na cidade. Alguns desses escravos são usados para seduzir e chantagear altos magistrados.",
    "Documentos descobertos em um **Lugar** comprovam que grandes extensões de terra do planeta pertencem legitimamente a uma população oprimida. Um **Amigo** quer esses códigos para alimentar a resistência rebelde.",
    "Uma praga agrícola ataca as plantações do planeta, prenunciando fome generalizada. Um **Amigo** descobre que uma antiga estação orbital continha sementes imunes criadas antes do Grito.",
    "Um **Inimigo** ganancioso na alfândega apreende a nave do grupo sob um pretexto fútil, com o objetivo oculto de assustar comerciantes livres e monopolizar o tráfego estelar.",
    "Um objeto barato adquirido em um bazar por um PJ revela-se a chave criptográfica de uma instalação secreta Pretech. O capanga desastrado que a vendeu por engano foi executado pelo **Inimigo**, que agora persegue o grupo.",
]

def update_chapter_9():
    path = "content/1. Estrelas Incontáveis/9. Criação de Aventuras.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split before seeds section
    header_seeds = "### 9.4 Sementes de Aventura (100 Adventure Seeds)"
    header_seeds_pt = "### 9.4 Sementes de Aventura (100 Sementes)"
    
    if header_seeds in text:
        parts = text.split(header_seeds)
    elif header_seeds_pt in text:
        parts = text.split(header_seeds_pt)
    elif "### 9.4 Sementes de Aventura" in text:
        parts = text.split("### 9.4 Sementes de Aventura")
    else:
        print("Erro: Seção 9.4 não encontrada.")
        return

    top_content = parts[0]
    
    # Format translated seeds block
    seeds_block = ["### 9.4 Sementes de Aventura (100 Sementes)", "", "A lista a seguir apresenta **100 sementes de aventuras prontas** que o Mestre pode adaptar instantaneamente combinando os elementos das Tags de Mundos.", ""]
    for idx, s in enumerate(SEEDS_PT, 1):
        num_str = f"{idx:02d}" if idx < 100 else "100"
        seeds_block.append(f"**{num_str}.** {s}")
        seeds_block.append("")

    full_content = top_content.rstrip() + "\n\n" + "\n".join(seeds_block)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(full_content)
    print("Capítulo 9 atualizado com as 100 sementes 100% traduzidas em português!")

if __name__ == "__main__":
    update_chapter_9()
