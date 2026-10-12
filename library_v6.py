# -*- coding: utf-8 -*-
# v20261012-6：补全真实章节目录、中心思想、评论（长处/警惕/用法），单列书卡。由 library_v5.py 末尾 exec。
# CAT: full=完整真实章节目录；part=真实标题但只到篇/部；single=原作单篇无分章（目录概要）；summary=未查到完整目录（目录概要）
CAT={}; SRC={}
def F(zh,nodes,src,cat="full"):
    TREE[zh]=nodes; CAT[zh]=cat; SRC[zh]=src; KIND[zh]="full" if cat=="full" else "struct"
L=lambda xs:[H(x) for x in xs]
GB="Project Gutenberg"; AO="AmblesideOnline 全文目录"
ORBIS=['1 The Invitation', '2 God', '3 The World', '4 Heaven', '5 Fire', '6 The Air', '7 The Water', '8 The Clouds', '9 The Earth', '10 The Fruits of the Earth', '11 Metals', '12 Stones', '13 A Tree', '14 Fruits of Trees', '15 Flowers', '16 Pot-herbs', '17 Corn', '18 Shrubs', '19 Birds', '20 Tame-Fowl', '21 Singing Birds', '22 Birds that live in the Fields and Woods', '23 Ravenous Birds', '24 Water-Fowl', '25 Flying Vermin', '26 Four footed Beasts about the House', '27 Herd-Cattle', '28 Labouring Beasts', '29 Wild-Cattle', '30 Wild Beasts', '31 Creeping things', '32 Crawling Vermin', '33 Amphibious Creatures', '34 River-fish and Pond-fish', '35 Sea-fish and Shell-fish', '36 Man', '37 The Seven Ages of Man', '38 The outward parts of a Man', '39 The Head and the Hands', '40 The Flesh and Bowels', '41 The Chanels and Bones', '42 The outward and inward Senses', '43 The Soul of Man', '44 Deformed and monstrous People', '45 The Dressing of Gardens', '46 Husbandry', '47 Grasing', '48 The making of Honey', '49 Grinding', '50 Bread-baking', '51 Fishing', '52 Fowling', '53 Hunting', '54 Butchery', '55 Coquinaria（拉丁索引名）', '56 Cookery', '57 Brewing', '58 A Feast', '59 The dressing of Line', '60 Weaving', '61 Linen Cloaths', '62 The Taylor', '63 Sutor（拉丁索引名）', '64 The Carpenter', '65 The Mason', '66 Engines', '67 A House', '68 A Mine', '69 The Black-smith', '70 The Box-maker', '71 The Potter', '72 The parts of a House', '73 The Stove with the Bed-room', '74 Wells', '75 The Bath', '76 The Barbers Shop', '77 The Stable', '78 Dials', '79 The Picture', '80 Looking-glasses', '81 The Cooper', '82 The Cord-wainer', '83 The Travellor', '84 The Horseman', '85 Carriages', '86 Carrying to and fro', '87 Passage over Waters', '88 Swimming', '89 A Galley', '90 A Merchant Ship', '91 Shipwreck', '92 Writing', '93 Paper', '94 Printing', '95 The Book-sellers Shop', '96 The Book-binder', '97 A Book', '98 A School', '99 The Study', '100 Arts belonging to Speech', '101 Musical Instruments', '102 Philosophy', '103 Geometry', '104 The Aspects of the Planets', '105 The Apparitions of the Moon', '106 The Eclipses', '107 The Terrestial Sphere', '108 Europe', '109 Moral Philosophy', '110 Prudence', '111 Diligence', '112 Temperance', '113 Fortitude', '114 Patience', '115 Humanity', '116 Justice', '117 Liberality', '118 The Society betwixt Man and Wife', '119 The Tree of Consanguinity', '120 The Society betwixt Parents and Children', '121 The Society betwixt Master and Servant', '122 Urbs（拉丁索引名）', '123 A City', '124 Judgment', '125 The Torments of Malefactors', '126 Merchandizing', '127 Measures and Weights', '128 Physick', '129 A Burial', '130 A Stage-play', '131 Sleights', '132 The Fencing-School', '133 Tennis play', '134 Dice-play', '135 Races', '136 Boys Sports', '137 The Kingdom and Region', '138 Kingly Majesty', '139 The Souldier', '140 The Camp', '141 The Army and the Fight', '142 The Sea-fight', '143 The Besieging of a City', '144 Religion', '145 Gentilism', '146 Judaism', '147 Christianity', '148 Mahometism', '149 God’s Providence', '150 The last Judgment', '151 The Close']

F("忏悔录",[H(f"卷{c}") for c in "一 二 三 四 五 六 七 八 九 十 十一 十二 十三".split()],"拉丁原典十三卷；周士良译本（商务，1963）")
for t in TREE["忏悔录"]:
    g={"卷一":"婴孩与童年；学校里的罪","卷二":"十六岁；偷梨","卷三":"迦太基；读西塞罗《荷尔顿西乌斯》；摩尼教","卷四":"教修辞；朋友之死","卷五":"罗马、米兰；遇安波罗修","卷六":"米兰的挣扎","卷七":"新柏拉图主义与神的属性","卷八":"花园中“拿起来读”","卷九":"受洗；莫尼加之死","卷十":"记忆；现在的试探","卷十一":"时间","卷十二":"创1:1 解释","卷十三":"创世的寓意与安息"}[t[0]]
    t[1].append(P(g))
F("雄辩术原理",[H(f"卷{c}",[P(g)]) for c,g in zip("一 二 三 四 五 六 七 八 九 十 十一 十二".split(),
 ["幼儿教育与语法教师","修辞学校；修辞的定义与价值","修辞的部分与演说三类","绪言与陈述","证明（论证）","结语与情感；笑","布局","风格总论；比喻","修辞格；文章结构","阅读书目与写作操练","得体、记忆与发表","完美演说家：善于言说的好人"])],"Loeb 古典丛书分卷（十二卷）")
F("词源",[H(f"卷{c} {t}") for c,t in zip("一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五 十六 十七 十八 十九 二十".split(),
 ["语法 De grammatica","修辞与辩证 De rhetorica et dialectica","数学（四艺）De mathematica","医学 De medicina","法律与时间 De legibus et temporibus","书籍与教会职事 De libris et officiis ecclesiasticis","神、天使与圣徒 De Deo, angelis et sanctis","教会与派别 De ecclesia et sectis","语言、民族、国度 De linguis, gentibus, regnis","词语 De vocabulis","人与异象 De homine et portentis","动物 De animalibus","世界及其部分 De mundo et partibus","大地及其部分 De terra et partibus","建筑与田地 De aedificiis et agris","石与金属 De lapidibus et metallis","农事 De rebus rusticis","战争与竞技 De bello et ludis","船、建筑与衣物 De navibus, aedificiis et vestibus","食物与家用农具 De penu et instrumentis"])],"Lindsay 拉丁校勘本二十卷卷名")
F("大教学论",[H("致读者"),H("献辞"),H("教学艺术的用途")]+[H(f"第{i}章 {t}") for i,t in enumerate([
 "人是受造物中最高、最完全、最优越者","人的终极目的在今生之外","今生只是永生的预备","永生预备的三阶段：认识自己（及万物）、管理自己、归向神","学问、德行、虔信的种子天然植于人心","人要成为人，必须受教育","人在幼年最易成形，过此难以正确塑造","青少年须共同受教，故需学校","男女青少年都应入学","学校教育应当普及一切","迄今没有完善的学校","学校可以改革","学校改革的基础在于万事有确切秩序","教学的确切秩序须取法自然","延长生命的基础","教与学的普遍要求：必然成功的教学法","教与学的便易原则","教与学的彻底原则","教学的简捷与迅速原则","科学的教法","艺术的教法","语言的教法","道德的教法","灌输虔信的教法","若按真基督教改革学校，须移除异教书籍或更审慎地使用","学校纪律","按年龄与程度的四级学校","母育学校概要","国语学校概要","拉丁学校概要","大学、游学与“光明学院”","教学的普遍完善次序","实施此普遍方法的前提"],1)],"Keatinge 英译本“各章主题”（中文为本站译）")
F("世界图解",[H("序言与字母表"),H("课目（共151课，按1659英译本索引编号）",[H(x) for x in ORBIS])],"Project Gutenberg #28299 英拉对照本索引（英文为原标题）")
F("大学的理念",[H("序言"),H("第一部分 大学教学（讲演九篇）",L(["导言","神学是知识的一个分支","神学对其他知识分支的影响","其他知识分支对神学的影响","知识本身即是目的","知识与学问的关系","知识与专业技能的关系","知识与宗教的关系","教会对知识的责任"])),
 H("第二部分 大学科目（讲演与论文）",L(["引言信","告白","基督教与文学","文学","英国天主教文学","初级学习","当今一种不信的形式","大学讲道","基督教与自然科学","基督教与科学研究","心智的训练（对夜校学员讲）","基督教与医学"]))],"Project Gutenberg #24526 目录（中文为本站译）")
F("父母与孩子",[H("序言")]+[H(f"第{i}章 {t}") for i,t in enumerate(["家庭","作为统治者的父母","作为激发者的父母：儿童须重生进入理智生活","作为激发者的父母：心智生命靠观念成长","作为激发者的父母：属灵的事","作为激发者的父母：来自父母的原初观念","作为校长的父母","品格的培养：作为训练者的父母","品格的培养：缺点的处理","圣经课：作为宗教教导者的父母","信心与本分（书评）：作为道德教师的父母","信心与本分（书评）：哲学作为教育工具的主张","信心与本分（书评）：人凭信心活着，向神向人","父母要给出英雄的激励","可能吗？（书评）：父母对社会问题的态度","管教：给父母的思考","感觉与情感：父母可教育的感觉","感觉与情感：父母可教育的情感","“真理是什么？”：父母需要的道德分辨","说明理由：父母对竞争性考试的责任","向父母提出的教育理论纲要","教育理论问答","从何而来、往何处去：从何而来","从何而来、往何处去：往何处去","父母需要的伟大承认","永恒的孩子：给父母的最高完全之劝"],1)]+[H("附录")],AO+"（第2卷，中文为本站译）")
F("学校教育",[H("序言")]+[H(f"第{i}章 {t}") for i,t in enumerate(["家庭与学校中的受教与权威","家庭与学校中的受教与权威（二）：权威如何行事","“高明的不作为”","儿童作为人的若干权利","心理学与当代思想","若干教育理论检视","一个足够的教育理论","儿童应有的若干关系","一位伟大的教育家（书评）","体育训练中被忽视的方面","智育训练中被忽视的方面","德育训练中被忽视的方面","宗教训练中被忽视的方面","一个主导思想","教科书及其教育作用","如何使用教科书","教育是关系的科学：我们被所亲近的塑造","我们被所亲近的塑造（二）：更多亲和","我们被所亲近的塑造（三）：呼召——一份教育宣言","课程建议（一）","课程建议（二）：教科书","课程建议（三）：对知识的爱"],1)]+[H("附录")],AO+"（第3卷，中文为本站译）")
F("智性生活",[H("1 智性的呼召",L(["智识者有神圣的呼召","智识者并不孤立","智识者属于他的时代"])),H("2 天主教智识者的德性",L(["共同的德性","智识者特有的德性","祈祷的精神","身体的操练"])),
 H("3 生活的安排",L(["简化","独处","与同伴合作","培养必要的交往","保留必要的行动","守护内在的静默"])),H("4 工作的时间",L(["工作的连续","夜间的工作","早晨与晚间","充盈的时刻"])),
 H("5 工作的领域",L(["比较研究","托马斯主义：知识的理想框架","我们的专业","必要的牺牲"])),H("6 工作的精神",L(["研究的热忱","专注","顺服真理","眼界的广阔","奥秘感"])),
 H("7 工作的预备",[H("A 阅读",L(["不要多读","选择得当","四种阅读","接触天才作者","调和而非强调对立","吸收并活出所读"])),H("B 记忆的管理",L(["记什么","按什么次序记","如何记"])),H("C 笔记",L(["如何做笔记","如何分类笔记","如何使用笔记"]))]),
 H("8 创造性的工作",L(["写作","超脱自我与世界","恒心、忍耐与坚持","把事做好并做完","不尝试力所不及的事"])),H("9 工作者与人",L(["保持与生活的接触","懂得休息","接受考验","珍惜喜乐","期待果实"]))],"美国天主教大学出版社英译本目录（中文为本站译）")
F("如何阅读一本书",[H("序言"),H("第一篇 阅读的层次",L(["第一章 阅读的活力与艺术","第二章 阅读的层次","第三章 阅读的第一个层次：基础阅读","第四章 阅读的第二个层次：检视阅读","第五章 如何做一个自我要求的读者"])),
 H("第二篇 阅读的第三个层次：分析阅读",L(["第六章 一本书的分类","第七章 透视一本书","第八章 与作者找出共通的词义","第九章 判断作者的主旨","第十章 公正地评断一本书","第十一章 赞同或反对作者","第十二章 辅助阅读"])),
 H("第三篇 阅读不同读物的方法",L(["第十三章 如何阅读实用型的书","第十四章 如何阅读想像文学","第十五章 阅读故事、戏剧与诗的一些建议","第十六章 如何阅读历史书","第十七章 如何阅读科学与数学","第十八章 如何阅读哲学书","第十九章 如何阅读社会科学"])),
 H("第四篇 阅读的最终目标",L(["第二十章 阅读的第四个层次：主题阅读","第二十一章 阅读与心智的成长"])),H("附录一 建议阅读书目"),H("附录二 四种层次阅读的练习与测验"),H("索引")],"商务印书馆 2004 年郝明义、朱衣译本目录（豆瓣）")
F("教育学原理",[H("一 导论 Inleiding"),H("二 教育的目的 Het doel der opvoeding"),H("三 教育的出发点 Het uitgangspunt der opvoeding"),H("四 教育的方法 De methode der opvoeding")],"1904 年荷文原版（neocalvinism.org 全文 PDF）")
F("基督教教育哲学",L(["序言","对世界观的需要","基督教世界观","基督教有神论之外的选项","中立","伦理","基督教教育哲学","学术事项","从幼儿园到大学"])+[H("附录",L(["A 公共教育","B 新教世界观","C 艺术与福音","D 学习","E 以自然主义为基础的道德教育"]))],"Trinity Foundation《克拉克全集》第10卷目录（中文为本站译）")
F("美国教育的弥赛亚特性",[H("前言；序；导言（Ivan R. Bierly）")]+[H(f"{i} {t}") for i,t in enumerate(["博雅教育","教育的“神圣权利”","贺拉斯·曼与美国教育的弥赛亚特性","詹姆斯·卡特：左右人民的引擎","谢尔登：奥斯威戈与世俗学校","亨利·巴纳德：天球的运转","哈里斯：国家与人的真我","约翰·斯韦特：国家的自我保存","德加莫：道德即社会适应","帕克上校：神圣国家中的神圣儿童","威廉·詹姆斯：教育与条件作用","巴特勒：为国家而教育","斯坦利·霍尔：以儿童为中心的社会","霍恩：人与普遍者","杜威的新耶路撒冷：“伟大共同体”","华生：科学与乌托邦","沃什伯恩：拯救民主的教育","桑代克：教育即科学","博德：“进步主义是新的绝对主义吗？”","克伯屈：废除过去","拉格：民主作为弥赛亚宗教","康茨：谁来控制教育？","布拉梅尔德：民主与共识","幼儿园：新伊甸的模型","大学在法律之上吗？","高等教育的自由","“教育作为宗教”","最小公分母"],1)]+[H("附录（David L. Hoggan）")],"Ross House 1995 版目录；初版 Craig Press 1963（中文为本站译）")
F("为负责任的行动而教育",[H("第一部",L(["倾向的学习","教导责任","对立的教育理论"])),H("第二部",L(["道德主体的结构","以管教培养倾向","以示范培养倾向","倾向的内化","道德的认知结构","再一个策略：决疑法","若干限定与应用"])),H("第三部",L(["价值澄清的策略"])),H("附录 对分类学的反思"),H("索引")],"Internet Archive 1980 年版（中文为本站译）")
F("教育、基督教与国家",L(["信心与知识","基督教学术的重要性（为传福音／为护教／为建立教会）","基督教与文化","改革政府学校","基督教学校的必要","要设立联邦教育部吗？","拟议的教育部（1926 年国会作证）","基督教学校：美国的盼望","威斯敏斯特神学院：宗旨与规划"]),"Trinity Foundation 1987 年版（据 Douglas Douma 书评逐篇核对；中文为本站译）")
F("基督教教育的基础",[H("编者序"),H("第一部",L(["教育中的对立（范泰尔）","在对基督教学校的态度上做改革宗（伯克富）"])),H("第二部",L(["创造：人的教育——神命定的需要（范泰尔）","圣约：恩典之约及其对基督教教育的意义（伯克富）","信心：信心与我们的事工（范泰尔）","权柄：基督教学校与权柄（伯克富）","永生：完满的生命（范泰尔）"])),H("注释")],"P&R 1990 年版目录（中文为本站译）")
F("基督教教育哲学阐释",[H("序言"),H("导论")]+[H(f"{i} {t}") for i,t in enumerate(["基督教信仰的知识论基础","教育与偶像崇拜","教育作为圣约的一个面向","教育与治理全地","为动物命名：敬虔求学的个案","教育与文明","论教会在提供教育上的角色"],1)]+[H("附录A 圣经与诸约"),H("附录B 敬拜与治理")],"Kuyper Foundation 版目录（中文为本站译）")
F("重修荒场",L(["导言（Detweiler）","教育中的对立导论（Wilson）","个人圣洁的重要（Wilson）","基督教学校的士气与敬虔纪律（Spencer）","合乎圣经的世界观思考（Schlect）","世界观个案：数学课里的基督教（Nance）","平等主义：大敌（Wilson）","三艺在小学的应用（Garfield）","古典模式：三艺入门（Spencer）","教学七律（Spencer）","逻辑的为何与如何（Nance）","拉丁文的为何与如何（Wilson）","历史的为何与如何（Schlect）","文学的为何与如何（Wilson）","修辞的为何与如何（Wilson）","护教学的为何与如何（Wilson）","章程、政策与准则（Wilson）","课程的选择与监督（Garfield）","仆人学校（Garfield）","代行亲职（Spencer）","办学的实际步骤（Garfield）","政府教育的兴衰（Wilson）"]),"图书馆编目内容附注（Canon Press 1996，中文为本站译）")
F("神的教化",L(["神的教化","教学的“障碍”：为什么约翰尼学得越来越少","反对教育券的简短声明","校服的圣经意义","古典就等于改革宗吗？","逻辑大骗局","为灰修士学院辩护","福音派学院为何不是","古典学问与基督教学院"]),"Canon Press 1999 年版篇目（中文为本站译）")
F("为平安而教育",L(["序言","导论","重新思考基督教高等教育","为平安而教：论基督教学院教育的目标","二十世纪末基督教学院的使命","信仰与学问的整合——这个观念","论合乎圣经的人观心理模型","信仰与学问的连接点","我们为之教育的世界","为无私的学问辩护","后现代文化中基督教大学的计划","为公义而教：塑造学生的行动倾向","自述：二十年思考基督教高等教育","学术与基督教信念能相融吗？","凯波尔论基督教学术","特殊视角：偏见还是通道？","宗教性大学的学术自由","在多元社会中并为多元社会的基督教学问","手工应在基督教学院有地位吗？","何为改革宗的基督教高等教育观？","勇敢的呼召：回应《信仰与理性》通谕","后记","参考书目","索引"]),"Eerdmans 2004 年版目录（柏林洪堡大学图书馆目录扫描；中文为本站译）")
F("多特教会规章（第21条等）",[H("第1条 总则"),H("第一部 论职分（第2–28条）",[H("第21条 长执会须设立好的学校教师")]),H("第二部 论会议（第29–52条）"),H("第三部 论教义、圣礼及其他仪式（第53–70条）"),H("第四部 论惩戒与教会劝诫（第71–86条）")],"1619 年多特教会规章四部八十六条")
F("哲学的慰藉",[H(f"卷{c}",[P(g)]) for c,g in zip("一 二 三 四 五".split(),["哲学女神来访，诊断病因","命运之轮：外在之物不能给福","真福在神（含“哦，以永恒之理治理世界者”诗）","恶人为何似乎得势；天意与命运","天意、预知与自由意志"])],"拉丁原典五卷（各卷散文与诗交替）")
F("闲暇：文化的基础",[H("T. S. 艾略特导言"),H("闲暇：文化的基础"),H("哲学行动")],"1952 年 Dru 英译本（WorldCat/Internet Archive）","part")
F("派代亚计划",[H("第一部 一个民族的学校教育"),H("第二部 基础学校教育的要素",L(["对所有人相同的目标","对所有人相同的课程","克服起初的障碍","个别差异"])),H("第三部 教与学",[P("三种教学：讲授、辅导、苏格拉底研讨；教师培养；校长")]),H("第四部 基础教育之后",[P("谋生、高等学习、自由制度的未来")])],"图书馆编目与评论所列篇章（部分章名未能逐一核实）","part")
F("训练有素的心智",[H("第一部 语法期（学前–4年级）"),H("第二部 逻辑期（5–8年级）"),H("第三部 修辞期（9–12年级）"),H("第四部 在家教育的实际问题",[P("各部内按科目分章：阅读写作、历史、数学、科学、语言、艺术音乐等")])],"出版社介绍（各版章名有变动，未逐章核实）","part")
F("异象之约",[H("文学与生活"),H("教育"),H("宗教"),H("书信")],"Eerdmans 1958 年版四部分（篇名未逐一核实）","part")

SINGLE={
"致青年：论如何从希腊文学获益":"原作为一篇劝勉辞，现代版本仅编节号（1–10），无章题。",
"论教师":"原作为奥古斯丁与儿子阿德奥达图斯的对话，后世编者分十四章但无章题。",
"致莱塔书（第107封信）":"原作为书信一封，仅有节号（1–13）。",
"论诸艺归于神学":"原作为短论，仅有节号（1–26）。",
"致德意志各城市市长与议员书":"原作为一篇公开信，路德未分章。",
"论送子女上学的讲道":"原作为一篇讲道，未分章。",
"论正确开办文学学校":"原作为致斯特拉斯堡市政官的短论，未分章。",
"论教育":"原作为致哈特利布的书信体短文，未分章。",
"领域主权":"原作为 1880 年自由大学开学演讲，未分章。",
"失落的学艺":"原作为 1947 年牛津演讲，未分章。",
"现代教育与古典":"原作为单篇论文（后收入《文集》），未分章。",
}
for k,v in SINGLE.items(): CAT[k]="single"; SRC[k]=v

def cat(zh): return CAT.get(zh, "full" if KIND.get(zh, TOC.get(zh,("struct",))[0])=="full" else "summary")
# 古典、中世纪分卷著作：卷次即作者原分（真实章节层级）
for zh in ["理想国","尼各马可伦理学","论演说家","论基督教教义","教导（圣俗学问指南）","教学论（学习指南）","为三艺辩护（逻辑论）","菲萝洛基亚与墨丘利的婚礼","算术原理","论神职人员的培育","视察员教导（萨克森学校规程）","日内瓦学院章程","教师之书"]:
    CAT[zh]="full"; SRC.setdefault(zh,"原作分卷/分部（卷次为真实层级，卷下说明为本站要点）")
SUMNOTE="未能查到可核实的完整章节目录；以下为本站整理的目录概要，不是原书标题。"

# 中心思想 = 1–2 句；评论 = 长处 / 警惕 / 用法
import re as _re
def _ev_parts(b):
    ev=_re.sub(r"<[^>]+>","",b["ev"]); m=_re.split(r"⚠️",ev)
    pro=m[0].replace("✅","").strip(" 。"); con=(m[1].strip(" 。") if len(m)>1 else "")
    return pro,con
USE={
"理想国":"只精读卷二–三、卷七：讨论“故事塑造灵魂”和“洞穴上升”，再用诗19与罗1对照“光从哪里来”。",
"尼各马可伦理学":"读卷二（习惯与中道）给教师和家长做“习惯清单”；同时用海德堡问答第86–91问说明成圣的根源是基督而非习惯本身。",
"论演说家":"修辞期学生读卷一选段，讨论“雄辩须以广博学问为本”，并与雅各书3章对照“舌头”。",
"雄辩术原理":"教师读卷一、卷十、卷十二：幼儿语言环境、读写操练与“善人善言”；作为写作课程设计的古典范本。",
"致青年：论如何从希腊文学获益":"给中学生作阅读伦理的入门：拿来一段希腊诗，练习“蜜蜂采花”——取其善、拒其恶。",
"论教师":"教师读书会一次读完：讨论“语言只是提醒，光照来自基督”，再对照加尔文《要义》1.7–9 圣灵内证。",
"论基督教教义":"卷二与卷四是重点：建立“掠夺埃及人”的课程原则与讲道修辞；适合学校领袖制订文学书单原则。",
"忏悔录":"高年级读卷一（学校与童年）、卷八（悔改）、卷十（记忆）；讨论教育中的“欲望秩序”。",
"致莱塔书（第107封信）":"家长直接借用：字母游戏、以圣经人名练字、按次序读经，并为孩子选择环境与同伴。",
"菲萝洛基亚与墨丘利的婚礼":"只作历史参考：用来说明“七艺”名称与次序的来源；不必通读。",
"算术原理":"数学教师了解中世纪四艺中“数”的观念；可选读卷一论数之和谐，配合诗篇谈受造的秩序。",
"哲学的慰藉":"修辞期读卷二–三：讨论幸福与命运；补上波爱修没有说出的——十字架与复活才是真慰藉。",
"教导（圣俗学问指南）":"学校领袖读卷二短短七章，看俗学如何服侍读经；作“修院式”图书馆规划的参考。",
"词源":"作工具书：给拉丁课找词源与中世纪知识框架；不需通读。",
"论神职人员的培育":"读卷三论学问部分，说明加洛林时期“学七艺为读圣经”的传统。",
"教学论（学习指南）":"教师读卷三“阅读方法与学者德性”（谦卑、安静、简朴）；拿来做教师培训的一课。",
"为三艺辩护（逻辑论）":"读卷一，看12世纪如何反驳“学语法逻辑没用”的功利派；今日家长会可引用。",
"论诸艺归于神学":"教师读一遍（很短）：讨论“一切学科都指向神”，再用比利时信条第2条“两本书”校正其神秘主义倾向。",
"论教师（真理论第11题）":"与奥古斯丁《论教师》对读：讨论教师作为“次因”的尊严与限度。",
"致德意志各城市市长与议员书":"学校领袖与董事会必读：语言是福音的刀鞘；城市（今日的教会与家庭）有办学责任。",
"视察员教导（萨克森学校规程）":"按三班结构对照今日课程：识字–语法–修辞，加上教理问答与音乐。",
"论送子女上学的讲道":"家长会讲章素材：上学是呼召，不只是谋生；对照第五诫与海德堡问答第104问。",
"论正确开办文学学校":"学校领袖了解“年级制+敬虔雄辩”的源头，设计逐年升级与考核。",
"日内瓦学院章程":"对照今日学校章程：信仰告白、班级制度、纪律；看改革宗学校怎样把教会、学校与城市连起来。",
"教师之书":"拉丁教师借用“双重翻译”法；家长读第一书论温和管教。",
"多特教会规章（第21条等）":"长执会与学校董事会读第21条：教会对学校有监督责任；配合三种要理问答层级规划。",
"语言入门":"拉丁教师了解“按主题学词汇、句子对照”的方法源头；可仿作双语主题句卡。",
"论教育":"读全文（短）：抄下“修复始祖堕落”的定义，讨论其与改革宗“神的形像更新”（西3:10）的异同。",
"大教学论":"教师读第16–19章（便易、彻底、简捷原则）与第27–31章（四级学校）；其泛智乐观要用堕落论校正。",
"世界图解":"低年级直接使用：一课一图，名词配图；可做中文–英文–拉丁三语卡。",
"大学的理念":"读第一部第5–7讲（知识本身即目的）；学校领袖讨论博雅与职业的关系。",
"领域主权":"董事会读：家庭、教会、学校、国家各有主权；据此划定学校与家长、教会的权责。",
"家庭教育":"家长借用叙述、习惯训练、户外观察；在“人观”处用海德堡问答第5–8问校正。",
"父母与孩子":"家长读第2章（作为统治者的父母）与第7章（作为校长的父母）；讨论父母权柄来自神。",
"加尔文主义讲座":"教师读第四讲（学术）：普遍恩典与对立并存，作为学科整合的框架。",
"教育学原理":"中文研究者可据荷文目录整理：目的–出发点–方法三分，做改革宗教育学的骨架。",
"学校教育":"教师读第15–16章（教科书）与第20–22章（课程建议）：用“活的书”替换干瘪课本。",
"青少年的教育":"中学教师与家长了解巴文克对青春期的关注：宗教与道德成长需要家庭与学校同行。",
"新教育":"研究用：了解巴文克如何回应 20 世纪初的儿童研究与新教育运动。",
"智性生活":"教师与高中生读第3–4章（生活安排与时间）和第7章（阅读、记忆、笔记）；把托马斯主义框架换成改革宗认信框架。",
"现代教育与古典":"领袖读一遍：教育目的取决于人生观；拿来回应“古典只是方法”的说法。",
"巴文克的教育哲学":"研究用：英文世界最早系统介绍巴文克教育思想的论文。",
"如何阅读一本书":"高中阅读课教材：分析阅读四问；第十八章读哲学书可配合要理问答训练提问。",
"人之废":"全校读书会：先读第1章“无胸之人”讨论情感教育，再读附录“道之例证”对照十诫。",
"基督教教育哲学":"领袖读“中立”一章：教育不可能中立；再读“从幼儿园到大学”作课程讨论。",
"失落的学艺":"教师入门必读：了解三阶段说的出处；同时说明它是一篇演讲，不是课程标准。",
"闲暇：文化的基础":"教师读第一篇：闲暇不是懒散而是受敬拜滋养的静观；对照安息日诫命。",
"基督教教育的基本原理":"研究用：1953 年北美改革宗教育论文集，可追溯范泰尔“对立”一文的出处。",
"异象之约":"高中文学教师读“教育”部分：基督徒如何读文学、为何博雅。",
"美国教育的弥赛亚特性":"领袖读第3章（贺拉斯·曼）与第15章（杜威）：认出公共教育中的救赎叙事。",
"基督教教育文集":"领袖读：对立、圣约、知识论；把范泰尔的预设论用在课程审查上。",
"为负责任的行动而教育":"教师读第二部：管教、示范、讲理三种培养倾向的方法，直接用于课堂管理。",
"规范与高贵":"领袖读第8章（基督教 paideia 的应许）与第11–12章（学园与三校设计）。",
"派代亚计划":"借用“三柱教学”：讲授、辅导、苏格拉底研讨；用来检查课表是否只有讲授。",
"教育、基督教与国家":"家长会与董事会读“基督教学校的必要”：自由、真理与圣约儿女。",
"基础":"",
"基督教教育的基础":"新教师入职必读：伯克富论圣约、范泰尔论对立，两篇各一次讨论。",
"与神同行在课堂":"教师用作课程与教学设计手册：每单元写出“信仰视角”与评量方式。",
"基督教教育哲学阐释":"领袖读第3章“教育作为圣约的一个面向”：父母责任与学校的代行角色。",
"重修荒场":"新办学校的实务手册：第8–16章各科“为何与如何”，第17–21章办学章程。",
"古典教育：席卷美国的运动":"了解运动全景与路线差异；作为向家长解释“古典有多种”的资料。",
"训练有素的心智":"在家教育家庭的课程清单；书单中世俗与宗教材料需按信条筛选。",
"神的教化":"读“神的教化”与“古典就等于改革宗吗？”两篇；注意作者神学立场需分辨。",
"古典教育与在家教育":"给初接触的家长一本小册：一晚读完，讨论三艺。",
"古典基督教教育之辩":"领袖读“对立”与“古典基督教的回答”两章；书中涉及的作者立场见难点⑥。",
"古典教育导论：家长指南":"家长入门小册：用于招生说明会。",
"为平安而教育":"高等教育与高中领袖读“为平安而教”与“凯波尔论基督教学术”两篇。",
"智慧与雄辩":"学校实务首选：第4–5章（共同体与课程）作为学校发展规划的蓝本。",
"渴慕神国":"教师读第1–2章：礼仪塑造爱；据此检视学校日常作息（晨祷、诗歌、节期）。",
"为真理之故的美":"数学与科学教师读第1、4章：四艺与美；用诗19说明受造秩序。",
"核心：古典教育的根基":"家长用第二部各章（阅读、写作、数学、历史）作语法期课程清单。",
"毁掉孩子想象力的十种方法":"家长读书会：每章一项自我检查（户外、独处、童话、英雄）。",
"博雅传统":"领袖与教师读“范式”一章（PGMAPT），用来规划从敬虔到神学的全课程。",
"救赎六艺":"华人学校与家庭：读第7–9章，讨论礼乐书数射御如何在基督里被分辨和使用。",
"重获失落的学艺":"中文读者入门：先读第三部第7章“三艺与基督教学校”，再读附录塞耶斯原文。",
}
def comment_html(b):
    pro,con=_ev_parts(b); u=USE.get(b["zh"]) or "按本卡“推荐对象”选读相关章节，并用三项联合信条校正其神学预设。"
    return f'''<div class="bk-sec bk-cmt"><h5>评论 <small>欧陆改革宗视角</small></h5>
<dl class="cmt"><dt>长处</dt><dd>{pro}</dd>{f"<dt>警惕</dt><dd>{con}</dd>" if con else ""}<dt>用法</dt><dd>{u}</dd></dl></div>'''

_old_tree_html=tree_html
def tree_html(nodes,pre="",lv=1):
    out=[]
    for i,(t,c) in enumerate(nodes,1):
        num=f"{pre}{i}"; pt=t.startswith("~"); txt=t[1:] if pt else t
        own=bool(_re.match(r'^(第|卷|§|附录|\d|[一二三四五六七八九十]+ )',txt))
        lab=('<span class="tn-num" aria-hidden="true"></span>' if own else f'<span class="tn-num">{num}</span>')+f'<span class="tn-t">{txt}</span>'+('<span class="kp">要点</span>' if pt else '')
        cls=f"tn l{min(lv,4)}"+(" pt" if pt else "")+(" own" if own else "")
        if c: out.append(f'<li class="{cls}"><details{" open" if lv==1 and len(nodes)<=14 and len(c)<=24 else ""}><summary>{lab}</summary><ul>{tree_html(c,num+".",lv+1)}</ul></details></li>')
        else: out.append(f'<li class="{cls}"><span class="tn-leaf">{lab}</span></li>')
    return "".join(out)

CATLAB={"full":("完整章节目录","ok"),"part":("真实篇/部标题（章名未全）","part"),"single":("原作无分章 · 目录概要","single"),"summary":("目录概要（未查到完整目录）","sum")}
def toc_html(b):
    tr=to_tree(b["zh"]); c=cat(b["zh"]); lab,cl=CATLAB[c]
    note=SRC.get(b["zh"]) or (SUMNOTE if c=="summary" else "")
    if c=="summary": note=SUMNOTE
    return f'''<div class="bk-sec bk-toc"><h5>目录 <span class="toc-badge {cl}">{lab}</span> <small>{count(tr)} 条</small></h5>
<p class="toc-src">{"📖 来源：" if c in ("full","part") else "ℹ️ "}{note}</p>
<div class="tree-ctrl"><button type="button" class="tc-btn" data-tc="open">全部展开</button><button type="button" class="tc-btn" data-tc="close">全部收起</button></div>
<ul class="tree">{tree_html(tr)}</ul></div>'''

def book_cards():
    out=[]
    for b in sorted(B,key=lambda x:x["y"]):
        gname,gc=G[b["g"]]; t=TRAD.get(b["zh"],"E"); tn,tc=T[t]
        zz="yes" if b["zh"] in ZH else "no"
        s=(b["zh"]+" "+b["orig"]+" "+b["au"]).replace('"',"")
        if zz=="yes":
            zt,ztr,zpub,zyr,zn=ZH[b["zh"]]; zb=f'<span class="pill zh">🀄 中译：{zt} · {ztr} · {zpub} · {zyr}</span>'
        elif b["zh"] in WEBZH: zb=f'<span class="pill web">🌐 {WEBZH[b["zh"]]}</span>'
        else: zb='<span class="pill no">暂无中译（书名为本站译）</span>'
        out.append(f'''<article class="book" id="bk-{zlib.crc32(b["zh"].encode())%1000000}" data-g="{b["g"]}" data-a="{b["a"]}" data-zh="{zz}" data-t="{t}" data-s="{s}" style="--c:{gc}">
<header class="bk-head"><div class="bk-meta"><span class="pill grp">{gname}</span><span class="pill trad" style="--tc:{tc}">{tn}</span><span class="pill yr">{b["ys"]}</span></div>
<h4 class="book-title">《{b["zh"]}》</h4><p class="book-orig">{b["orig"]}</p>
<p class="book-au">{b["au"]} <span class="stars" aria-label="难度{b["st"]}星">{stars(b["st"])}</span></p>
<div class="bk-zh">{zb}</div></header>
<div class="bk-sec bk-thesis"><h5>中心思想</h5><p>{b["core"]}</p></div>
{toc_html(b)}
{comment_html(b)}
<p class="bk-foot"><span>推荐：{b["who"]}</span><span class="mem">记忆：{b["mem"]}</span></p>
</article>''')
    return "".join(out)

def shelf():
    sp=""
    for b in sorted(B,key=lambda x:x["y"]):
        n=len(b["zh"]); h=max(120,46+n*17)
        yr=str(b["y"]).replace("-","前")
        sp+=f'<a class="spine{" zh" if b["zh"] in ZH else ""}" href="#bk-{zlib.crc32(b["zh"].encode())%1000000}" style="--c:{G[b["g"]][1]};--h:{h}px" title="《{b["zh"]}》{b["au"].split(" ")[0]} · {b["ys"]}" aria-label="《{b["zh"]}》，{b["ys"]}"><span>{b["zh"]}</span><em>{yr}</em></a>'
    leg="".join(f'<span class="lg"><i style="--c:{c}"></i>{n}</span>' for n,c in G.values())
    return f'<div class="shelf" role="list">{sp}</div><div class="shelf-leg">{leg}<span class="lg"><i class="zhm"></i>金顶 = 已有中译</span></div><p class="viz-note">书脊按年代排列，可左右滑动；书名完整竖排，悬停或长按可见作者与年份；点击跳到该书卡片。</p>'

for b in B:
    if b["zh"]=="美国教育的弥赛亚特性": b["ys"]="1963年（Craig Press）"
NFULL=sum(1 for b in B if cat(b["zh"])=="full"); NPART=sum(1 for b in B if cat(b["zh"])=="part")
NSINGLE=sum(1 for b in B if cat(b["zh"])=="single"); NSUM=sum(1 for b in B if cat(b["zh"])=="summary")
F("青少年的教育",[H("第一部分 青少年教育史 Uit de geschiedenis der neopaedie",L(["§1 在原始民族中 Bij de Natuurvolken","§2 在希腊与罗马 In Griekenland en Rome","§3 在基督教会中 In de Christelijke Kerk","§4 在基督教社会中 In de Christelijke Maatschappij","§5 宗教改革之后 Na de Hervorming","§6 在主日学中 In de Zondagscholen","§7 在青年会中 In de Jongelingsvereenigingen","§8 来自政府方面 Van Overheidswege"])),
 H("第二部分 青少年教育的任务 Over de taak der neopaedie",L(["§9 现有青少年教育的缺口 Leemten in de bestaande Neopaedie","§10 青少年教育的必要 Noodzakelijkheid der Neopaedie","§11 青少年教育的原则 Beginselen der Neopaedie","§12 青少年的教育者 De opvoeders der rijpere jeugd","§13 青少年心理学 Psychologie van de rijpere jeugd","§14 宗教与道德教育 De godsdienstig-zedelijke Opvoeding","§15 社会教育 De sociale Opvoeding","§16 政治教育 De politieke Opvoeding","§17 方法 Methode","§18 组织 Organisatie"]))],"1916 年 Kok 版荷文原书目录（neocalvinism.org 全文 PDF；中文为本站译）")
NFULL=sum(1 for b in B if cat(b["zh"])=="full"); NPART=sum(1 for b in B if cat(b["zh"])=="part")
NSINGLE=sum(1 for b in B if cat(b["zh"])=="single"); NSUM=sum(1 for b in B if cat(b["zh"])=="summary")
