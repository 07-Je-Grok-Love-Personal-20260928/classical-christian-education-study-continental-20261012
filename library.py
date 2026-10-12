# -*- coding: utf-8 -*-
# 书库（由 sections.py exec）。tocv=True 表示目录/结构已经网上核对；False 表示“目录概要（未逐章核对）”。
# zhn：'中译' = 已核实的已出版/已发布中文译名；'译名' = 本站自译。
G={"classical":("🏛️ 古典源头","#6ba3e0"),"patristic":("✝️ 教父与中世纪","#b39ddb"),"reform":("🔥 宗教改革","#c45c5c"),"modern":("🌷 近现代奠基","#e6d4a0"),"movement":("🧰 当代运动","#f0b8b8")}
AUD={"parent":"家长","teacher":"教师","leader":"学校领袖"}
B=[
dict(g="classical",a="teacher leader",zh="理想国",zhn="中译",orig="Politeia (Republic)",au="柏拉图 Plato",y=-375,ys="约前375年（约数）",tocv=False,
 toc="十卷。教育集中在卷二–三（诗乐与体育、审查故事）与卷七（洞穴喻、数学与辩证法的上升课程）。",
 core="教育是灵魂的转向（从影子转向实在），而不是往空容器里灌知识。",
 ev="✅ 看见教育塑造爱与欲望，并重视数学训练心智。⚠️ 哲人王与城邦控制儿童、灵魂先存与回忆说，违背圣经的人观与家庭领域；比利时信条14、多特三四4：理性之光不足以引人到真神。",
 who="教师、领袖",st=4,mem="洞穴：转身向光；但真光是基督（约1:9）。"),
dict(g="classical",a="teacher leader",zh="尼各马可伦理学",zhn="中译",orig="Ethika Nikomacheia",au="亚里士多德 Aristotle",y=-330,ys="约前4世纪后期（约数）",tocv=False,
 toc="十卷：幸福与目的、德性是习惯与中道、自愿与选择、各项德性、公正、理智德性、自制、友爱、快乐与沉思生活。",
 core="德性靠反复行动养成为第二天性；教育就是习惯化与理性的结合。",
 ev="✅ “习惯塑造品格”对课堂常规、背诵、礼仪很有用。⚠️ 德性的源头是人自己、终点是自我完善；改革宗：善行出于真信心、照神律法、为神荣耀（海德堡问答91）。",
 who="教师、领袖",st=4,mem="习惯成自然——但新心出于恩典。"),
dict(g="classical",a="teacher",zh="论演说家",zhn="译名",orig="De Oratore",au="西塞罗 Cicero",y=-55,ys="前55年",tocv=False,
 toc="三卷对话：演说家需要的广博学识、立意与布局、风格与发表。",
 core="理想演说家必须通晓哲学、法律、历史——修辞以广博学问为根。",
 ev="✅ 修辞课的经典范本，反对空洞技巧。⚠️ 目标是共和国的荣誉；基督徒修辞的动机是爱与真理（弗4:15）。",
 who="教师",st=4,mem="西塞罗：口才要有学问作底。"),
dict(g="classical",a="teacher leader",zh="雄辩术原理",zhn="中译",orig="Institutio Oratoria",au="昆体良 Quintilian",y=95,ys="约公元95年（约数）",tocv=False,
 toc="十二卷：卷一–二幼年与初级教育、教师品格；卷三–十一修辞理论（立意、布局、风格、记忆、发表）；卷十二理想演说家“善言的好人”。",
 core="从摇篮开始的系统教育；反对体罚，重视教师品格与因材施教。",
 ev="✅ 卷一对幼儿语言教育、教师品格的观察至今实用。⚠️ “好人”靠修养养成，没有罪与恩典的维度。",
 who="教师、领袖",st=3,mem="昆体良：善言的好人，从摇篮教起。"),
dict(g="patristic",a="teacher leader parent",zh="论基督教教义",zhn="中译",orig="De doctrina christiana",au="奥古斯丁 Augustine",y=396,ys="约396年开笔，约426/427年完成",tocv=False,
 toc="四卷：卷一“事物”（享受神、使用万物）；卷二–三“记号”（释经所需的语言、学问与“掠夺埃及人”）；卷四讲道修辞。",
 core="一切学问是为了读懂圣经、爱神爱人；异教中的真理属于神，可以取用。",
 ev="✅ 改革宗使用古典的总原则：享受神、使用万物；真理都是神的。⚠️ 寓意释经偏多；读时以圣经清晰性与充足性为准（比利时信条7）。",
 who="家长、教师、领袖",st=4,mem="享受神，使用万物；拿金子，不拜金牛犊。"),
dict(g="patristic",a="teacher",zh="论教师",zhn="中译",orig="De magistro",au="奥古斯丁 Augustine",y=389,ys="约389年（约数）",tocv=False,
 toc="与儿子阿德奥达图斯的对话：语词作为记号能否教导；结论是内在的教师基督光照人。",
 core="人类教师只能提示，真正使人明白的是内在的教师基督。",
 ev="✅ 使教师谦卑：理解与归信是神的工作（多特三四11–12）。⚠️ 带有柏拉图式光照论色彩，需要用圣灵借道工作的教义校正。",
 who="教师",st=4,mem="老师指路，基督开眼。"),
dict(g="patristic",a="teacher leader",zh="教导（圣俗学问指南）",zhn="译名",orig="Institutiones divinarum et saecularium litterarum",au="卡西奥多鲁斯 Cassiodorus",y=562,ys="约6世纪中叶（约数）",tocv=False,
 toc="两卷：卷一圣学（圣经各卷、注释者、抄经）；卷二俗学（七艺简明手册）。",
 core="为修士设计的阅读课程：先圣经，后七艺；七艺服事释经。",
 ev="✅ 把七艺明确放在圣经之下，并保存古典文本。⚠️ 修院式分离圣俗；改革宗的呼召观使一切合法职业都是事奉。",
 who="教师、领袖",st=3,mem="卡西奥多鲁斯：先圣书，再七艺。"),
dict(g="patristic",a="teacher leader",zh="教学论（学习指南）",zhn="译名",orig="Didascalicon de studio legendi",au="圣维克多的雨果 Hugh of St Victor",y=1127,ys="约1120年代后期（约数）",tocv=True,
 toc="六卷：卷一–三世俗学问（分类、七艺、阅读方法与学者德性）；卷四–六圣经阅读（正典、历史—寓意—道德三层读法）。",
 core="“学习一切，以后你会发现没有什么是多余的”；阅读是恢复神形像的途径。",
 ev="✅ 把学习与谦卑、默想、德性连在一起。⚠️ 学习被看作恢复形像的途径，带有修养救赎色彩；恢复靠基督（海德堡第33主日）。",
 who="教师、领袖",st=4,mem="雨果：读书是灵修，但医治在基督。"),
dict(g="patristic",a="teacher",zh="为三艺辩护（逻辑论）",zhn="译名",orig="Metalogicon",au="索尔兹伯里的约翰 John of Salisbury",y=1159,ys="1159年",tocv=True,
 toc="四卷：为语法与逻辑辩护，反对图省事的“康尼菲修斯派”；回忆沙特尔学派的教学；评论亚里士多德《工具论》。",
 core="三艺不可跳过；学问的捷径造成空洞的人。",
 ev="✅ 对“速成文凭”的批评直指今日。⚠️ 中世纪框架中恩典成全自然的倾向需留意。",
 who="教师",st=4,mem="不学语法逻辑，就是康尼菲修斯。"),
dict(g="reform",a="parent leader",zh="致德意志各城市市长与议员书",zhn="译名",orig="An die Ratherren aller Städte deutsches Lands",au="路德 Martin Luther",y=1524,ys="1524年",tocv=False,
 toc="书信体：父母失职与城市责任；语言（希伯来、希腊、拉丁）是福音的刀鞘；男女孩都应上学；建立图书馆。",
 core="为了福音和社会，城市必须开办并维持学校；古典语言保护福音。",
 ev="✅ 改教者的教育宣言，与海德堡问答103“维持学校”一脉相承。⚠️ 交给市政承担，后来易滑向国家主导教育；需用领域主权平衡。",
 who="家长、领袖",st=2,mem="路德1524：语言是福音的刀鞘。"),
dict(g="reform",a="leader teacher",zh="视察员教导（萨克森学校规程）",zhn="译名",orig="Unterricht der Visitatoren",au="梅兰希顿 Philipp Melanchthon",y=1528,ys="1528年",tocv=True,
 toc="学校部分把拉丁学校分为三级：①读写、基础语法、祷文；②语法进阶、圣经、德育、音乐；③翻译、古典文学、修辞与演说。",
 core="分级、少而精、拉丁为主，教理贯穿。",
 ev="✅ 改教时期课程设计范本，可直接参照分学段。⚠️ 路德宗传统，圣餐与礼仪部分与改革宗不同。",
 who="领袖、教师",st=3,mem="梅兰希顿1528：三级拉丁学校。"),
dict(g="reform",a="leader",zh="日内瓦学院章程",zhn="译名",orig="Leges Academiae Genevensis",au="加尔文等 John Calvin et al.",y=1559,ys="1559年",tocv=True,
 toc="私塾七个班级（从字母与法语、拉丁到希腊文、古典阅读、修辞）；公学讲授神学、希伯来文、希腊文、艺学；附信仰告白与纪律。",
 core="改革宗学校模式：古典语言+信条+教会纪律，培养牧者与公民。",
 ev="✅ 欧陆改革宗古典教育的原型，教会—学校关系清楚。⚠️ 城邦政教结合的环境与今日不同。",
 who="学校领袖",st=3,mem="日内瓦1559：七班私塾，一座公学。"),
dict(g="reform",a="teacher leader",zh="大教学论",zhn="中译",orig="Didactica Magna",au="夸美纽斯 Jan Amos Comenius",y=1657,ys="拉丁文本1657年",tocv=False,
 toc="三十余章：人的终极目的与教育必要性、普及教育、按自然秩序教学的原则、语言/德性/虔诚的教法、学制（母育、母语、拉丁、大学四级）。",
 core="把一切知识教给一切人；按自然顺序、由感官到理解。",
 ev="✅ 分级学制、图文并茂、普及教育。⚠️ 对教育改造世界期望过高（多特三四4）；属弟兄合一会，非三项联合信条传统。",
 who="教师、领袖",st=3,mem="夸美纽斯：一切人学一切事。"),
dict(g="reform",a="parent teacher",zh="世界图解",zhn="中译",orig="Orbis Sensualium Pictus",au="夸美纽斯 Jan Amos Comenius",y=1658,ys="1658年",tocv=False,
 toc="约一百五十课图文对照：从神、世界、自然、人体到手艺、社会、宗教，拉丁文与母语并列。",
 core="第一部儿童图画课本：看图学词、学物。",
 ev="✅ 语法期的范本：词与物对应（创2:19–20）。⚠️ 同上，非改革宗。",
 who="家长、教师",st=1,mem="图画书之父：看图识词。"),
dict(g="modern",a="leader",zh="领域主权",zhn="译名",orig="Souvereiniteit in eigen kring",au="凯波尔 Abraham Kuyper",y=1880,ys="1880年（自由大学开学演讲）",tocv=False,
 toc="演讲：自由大学的三重意义——领域主权、改革宗原则、学术自由。",
 core="家庭、教会、学校、国家各有神所授的主权；基督对每一领域宣告主权。",
 ev="✅ 改革宗学校论的基石：学校受家长委托，不归国家或教会直接掌控。⚠️ 实务上需防止“领域”变成隔离主义。",
 who="学校领袖",st=3,mem="凯波尔1880：一寸不让。"),
dict(g="modern",a="teacher leader",zh="教育学原理",zhn="译名",orig="Paedagogische beginselen",au="巴文克 Herman Bavinck",y=1904,ys="1904年",tocv=False,
 toc="目录概要（未逐章核对）：教育的基础（人观、神的形像）、目标、主体与对象、手段。尚无完整英译。",
 core="教育建基于创造与神的形像；恩典恢复自然，而不废除自然。",
 ev="✅ 最贴近三项联合信条的教育学理论。⚠️ 中文、英文资料少，多靠二手介绍。",
 who="教师、领袖",st=5,mem="巴文克1904：恩典恢复自然。"),
dict(g="modern",a="parent teacher",zh="青少年的教育",zhn="译名",orig="De opvoeding der rijpere jeugd",au="巴文克 Herman Bavinck",y=1916,ys="1916年",tocv=False,
 toc="目录概要（未逐章核对）：青春期的心理、宗教与道德发展，家庭与学校如何陪伴。",
 core="以改革宗人观吸收当时心理学，讨论青少年的成长。",
 ev="✅ 对修辞期（青少年）的牧养有帮助。⚠️ 部分心理学已过时。",
 who="家长、教师",st=4,mem="巴文克1916：陪伴青少年。"),
dict(g="modern",a="parent teacher leader",zh="人之废",zhn="中译",orig="The Abolition of Man",au="C.S.路易斯 C. S. Lewis",y=1943,ys="1943年",tocv=True,
 toc="三章：①没有胸膛的人；②道；③人之废。附录：道的例证。",
 core="现代教育切除“胸膛”（受训练的情感），使人不再按客观价值去爱该爱的。",
 ev="✅ 有力论证客观价值与情感教育。⚠️ 以普世“道”为基础，接近自然法，未诉诸特殊启示；改革宗会补上罗1:18–21：人知道却压制。",
 who="家长、教师、领袖",st=3,mem="路易斯1943：没有胸膛的人。"),
dict(g="modern",a="parent teacher leader",zh="失落的学习工具",zhn="译名",orig="The Lost Tools of Learning",au="多萝西·塞耶斯 Dorothy L. Sayers",y=1947,ys="1947年演讲，1948年刊印",tocv=False,
 toc="单篇演讲：现代学生会很多科目却不会思考；提出三艺阶段对应（鹦鹉期、好辩期、诗意期）。",
 core="教学生“如何学习”的工具，而非只装科目。",
 ev="✅ 点燃现代运动。⚠️ 阶段对应是她的现代构想，不是古代传统，也不是圣经。",
 who="所有人",st=1,mem="塞耶斯1947：鹦鹉、好辩、诗意。"),
dict(g="modern",a="teacher leader",zh="基督教教育文集",zhn="译名",orig="Essays on Christian Education",au="范泰尔 Cornelius Van Til",y=1974,ys="1974年（图书馆目录；部分资料作1971年）",tocv=False,
 toc="文集，分三部分，第三部分曾单独发表；主题含改革宗教育观、对中立的批判、教师与学生。",
 core="没有中立的教育；一切知识以神的自我启示为前提。",
 ev="✅ 预设论把对立讲得最尖锐。⚠️ 对普遍恩典与使用异教经典的语气可能比凯波尔、巴文克更严厉，需平衡。",
 who="教师、领袖",st=4,mem="范泰尔：没有中立地带。"),
dict(g="movement",a="teacher leader",zh="规范与高贵",zhn="译名",orig="Norms and Nobility: A Treatise on Education",au="戴维·希克斯 David V. Hicks",y=1981,ys="1981年",tocv=True,
 toc="美德是学习的果子；道就是真理；教导“成人之父”；专制的意象；拯救表象；论教条的必要；大众的高贵化；基督教 paideia 的应许；课程提案；问题与假设；一座学园三所学校；学校中的学校；结语。",
 core="教育的目标是塑造“理想类型”的人，以规范和高贵为标尺。",
 ev="✅ 深刻、文雅，为运动提供哲学。⚠️ 偏重古典人文理想，罪与恩典着墨少。",
 who="教师、领袖",st=5,mem="希克斯：美德是学习的果子。"),
dict(g="movement",a="parent teacher leader",zh="重拾失落的学习工具",zhn="译名",orig="Recovering the Lost Tools of Learning",au="道格拉斯·威尔逊 Douglas Wilson",y=1991,ys="1991年",tocv=True,
 toc="四部十二章：一、现代世俗教育的失败；二、独特的基督教教育（教育的真职分、知识的性质、在亚当里的学生）；三、独特的古典教育（古典心智、三艺与基督教学校、现代性障碍、“敬虔的”无知、在家教育）；四、结论（国家的界限、需要古典与基督教教育）。",
 core="把塞耶斯模式与基督教学校结合，反对国家教育。",
 ev="✅ 运动起点，“在亚当里的学生”一章承认罪。⚠️ 作者与联邦愿景争议（见难点⑥）；非欧陆改革宗。",
 who="家长、教师、领袖",st=2,mem="威尔逊1991：运动起点。"),
dict(g="movement",a="parent leader",zh="古典教育：席卷美国的运动",zhn="译名",orig="Classical Education: The Movement Sweeping America",au="维思与克恩 Gene Edward Veith Jr. & Andrew Kern",y=1997,ys="1997年（2001年二版）",tocv=False,
 toc="目录概要（未逐章核对）：美国教育的问题；古典教育的定义；基督教、民主、道德等多种古典主义路线；在家教育与高等教育（二版增章）。",
 core="古典教育以真、善、美滋养灵魂，培养智慧与美德。",
 ev="✅ 路线总览广，适合入门。⚠️ 维思是路德宗，书中也介绍天主教与世俗路线，需自行分辨。",
 who="家长、领袖",st=2,mem="维思与克恩：运动地图。"),
dict(g="movement",a="parent",zh="训练有素的心智",zhn="译名",orig="The Well-Trained Mind: A Guide to Classical Education at Home",au="苏珊·怀斯·鲍尔与杰西·怀斯 Susan Wise Bauer & Jessie Wise",y=1999,ys="1999年",tocv=True,
 toc="三部：一、语法期（学前–4年级）；二、逻辑期（5–8年级）；三、修辞期（9–12年级）；各部按科目给方法与资源。",
 core="在家古典教育的操作手册，四年历史循环。",
 ev="✅ 极具操作性。⚠️ 有意保持宗教中立，信仰教育要家长自己加上（海德堡问答为骨架）。",
 who="家长",st=2,mem="鲍尔：四年一循环。"),
dict(g="movement",a="parent",zh="古典教育与在家教育",zhn="译名",orig="Classical Education and the Homeschool",au="威尔逊、卡利汉、琼斯 Douglas Wilson, Wes Callihan, Douglas Jones",y=2001,ys="2001年（修订小册）",tocv=False,
 toc="目录概要（未逐章核对）：约七十页小册，概述在家实施古典与基督教教育、三艺。",
 core="在家同样可以做古典基督教教育。",
 ev="✅ 简短入门。⚠️ 同威尔逊的神学注意点。",
 who="家长",st=1,mem="一本小册，在家起步。"),
dict(g="movement",a="parent leader",zh="古典基督教教育之辩",zhn="译名",orig="The Case for Classical Christian Education",au="道格拉斯·威尔逊 Douglas Wilson",y=2003,ys="2003年",tocv=True,
 toc="序；墙上的又一块砖；十年之后；对立；古典基督教的回答；基督教学校的生活；课程建议；永恒成果的黎明；注释。",
 core="对立是根本：中立教育不存在，基督徒需要自己的学校。",
 ev="✅ “对立”一章与凯波尔、范泰尔相通。⚠️ 同上。",
 who="家长、领袖",st=2,mem="威尔逊2003：对立。"),
dict(g="movement",a="parent",zh="古典教育导论：家长指南",zhn="译名",orig="An Introduction to Classical Education: A Guide for Parents",au="克里斯托弗·佩林 Christopher A. Perrin",y=2004,ys="2004年",tocv=False,
 toc="目录概要（未逐章核对）：约四十八页；古典教育的历史与复兴、三艺、古典语言、伟大书籍整合。",
 core="给家长的最短入门。",
 ev="✅ 适合发给新家长。⚠️ 篇幅短，神学深度有限。",
 who="家长",st=1,mem="佩林：四十八页入门。"),
dict(g="movement",a="teacher leader",zh="渴慕神国",zhn="译名",orig="Desiring the Kingdom: Worship, Worldview, and Cultural Formation",au="詹姆斯·K·A·史密斯 James K. A. Smith",y=2009,ys="2009年",tocv=True,
 toc="导论；一、渴慕与想象的动物（礼仪人；爱需要操练；危险时代的爱人）；二、渴慕神国（从敬拜到世界观；操练神国；基督教大学是为爱人设的）。",
 core="人首先是爱的动物；教育通过“文化礼仪”塑造人的爱。",
 ev="✅ 提醒学校的日常习惯在塑造爱。⚠️ 作者属于基督教改革宗教会（CRC）背景并吸收多元传统；偏重礼仪与习惯，需以海德堡问答65（信心由圣灵借福音宣讲而生）平衡。",
 who="教师、领袖",st=4,mem="史密斯：你就是你所爱的。"),
dict(g="movement",a="teacher",zh="为真理之故的美",zhn="译名",orig="Beauty for Truth's Sake: On the Re-enchantment of Education",au="斯特拉特福德·考德科特 Stratford Caldecott",y=2009,ys="2009年",tocv=True,
 toc="导论：与宇宙同唱；四道的传统；教育诗意想象；失落的世界智慧；黄金圆环；向年轻眼目的基路伯合唱；宇宙论的礼仪成全；结论：超越信仰与理性。",
 core="重新发现四艺：数学与宇宙的美把人引向神。",
 ev="✅ 四艺讲得最美。⚠️ 天主教圣礼宇宙观；改革宗用诗19篇与比利时信条2读受造界，但不把自然看作恩典的通道。",
 who="教师",st=4,mem="考德科特：四艺通向美。"),
dict(g="movement",a="parent",zh="核心：古典教育的根基",zhn="译名",orig="The Core: Teaching Your Child the Foundations of Classical Education",au="利·博廷斯 Leigh A. Bortins",y=2010,ys="2010年",tocv=True,
 toc="一、古典模式（今日教育错在哪；为何需要；如何帮助你）；二、语法教育的核心（阅读、写作、数学、地理、历史、科学、艺术；课表与资源）；结语。",
 core="语法期的记忆与背诵是一切的基础。",
 ev="✅ 实用、具体。⚠️ 偏重背诵量，注意难点④（小孩负担过重）。",
 who="家长",st=1,mem="博廷斯：核心在背诵。"),
dict(g="movement",a="teacher leader",zh="博雅传统",zhn="译名",orig="The Liberal Arts Tradition: A Philosophy of Christian Classical Education",au="凯文·克拉克与拉维·杰恩 Kevin Clark & Ravi Scott Jain",y=2013,ys="2013年（2019年修订）",tocv=True,
 toc="范式；敬虔；体育与音乐；七艺（三艺：语法、辩证、修辞；四艺：算术、几何、天文、音乐）；哲学（自然、道德、形而上）；神学；文化、呼召与课程；附录。",
 core="PGMAPT 范式：敬虔—体育与音乐—七艺—哲学—神学，比塞耶斯三阶段更完整。",
 ev="✅ 把“敬虔”放在首位，最接近“敬畏为根”。⚠️ 合一性的表述需由信条充实：敬虔的内容就是要理问答。",
 who="教师、领袖",st=4,mem="PGMAPT：敬虔先行，神学为冠。"),
]

exec(open('library_ext.py',encoding='utf-8').read())
def _old_stars(n): return "★"*n+"☆"*(5-n)

def _old_book_cards():
    out=[]
    for i,b in enumerate(sorted(B,key=lambda x:x["y"])):
        gname,gc=G[b["g"]]
        tl="✅ 目录/结构已核对" if b["tocv"] else "📝 目录概要（未逐章核对）"
        out.append(f'''<article class="book reveal" data-g="{b["g"]}" data-a="{b["a"]}" style="--c:{gc}">
<div class="book-head"><span class="book-grp">{gname}</span><span class="book-year">{b["ys"]}</span></div>
<h4 class="book-title">《{b["zh"]}》<small class="zhn">{b["zhn"]}</small></h4>
<p class="book-orig"><i>{b["orig"]}</i></p>
<p class="book-au">✍️ {b["au"]} · <span class="stars" aria-label="难度{b["st"]}星">{stars(b["st"])}</span></p>
<details class="book-more"><summary>目录 · 观点 · 评价</summary>
<p><b class="tocflag">{tl}</b><br>{b["toc"]}</p>
<p><b>💎 核心观点：</b>{b["core"]}</p>
<p><b>⚖️ 改革宗评价：</b>{b["ev"]}</p>
<p><b>👥 推荐：</b>{b["who"]}</p>
</details>
<p class="mem small">🧠 {b["mem"]}</p>
</article>''')
    return "".join(out)

def _old_book_table():
    rows="".join(f'<tr><td data-v="{b["y"]}">{b["ys"]}</td><td>{b["au"]}</td><td>《{b["zh"]}》<br><small>{b["orig"]}</small></td><td>{G[b["g"]][0]}</td><td>{"✅" if b["tocv"] else "📝"}</td></tr>' for b in sorted(B,key=lambda x:x["y"]))
    return f'<div class="table-wrap"><table class="sortable" id="book-table"><thead><tr><th data-k="num">年份 ⇅</th><th>作者 ⇅</th><th>书名 ⇅</th><th>组别 ⇅</th><th>目录</th></tr></thead><tbody>{rows}</tbody></table></div>'

def _old_book_timeline():
    items="".join(f'<li class="tl-item reveal" style="--c:{G[b["g"]][1]}"><span class="tl-y">{b["ys"].split("（")[0]}</span><span class="tl-t">《{b["zh"]}》<small>{b["au"].split(" ")[0]}</small></span></li>' for b in sorted(B,key=lambda x:x["y"]))
    return f'<ol class="book-tl">{items}</ol>'



FLIP=[("三艺是哪三门？","语法 · 逻辑 · 修辞"),("四艺是哪四门？","算术 · 几何 · 音乐 · 天文"),("箴1:7 说什么是知识的开端？","敬畏耶和华"),
("“掠夺埃及人”出自谁的哪本书？","奥古斯丁《论基督教教义》卷二"),("塞耶斯演讲哪一年？","1947年（1948年刊印）"),("路德致议员书哪一年？","1524年"),
("日内瓦学院哪一年？","1559年"),("海德堡问答哪一问讲“维持学校”？","问答103（第38主日）"),("领域主权是谁提出、哪一年？","凯波尔，1880年"),
("《人之废》第一章叫什么？","没有胸膛的人"),("PGMAPT 指什么？","敬虔·体育与音乐·七艺·哲学·神学（《博雅传统》）"),("比利时信条第2条讲什么？","两本书：受造界与圣经"),
("多特第三四项第4条讲什么？","残存的自然之光不足以使人得救"),("《规范与高贵》作者与年份？","戴维·希克斯，1981年"),("《训练有素的心智》分几部？","三部：语法期、逻辑期、修辞期"),
("“内在的教师”出自哪里？","奥古斯丁《论教师》")]
def flip_deck():
    return '<div class="flip-deck">'+"".join(f'<button type="button" class="flip" aria-label="翻转卡片"><span class="flip-in"><span class="flip-f">❓ {q}</span><span class="flip-b">💡 {a}</span></span></button>' for q,a in FLIP)+'</div>'

QUIZ=[("古典教育本身就是基督教的吗？","不是。古典回答“怎么教、教什么”，基督教回答“为了谁、凭什么”。看神观、人观与教理问答。"),
("塞耶斯三阶段来自古代吗？","不是。是1947年的现代教学法构想；古人把三艺当学科。"),
("基督徒为什么可以读荷马和柏拉图？","普遍恩典：非信徒也能发现真理；同时持守对立，不接收其神观。原则来自奥古斯丁“掠夺埃及人”。"),
("谁是孩子的第一位教理老师？","父母。多特会议列三种教理问答：家中父母、学校教师、教会牧师；洗礼时父母立誓。"),
("威尔逊2017年放弃了联邦愿景的观点吗？","没有。他放弃的是标签，明言信念未变，仍认同《联合联邦愿景声明》。"),
("教育能使孩子重生吗？","不能。重生是圣灵的主权工作（约3:5–8；多特三四11–12）。教育是约中养育。"),
("《博雅传统》比塞耶斯多了什么？","在三艺前加上敬虔、体育与音乐，在后加上哲学与神学（PGMAPT）。"),
("梅兰希顿1528把拉丁学校分几级？","三级：读写与基础语法 → 语法进阶、圣经、音乐 → 翻译、古典、修辞。")]
def quiz():
    return '<div class="quiz">'+"".join(f'<details class="q reveal"><summary><span class="qn">Q{i+1}</span> {q}</summary><p>✅ {a}</p></details>' for i,(q,a) in enumerate(QUIZ))+'</div>'

def filter_bar():
    g="".join(f'<button type="button" class="lf" data-fg="{k}">{v[0]}</button>' for k,v in G.items())
    t="".join(f'<button type="button" class="lf" data-ft="{k}">{v[0]}</button>' for k,v in T.items())
    a="".join(f'<button type="button" class="lf" data-fa="{k}">{v}</button>' for k,v in AUD.items())
    return ('<div class="lib-filter" id="lib-filter" role="search" aria-label="书库筛选">'
     '<div class="lf-row"><input type="search" id="lib-search" class="lib-search" placeholder="🔍 搜索书名 / 作者 / 原名…" aria-label="搜索书库" autocomplete="off" />'
     '<div class="view-tog" role="group" aria-label="视图"><button type="button" class="vt on" data-v="card">▦ 卡片</button><button type="button" class="vt" data-v="list">☰ 列表</button></div></div>'
     f'<div class="lf-row"><span class="lf-label">组别</span><button type="button" class="lf on" data-fg="all">全部</button>{g}</div>'
     f'<div class="lf-row"><span class="lf-label">传统</span><button type="button" class="lf on" data-ft="all">全部</button>{t}</div>'
     f'<div class="lf-row"><span class="lf-label">中译</span><button type="button" class="lf on" data-fz="all">全部</button><button type="button" class="lf" data-fz="yes">🀄 已有中译</button><button type="button" class="lf" data-fz="no">暂无中译</button>'
     f'<span class="lf-label">读者</span><button type="button" class="lf on" data-fa="all">全部</button>{a}</div></div>')

LIB=f'''
<section>
<h2 id="sec-library">十二、书库：基督教古典教育核心书目</h2>
<p class="lead">这是<span class="mark-core">广泛的核心书目</span>（不可能真正穷尽“全部”），每本书的作者、年份与存在都经网上检索核实，查不到的一律删去。共 <b class="counter" data-to="{N}">{N}</b> 本，每本书都显示 <b>📑 目录</b>：<b class="counter" data-to="{NV}">{NV}</b> 本为核对过的完整章节目录，其余为按公认卷册或部分划分的“结构目录”，不编造章名。目录以树状展开：来源中的真实标题用编号（1 / 1.1 / 1.1.1）显示，本站整理的内容用虚线框标“要点概括”，两者分开。<b class="counter" data-to="{NZH}">{NZH}</b> 本已有核实的中文版（标 🀄，含译者、出版方、年份）。</p>
<div class="stat-row">
 <div class="stat"><b class="counter" data-to="{N}">{N}</b><span>本书</span></div>
 <div class="stat"><b class="counter" data-to="5">5</b><span>组别</span></div>
 <div class="stat"><b class="counter" data-to="{NV}">{NV}</b><span>完整章节目录</span></div>
 <div class="stat"><b class="counter" data-to="{NZH}">{NZH}</b><span>已有中译</span></div>
 <div class="stat"><b class="counter" data-to="2400">2400</b><span>年跨度（约）</span></div>
</div>
{filter_bar()}
<h3 id="sec-shelf">书架视图</h3>
{shelf()}
<h3 id="sec-charts">中译与组别图表</h3>
{charts()}
<h3 id="sec-cards">书卡（含目录）</h3>
<p class="lib-count" id="lib-count" aria-live="polite"></p>
<div class="book-grid" id="book-grid">{book_cards()}</div>
<div class="more-wrap"><button type="button" class="btn-more" id="lib-more">加载更多</button></div>

<h3 id="sec-zhlist">中文书单（已有中译本）</h3>
<p>只列查到译者、出版方、年份的中文版。奥古斯丁《论教师》目前只有网络译文，未计入。《训练有素的心智》只查到版权代理的拟译名，未见出版，按“暂无中译”处理。</p>
{zh_list()}
<h3 id="sec-zhflip">中译书名记忆卡</h3>
{zh_flips()}
<h3 id="sec-cmap">作者 → 思想 概念图</h3>
{concept_map()}
<h3 id="sec-booktl">书目时间轴（动画）</h3>
{book_timeline()}

<h3 id="sec-booktable">全部书目表（点表头排序）</h3>
{book_table()}

<h3 id="sec-readpath">阅读路径</h3>
<div class="flow">
<div class="step">1️⃣ 塞耶斯《失落的学艺》<br><small>一晚读完</small></div><span class="arr">→</span>
<div class="step">2️⃣ 路易斯《人之废》<br><small>为什么要教“胸膛”</small></div><span class="arr">→</span>
<div class="step">3️⃣ 威尔逊《重获失落的学艺》（有中译）<br><small>运动起点（带着难点⑥读）</small></div><span class="arr">→</span>
<div class="step">4️⃣ 克拉克与杰恩《博雅传统》<br><small>完整范式</small></div><span class="arr">→</span>
<div class="step">5️⃣ 奥古斯丁《论基督教教义》<br><small>使用异教学问的总原则</small></div>
</div>
<p><b>再深入：</b>家长→《训练有素的心智》《核心》；教师→《规范与高贵》《为真理之故的美》《雄辩术原理》卷一；领袖→路德1524、日内瓦学院章程1559、凯波尔《领域主权》、巴文克教育学著作、范泰尔文集。</p>
</section>

<section>
<h2 id="sec-stepper">十三、三艺动画步进器</h2>
<div class="stepper" id="stepper">
 <div class="st-tabs" role="tablist">
  <button type="button" role="tab" class="st-tab on" data-i="0">📝 语法</button>
  <button type="button" role="tab" class="st-tab" data-i="1">🧩 逻辑</button>
  <button type="button" role="tab" class="st-tab" data-i="2">🎤 修辞</button>
 </div>
 <div class="st-bar"><span id="st-fill"></span></div>
 <div class="st-panels">
  <div class="st-panel on"><h4>知道“是什么”</h4><p>记忆、词汇、拉丁变格、海德堡问答背诵、历史歌诀。<br><b>问句：</b>谁？什么？何时？<br><b>经文：</b>申6:6–7</p></div>
  <div class="st-panel"><h4>明白“为什么”</h4><p>定义、三段论、谬误识别、论证图。<br><b>问句：</b>为什么？是否成立？<br><b>经文：</b>约一4:1；徒17:11</p></div>
  <div class="st-panel"><h4>能“说出来、用出来”</h4><p>演讲、议论文、辩论、毕业论文答辩。<br><b>问句：</b>怎样说服、怎样服事？<br><b>经文：</b>弗4:15；彼前3:15</p></div>
 </div>
 <div class="st-ctrl"><button type="button" class="btn-text" id="st-prev">← 上一步</button><button type="button" class="btn-text" id="st-play">⏸ 暂停</button><button type="button" class="btn-text" id="st-next">下一步 →</button></div>
</div>
</section>

<section>
<h2 id="sec-flip">十四、记忆翻卡</h2>
<p>点卡片翻面，正面是问题，背面是答案。</p>
{flip_deck()}
</section>

<section>
<h2 id="sec-onepage">十五、一页记忆总结</h2>
<div class="mindgrid">
 <div class="mind-root">🎯 敬畏为根 · 圣约为家 · 三艺为器 · 基督为王</div>
 <div class="mind-branch" style="--c:#3d9a6a"><h4>📌 4 个数字</h4><ul><li>1524 路德致议员书</li><li>1559 日内瓦学院</li><li>1563 海德堡问答</li><li>1947 塞耶斯演讲</li></ul></div>
 <div class="mind-branch" style="--c:#6ba3e0"><h4>📌 3 + 4</h4><ul><li>三艺：语法、逻辑、修辞（记、辨、说）</li><li>四艺：算术、几何、音乐、天文（数、形、声、天）</li></ul></div>
 <div class="mind-branch" style="--c:#d4af37"><h4>📌 5 本必读</h4><ul><li>塞耶斯 → 路易斯 → 威尔逊 → 克拉克与杰恩 → 奥古斯丁</li></ul></div>
 <div class="mind-branch" style="--c:#c45c5c"><h4>📌 4 条信条</h4><ul><li>比利时2：两本书</li><li>比利时14 / 多特三四4：残光不足</li><li>海德堡74：儿女在约中</li><li>海德堡103：维持学校</li></ul></div>
 <div class="mind-branch" style="--c:#b39ddb"><h4>📌 6 个方法</h4><ul><li>背诵、讨论、叙述、抄写、展示、辩论</li><li>口诀：背讨叙抄展辩</li></ul></div>
 <div class="mind-branch" style="--c:#f08a8a"><h4>📌 6 个警示</h4><ul><li>古典≠基督教；道德主义；精英化</li><li>小孩过载；教育不重生；联邦愿景</li></ul></div>
</div>
</section>

<section>
<h2 id="sec-quiz">十六、自测</h2>
<p>先想答案，再点开。</p>
{quiz()}
</section>
'''
