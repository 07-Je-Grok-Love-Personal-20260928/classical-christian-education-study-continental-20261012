# -*- coding: utf-8 -*-
# v20261012-5：扩充书目、传统标签、3–4 层目录树。由 library_ext.py 末尾 exec。
# 目录树节点：("标题",[子节点]) = 来源中的真实标题；("~要点",[...]) = 本站要点概括（视觉区分）。
T={"R":("改革宗","#d4af37"),"L":("路德宗","#c45c5c"),"C":("天主教","#b39ddb"),"A":("圣公会","#6ba3e0"),"E":("其他新教/福音派","#5ec4c0"),"F":("教父/中世纪大公","#a8dfc4"),"P":("古典·非基督教","#e8a85c")}
TRAD={"理想国":"P","尼各马可伦理学":"P","论演说家":"P","雄辩术原理":"P","论基督教教义":"F","论教师":"F","教导（圣俗学问指南）":"F","教学论（学习指南）":"F","为三艺辩护（逻辑论）":"F",
"致德意志各城市市长与议员书":"L","视察员教导（萨克森学校规程）":"L","日内瓦学院章程":"R","大教学论":"E","世界图解":"E","领域主权":"R","教育学原理":"R","青少年的教育":"R",
"人之废":"A","失落的学艺":"A","基督教教育文集":"R","规范与高贵":"E","重获失落的学艺":"E","古典教育：席卷美国的运动":"L","训练有素的心智":"E","古典教育与在家教育":"E",
"古典基督教教育之辩":"E","古典教育导论：家长指南":"E","渴慕神国":"R","为真理之故的美":"C","核心：古典教育的根基":"E","博雅传统":"E","智慧与雄辩":"E","救赎六艺":"E","家庭教育":"A"}

def nb(g,a,t,zh,orig,au,y,ys,core,ev,who,st,mem,tree,kind="struct"):
    TRAD[zh]=t; TREE[zh]=tree; KIND[zh]=kind
    B.append(dict(g=g,a=a,zh=zh,zhn="",orig=orig,au=au,y=y,ys=ys,tocv=kind=="full",toc="",core=core,ev=ev,who=who,st=st,mem=mem))
TREE={}; KIND={}
P=lambda s,c=None:("~"+s,c or [])
H=lambda s,c=None:(s,c or [])

# ——— 已验证可深入的现有书目（真实多层标题）———
TREE["博雅传统"]=[H("前言；出版说明；序"),H("范式"),H("敬虔"),H("体育与音乐"),
 H("七艺",[H("三艺",[H("语法"),H("辩证"),H("修辞")]),H("四艺",[H("算术"),H("几何"),H("天文"),H("音乐")])]),
 H("哲学",[H("自然哲学"),H("道德哲学"),H("形而上学（神圣哲学）")]),H("神学"),H("文化、呼召与课程"),H("附录一至五；参考书目；索引")]; KIND["博雅传统"]="full"
TREE["智慧与雄辩"]=[H("引言：教育经济学——需求与供给"),
 H("第一章 教育的目标：智慧与雄辩",[H("为何"),H("如何"),H("我们不是什么"),H("预设")]),
 H("第二章 形成中的丰厚传统",[H("塞耶斯模式"),H("文法"),H("辩证法"),H("修辞")]),
 H("第三章 世界观与博雅技艺",[H("世界观、文化熏陶及形成过程"),H("塑造拥有上帝形象的人"),H("范式的重要性"),H("以谦卑之心拥有世界观思维")]),
 H("第四章 信仰与学习的共同体",[H("风气"),H("关系"),H("传统"),H("课外活动"),H("学生仪态"),H("职业操守"),H("课堂管理"),H("班级规模"),H("外观"),H("招生"),H("计划")]),
 H("第五章 博雅技艺课程",[H("12-K 课程"),H("设计课程范围及顺序",[H("总原则"),H("确定范围与顺序"),H("学术严谨性"),H("综述")]),H("博雅技艺与科学")]),
 H("第六章 语言技艺（更新的三艺）",[H("阅读、书写、拼写与词汇"),H("英语文法"),H("文学"),H("历史"),H("人文课程"),H("古典语言"),H("现代外语"),H("计算机操作"),H("辩证法"),H("辩论"),H("公民学"),H("修辞"),H("写作、演讲、表演"),H("论文写作与答辩")]),
 H("第七章 数学技艺与科学",[H("算术"),H("几何学"),H("自然科学"),H("音乐"),H("真正的知识")]),
 H("第八章 修辞学课程",[H("学习修辞学的理由"),H("注重修辞学的学校——三艺的逆转"),H("文法学校中的修辞学"),H("奥古斯丁的雄辩范式"),H("更新的阿甫托尼乌斯")]),
 H("第九章 教师与博雅传统",[H("个人挑战"),H("思想的习惯"),H("心灵的习惯")]),
 H("第十章 学习与博雅传统",[H("教与学的模式"),H("获得新知识"),H("合宜的信息"),H("记忆的感知模式"),H("批判性互动"),H("有意义的表达")]),
 H("附录",[H("A 写给家长的话"),H("B 公共领域的博雅传统",[H("希伯来人"),H("不同世界的共同主题"),H("危机")]),H("C 统一的共同体",[H("开放的共同体"),H("有规划的共同体"),H("统一共同体中的权柄")])]),H("参考书目")]; KIND["智慧与雄辩"]="full"
TREE["人之废"]=[H("中译导言：道与意识形态",[H("一 道与意识形态"),H("二 上帝之死，与你我有关"),H("三 作为卫道士的路易斯"),H("四 现代人也许更需要卫道士"),H("五 路易斯为何厚古薄今"),H("六 算是结语")]),H("译文说明"),
 H("1 无胸之人",[P("批评一本语法教材把价值判断说成“只是情感”"),P("“胸膛”：受训练的情感，连接理性与欲望")]),H("2 道",[P("客观价值的普遍传统，路易斯称之为“道”")]),H("3 人之废",[P("征服自然最终变成少数“操控者”征服人")]),
 H("4 附录：道之例证",[H("一、一般善行"),H("二、特别善行"),H("三、对父母、长上及祖先之义务"),H("四、对子孙后代之义务"),H("五、公义"),H("六、信德"),H("七、仁慈"),H("八、气节")]),H("译附 路易斯：《主观论之毒害》"),H("答谢")]; KIND["人之废"]="full"
TREE["重获失落的学艺"]=[H("致谢"),
 H("第一部分 现代世俗教育的失败",[H("一 教育危机"),H("二 对世俗教育和基督教教育改革的建议")]),
 H("第二部分 如何拥有独特的基督教教育",[H("三 教育的真正使命"),H("四 知识的特性"),H("五 亚当里面的学生",[P("学生是堕落的罪人，纪律与福音都必需")])]),
 H("第三部分 通向独具特色的古典教育",[H("六 古典思想"),H("七 三艺与基督教学校",[P("采用塞耶斯三阶段")]),H("八 现代性的阻隔"),H("九 “敬虔”的无知问题"),H("十 在家上学，作为另一种选择")]),
 H("第四部分 结论",[H("十一 国家的局限：总结"),H("十二 总结：需要基督教古典教育")]),
 H("附录",[H("A 失落的学艺（塞耶斯）"),H("B 逻各斯学校课程材料"),H("C 简短的历史描述")]),H("参考书目")]; KIND["重获失落的学艺"]="full"

# ——— 新增书目（均经搜索核实作者、年份与存在）———
nb("patristic","teacher parent","F","致青年：论如何从希腊文学获益","Ad adolescentes (Address to Young Men on the Right Use of Greek Literature)","大巴西流 Basil of Caesarea",370,"4世纪后期（约数）",
 "像蜜蜂采花：从希腊诗人与哲人中只取合乎德性的部分，为永生作预备。","✅ 教父使用异教经典的经典范例。⚠️ 偏重道德范例，福音与恩典着墨少；改革宗要补上海德堡第一主日的安慰与第三部分“感恩”。","教师、家长",2,"巴西流：像蜜蜂一样读荷马。",
 [H("§1–§3",[P("为何年轻人可读异教文学：为永生作预备，如先在水中观日影")]),H("§4–§6",[P("蜜蜂喻：选择性阅读，效法德行、避开恶行")]),H("§7–§10",[P("希腊人物的德行例证与基督徒的节制、操练")])])
nb("patristic","parent","F","致莱塔书（第107封信）","Epistula CVII ad Laetam","耶柔米 Jerome",403,"约403年",
 "女孩的教育：从字母积木开始，以诗篇、箴言、福音书为课本，远离世俗享乐。","✅ 家庭与圣经为中心、女童教育受重视。⚠️ 修道式禁欲理想（独身、苦行）不合改革宗呼召观。","家长",2,"耶柔米：用字母积木教圣经。",
 [P("早期识字：象牙字母、以圣经人名练字"),P("读经次序：诗篇 → 箴言 → 传道书 → 约伯 → 福音书、使徒书信 → 先知书等"),P("同伴、仆人与家庭环境的影响"),P("限制异教文学与世俗娱乐")])
nb("patristic","teacher parent","F","忏悔录","Confessiones","奥古斯丁 Augustine",398,"约397–400年（约数）",
 "卷一–二回忆童年上学：被迫背诵、贪爱维吉尔故事、为虚荣学修辞。","✅ 对罪如何渗入学习的最深自省（罗1:21）。⚠️ 新柏拉图主义残留；读时以圣经人观为准。","教师、家长",3,"奥古斯丁：为狄多哭，却不为自己的罪哭。",
 [H("卷一",[P("婴孩已有罪；学字母被打；爱读埃涅阿斯却厌希腊文")]),H("卷二",[P("十六岁辍学闲居；偷梨")]),H("卷三",[P("迦太基求学修辞；读西塞罗《荷尔顿西乌斯》而爱智慧")]),H("卷四–五",[P("教授修辞；摩尼教；到罗马与米兰")]),H("卷六–九",[P("安波罗修讲道；花园归信；母亲莫尼卡")]),H("卷十",[P("记忆与自省")]),H("卷十一–十三",[P("时间、创世记释义")])])
nb("patristic","teacher","F","哲学的慰藉","De consolatione philosophiae","波爱修斯 Boethius",524,"约524年",
 "狱中对话：哲学女神带人从命运的变幻转向至善。","✅ 中世纪最常读的书之一，训练逻辑与诗。⚠️ 几乎不提基督；斯多亚与新柏拉图色彩浓。","教师",3,"波爱修斯：命运之轮转，至善不动。",
 [H("卷一",[P("哀叹与哲学女神出现")]),H("卷二",[P("命运之轮")]),H("卷三",[P("真幸福即至善即神")]),H("卷四",[P("恶人为何昌盛；天命与命运")]),H("卷五",[P("预知与自由意志")]),P("各卷散文（prosa）与诗歌（metrum）交替")])
nb("patristic","teacher","F","算术原理","De institutione arithmetica","波爱修斯 Boethius",500,"约6世纪初（约数）",
 "以尼科马库斯为本的数论教本；首次用“四艺”（quadrivium）一词。","✅ 四艺的源头文本。⚠️ 毕达哥拉斯数论带有神秘色彩。","教师",4,"波爱修斯：四艺之名由此来。",
 [H("卷一",[P("四艺总论；数的分类：奇偶、完全数、比例")]),H("卷二",[P("图形数、比例与中项")])])
nb("patristic","teacher leader","P","菲萝洛基亚与墨丘利的婚礼","De nuptiis Philologiae et Mercurii","马蒂亚努斯·卡佩拉 Martianus Capella",430,"5世纪（约数）",
 "寓言：七位侍女（七艺）在婚礼上各自陈述其学问；中世纪七艺的标准化来源。","✅ 七艺课程的“地图”。⚠️ 异教寓言框架，作者宗教立场多被视为非基督教。","教师、领袖",4,"卡佩拉：七位侍女就是七艺。",
 [H("卷一–二 婚礼寓言"),H("卷三 语法"),H("卷四 辩证"),H("卷五 修辞"),H("卷六 几何"),H("卷七 算术"),H("卷八 天文"),H("卷九 和声（音乐）")])
nb("patristic","teacher leader","F","词源","Etymologiae","塞维利亚的依西多禄 Isidore of Seville",630,"约7世纪初（约数，未完成）",
 "中世纪百科全书：从词源进入万事万物，七艺居首。","✅ 保存古代知识，体现“学问都可归主”。⚠️ 许多词源不可靠。","教师、领袖",3,"依西多禄：七艺开卷的百科全书。",
 [H("卷一 语法"),H("卷二 修辞与辩证"),H("卷三 数学（算术、几何、音乐、天文）"),H("卷四 医学"),H("卷五 法律与时间"),H("卷六–八 圣经、教会、神与天使、异端"),H("卷九–二十 语言民族、人、动物、世界、地理、建筑、矿物、农业、战争、船舶衣物、器具")])
nb("patristic","leader teacher","F","论神职人员的培育","De institutione clericorum","拉巴努斯·毛鲁斯 Rabanus Maurus",819,"819年",
 "加洛林时期的神职教育手册：神职、礼仪，最后一卷讲圣经与七艺如何服事讲道。","✅ 延续奥古斯丁“学问服事圣经”。⚠️ 圣职等级与圣礼观为罗马传统。","领袖、教师",4,"拉巴努斯：七艺为讲台服务。",
 [H("卷一",[P("神职等级、服饰、圣礼")]),H("卷二",[P("日课、节期、礼仪")]),H("卷三",[P("圣经释读、七艺、讲道")])])
nb("patristic","teacher","C","论教师（真理论第11题）","De magistro (Quaestiones disputatae de veritate, q. 11)","托马斯·阿奎那 Thomas Aquinas",1257,"约1256–1259年",
 "人可以作为外在助因真正地教导，好比医生协助自然康复；神是首要的教师。","✅ 平衡奥古斯丁：人类教师确有职分。⚠️ 理性—信仰框架偏亚里士多德，恩典成全自然。","教师",4,"阿奎那：老师如医生，助自然而行。",
 [H("第11题 论教师",[H("第1条 人能否教导并被称为教师（唯有神能？）"),H("第2条 人能否称为自己的教师"),H("第3条 人能否被天使教导"),H("第4条 教导属于活动生活还是沉思生活")])],"full")
nb("patristic","teacher leader","C","论诸艺归于神学","De reductione artium ad theologiam","波纳文图拉 Bonaventure",1255,"约1253–1257年",
 "一切光都来自众光之父：机械技艺、感官、哲学、圣经四种光，最终都指向神学。","✅ “一切学问归于神”的结构图。⚠️ 圣礼主义与神秘主义色彩。","教师、领袖",4,"波纳文图拉：四种光，同归众光之父（雅1:17）。",
 [P("外在之光：机械技艺"),P("较低之光：感官知觉"),P("内在之光：哲学（理性、自然、道德）"),P("较高之光：圣经"),P("各种光如何“归于”神学：道成肉身、生活次序、与神联合")])
nb("reform","parent leader","L","论送子女上学的讲道","Eine Predigt, daß man Kinder zur Schulen halten solle","路德 Martin Luther",1530,"1530年",
 "父母有责任让孩子上学：为教会预备传道人，为社会预备官员与人才。","✅ 把教育放在呼召与公共利益之下。⚠️ 主张强制上学的论证需配合领域主权，避免国家吞并家庭。","家长、领袖",2,"路德1530：上学为讲台，也为市政厅。",
 [H("第一部分：属灵的益处",[P("传道职分需要受教育的人")]),H("第二部分：属世的益处",[P("法律、政府、医学等需要受教育的人")]),P("劝勉父母与官长")])
nb("reform","leader","R","论正确开办文学学校","De literarum ludis recte aperiendis","斯图谟 Johann Sturm",1538,"1538年",
 "斯特拉斯堡文理中学的蓝图：分班、拉丁雄辩、敬虔，目标是“智慧而雄辩的敬虔”。","✅ 加尔文在斯特拉斯堡亲见，影响日内瓦学院。⚠️ 偏重西塞罗式拉丁文体。","学校领袖",3,"斯图谟1538：敬虔、智慧、雄辩。",
 [P("学校目标：敬虔与雄辩"),P("按年级分班与逐年升级"),P("拉丁与希腊课程次序"),P("教师与考核")])
nb("reform","teacher parent","A","教师之书","The Scholemaster","罗杰·阿斯卡姆 Roger Ascham",1570,"1570年（遗著）",
 "反对体罚，主张温和而严格；以“双重翻译”教拉丁文。","✅ 英国新教人文主义教育的经典，方法至今可用。⚠️ 部分对意大利文化的批评带时代偏见。","教师、家长",3,"阿斯卡姆：双重翻译，温和教书。",
 [H("第一书 青年的养育",[P("反对体罚；温和与爱"),P("“快才”与“慢才”的比较")]),H("第二书 学习拉丁文的捷径",[H("翻译"),H("意译"),H("韵文转写"),H("摘要"),H("模仿"),H("演说")])])
nb("reform","leader teacher","A","论教育","Of Education","弥尔顿 John Milton",1644,"1644年",
 "致哈特利布的书信体短论：教育要“修复我们始祖的堕落”，培养能担任一切公私职分的人。","✅ 名句般的目标与创造—堕落—救赎框架相合。⚠️ 课程过于庞大，偏重人文主义理想。","领袖、教师",3,"弥尔顿：教育修补始祖的废墟。",
 [P("教育目的：重新正确认识神，修复堕落"),P("从感官可见之物入手"),P("学院设想：12至21岁，学习、操练与饮食"),P("课程：语言、自然、伦理、政治、神学、修辞")])
nb("reform","teacher","E","语言入门","Janua linguarum reserata","夸美纽斯 Jan Amos Comenius",1631,"1631年",
 "约百章、千句拉丁—母语对照，按事物分类学语言。","✅ 词与物同学，语法期利器。⚠️ 非三项联合信条传统。","教师",2,"夸美纽斯：千句话打开语言之门。",
 [P("约一百章、约一千句"),P("按主题排列：自然、人体、手艺、家庭、国家、宗教"),P("拉丁与母语对照")])
nb("reform","leader","R","多特教会规章（第21条等）","Church Order of Dort","多特会议 Synod of Dort",1619,"1618–1619年",
 "长执会要设法使各处有好的学校教师，教孩子读写、语言、敬虔与要理问答。","✅ 欧陆改革宗学校传统的教会法依据。⚠️ 历史版本与今日各教会修订版条号不同。","学校领袖",2,"多特第21条：长执会要看顾好教师。",
 [P("第21条：长执会负责设立好的学校教师"),P("教师教读写、语言、敬虔与要理问答"),P("与会议第17场议决的三种教理问答（家、校、会）相呼应")])
nb("modern","leader teacher","R","加尔文主义讲座","Lectures on Calvinism (Stone Lectures)","凯波尔 Abraham Kuyper",1898,"1898年",
 "加尔文主义是一个完整的生命体系；第四讲论学术：普遍恩典使学术可能，重生造成两种学术。","✅ 改革宗世界观与教育的总纲。⚠️ “两种学术”需要与普遍恩典平衡。","领袖、教师",3,"凯波尔1898：两种人，两种学术。",
 [H("第一讲 加尔文主义：一个生命体系"),H("第二讲 加尔文主义与宗教"),H("第三讲 加尔文主义与政治"),H("第四讲 加尔文主义与学术",[P("普遍恩典使学术成为可能"),P("重生与未重生者的两种学术")]),H("第五讲 加尔文主义与艺术"),H("第六讲 加尔文主义与将来")],"full")
nb("modern","teacher","R","新教育","De nieuwe opvoeding","巴文克 Herman Bavinck",1917,"1917年",
 "评论当时的“新教育”运动与教育心理学，以改革宗原则回应。","✅ 示范如何批判地吸收新学科。⚠️ 尚无完整英译，内容多靠二手。","教师",5,"巴文克1917：审查“新教育”。",
 [P("教育理想与时代文化"),P("儿童研究与教育心理学"),P("改革宗的回应")])
nb("modern","teacher leader","R","基督教教育的基础","Foundations of Christian Education: Addresses to Christian Teachers","伯克富、范泰尔 Louis Berkhof & Cornelius Van Til",1990,"1990年（演讲合集，丹尼斯·约翰逊编）",
 "对基督教学校教师的演讲：没有中立，学校是圣约养育的延伸。","✅ 改革宗教育论的入门合集。⚠️ 演讲体，体系性不如专著。","教师、领袖",3,"伯克富与范泰尔：对老师说的话。",
 [P("伯克富：基督教教育的目标与圣约"),P("范泰尔：教育的对立性"),P("范泰尔：基督教教育是适合圣约儿女的唯一教育")])
nb("modern","teacher leader","R","基督教教育的基本原理","Fundamentals in Christian Education","雅尔斯玛（编） Cornelius Jaarsma (ed.)",1953,"1953年",
 "北美改革宗学校运动的论文集，含舒尔茨《神的人得以完全》等。","✅ 系统表达北美改革宗学校的目标。⚠️ 文集，水平不一。","教师、领袖",4,"雅尔斯玛1953：改革宗学校论文集。",
 [P("教育的目标：神的人得以完全（提后3:17）"),P("儿童观、课程观、学校与家庭教会的关系")])
nb("modern","teacher","R","巴文克的教育哲学","The Educational Philosophy of Herman Bavinck","雅尔斯玛 Cornelius Jaarsma",1935,"1935年",
 "英文世界介绍巴文克教育学的早期专著。","✅ 读不了荷兰文时的桥梁。⚠️ 二手诠释。","教师",4,"雅尔斯玛1935：巴文克教育学英文导读。",
 [P("巴文克的人观与神的形像"),P("教育目标、手段与学校")])
nb("modern","teacher leader","R","基督教教育哲学","A Christian Philosophy of Education","戈登·克拉克 Gordon H. Clark",1946,"1946年",
 "从神的启示出发建立知识论，批判杜威式实用主义教育。","✅ 有力批判世俗教育预设。⚠️ 克拉克的理性主义知识论与范泰尔有争论，需留意。","教师、领袖",4,"克拉克1946：从启示出发的知识论。",
 [P("世俗教育哲学批判（实用主义）"),P("有神论知识论"),P("课程与学科的统一")])
nb("modern","leader","R","美国教育的弥赛亚特性","The Messianic Character of American Education","鲁什杜尼 Rousas J. Rushdoony",1963,"1963年",
 "美国公共教育思想史：教育被当作拯救社会的“弥赛亚”。","✅ 揭示国家教育的宗教性。⚠️ 作者的神治主义（theonomy）主张不为多数改革宗教会接受。","学校领袖",4,"鲁什杜尼：学校被当成救主。",
 [P("贺拉斯·曼等人物的教育思想逐一评析"),P("国家教育的救赎主义"),P("基督教替代方案")])
nb("modern","teacher","R","异象之约","Testament of Vision","亨利·齐尔斯特拉 Henry Zylstra",1958,"1958年",
 "加尔文学院教授的文集：文学、文化与基督教博雅教育。","✅ 改革宗看待文学与文化的典范文字。⚠️ 文集，未系统论学校。","教师",3,"齐尔斯特拉：以异象读文学。",
 [P("基督徒与文化、文学"),P("博雅教育的目的")])
nb("modern","teacher leader","R","为负责任的行动而教育","Educating for Responsible Action","沃尔特斯托夫 Nicholas Wolterstorff",1980,"1980年",
 "基督教学校应培养负责任的行动倾向，而不只是理论知识。","✅ 把教育与生活实践连接。⚠️ 偏重社会行动，可能弱化教理传承。","教师、领袖",4,"沃尔特斯托夫1980：教出行动的倾向。",
 [P("教育目标：负责任的行动"),P("塑造倾向的方法：示范、管教、讲理")])
nb("modern","teacher leader","R","为平安而教育","Educating for Shalom: Essays on Christian Higher Education","沃尔特斯托夫 Nicholas Wolterstorff",2004,"2004年",
 "十九篇论文：以圣经“平安”（shalom）为基督教高等教育的目标。","✅ 改革宗哲学家的大学论。⚠️ 出版方自述其教学法“日益进步主义”，并强调社会正义，需与古典与信条传统对照。","教师、领袖",4,"沃尔特斯托夫2004：教育为平安。",
 [P("基督教高等教育的目的"),P("对古典基础主义、博雅教育等模式的批判"),P("学术自由与学术群体")])
nb("modern","teacher","R","与神同行在课堂","Walking with God in the Classroom","范布鲁门 Harro Van Brummelen",1992,"1992年（Welch 版；后有修订）",
 "基督徒教师的课堂实务：课程、教学、评量都在神的呼召下。","✅ 加拿大改革宗学校的实践手册。⚠️ 非古典路线。","教师",2,"范布鲁门：课堂也是同行之处。",
 [P("教学是呼召"),P("课程规划、教学方法、评量")])
nb("modern","leader parent","R","教育、基督教与国家","Education, Christianity and the State","梅钦 J. Gresham Machen",1987,"1987年（文集；文章作于1920–30年代）",
 "反对国家垄断教育，主张基督教学校的必要。","✅ 旧普林斯顿/威斯敏斯特传统的教育声音。⚠️ 美国处境色彩浓。","领袖、家长",2,"梅钦：基督教学校的必要性。",
 [P("基督教学校的必要性"),P("国家与教育的界限")])
nb("modern","teacher leader","R","基督教教育哲学阐释","The Christian Philosophy of Education Explained","派克斯 Stephen C. Perks",1992,"1992年",
 "从圣经出发的教育哲学：父母责任、国家界限、课程。","✅ 系统、圣经性强，参考书目丰富。⚠️ 立场接近重建主义，部分政治主张需分辨。","教师、领袖",4,"派克斯：从圣经重建教育哲学。",
 [P("教育的圣经基础与父母责任"),P("国家教育批判"),P("基督教课程")])
nb("movement","parent leader","E","重修荒场","Repairing the Ruins: The Classical and Christian Challenge to Modern Education","威尔逊（编） Douglas Wilson (ed.)",1996,"1996年",
 "古典基督教学校同工的文集：三艺的“为什么”与“怎么做”、课程规划、建校。","✅ 学校实务丰富。⚠️ 威尔逊圈子，见难点⑥。","家长、领袖",2,"重修荒场：建校实务。",
 [P("古典基督教教育的独特性"),P("三艺的理由与方法"),P("课程规划与心的教育"),P("建立学校")])
nb("movement","teacher leader","E","神的教化","The Paideia of God and Other Essays on Education","道格拉斯·威尔逊 Douglas Wilson",1999,"1999年",
 "弗6:4 的“教养”是整全文化塑造；基督徒要预备自己的文化。","✅ 把 paideia 读进圣约养育。⚠️ 后千禧年与文化愿景色彩；见难点⑥。","教师、领袖",3,"威尔逊1999：主的 paideia 是整全文化。",
 [P("神的教化（paideia）"),P("基督教文化的预备"),P("其他教育论文")])
nb("movement","parent","C","毁掉孩子想象力的十种方法","Ten Ways to Destroy the Imagination of Your Child","安东尼·埃索伦 Anthony Esolen",2010,"2010年",
 "反讽体：用“十种毁法”反证童年需要自由、户外、故事、英雄与超越。","✅ 文笔犀利，适合家长。⚠️ 天主教作者；文化批评多于教育学。","家长",2,"埃索伦：反着说的育儿书。",
 [H("引言：格伦德尔的坏日子"),H("真理是你的敌人"),H("把孩子关在室内"),H("永远别让孩子独处"),H("让孩子远离机器与匠人"),H("用政治口号取代童话"),H("诋毁英雄与爱国"),H("把英雄都削矮"),H("把爱降为自恋与性"),H("抹平男女之别"),H("用浅薄虚幻分散注意"),H("否认超越")],"full")
nb("movement","teacher leader","C","闲暇：文化的基础","Muße und Kult (Leisure, the Basis of Culture)","约瑟夫·皮珀 Josef Pieper",1948,"1948年",
 "闲暇不是偷懒，而是接受性的沉思；文化根于敬拜。","✅ 纠正“全勤功利”教育；安息日的维度（海德堡第38主日）。⚠️ 天主教圣礼与托马斯主义框架。","教师、领袖",3,"皮珀：闲暇是文化的根。",
 [H("闲暇：文化的基础",[P("“全面劳动”世界的批判"),P("闲暇即沉思与庆典"),P("敬拜是闲暇的根")]),H("哲学行动")])
nb("movement","teacher","C","智性生活","La vie intellectuelle","塞尔蒂扬日 A.-G. Sertillanges",1921,"1921年",
 "给学者的生活指南：时间、专注、阅读、笔记、德性。","✅ 学习习惯的实务宝库。⚠️ 道明会托马斯主义背景。","教师",3,"塞尔蒂扬日：学问是一种德性生活。",
 [P("智性呼召"),P("德性与学问"),P("时间安排与专注"),P("阅读、记忆、笔记、写作")])
nb("movement","parent teacher","P","如何阅读一本书","How to Read a Book","莫提默·艾德勒 Mortimer J. Adler",1940,"1940年（1972年与范多伦修订）",
 "阅读分四层：基础、检视、分析、主题阅读。","✅ 文法—逻辑—修辞式阅读的操作指南。⚠️ 非基督教著作（伟大书籍运动），价值中立的“伟大对话”需以圣经为准。","家长、教师",2,"艾德勒：四层阅读。",
 [H("第一篇 阅读的层次",[P("基础阅读、检视阅读")]),H("第二篇 分析阅读"),H("第三篇 阅读不同读物的方法"),H("第四篇 阅读的最终目标",[P("主题阅读")])])
nb("movement","leader","P","派代亚计划","The Paideia Proposal","莫提默·艾德勒 Mortimer J. Adler",1982,"1982年",
 "为所有孩子提供同一套博雅教育：讲授、辅导、苏格拉底式研讨三种教学。","✅ “三柱”教学法很实用。⚠️ 非基督教、民主公民教育框架。","学校领袖",2,"艾德勒1982：讲授、辅导、研讨三柱。",
 [P("一种轨道给所有学生"),P("三种教学：讲授、辅导训练、苏格拉底研讨"),P("教师与校长的角色")])
nb("movement","leader teacher","C","大学的理念","The Idea of a University","纽曼 John Henry Newman",1852,"1852年（九篇讲演；1873年合编）",
 "大学教授普遍知识，知识本身即目的；神学必须在大学中。","✅ 为博雅教育与神学的学术地位辩护。⚠️ 作者归入天主教，教会观不同。","领袖、教师",4,"纽曼：知识本身即目的，神学不可缺席。",
 [H("第一部分 大学教学（九篇讲演）",[H("一 引论"),H("二 神学是知识的一个分支"),H("三 神学对其他知识分支的影响"),H("四 其他知识分支对神学的影响"),H("五 知识本身即目的"),H("六 知识与学问"),H("七 知识与职业技能"),H("八 知识与宗教"),H("九 教会对知识的责任")]),
  H("第二部分 大学科目（讲演与论文）",[H("基督教与文学"),H("文学"),H("英国天主教文学"),H("基础学科"),H("当今一种不信的形式"),H("大学讲道"),H("基督教与自然科学"),H("基督教与科学研究"),H("心智的操练"),H("基督教与医学")])],"full")
nb("movement","teacher leader","A","现代教育与古典","Modern Education and the Classics","T.S.艾略特 T. S. Eliot",1932,"1932年（文章）",
 "教育问题根本是宗教问题；古典研究与基督教文明共存亡。","✅ 简短有力。⚠️ 圣公会高派立场。","教师、领袖",3,"艾略特：教育问题是宗教问题。",
 [P("教育的目的取决于人生观"),P("古典学问与基督教文明")])
nb("modern","parent","A","父母与孩子","Parents and Children","夏洛特·梅森 Charlotte Mason",1897,"1897年",
 "父母在教育中的角色、家庭氛围、习惯与观念。","✅ 家庭教育实用。⚠️ 梅森不是改革宗，人观偏乐观。","家长",2,"梅森：家庭是第一所学校。",
 [P("父母的职分"),P("观念与习惯"),P("家庭氛围")])
nb("modern","parent teacher","A","学校教育","School Education","夏洛特·梅森 Charlotte Mason",1904,"1904年",
 "九至十二岁儿童的课程：活的书、叙述、自然、艺术。","✅ 课程设计细节多。⚠️ 同上。","家长、教师",2,"梅森：活的书进课堂。",
 [P("课程原则"),P("各科教学"),P("叙述与好书")])

# 新增已核实中译本
ZH.update({
"忏悔录":("《忏悔录》","周士良 译","商务印书馆","1963",""),
"哲学的慰藉":("《哲学的慰藉》","荣震华 译（另有代国强、贺国坤、杨德友译本）","商务印书馆","2012",""),
"加尔文主义讲座":("《金石之言：从加尔文主义论宗教、政治、学术和艺术》","郭熙安 译","改革宗出版社","2018",""),
"闲暇：文化的基础":("《闲暇：文化的基础》","刘森尧 译","立绪文化（台湾）","2003",""),
"如何阅读一本书":("《如何阅读一本书》","郝明义、朱衣 译","商务印书馆","2004",""),
"大学的理念":("《大学的理念》","高师宁 等译","贵州教育出版社","2003",""),
"父母与孩子":("《父母与孩子》","赵昌荣 译","中国发展出版社","2013",""),
"学校教育":("《学校教育》","李庆华 译","中国发展出版社","2013",""),
})

def to_tree(zh):
    if zh in TREE: return TREE[zh]
    kind,items=TOC[zh]
    out=[]
    for it in items:
        if kind=="struct" and " " in it and it.index(" ")<=8:
            h,rest=it.split(" ",1); out.append((h,[("~"+x.strip(),[]) for x in rest.replace("：","；").split("；") if x.strip()]))
        elif "：" in it and it.index("：")<24:
            h,rest=it.split("：",1); ch=[x.strip() for x in rest.split("；") if x.strip()]
            out.append((h,[(c if kind=="full" else "~"+c,[]) for c in ch]))
        elif kind=="struct" and " " in it:
            h,rest=it.split(" ",1); out.append((h,[("~"+x.strip(),[]) for x in rest.split("；") if x.strip()]))
        else: out.append((it,[]))
    return out

def depth(nodes):
    return 0 if not nodes else 1+max(depth(c) for _,c in nodes)
def real_depth(nodes):
    return 0 if not nodes else max((0 if t.startswith("~") else 1+real_depth(c)) for t,c in nodes)
def count(nodes): return sum(1+count(c) for _,c in nodes)

def tree_html(nodes,pre="",lv=1):
    out=[]
    for i,(t,c) in enumerate(nodes,1):
        num=f"{pre}{i}"; pt=t.startswith("~"); txt=t[1:] if pt else t
        lab=f'<span class="tn-num">{num}</span><span class="tn-t">{txt}</span>'+('<span class="kp">要点概括</span>' if pt else '')
        cls=f"tn l{min(lv,4)}"+(" pt" if pt else "")
        if c: out.append(f'<li class="{cls}"><details{" open" if lv==1 and i==1 else ""}><summary>{lab}</summary><ul>{tree_html(c,num+".",lv+1)}</ul></details></li>')
        else: out.append(f'<li class="{cls}"><span class="tn-leaf">{lab}</span></li>')
    return "".join(out)

import re as _re
def kp_branch(b):
    ev=_re.sub(r"<[^>]+>","",b["ev"])
    parts=[x.strip(" 。") for x in _re.split(r"[✅⚠️]+",ev) if x.strip(" 。")]
    pros=[x for x in _re.split(r"；|。",parts[0]) if x.strip()] if parts else []
    cons=[x for x in _re.split(r"；|。",parts[1]) if x.strip()] if len(parts)>1 else []
    return ("~全书要点概括（本站整理）",[("~核心观点",[("~"+b["core"],[])]),("~可借鉴",[("~"+x,[]) for x in pros]),("~需分辨",[("~"+x,[]) for x in cons])])
def full_tree(b): return to_tree(b["zh"])+[kp_branch(b)]
def toc_html(b):
    tr=full_tree(b); kind=KIND.get(b["zh"], TOC.get(b["zh"],("struct",))[0])
    lab="完整章节目录" if kind=="full" else "结构目录"
    return f'''<details class="toc-panel" open><summary>📑 目录 <span class="toc-n">{count(tr)} 节点 · {depth(tr)} 层 · {lab}</span></summary>
<div class="tree-ctrl"><button type="button" class="tc-btn" data-tc="open">全部展开</button><button type="button" class="tc-btn" data-tc="close">全部收起</button></div>
<ul class="tree">{tree_html(tr)}</ul></details>'''

def book_cards():
    out=[]
    for b in sorted(B,key=lambda x:x["y"]):
        gname,gc=G[b["g"]]; t=TRAD.get(b["zh"],"E"); tn,tc=T[t]
        zz="yes" if b["zh"] in ZH else "no"
        s=(b["zh"]+" "+b["orig"]+" "+b["au"]).replace('"',"")
        out.append(f'''<article class="book" id="bk-{zlib.crc32(b["zh"].encode())%1000000}" data-g="{b["g"]}" data-a="{b["a"]}" data-zh="{zz}" data-t="{t}" data-s="{s}" style="--c:{gc}">
<div class="book-cover"><span class="book-grp">{gname}</span><span class="trad" style="--tc:{tc}">{tn}</span><span class="book-year">{b["ys"]}</span>{'<span class="zh-pill">中译</span>' if zz=="yes" else ''}</div>
<h4 class="book-title">《{b["zh"]}》</h4>
<p class="book-orig"><i>{b["orig"]}</i></p>
<p class="book-au">✍️ {b["au"]} · <span class="stars" aria-label="难度{b["st"]}星">{stars(b["st"])}</span></p>
{zh_badge(b)}
<p class="book-core">💎 {b["core"]}</p>
{toc_html(b)}
<details class="book-more"><summary>⚖️ 改革宗评价 · 👥 推荐</summary>
<p><b>改革宗评价：</b>{b["ev"]}</p>
<p><b>推荐：</b>{b["who"]}</p>
</details>
<p class="mem small">🧠 {b["mem"]}</p>
</article>''')
    return "".join(out)

def book_table():
    rows="".join(f'<tr><td data-v="{b["y"]}">{b["ys"]}</td><td>{b["au"]}</td><td>《{b["zh"]}》<br><small>{b["orig"]}</small></td><td>{G[b["g"]][0]}</td><td>{T[TRAD.get(b["zh"],"E")][0]}</td><td>{"✅" if b["zh"] in ZH else "—"}</td><td>{real_depth(to_tree(b["zh"]))}+{depth(full_tree(b))-real_depth(to_tree(b["zh"]))}</td></tr>' for b in sorted(B,key=lambda x:x["y"]))
    return f'<div class="table-wrap"><table class="sortable" id="book-table"><thead><tr><th>年份 ⇅</th><th>作者 ⇅</th><th>书名 ⇅</th><th>组别 ⇅</th><th>传统 ⇅</th><th>中译 ⇅</th><th>标题层/要点层 ⇅</th></tr></thead><tbody>{rows}</tbody></table></div>'

def trad_chart():
    rows=""
    mx=max(sum(1 for b in B if TRAD.get(b["zh"],"E")==k) for k in T)
    for k,(n,c) in T.items():
        v=sum(1 for b in B if TRAD.get(b["zh"],"E")==k)
        rows+=f'<div class="sc-row"><span class="sc-l">{n}</span><div class="sc-bar"><span class="sc-y" style="--w:{v*100/mx:.0f}%;--c:{c}">{v}</span></div><span class="sc-t">{v}</span></div>'
    return f'<div class="chart-card"><h4>⛪ 传统分布</h4>{rows}<p class="viz-note">按作者所属传统；“古典·非基督教”含艾德勒等。</p></div>'

_old_charts=charts
def charts():
    yes=sum(1 for b in B if b["zh"] in ZH); n=len(B); pct=round(yes*100/n)
    rows=""
    for k,(name,c) in G.items():
        bs=[b for b in B if b["g"]==k]; y=sum(1 for b in bs if b["zh"] in ZH)
        rows+=f'<div class="sc-row"><span class="sc-l">{name}</span><div class="sc-bar"><span class="sc-y" style="--w:{y*100/max(1,len(bs)):.0f}%;--c:{c}">{y}</span><span class="sc-n" style="--w:{(len(bs)-y)*100/max(1,len(bs)):.0f}%">{len(bs)-y}</span></div><span class="sc-t">{len(bs)}</span></div>'
    return f'''<div class="chart-grid">
<div class="chart-card"><h4>🀄 中译状态</h4><div class="donut" style="--p:{pct}"><div><b>{yes}</b><span>/ {n} 本已有中译</span></div></div></div>
<div class="chart-card"><h4>📚 组别 × 中译</h4>{rows}</div>
{trad_chart()}</div>'''

CMAP += [("巴西流 / 耶柔米","#a8dfc4",["蜜蜂采花","圣经为课本"]),("卡佩拉 / 依西多禄","#b39ddb",["七艺地图","百科全书"]),("阿奎那 / 波纳文图拉","#b39ddb",["教师如医生","诸艺归于神学"]),
("阿斯卡姆 / 弥尔顿","#6ba3e0",["双重翻译","修复始祖的堕落"]),("纽曼 / 皮珀","#b39ddb",["知识本身即目的","闲暇是文化的根"]),("克拉克 / 鲁什杜尼 / 沃尔特斯托夫","#d4af37",["启示的知识论","教育不是救主","为平安而教育"]),("艾德勒","#e8a85c",["四层阅读","三柱教学"])]

N=len(B); NZH=sum(1 for b in B if b["zh"] in ZH)
NV=sum(1 for b in B if KIND.get(b["zh"],TOC.get(b["zh"],("struct",))[0])=="full")
REAL3=[b["zh"] for b in B if real_depth(to_tree(b["zh"]))>=3]
REAL2=[b["zh"] for b in B if real_depth(to_tree(b["zh"]))==2]
DEEP3=[b["zh"] for b in B if depth(to_tree(b["zh"]))>=3]

DEEP3=[b["zh"] for b in B if depth(full_tree(b))>=3]
exec(open('library_v6.py',encoding='utf-8').read())
