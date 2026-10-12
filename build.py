# -*- coding: utf-8 -*-
"""生成 index.html。改内容改这里，然后 python3 build.py。"""
V = "cce20261012"

ERAS = [
 dict(id="era-hebrew", c="#3d9a6a", ico="📜", when="约前15–前5世纪（传统）", name="希伯来：家中的施玛", hook="敬畏耶和华是知识的开端——教育从家门口开始。",
  cause="神立约时把律法交给全民，而不是交给祭司阶层私藏。约要代代相传，下一代的信仰就不能靠运气。",
  bg="古代近东的书吏学校服务王宫与神庙，读写是精英技能。以色列的独特在于：申命记第6章把教导交给每个父亲，场景是坐在家里、行在路上、躺下、起来——生活本身就是课堂。",
  core="知识的根是关系：认识耶和华、敬畏祂，然后才谈技能。箴言把智慧（hokmah）定义为在神造的秩序里活得合宜。",
  why="出埃及一代亲眼看见神迹，第二代没有看见（士2:10）。没有教导，救恩历史一代就断。",
  did="施玛（申6:4–9）、逾越节孩子发问的礼仪（出12:26–27）、记念石（书4:6–7）、箴言父训子的体裁（箴1–9）。",
  bible="申6:4–9；诗78:1–8；箴1:7、9:10、22:6；传12:13。这是圣约传承：约的应许给你们和你们的儿女。",
  creed="海德堡第1主日（唯一的安慰）；第38主日问答103（维持传道与学校）。",
  hard="箴22:6 是智慧格言，不是机械保证；孩子归主最终是神的恩典，不是方法的产物。",
  home="把信仰嵌入日常节奏：饭桌、路上、睡前。教会：教理问答班就是现代版的“孩子问，父亲答”。学校：每门课回到“这与认识神有何关系”。",
  mem="施玛在家，箴言在心：先敬畏，后知识。"),
 dict(id="era-greek", c="#6ba3e0", ico="🏛️", when="约前387年起", name="希腊 paideia：柏拉图学园、亚里士多德", hook="培养城邦里有德的人——问得深，但没有十字架。",
  cause="雅典民主需要会说话、会辩论的公民；智者派收费教演说术，柏拉图认为他们教的是说服而不是真理。",
  bg="约前387年柏拉图在雅典城外阿卡德米建学园；亚里士多德（前384–前322）在学园二十年，后在吕克昂讲学（约前335年起）。paideia 指整全的人格塑造：体育、音乐、文法、哲学。",
  core="教育的目标是德性（aretē）与理性生活；逻辑工具（三段论）与学科分类由亚里士多德奠定。",
  why="他们看见：人不是只要技能，还要被塑造成某种人。这个洞见是真的，只是他们找错了源头和终点。",
  did="对话体辩证法、学科分科、逻辑学（《工具论》）、伦理学与政治学。后来‘自由技艺’的雏形在希腊化时代成形。",
  bible="徒17:16–34 保罗在雅典引用他们的诗人，却宣告复活与审判。林前1:20–25：世人凭智慧不认识神。",
  creed="比利时信条第14条：人堕落后仍保有些许自然之光；多特第三四项第4条：这光不足以使人得救，甚至不能在属世之事上正确使用。",
  hard="希腊德性是靠理性自我完成；圣经的圣洁是靠恩典被更新。同一个词‘德性’，引擎完全不同。",
  home="教孩子问‘为什么’与下定义——这是可借用的工具。教会：护教时像保罗一样懂对方又不折衷。学校：读柏拉图要带着林前1章读。",
  mem="希腊问对了‘成为什么人’，答错了‘靠什么成为’。"),
 dict(id="era-rome", c="#e8a85c", ico="🗣️", when="前1世纪–1世纪", name="罗马：自由技艺与修辞（西塞罗、昆体良）", hook="好人善言——罗马把教育做成了制度。",
  cause="罗马共和与帝国治理靠法庭、元老院与行省行政，口才就是权力。",
  bg="西塞罗（前106–前43）主张演说家要通晓各门学问；昆体良（约35–约100）《雄辩术原理》详述从幼儿到成人的修辞教育，提出‘善言的好人’理想。拉丁文成为西方学术语言。",
  core="artes liberales：适合自由人（而非奴隶）学习的技艺；以文法与修辞为中心，培养公共生活的人。",
  why="帝国需要统一的精英语言与表达；这套体系后来成了教会传讲与释经的载体。",
  did="文法学校（grammaticus）→修辞学校（rhetor）的分级制度；大量拉丁经典成为课本。",
  bible="罗马的道路与通用语成了福音传播的预备（加4:4‘时候满足’）。保罗的书信也运用了修辞结构，但他拒绝高言大智（林前2:1–5）。",
  creed="比利时信条第2条：神借受造界与圣经两本书使人认识祂——语言与逻辑属于受造秩序。",
  hard="修辞能为谎言服务。古典教育若只剩‘口才’，就是罗马的复活，不是基督教的。",
  home="教孩子把一件事说清楚、写清楚。教会：讲道要清楚而不炫技。学校：修辞课以真理为内容、以爱为动机（弗4:15）。",
  mem="罗马给了工具箱：文法、修辞；箱子里装什么，罗马说不准。"),
 dict(id="era-church", c="#b39ddb", ico="✝️", when="4–6世纪", name="早期教会：奥古斯丁、波爱修斯、卡西奥多鲁斯", hook="掠夺埃及人的金子——异教学问可用，但要为主所用。",
  cause="帝国基督教化后，信徒要问：异教的文法、修辞、哲学还能不能学？特土良问‘雅典与耶路撒冷何干’，奥古斯丁给出更细的回答。",
  bg="奥古斯丁（354–430）出身北非，曾任米兰修辞教授，归信后任希波主教。《论基督教教义》约396年开笔、约426年完成，第二卷用以色列出埃及时带走埃及人金银的比喻。帝国西部崩溃（476年为传统标记）。波爱修斯（约480–524）首用‘四艺’一词并译亚里士多德逻辑；卡西奥多鲁斯（约485–约585）在维瓦留姆修院编《教导》，把七艺与抄经结合。",
  core="一切真理都属于神；学问是为了理解圣经、爱神爱人。七艺：三艺（文法、逻辑、修辞）+四艺（算术、几何、音乐、天文）。",
  why="教会需要读懂并讲解圣经、反驳异端；蛮族入侵使典籍面临失传，修院成了保存所。",
  did="奥古斯丁把释经学与修辞学合一；波爱修斯《哲学的慰藉》成为中世纪必读；修院抄写拯救了古典文本。",
  bible="出12:35–36（金银）；林后10:5（将人所有的心意夺回，使它都顺服基督）；西2:3（一切智慧知识的宝藏都藏在基督里）。",
  creed="尼西亚信经与亚他那修信经就产生在这个用希腊哲学词汇护卫圣经真理的时代：借词不借神。",
  hard="‘金子’要熔铸，不能连偶像一起搬进会幕（出32章金牛犊用的也是埃及的金子）。",
  home="读异教经典时问：哪里是真金，哪里是偶像？教会：信经是‘用借来的词说圣经的话’的范例。学校：每本古典书配一条圣经透镜。",
  mem="奥古斯丁：拿金子，砸金牛犊。"),
 dict(id="era-carol", c="#5ec4c0", ico="👑", when="约800年", name="加洛林复兴：查理曼与阿尔昆", hook="皇帝下令办学——欧洲第一次‘全民扫盲’尝试。",
  cause="7–8世纪拉丁水平崩坏，神父读不懂礼仪书，抄本错误百出。",
  bg="查理曼约781年邀约克学者阿尔昆主持亚琛宫廷学校；789年《普遍劝谕》要求修院与主教座堂设学校教授诗篇、记谱、歌唱、算数与文法。800年查理曼加冕。加洛林小写体让书写更清楚。",
  core="教育为了正确敬拜与治理：先修正经文与礼仪，再修正人。",
  why="一个帝国若要‘基督教’，先得有人会读圣经。",
  did="校勘拉丁圣经（武加大）、建立座堂/修院学校网络、统一字体、保存古典作品（今存大量拉丁古典最早抄本出自这一时期）。",
  bible="尼8:8（以斯拉清楚念、讲明意思）——会读才能明白。",
  creed="使徒信经与主祷文在此时期被要求所有信徒背诵——要理问答的远祖。",
  hard="由君王主导的教会教育容易把信仰变成国家工程；改革宗的领域主权正是要分清教会、国家、家庭。",
  home="家里先确保孩子会读、会背信经与主祷文。教会：教会自己负责教义教育，不外包给国家。学校：书写与文本准确是敬虔的一部分。",
  mem="查理曼要学校，阿尔昆来办；先修经文，再修人。"),
 dict(id="era-medieval", c="#d4af37", ico="🎓", when="约11–15世纪", name="座堂学校与大学：博洛尼亚、巴黎、牛津", hook="大学从教会里长出来——神学被称为‘学问的女王’。",
  cause="城市复兴、法律与行政需求增加，座堂学校的师生聚集成行会（universitas）。",
  bg="博洛尼亚（传统定于1088年，约数）以法学著称；巴黎约12世纪末成形，以神学著称；牛津约12世纪后期开始有教学。课程：先读七艺取得文学学位，再进修神学、法学、医学。经院哲学用问题—反方—正方—答辩的方法；伦巴德《四部语录》为神学教科书；阿奎那（1225–1274）综合亚里士多德与神学。",
  core="信仰寻求理解（安瑟伦语）；系统、分辨、辩论的训练。",
  why="要把启示与理性、圣经与教父的众多权威调和成体系。",
  did="学位制度、讲座与辩论（disputatio）、大学自治——现代大学的骨架。",
  bible="箴25:2 察考事情是君王的荣耀；赛1:18 来，我们彼此辩论。",
  creed="改革宗经院主义（如图伦丁）继承了这一方法，但把圣经的权威置于一切传统之上（比利时信条第7条）。",
  hard="方法本身中立，但当亚里士多德的框架凌驾圣经、恩典被看作‘成全自然’的补充时，就走偏。改革宗承认自然的价值，但强调罪的全面败坏。",
  home="教孩子先陈述对方观点再回应。教会：学会分辨问题、定义词语。学校：辩论课是经院方法的遗产。",
  mem="大学 = 教会里长出的行会；七艺是门槛，神学是女王。"),
 dict(id="era-renaiss", c="#e0b0b0", ico="📖", when="约14–16世纪", name="文艺复兴人文主义：回到源头（Erasmus）", hook="Ad fontes——回到原文，宗教改革的引信。",
  cause="人文主义者厌倦经院拉丁的繁琐，要读西塞罗原文、读希腊原文。",
  bg="意大利城邦（佛罗伦萨等）赞助学术；1453年君士坦丁堡陷落前后希腊学者与抄本西传；约1450年代古腾堡印刷术。伊拉斯谟（1466–1536）1516年出版希腊文新约。",
  core="ad fontes：语言学精确与原典阅读；studia humanitatis（文法、修辞、诗、历史、道德哲学）。",
  why="要找回纯正的古代——对人文主义者是西塞罗，对改革者是使徒。",
  did="希腊文/希伯来文研究、校勘学、文法课本、印刷普及。",
  bible="诗119:18 求你开我的眼睛；徒17:11 庇哩亚人天天考查圣经。",
  creed="比利时信条第3–7条：圣经是神的道、正典、充足——回到源头最终是回到圣经本身。",
  hard="伊拉斯谟与路德1524–25年就自由意志论战：同样的语言工具，不同的人论。古典技能不保证正统。",
  home="让孩子学一点原文与词源。教会：鼓励查考圣经而非只听二手。学校：拉丁文/希腊文是工具，不是身份标签。",
  mem="伊拉斯谟下蛋，路德孵小鸡（16世纪流传的俗语，不是史实陈述）——工具一样，信仰不同。"),
 dict(id="era-ref", c="#c45c5c", ico="🔥", when="1524–1619", name="宗教改革：路德、梅兰希顿、斯图谟、加尔文、海德堡、多特", hook="人人读圣经，所以人人要上学——改教者是学校的建造者。",
  cause="唯独圣经要求平信徒能读圣经；修院解散后原有学校瓦解；家长不送孩子上学。",
  bg="1524年路德致德意志各城市议员书，要求市政开办并维持基督教学校，男女孩都要受教。梅兰希顿（1497–1560）设计课程与学校章程，被称为‘德意志之师’。斯图谟1538年在斯特拉斯堡建文理中学，分级授课；加尔文1538–41年在斯特拉斯堡亲见。1559年加尔文建日内瓦学院，伯撒为首任院长，分私塾（初级学校）与公学（高级）。1563年帕拉丁选侯腓特烈三世颁布海德堡要理问答，乌尔西努斯主笔，作学校与教会的教理教材。1618–19年多特会议议定三种教理问答：家中父母、学校教师、教会牧师。",
  core="教育为了认识神的道、服事教会与社会（呼召观）；要理问答是脊梁，古典语言是工具。",
  why="改教若只停在讲台，一代就会回潮；必须有受过训练的牧师与会读圣经的会众。",
  did="市立学校、拉丁学校、学院（日内瓦培养了大批派往法国等地的牧师）、要理问答、教会规章中的学校条款。",
  bible="申6；提后3:15（提摩太从小明白圣经）；弗6:4（照主的教训和警戒养育他们）。",
  creed="海德堡问答74（婴孩属于约）、103（维持学校）；多特教会规章（学校与教理）；改革宗洗礼仪式中父母立誓按所教导的教义教养孩子。",
  hard="改教者用的就是人文主义的古典课程，但目的被重新定位：不为西塞罗式的雄辩，而为圣经与呼召。",
  home="父母是第一位教理老师（多特所列三种之首）。教会：坚持主日教理讲道与教理班。学校：古典课程+要理问答双轨。",
  mem="1524路德写信，1559日内瓦开学，1563海德堡出书，1618多特立规。"),
 dict(id="era-comenius", c="#a8dfc4", ico="🌱", when="17世纪", name="夸美纽斯：《大教学论》", hook="把一切知识教给一切人——近代教学法之父。",
  cause="三十年战争（1618–1648）摧毁中欧，夸美纽斯所属的弟兄合一会流亡。",
  bg="夸美纽斯（1592–1670）曾在赫尔伯恩与海德堡求学，《大教学论》先以捷克文写成，拉丁文本1657年出版。他也编了图画课本《世界图解》（1658）。",
  core="教育按孩子的发展顺序、由感官到理解、由简到繁；普及教育，包括女孩与穷人。",
  why="他相信教育能修复被战争撕裂的世界——这里既有亮光也有危险。",
  did="分级学制设想、图文教材、母语教育。",
  bible="他以创世与救赎为框架，但对教育改造世界抱有很高期望。",
  creed="多特第三四项第4条提醒：人的光和方法不能使人重生。",
  hard="后人常把夸美纽斯读成现代进步教育的源头；他自己是敬虔的，但‘教育能救世’的乐观要被改革宗纠正。",
  home="教学顺序要合孩子的年龄。教会：给儿童合适的图解教材。学校：方法服务于真理，不取代恩典。",
  mem="夸美纽斯：图画书之父，方法好，别把方法当救主。"),
 dict(id="era-dutch", c="#e6d4a0", ico="🌷", when="1880–20世纪初", name="荷兰新加尔文主义：凯波尔、巴文克", hook="‘没有一寸不属于基督’——基督徒学校是信仰的必然。",
  cause="19世纪荷兰公立学校走向中立/世俗，正统改革宗家长争取自办基督教学校的权利（学校之争）。",
  bg="凯波尔1880年创办阿姆斯特丹自由大学，就职演讲题为《领域主权》，其中名句大意是：在人类生活的整个领域中，没有一寸是基督不宣告‘这是我的’。1917年宪法修订使基督教学校获得同等公费（学校之争的平息）。巴文克著有教育学著作（如1904年《教育学原理》）。",
  core="领域主权：家庭、教会、学校、国家各有神所授的权柄；普遍恩典解释非信徒何以有真知灼见；对立（antithesis）提醒信与不信的根本分歧。",
  why="中立是幻想：每一种教育都预设一种人观与世界观。",
  did="自由大学、基督教小学网络、改革宗教育学。",
  bible="西1:16–17；林后10:5；罗12:2；西3:10（在知识上渐渐更新）。",
  creed="比利时信条第2、14条；多特第三四项第4条；海德堡第33主日（悔改：旧人死、新人活）。",
  hard="普遍恩典不是‘异教也能得救’，对立不是‘拒绝一切异教学问’。两者要同时握住。",
  home="父母选择学校时问：这学校的人观是什么？教会：不替代学校，但牧养家庭与教师。学校：教师是在家长委托下的领域，而非国家代理人。",
  mem="凯波尔1880：一寸不让；巴文克：恩典恢复自然。"),
 dict(id="era-modern", c="#f0b8b8", ico="🧰", when="1947–今", name="现代复兴：塞耶斯与古典基督教学校运动", hook="‘失落的学习工具’——一篇演讲点燃一场运动。",
  cause="20世纪进步主义教育重技能与经验，轻语言、逻辑与经典。",
  bg="多萝西·塞耶斯1947年在牛津演讲《失落的学习工具》，提出把三艺对应儿童阶段：文法期（记忆）、逻辑期（辩论）、修辞期（表达）。道格拉斯·威尔逊1991年出版《重拾失落的学习工具》，推动美国古典基督教学校；古典基督教学校协会（ACCS）约1994年成立。",
  core="以三艺为方法框架、以西方经典与拉丁文为内容、以基督教世界观为整合。",
  why="家长寻找比世俗公立教育更深、更整全的选项。",
  did="大批古典基督教学校、在家教育课程、伟大书籍（Great Books）阅读。",
  bible="诗111:10；箴1:7——运动常引用，但其框架需要被圣经检验。",
  creed="欧陆改革宗读者应补上：要理问答（海德堡）、圣约养育、教会规章中的学校传统——这些在运动中常被弱化。",
  hard="① 塞耶斯阶段对应是现代改编，古人从未把三艺当儿童发展阶段。② 威尔逊属于美国的 CREC（与联邦愿景争议相关），不是欧陆改革宗三项联合信条传统。③ 古典≠自动基督教。",
  home="借用阶段观作教学参考，但按孩子实际调整。教会：把要理问答放回古典课程中心。学校：查验‘西方经典’是否被当成救恩替代品。",
  mem="塞耶斯1947点火，威尔逊1991建校；阶段是教法，不是经文。"),
]

def era_rail():
    out=[]
    for e in ERAS:
        out.append(f'<div class="era-chip" style="--c:{e["c"]}"><a href="#{e["id"]}"><span class="era-ico" aria-hidden="true">{e["ico"]}</span><span class="era-when">{e["when"]}</span><span class="era-name">{e["name"]}</span><p class="era-hook">{e["hook"]}</p></a></div>')
    return '<div class="era-rail">'+"".join(out)+'</div>'

def era_sections():
    out=[]
    for e in ERAS:
        out.append(f'''<div class="era-sec" style="--c:{e["c"]}">
<h3 id="{e["id"]}">{e["ico"]} {e["name"]}<span class="badge">{e["when"]}</span></h3>
<div class="facet">
<div class="f-cause"><b>⏪ 前因</b><p>{e["cause"]}</p></div>
<div class="f-bg"><b>🗺️ 真实背景</b><p>{e["bg"]}</p></div>
<div class="f-core"><b>💎 核心</b><p>{e["core"]}</p></div>
<div class="f-why"><b>❓ 为什么</b><p>{e["why"]}</p></div>
<div class="f-did"><b>🛠️ 写了 / 做了什么</b><p>{e["did"]}</p></div>
<div class="f-bible"><b>📖 圣经与圣约</b><p>{e["bible"]}</p></div>
<div class="f-creed"><b>📜 信条对照</b><p>{e["creed"]}</p></div>
<div class="f-hard"><b>⚠️ 难点</b><p>{e["hard"]}</p></div>
<div class="f-app"><b>🏠⛪🏫 应用（家庭 · 教会 · 学校）</b><p>{e["home"]}</p></div>
</div>
<p class="mem">🧠 记忆句：{e["mem"]}</p>
</div>''')
    return "\n".join(out)

# 示意地图：x=(经度+4)*22, y=(55-纬度)*22
CITIES=[("耶路撒冷",35.2,31.8,"#3d9a6a",-60,22),("雅典",23.7,38.0,"#6ba3e0",8,-8),("罗马",12.5,41.9,"#e8a85c",8,18),
("希波",7.75,36.9,"#b39ddb",8,18),("亚琛",6.1,50.8,"#5ec4c0",-46,4),("巴黎",2.35,48.85,"#d4af37",-40,6),
("牛津",-1.26,51.75,"#d4af37",8,-8),("维滕堡",12.65,51.87,"#c45c5c",8,4),("日内瓦",6.15,46.2,"#c45c5c",-54,8),
("斯特拉斯堡",7.75,48.58,"#c45c5c",-80,16),("海德堡",8.69,49.4,"#c45c5c",10,4),("阿姆斯特丹",4.9,52.37,"#e6d4a0",8,-8),("博洛尼亚",11.34,44.5,"#d4af37",8,4)]
def map_svg():
    g=[]
    for lon in range(0,41,5):
        x=(lon+4)*22; g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="540" stroke="rgba(255,255,255,.05)"/>')
    for lat in range(30,56,5):
        y=(55-lat)*22; g.append(f'<line x1="0" y1="{y}" x2="900" y2="{y}" stroke="rgba(255,255,255,.05)"/>')
    pts=[]
    for n,lon,lat,c,dx,dy in CITIES:
        x=(lon+4)*22; y=(55-lat)*22
        pts.append(f'<circle class="pulse" cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{c}" opacity=".4"/><circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="{c}"/><text x="{x+dx:.0f}" y="{y+dy:.0f}" fill="#f3ead2" font-size="15">{n}</text>')
    # 路线：传承示意
    route=[(35.2,31.8),(23.7,38.0),(12.5,41.9),(7.75,36.9),(6.1,50.8),(2.35,48.85),(12.65,51.87),(6.15,46.2),(8.69,49.4),(4.9,52.37)]
    d="M"+" L".join(f"{(a+4)*22:.0f},{(55-b)*22:.0f}" for a,b in route)
    return f'''<div class="map-wrap"><svg viewBox="0 0 900 540" role="img" aria-label="古典与基督教教育重镇示意图">
<rect width="900" height="540" fill="#0b1626"/>{"".join(g)}
<text x="330" y="420" fill="rgba(107,163,224,.35)" font-size="26">地 中 海（示意）</text>
<text x="60" y="80" fill="rgba(107,163,224,.25)" font-size="18">北海方向</text>
<path d="{d}" fill="none" stroke="rgba(212,175,55,.45)" stroke-width="2" stroke-dasharray="6 6"/>
{"".join(pts)}
<text x="12" y="528" fill="rgba(255,255,255,.45)" font-size="13">示意图：按经纬度粗略投影，不画海岸线，非精确比例；虚线为思想传承顺序，不是实际路线。</text>
</svg></div>'''

GEO=[("耶路撒冷","#3d9a6a","圣约之城；家庭与会堂诵读律法；口传与背诵文化。"),
("雅典","#6ba3e0","城邦民主、公共辩论、哲学学园；‘爱智慧’的发源地。"),
("罗马","#e8a85c","法律、行政与修辞；拉丁文成为西方学术通用语。"),
("希波（今阿尔及利亚安纳巴）","#b39ddb","罗马北非行省，拉丁基督教重镇；奥古斯丁任主教之地。"),
("亚琛","#5ec4c0","法兰克帝国宫廷；查理曼与阿尔昆的宫廷学校。"),
("巴黎 / 牛津 / 博洛尼亚","#d4af37","城市复兴中的行会式大学；神学、法学与七艺课程。"),
("维滕堡","#c45c5c","萨克森小城大学；路德与梅兰希顿，德语改教与学校改革中心。"),
("斯特拉斯堡","#c45c5c","帝国自由城，德法交界；斯图谟分级中学，加尔文曾在此牧养法语难民会众。"),
("日内瓦","#c45c5c","法语城邦共和国，难民之城；1559年学院成为改革宗牧者摇篮。"),
("海德堡","#c45c5c","帕拉丁选侯国首都，内卡河畔大学城；1563年要理问答。"),
("阿姆斯特丹","#e6d4a0","商业共和国传统、宗教多元；1880年自由大学，领域主权。")]

def geo_cards():
    return '<div class="card-grid">'+"".join(f'<div class="card" style="border-top:3px solid {c}"><h4 style="color:{c}">📍 {n}</h4><p class="mb-0">{t}</p></div>' for n,c,t in GEO)+'</div>'

HTML=f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="description" content="欧陆改革宗视角的基督教古典教育研读：圣经整体、圣约养育、教育史时代线、三艺四艺、信条对照。" />
<title>欧陆改革宗 · 基督教古典教育研读</title>
<link rel="stylesheet" href="assets/styles.css?v={V}" />
</head>
<body>
<header class="site-header">
  <button type="button" class="menu-toggle" id="menu-toggle" aria-label="切换目录" aria-expanded="false" aria-controls="sidebar"><span></span><span></span><span></span></button>
  <span class="sr-only">欧陆改革宗 · 基督教古典教育研读</span>
  <div class="header-spacer" aria-hidden="true"></div>
  <div class="progress-bar" id="progress-bar" role="progressbar" aria-label="阅读进度"></div>
</header>
<div class="sidebar-overlay" id="sidebar-overlay"></div>
<aside class="sidebar" id="sidebar" aria-label="目录">
  <div class="sidebar-brand"><div class="sidebar-brand-text"><span class="brand-title">基督教古典教育 · 改革宗研读</span><span class="brand-sub">圣约 · 三艺 · 时代 · 信条</span></div>
  <button type="button" class="sidebar-close" id="sidebar-close" aria-label="关闭目录">×</button></div>
  <div class="toc-search-wrap"><input type="search" class="toc-search" id="toc-search" placeholder="筛选章节…" autocomplete="off" aria-label="搜索目录" /></div>
  <div class="toc-label">目录导航</div>
  <nav class="toc-nav" id="toc-nav"></nav>
  <div class="sidebar-footer"><button type="button" class="btn-text" id="expand-all">展开全部</button><button type="button" class="btn-text" id="collapse-all">收起全部</button></div>
</aside>
<div class="app-shell" id="app-shell"><main class="main" id="main"><div class="content-inner">

<section class="hero" id="top">
  <div class="hero-mark" aria-hidden="true"></div>
  <h1>基督教古典教育 · 欧陆改革宗研读</h1>
  <p class="hero-brand-line">敬畏耶和华是知识的开端；拿埃及的金子，不造金牛犊。</p>
  <p class="lead">古典教育是一套工具（语言、逻辑、表达、数与秩序）与一份书单（两千多年的经典）。它本身<span class="mark-warn">不是福音</span>。改革宗的问题只有一个：这些工具与书怎样被放在<span class="mark-core">基督的主权</span>与<span class="mark-christ">恩典之约</span>之下，用来养育约中的孩子。</p>
  <div class="hero-meta">
    <a class="chip chip-green" href="#sec-frame">圣经整体</a><a class="chip chip-gold" href="#sec-timeline">时代线</a>
    <a class="chip chip-teal" href="#sec-geo">地图</a><a class="chip chip-purple" href="#sec-arts">三艺四艺</a>
    <a class="chip chip-rose" href="#sec-hard">难点</a><a class="chip chip-blue" href="#sec-memory">记忆路径</a>
  </div>
  <div class="mark-legend"><span><span class="mark-core">核心</span></span><span><span class="mark-christ">基督/圣约</span></span><span><span class="mark-warn">警示/难点</span></span><span><span class="mark-creed">信条</span></span></div>
</section>

<section id="sec-frame-wrap">
<h2 id="sec-frame">一、先看整本圣经：教育在救赎历史中的位置</h2>
<div class="flow">
 <div class="step">🌍 创造<br><small>按神形像造人，受托治理（创1:26–28）</small></div><span class="arr">→</span>
 <div class="step">🌑 堕落<br><small>心思昏暗（罗1:21；弗4:18）</small></div><span class="arr">→</span>
 <div class="step">✝️ 救赎<br><small>心意更新（罗12:2；西3:10）</small></div><span class="arr">→</span>
 <div class="step">👑 成全<br><small>万有在基督里同归于一（弗1:10）</small></div>
</div>
<div class="card-grid">
 <div class="card card-gold"><span class="card-tag">创造</span><h4>为什么人要学习？</h4><p>文化使命（创1:28）要求人认识、命名、治理受造界。亚当给动物起名（创2:19–20）就是第一堂‘文法课’：语言对应实在。学习不是堕落后的补救，而是神形像的本分。</p></div>
 <div class="card"><span class="card-tag">堕落</span><h4>为什么学习会走偏？</h4><p>罪没有消灭理性，却使理性背离神（罗1:21–22）。人仍能算对数学，却不肯把荣耀归给定下数学秩序的神。因此<span class="mark-warn">知识多不等于智慧</span>。</p></div>
 <div class="card"><span class="card-tag">救赎</span><h4>恩典如何改变学习？</h4><p>新人在知识上渐渐更新（西3:10）；将人所有的心意夺回，使它都顺服基督（林后10:5）。教育不能重生人，但重生的人需要被教育。</p></div>
 <div class="card"><span class="card-tag">基督</span><h4>一切学科的中心</h4><p>万有靠祂造、靠祂而立（西1:16–17）；一切智慧知识的宝藏都藏在祂里面（西2:3）。所以没有‘中立科目’。</p></div>
 <div class="card"><span class="card-tag">智慧文学</span><h4>敬畏是开端</h4><p>箴1:7：敬畏耶和华是知识的开端。‘开端’既是起点也是首要原则：不是学到最后才加上信仰，而是信仰决定怎样学。</p></div>
 <div class="card"><span class="card-tag">两本书</span><h4>受造界与圣经</h4><p>比利时信条第2条：神借受造界（如一本好书）与圣经使人认识祂。四艺读第一本书，三艺帮助读第二本书；第二本书校正对第一本书的读法。</p></div>
</div>

<h3 id="sec-covenant">圣约神学：为什么教育是约的义务</h3>
<div class="mindgrid">
 <div class="mind-root">🤝 恩典之约：我要作你和你后裔的神（创17:7）</div>
 <div class="mind-branch" style="--c:#3d9a6a"><h4>儿女在约中</h4><ul><li>创17：割礼给婴孩</li><li>徒2:39：应许归给你们和你们的儿女</li><li>海德堡问答74：婴孩当受洗</li></ul></div>
 <div class="mind-branch" style="--c:#d4af37"><h4>父母的誓约</h4><ul><li>改革宗洗礼仪式：父母承诺按所信教义竭力教养孩子</li><li>弗6:4：照主的教训和警戒</li><li>教育是还愿，不是消费选择</li></ul></div>
 <div class="mind-branch" style="--c:#c45c5c"><h4>教会的看顾</h4><ul><li>多特会议：家庭、学校、教会三种教理问答</li><li>教会规章要求设好的学校教师</li><li>海德堡问答103：维持传道与学校</li></ul></div>
 <div class="mind-branch" style="--c:#6ba3e0"><h4>养育的目标</h4><ul><li>海德堡第1主日：唯一的安慰</li><li>第33主日：旧人治死、新人复活</li><li>不是造‘精英’，是造门徒</li></ul></div>
</div>

<h3 id="sec-grace">普遍恩典与对立：为什么能读异教经典</h3>
<div class="table-wrap"><table><thead><tr><th>概念</th><th>意思</th><th>对古典教育的意义</th></tr></thead><tbody>
<tr><td><span class="mark-core">普遍恩典</span></td><td>神约束罪，使非信徒也能发现真实的东西（太5:45）</td><td>欧几里得的几何、亚里士多德的逻辑是真实发现，可以使用</td></tr>
<tr><td><span class="mark-warn">对立（antithesis）</span></td><td>信与不信在根本方向上相反（创3:15；林后6:14–15）</td><td>不能把柏拉图的人观、斯多亚的命运观连同工具一起接收</td></tr>
<tr><td><span class="mark-creed">残存自然之光</span></td><td>比利时14；多特三四4：有残光，但不足以得救，且被人压制</td><td>古典德性可作镜子，不能作救主</td></tr>
<tr><td><span class="mark-christ">更新</span></td><td>海德堡第33主日；罗12:2</td><td>教育的终点是心意更新后的服事，而非自我完善</td></tr>
</tbody></table></div>
<p>三大普世信经本身就是古典教育的成果与教材：<span class="mark-creed">使徒信经</span>是受洗的信仰纲要，<span class="mark-creed">尼西亚信经</span>用希腊词（本质、位格）护卫圣经，<span class="mark-creed">亚他那修信经</span>是精确定义的范本。会背信经，就是在练习‘文法’；会解释信经，就是在练习‘逻辑’与‘修辞’。</p>
</section>

<section>
<h2 id="sec-timeline">二、时代线：一张色卡记住两千五百年</h2>
<p>只用公认锚点，<span class="mark-warn">“约”字表示大约年代</span>。点任一色卡跳到详解。</p>
{era_rail()}
<div class="table-wrap"><table><thead><tr><th>必记数字</th><th>事件</th><th>挂钩</th></tr></thead><tbody>
<tr><td>约前387</td><td>柏拉图学园</td><td>学院（academy）一词的来源</td></tr>
<tr><td>约396–426</td><td>奥古斯丁《论基督教教义》</td><td>埃及人的金子</td></tr>
<tr><td>约800</td><td>查理曼加冕、阿尔昆办学</td><td>整数年好记</td></tr>
<tr><td>1524</td><td>路德致议员书</td><td>九十五条后七年</td></tr>
<tr><td>1559</td><td>日内瓦学院</td><td>加尔文晚年最后的建设之一</td></tr>
<tr><td>1563</td><td>海德堡要理问答</td><td>学院后四年</td></tr>
<tr><td>1618–19</td><td>多特会议</td><td>三种教理问答</td></tr>
<tr><td>1880</td><td>自由大学</td><td>领域主权</td></tr>
<tr><td>1947</td><td>塞耶斯演讲</td><td>失落的工具</td></tr>
<tr><td>1991</td><td>威尔逊著作</td><td>运动起点</td></tr>
</tbody></table></div>
</section>

<section>
<h2 id="sec-geo">三、地理：从耶路撒冷到阿姆斯特丹</h2>
{map_svg()}
<h3 id="sec-geo-culture">各地文化区域特征</h3>
{geo_cards()}
</section>

<section>
<h2 id="sec-story">四、故事线：四幕剧</h2>
<div class="story-list">
 <div class="story-card s-promise"><span class="story-num">1</span><h3>家门口的约</h3><p>神把律法交给父亲们，教育是约的传承。</p></div>
 <div class="story-card"><span class="story-num">2</span><h3>异教的工具箱</h3><p>希腊罗马发明了逻辑、修辞与七艺，却没有十字架。</p></div>
 <div class="story-card s-christ"><span class="story-num">3</span><h3>教会接过工具</h3><p>奥古斯丁到中世纪大学：工具被带进教会，有时也带进了偶像。</p></div>
 <div class="story-card s-end"><span class="story-num">4</span><h3>改教与再出发</h3><p>回到圣经，要理问答为心，古典为器；荷兰与现代运动各自延续。</p></div>
</div>
</section>

<section>
<h2 id="sec-arts">五、七艺：三艺与四艺</h2>
<div class="table-wrap"><table><thead><tr><th>三艺 trivium</th><th>对象</th><th>古代意义</th><th>改革宗用途</th></tr></thead><tbody>
<tr><td>📝 文法 grammatica</td><td>语言</td><td>读懂文本、正确用词，含文学阅读</td><td>读懂圣经与信条；尊重神所赐语言</td></tr>
<tr><td>🧩 逻辑 dialectica</td><td>推理</td><td>定义、分类、三段论、辨谬</td><td>分辨真理与异端（约一4:1）</td></tr>
<tr><td>🎤 修辞 rhetorica</td><td>说服</td><td>按场合、听众说服人</td><td>用爱心说诚实话（弗4:15）；讲道与护教</td></tr>
</tbody></table></div>
<div class="table-wrap"><table><thead><tr><th>四艺 quadrivium</th><th>对象</th><th>古代意义</th><th>改革宗用途</th></tr></thead><tbody>
<tr><td>🔢 算术</td><td>数本身</td><td>数的性质</td><td>神是有秩序的神（林前14:33）</td></tr>
<tr><td>📐 几何</td><td>空间中的数</td><td>欧几里得式证明</td><td>受造界的稳定可知</td></tr>
<tr><td>🎵 音乐</td><td>时间中的数</td><td>比例与和谐，非仅演奏</td><td>诗篇歌唱；日内瓦诗篇</td></tr>
<tr><td>🌌 天文</td><td>时空中的数</td><td>天体运行与历法</td><td>诸天述说神的荣耀（诗19:1）</td></tr>
</tbody></table></div>
<div class="warn-box"><b>⚠️ 难点：塞耶斯阶段对应</b><p class="mb-0">文法期（约小学）、逻辑期（约初中）、修辞期（约高中）是1947年塞耶斯的现代改编。古代与中世纪的三艺是学科，不是儿童发展阶段。可以当教学经验参考，<span class="mark-warn">不能当作圣经或古代传统</span>。</p></div>
</section>

<section>
<h2 id="sec-eras">六、逐时代详解</h2>
<p>每个时代都按：前因 → 真实背景 → 核心 → 为什么 → 做了什么 → 圣经与圣约 → 信条对照 → 难点 → 应用 → 记忆句。</p>
{era_sections()}
</section>

<section>
<h2 id="sec-hard">七、四大难点（务必分清）</h2>
<div class="card-grid">
 <div class="warn-box"><b>① 古典 ≠ 自动基督教</b><p class="mb-0">西塞罗与柏拉图的学校也是古典的。决定一所学校是否基督教的，是它教导的神观与人观，不是拉丁文课。</p></div>
 <div class="warn-box"><b>② 希腊德性 vs 恩典</b><p class="mb-0">德性靠习惯与理性养成；圣洁由圣灵借道更新（海德堡第33主日）。古典品格教育若取代称义与成圣，就是新律法主义。</p></div>
 <div class="warn-box"><b>③ 塞耶斯阶段是教法</b><p class="mb-0">有用，但不是经文，也不是古代。</p></div>
 <div class="warn-box"><b>④ 教育不能重生人</b><p class="mb-0">多特第三四项第4条：自然之光不足；重生是圣灵的主权工作（约3:5–8）。教育是蒙恩之约中的养育，不是救恩的手段。</p></div>
</div>
</section>

<section>
<h2 id="sec-angles">八、不同视角</h2>
<div class="facet">
 <div class="f-app"><b>👨‍👩‍👧 父母</b><p>我是第一位教师（申6；多特）。我的洗礼誓约要求我关心孩子学什么、由谁教。古典课程是工具，家中的敬拜与教理才是根。</p></div>
 <div class="f-why"><b>🧑‍🏫 教师</b><p>我在家长委托的领域工作（领域主权）。每一门课：真理在哪？神的荣耀在哪？罪如何扭曲这门学问？</p></div>
 <div class="f-creed"><b>⛪ 牧师</b><p>教会不办一切，但必须牧养：主日教理讲道、教理班、看顾教师与家长。不让‘古典’成为新的身份骄傲。</p></div>
 <div class="f-did"><b>🎒 学生</b><p>学拉丁文、逻辑、几何，是为了读得懂、想得清、说得真，最终爱神爱人。我不是因成绩被称义的。</p></div>
</div>
</section>

<section>
<h2 id="sec-memory">九、记忆路径：一句一时代</h2>
<div class="flow">
<div class="step">📜 施玛在家</div><span class="arr">→</span><div class="step">🏛️ 希腊问德</div><span class="arr">→</span><div class="step">🗣️ 罗马善言</div><span class="arr">→</span>
<div class="step">✝️ 奥古斯丁拿金子</div><span class="arr">→</span><div class="step">👑 查理曼办学</div><span class="arr">→</span><div class="step">🎓 大学女王</div><span class="arr">→</span>
<div class="step">📖 回到源头</div><span class="arr">→</span><div class="step">🔥 1524·1559·1563·1618</div><span class="arr">→</span><div class="step">🌷 一寸不让</div><span class="arr">→</span><div class="step">🧰 失落的工具</div>
</div>
<p class="mem">🧠 总纲：敬畏为根，圣约为家，三艺为器，基督为王。</p>
</section>

<footer class="site-footer">
  <div class="footer-brand">欧陆改革宗 · 基督教古典教育研读</div>
  <div class="footer-sub">v20261012</div>
  <p>讲解为原作。经文只标章节，信条只标条款号。约数年代已标“约”。地图为示意。</p>
  <p class="mb-0">Soli Deo Gloria.</p>
</footer>
</div></main></div>
<button type="button" class="back-top" id="back-top" aria-label="回到顶部">↑</button>
<script src="assets/app.js?v={V}"></script>
</body>
</html>
'''
open("index.html","w",encoding="utf-8").write(HTML)
print("ok", len(HTML))
