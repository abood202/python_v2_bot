from info import *
# from filters_links import words_containing_char
import time

#*التحقق من الرابط
#*استخراج الروابط من الرسالة في قائمة
#*التعامل مع الروابط

#?التحقق من الرابط
def link_ceack(message,chat_id,list_fowrword):
    """
    بعد التحقق من الروابط ومعرفة هل النتيجة True or False\n
    اذا False معناه ان الرابط مش من قائمة الروابط\n
    اذا True معناه ان الروابط مظبوطة او مفيش رابط\n
    هيتحقق هنا اذا الرابط فيه @ ولا لأ\n
    واذا اسم مستخدم ولا اسم قناةوهيرجع النتيجة
    """
    text_message = message.text
    message_id = message.id
    user_id = message.from_user.id

    found_message = True

    litter = ["1","2","3","4","5","6","7","8","9","0",
              "a","b","c","d","e","f","g","h","i","j",
              "k","l","m","n","o","p","q","r","s","t",
              "u","v","w","x","y","z","A","B","C","D",
              "E","F","G","H","I","J","K","L","M","N",
              "O","P","Q","R","S","T","U","V","W","X",
              "Y","Z","_"]

    words_with_aat = []
    word_wit_at =''
    filter_username = []

    if text_message:
        text_message = text_message
    elif message.document:
        text_message = message.caption

    if "@" in text_message:

        #?هيستخرج الكلمات اللي فيها @
        word_with_Aat = words_containing_char(text_message,"@")

        for word in word_with_Aat:
            if "@" in word:
                new_word = word.split("@")
                for i in new_word:
                    if i == "":
                        pass
                    elif i not in words_with_aat:
                        words_with_aat.append(i)
   
        for i in words_with_aat:
            for x in i:
                if x in litter:
                    word_wit_at += x
                else:
                    filter_username.append(word_wit_at)
                    word_wit_at = ""
                    break
            if word_wit_at not in filter_username:
                filter_username.append(word_wit_at)
                word_wit_at = ""
            word_wit_at = ""

        for i in filter_username:
            if i == "":
                pass
            else:
                try:
                    info_username = bot.get_chat(f"@{i}")
                    id_group = info_username.id
                    type_group =  info_username.type
                    title_group =  info_username.title
                    username_group = info_username.username
                    if (username_group in list_fowrword) or (str(id_group) in list_fowrword):
                        pass
                    else:
                        Admins = [1814696703,5176738408]
                        for x in Admins:
                            bot.send_message(x,f"تم ارسال اسم المستخدم هذا داخل المجموعة \nهذا اسم مستخدم لقناة @{i}\nالاسم : {title_group}\nالايدي : {id_group}\nالنوع : {type_group}\nاسم المستخدم : @{username_group}")
                        found_message = False
                        return found_message
                    
                except:
                    pass

    return found_message

#? استخراج الكلمات التي تحتوي على الحرف المعين
def words_containing_char(sentence, char):
    # استخراج الكلمات التي تحتوي على الحرف المعين
    return [word for word in sentence.split() if char in word]

#?بيتفحص الروابط
#?استخراج الروابط من الرسالة
def check_in_links(text,links_list,chat_id,message_id):
    message_found = True 

    #?قائمة بامتدادات النطاقات
    domins = [".com",".uk",".فلسطين",".aaa",
".aarp",
".abarth",
".abb",
".abbott",
".abbvie",
".abc",
".able",
".abogado",
".abudhabi",
".ac",
".academy",
".accenture",
".accountant",
".accountants",
".aco",
".active",
".actor",
".ad",
".adac",
".ads",
".adult",
".ae",
".aeg",
".aero",
".aetna",
".af",
".afamilycompany",
".afl",
".africa",
".ag",
".agakhan",
".agency",
".ai",
".aig",
".aigo",
".airbus",
".airforce",
".airtel",
".akdn",
".al",
".alfaromeo",
".alibaba",
".alipay",
".allfinanz",
".allstate",
".ally",
".alsace",
".alstom",
".am",
".amazon",
".americanexpress",
".americanfamily",
".amex",
".amfam",
".amica",
".amsterdam",
".an",
".analytics",
".android",
".anquan",
".anz",
".ao",
".aol",
".apartments",
".app",
".apple",
".aq",
".aquarelle",
".ar",
".arab",
".aramco",
".archi",
".army",
".arpa",
".art",
".arte",
".as",
".asda",
".asia",
".associates",
".at",
".athleta",
".attorney",
".au",
".auction",
".audi",
".audible",
".audio",
".auspost",
".author",
".auto",
".autos",
".avianca",
".aw",
".aws",
".ax",
".axa",
".az",
".azure",
".ba",
".baby",
".baidu",
".banamex",
".bananarepublic",
".band",
".bank",
".bar",
".barcelona",
".barclaycard",
".barclays",
".barefoot",
".bargains",
".baseball",
".basketball",
".bauhaus",
".bayern",
".bb",
".bbc",
".bbt",
".bbva",
".bcg",
".bcn",
".bd",
".be",
".beats",
".beauty",
".beer",
".bentley",
".berlin",
".best",
".bestbuy",
".bet",
".bf",
".bg",
".bh",
".bharti",
".bi",
".bible",
".bid",
".bike",
".bing",
".bingo",
".bio",
".biz",
".bj",
".bl",
".black",
".blackfriday",
".blanco",
".blockbuster",
".blog",
".bloomberg",
".blue",
".bm",
".bms",
".bmw",
".bn",
".bnl",
".bnpparibas",
".bo",
".boats",
".boehringer",
".bofa",
".bom",
".bond",
".boo",
".book",
".booking",
".boots",
".bosch",
".bostik",
".boston",
".bot",
".boutique",
".box",
".bq",
".br",
".bradesco",
".bridgestone",
".broadway",
".broker",
".brother",
".brussels",
".bs",
".bt",
".budapest",
".bugatti",
".build",
".builders",
".business",
".buy",
".buzz",
".bv",
".bw",
".by",
".bz",
".bzh",
".ca",
".cab",
".cafe",
".cal",
".call",
".calvinklein",
".cam",
".camera",
".camp",
".cancerresearch",
".canon",
".capetown",
".capital",
".capitalone",
".car",
".caravan",
".cards",
".care",
".career",
".careers",
".cars",
".cartier",
".casa",
".case",
".caseih",
".cash",
".casino",
".cat",
".catering",
".catholic",
".cba",
".cbn",
".cbre",
".cbs",
".cc",
".cd",
".ceb",
".center",
".ceo",
".cern",
".cf",
".cfa",
".cfd",
".cg",
".ch",
".chanel",
".channel",
".charity",
".chase",
".chat",
".cheap",
".chintai",
".chloe",
".christmas",
".chrome",
".chrysler",
".church",
".ci",
".cipriani",
".circle",
".cisco",
".citadel",
".citi",
".citic",
".city",
".cityeats",
".ck",
".cl",
".claims",
".cleaning",
".click",
".clinic",
".clinique",
".clothing",
".cloud",
".club",
".clubmed",
".cm",
".cn",
".co",
".coach",
".codes",
".coffee",
".college",
".cologne",
".comcast",
".commbank",
".community",
".company",
".compare",
".computer",
".comsec",
".condos",
".construction",
".consulting",
".contact",
".contractors",
".cooking",
".cookingchannel",
".cool",
".coop",
".corsica",
".country",
".coupon",
".coupons",
".courses",
".cpa",
".cr",
".credit",
".creditcard",
".creditunion",
".cricket",
".crown",
".crs",
".cruise",
".cruises",
".csc",
".cu",
".cuisinella",
".cv",
".cw",
".cx",
".cy",
".cymru",
".cyou",
".cz",
".dabur",
".dad",
".dance",
".data",
".date",
".dating",
".datsun",
".day",
".dclk",
".dds",
".de",
".deal",
".dealer",
".deals",
".degree",
".delivery",
".dell",
".deloitte",
".delta",
".democrat",
".dental",
".dentist",
".desi",
".design",
".dev",
".dhl",
".diamonds",
".diet",
".digital",
".direct",
".directory",
".discount",
".discover",
".dish",
".diy",
".dj",
".dk",
".dm",
".dnp",
".do",
".docs",
".doctor",
".dodge",
".dog",
".doha",
".domains",
".doosan",
".dot",
".download",
".drive",
".dtv",
".dubai",
".duck",
".dunlop",
".duns",
".dupont",
".durban",
".dvag",
".dvr",
".dz",
".earth",
".eat",
".ec",
".eco",
".edeka",
".edu",
".education",
".ee",
".eg",
".eh",
".email",
".emerck",
".energy",
".engineer",
".engineering",
".enterprises",
".epost",
".epson",
".equipment",
".er",
".ericsson",
".erni",
".es",
".esq",
".estate",
".esurance",
".et",
".etisalat",
".eu",
".eurovision",
".eus",
".events",
".everbank",
".exchange",
".expert",
".exposed",
".express",
".extraspace",
".fage",
".fail",
".fairwinds",
".faith",
".family",
".fan",
".fans",
".farm",
".farmers",
".fashion",
".fast",
".fedex",
".feedback",
".ferrari",
".ferrero",
".fi",
".fiat",
".fidelity",
".fido",
".film",
".final",
".finance",
".financial",
".fire",
".firestone",
".firmdale",
".fish",
".fishing",
".fit",
".fitness",
".fj",
".fk",
".flickr",
".flights",
".flir",
".florist",
".flowers",
".flsmidth",
".fly",
".fm",
".fo",
".foo",
".food",
".foodnetwork",
".football",
".ford",
".forex",
".forsale",
".forum",
".foundation",
".fox",
".fr",
".free",
".fresenius",
".frl",
".frogans",
".frontdoor",
".frontier",
".ftr",
".fujitsu",
".fujixerox",
".fun",
".fund",
".furniture",
".futbol",
".fyi",
".ga",
".gal",
".gallery",
".gallo",
".gallup",
".game",
".games",
".gap",
".garden",
".gay",
".gb",
".gbiz",
".gd",
".gdn",
".ge",
".gea",
".gent",
".genting",
".george",
".gf",
".gg",
".ggee",
".gh",
".gi",
".gift",
".gifts",
".gives",
".giving",
".gl",
".glade",
".glass",
".gle",
".global",
".globo",
".gm",
".gmail",
".gmbh",
".gmo",
".gmx",
".gn",
".godaddy",
".gold",
".goldpoint",
".golf",
".goo",
".goodhands",
".goodyear",
".goog",
".google",
".gop",
".got",
".gov",
".gp",
".gq",
".gr",
".grainger",
".graphics",
".gratis",
".green",
".gripe",
".grocery",
".group",
".gs",
".gt",
".gu",
".guardian",
".gucci",
".guge",
".guide",
".guitars",
".guru",
".gw",
".gy",
".hair",
".hamburg",
".hangout",
".haus",
".hbo",
".hdfc",
".hdfcbank",
".health",
".healthcare",
".help",
".helsinki",
".here",
".hermes",
".hgtv",
".hiphop",
".hisamitsu",
".hitachi",
".hiv",
".hk",
".hkt",
".hm",
".hn",
".hockey",
".holdings",
".holiday",
".homedepot",
".homegoods",
".homes",
".homesense",
".honda",
".honeywell",
".horse",
".hospital",
".host",
".hosting",
".hot",
".hoteles",
".hotels",
".hotmail",
".house",
".how",
".hr",
".hsbc",
".ht",
".htc",
".hu",
".hughes",
".hyatt",
".hyundai",
".ibm",
".icbc",
".ice",
".icu",
".id",
".ie",
".ieee",
".ifm",
".iinet",
".ikano",
".il",
".im",
".imamat",
".imdb",
".immo",
".immobilien",
".in",
".inc",
".industries",
".infiniti",
".info",
".ing",
".ink",
".institute",
".insurance",
".insure",
".int",
".intel",
".international",
".intuit",
".investments",
".io",
".ipiranga",
".iq",
".ir",
".irish",
".is",
".iselect",
".ismaili",
".ist",
".istanbul",
".it",
".itau",
".itv",
".iveco",
".iwc",
".jaguar",
".java",
".jcb",
".jcp",
".je",
".jeep",
".jetzt",
".jewelry",
".jio",
".jlc",
".jll",
".jm",
".jmp",
".jnj",
".jo",
".jobs",
".joburg",
".jot",
".joy",
".jp",
".jpmorgan",
".jprs",
".juegos",
".juniper",
".kaufen",
".kddi",
".ke",
".kerryhotels",
".kerrylogistics",
".kerryproperties",
".kfh",
".kg",
".kh",
".ki",
".kia",
".kids",
".kim",
".kinder",
".kindle",
".kitchen",
".kiwi",
".km",
".kn",
".koeln",
".komatsu",
".kosher",
".kp",
".kpmg",
".kpn",
".kr",
".krd",
".kred",
".kuokgroup",
".kw",
".ky",
".kyoto",
".kz",
".la",
".lacaixa",
".ladbrokes",
".lamborghini",
".lamer",
".lancaster",
".lancia",
".lancome",
".land",
".landrover",
".lanxess",
".lasalle",
".lat",
".latino",
".latrobe",
".law",
".lawyer",
".lb",
".lc",
".lds",
".lease",
".leclerc",
".lefrak",
".legal",
".lego",
".lexus",
".lgbt",
".li",
".liaison",
".lidl",
".life",
".lifeinsurance",
".lifestyle",
".lighting",
".like",
".lilly",
".limited",
".limo",
".lincoln",
".linde",
".link",
".lipsy",
".live",
".living",
".lixil",
".lk",
".llc",
".llp",
".loan",
".loans",
".locker",
".locus",
".loft",
".lol",
".london",
".lotte",
".lotto",
".love",
".lpl",
".lplfinancial",
".lr",
".ls",
".lt",
".ltd",
".ltda",
".lu",
".lundbeck",
".lupin",
".luxe",
".luxury",
".lv",
".ly",
".ma",
".macys",
".madrid",
".maif",
".maison",
".makeup",
".man",
".management",
".mango",
".map",
".market",
".marketing",
".markets",
".marriott",
".marshalls",
".maserati",
".mattel",
".mba",
".mc",
".mcd",
".mcdonalds",
".mckinsey",
".md",
".me",
".med",
".media",
".meet",
".melbourne",
".meme",
".memorial",
".men",
".menu",
".meo",
".merckmsd",
".metlife",
".mf",
".mg",
".mh",
".miami",
".microsoft",
".mil",
".mini",
".mint",
".mit",
".mitsubishi",
".mk",
".ml",
".mlb",
".mls",
".mm",
".mma",
".mn",
".mo",
".mobi",
".mobile",
".mobily",
".moda",
".moe",
".moi",
".mom",
".monash",
".money",
".monster",
".montblanc",
".mopar",
".mormon",
".mortgage",
".moscow",
".moto",
".motorcycles",
".mov",
".movie",
".movistar",
".mp",
".mq",
".mr",
".ms",
".msd",
".mt",
".mtn",
".mtpc",
".mtr",
".mu",
".museum",
".music",
".mutual",
".mutuelle",
".mv",
".mw",
".mx",
".my",
".mz",
".na",
".nab",
".nadex",
".nagoya",
".name",
".nationwide",
".natura",
".navy",
".nba",
".nc",
".ne",
".nec",
".net",
".netbank",
".netflix",
".network",
".neustar",
".new",
".newholland",
".news",
".next",
".nextdirect",
".nexus",
".nf",
".nfl",
".ng",
".ngo",
".nhk",
".ni",
".nico",
".nike",
".nikon",
".ninja",
".nissan",
".nissay",
".nl",
".no",
".nokia",
".northwesternmutual",
".norton",
".now",
".nowruz",
".nowtv",
".np",
".nr",
".nra",
".nrw",
".ntt",
".nu",
".nyc",
".nz",
".obi",
".observer",
".off",
".office",
".okinawa",
".olayan",
".olayangroup",
".oldnavy",
".ollo",
".om",
".omega",
".one",
".ong",
".onl",
".online",
".onyourside",
".ooo",
".open",
".oracle",
".orange",
".org",
".organic",
".orientexpress",
".origins",
".osaka",
".otsuka",
".ott",
".ovh",
".pa",
".page",
".pamperedchef",
".panasonic",
".panerai",
".paris",
".pars",
".partners",
".parts",
".party",
".passagens",
".pay",
".pccw",
".pe",
".pet",
".pf",
".pfizer",
".pg",
".ph",
".pharmacy",
".phd",
".philips",
".phone",
".photo",
".photography",
".photos",
".physio",
".piaget",
".pics",
".pictet",
".pictures",
".pid",
".pin",
".ping",
".pink",
".pioneer",
".pizza",
".pk",
".pl",
".place",
".play",
".playstation",
".plumbing",
".plus",
".pm",
".pn",
".pnc",
".pohl",
".poker",
".politie",
".porn",
".post",
".pr",
".pramerica",
".praxi",
".press",
".prime",
".pro",
".prod",
".productions",
".prof",
".progressive",
".promo",
".properties",
".property",
".protection",
".pru",
".prudential",
".ps",
".pt",
".pub",
".pw",
".pwc",
".py",
".qa",
".qpon",
".quebec",
".quest",
".qvc",
".racing",
".radio",
".raid",
".re",
".read",
".realestate",
".realtor",
".realty",
".recipes",
".red",
".redstone",
".redumbrella",
".rehab",
".reise",
".reisen",
".reit",
".reliance",
".ren",
".rent",
".rentals",
".repair",
".report",
".republican",
".rest",
".restaurant",
".review",
".reviews",
".rexroth",
".rich",
".richardli",
".ricoh",
".rightathome",
".ril",
".rio",
".rip",
".rmit",
".ro",
".rocher",
".rocks",
".rodeo",
".rogers",
".room",
".rs",
".rsvp",
".ru",
".rugby",
".ruhr",
".run",
".rw",
".rwe",
".ryukyu",
".sa",
".saarland",
".safe",
".safety",
".sakura",
".sale",
".salon",
".samsclub",
".samsung",
".sandvik",
".sandvikcoromant",
".sanofi",
".sap",
".sapo",
".sarl",
".sas",
".save",
".saxo",
".sb",
".sbi",
".sbs",
".sc",
".sca",
".scb",
".schaeffler",
".schmidt",
".scholarships",
".school",
".schule",
".schwarz",
".science",
".scjohnson",
".scor",
".scot",
".sd",
".se",
".search",
".seat",
".secure",
".security",
".seek",
".select",
".sener",
".services",
".ses",
".seven",
".sew",
".sex",
".sexy",
".sfr",
".sg",
".sh",
".shangrila",
".sharp",
".shaw",
".shell",
".shia",
".shiksha",
".shoes",
".shop",
".shopping",
".shouji",
".show",
".showtime",
".shriram",
".si",
".silk",
".sina",
".singles",
".site",
".sj",
".sk",
".ski",
".skin",
".sky",
".skype",
".sl",
".sling",
".sm",
".smart",
".smile",
".sn",
".sncf",
".so",
".soccer",
".social",
".softbank",
".software",
".sohu",
".solar",
".solutions",
".song",
".sony",
".soy",
".spa",
".space",
".spiegel",
".sport",
".spot",
".spreadbetting",
".sr",
".srl",
".srt",
".ss",
".st",
".stada",
".staples",
".star",
".starhub",
".statebank",
".statefarm",
".statoil",
".stc",
".stcgroup",
".stockholm",
".storage",
".store",
".stream",
".studio",
".study",
".style",
".su",
".sucks",
".supplies",
".supply",
".support",
".surf",
".surgery",
".suzuki",
".sv",
".swatch",
".swiftcover",
".swiss",
".sx",
".sy",
".sydney",
".symantec",
".systems",
".sz",
".tab",
".taipei",
".talk",
".taobao",
".target",
".tatamotors",
".tatar",
".tattoo",
".tax",
".taxi",
".tc",
".tci",
".td",
".tdk",
".team",
".tech",
".technology",
".tel",
".telecity",
".telefonica",
".temasek",
".tennis",
".teva",
".tf",
".tg",
".th",
".thd",
".theater",
".theatre",
".tiaa",
".tickets",
".tienda",
".tiffany",
".tips",
".tires",
".tirol",
".tj",
".tjmaxx",
".tjx",
".tk",
".tkmaxx",
".tl",
".tm",
".tmall",
".tn",
".to",
".today",
".tokyo",
".tools",
".top",
".TOP",
".toray",
".toshiba",
".total",
".tours",
".town",
".toyota",
".toys",
".tp",
".tr",
".trade",
".trading",
".training",
".travel",
".travelchannel",
".travelers",
".travelersinsurance",
".trust",
".trv",
".tt",
".tube",
".tui",
".tunes",
".tushu",
".tv",
".tvs",
".tw",
".tz",
".ua",
".ubank",
".ubs",
".uconnect",
".ug",
".um",
".unicom",
".university",
".uno",
".uol",
".ups",
".us",
".uy",
".uz",
".va",
".vacations",
".vana",
".vanguard",
".vc",
".ve",
".vegas",
".ventures",
".verisign",
".versicherung",
".vet",
".vg",
".vi",
".viajes",
".video",
".vig",
".viking",
".villas",
".vin",
".vip",
".virgin",
".visa",
".vision",
".vista",
".vistaprint",
".viva",
".vivo",
".vlaanderen",
".vn",
".vodka",
".volkswagen",
".volvo",
".vote",
".voting",
".voto",
".voyage",
".vu",
".vuelos",
".wales",
".walmart",
".walter",
".wang",
".wanggou",
".warman",
".watch",
".watches",
".weather",
".weatherchannel",
".webcam",
".weber",
".website",
".wed",
".wedding",
".weibo",
".weir",
".wf",
".whoswho",
".wien",
".wiki",
".williamhill",
".win",
".windows",
".wine",
".winners",
".wme",
".wolterskluwer",
".woodside",
".work",
".works",
".world",
".wow",
".ws",
".wtc",
".wtf",
".xbox",
".xerox",
".xfinity",
".xihuan",
".xin",
".测试",
".कॉम",
".परीक्षा",
".セール",
".佛山",
".ಭಾರತ",
".慈善",
".集团",
".在线",
".한국",
".ଭାରତ",
".大众汽车",
".点看",
".คอม",
".ভাৰত",
".ভারত",
".八卦",
".বাংলা",
".公益",
".公司",
".香格里拉",
".网站",
".移动",
".我爱你",
".москва",
".испытание",
".қаз",
".католик",
".онлайн",
".сайт",
".联通",
".срб",
".бг",
".бел",
".时尚",
".微博",
".테스트",
".淡马锡",
".ファッション",
".орг",
".नेट",
".ストア",
".アマゾン",
".삼성",
".சிங்கப்பூர்",
".商标",
".商店",
".商城",
".дети",
".мкд",
".ею",
".ポイント",
".新闻",
".工行",
".家電",
".中文网",
".中信",
".中国",
".中國",
".娱乐",
".谷歌",
".భారత్",
".ලංකා",
".電訊盈科",
".购物",
".測試",
".クラウド",
".ભારત",
".通販",
".भारतम्",
".भारत",
".भारोत",
".பரிட்சை",
".网店",
".संगठन",
".餐厅",
".网络",
".ком",
".укр",
".香港",
".亚马逊",
".诺基亚",
".食品",
".δοκιμή",
".飞利浦",
".台湾",
".台灣",
".手表",
".手机",
".мон",
".澳門",
".닷컴",
".政府",
".გე",
".机构",
".组织机构",
".健康",
".ไทย",
".招聘",
".рус",
".рф",
".珠宝",
".大拿",
".ລາວ",
".みんな",
".グーグル",
".ευ",
".ελ",
".世界",
".書籍",
".ഭാരതം",
".ਭਾਰਤ",
".网址",
".닷넷",
".コム",
".天主教",
".游戏",
".vermögensberater",
".vermögensberatung",
".企业",
".信息",
".嘉里大酒店",
".嘉里",
".广东",
".இலங்கை",
".இந்தியா",
".հայ",
".新加坡",
".テスト",
".政务",
".xperia",
".xxx",
".xyz",
".yachts",
".yahoo",
".yamaxun",
".yandex",
".ye",
".yodobashi",
".yoga",
".yokohama",
".you",
".youtube",
".yt",
".yun",
".za",
".zappos",
".zara",
".zero",
".zip",
".zippo",
".zm",
".zone",
".zuerich",
".zw",
".INT",
".ARPA"]

    #?هيستخرج الروابط اللي فيها http او https
    # url_list = re.findall("(?P<url>https?://[^\s]+)", text)

    #?اذا قام باستخراج روابط
    # if (url_list != []) and (links_list !=[]):
    #     for url in url_list:
    #         for link in links_list:
    #             if link[-1]=="/":
    #                 text_url = link

    #             else:
    #                 text_url = link + "/"

    #             if text_url in url:
    #                 id_message = (url.split("/"))[-1]
    #                 # if id_message.isdigit():                        
    #                 message_found = True
    #                 break

    #             elif url in links_list:
    #                 message_found = True
    #                 break 

    #             else:
    #                 message_found = False
    #                 # return message_found
    
    # elif (url_list != []) and (links_list ==[]):
    #     message_found = False
    #     return message_found
    

    #?الجمل اللتي تحتوي علي هذا الدومين
    #?اذا بعت رابط مع كلام : هيستخرج الرابط
    sentences = []
    #?قائمة الدومينات المستخرجة
    list_domain = []
    #?هنا يحدد\يستخرج الدومينات الموجودة جوا الرابط
    for dom in domins:
        if dom in text:
            list_domain.append(dom)

    if (list_domain != []) and (links_list != []):
        for dom in list_domain:
            sentences += words_containing_char(text, dom)
        # for sentence in sentences:
        #     print(sentence)
        #     print(sentences)
        #     print("###########")
        #     for link in links_list:
        #         # print(sentence,"\n",link)
        #         if link[-1]=="/":
        #             tte = link
        #         else:
        #             tte = link + "/"
        #         if tte in sentence:
        #             print("tte in sentence")
        #             id_message = (sentence.split("/"))[-1]
        #             message_found = True
        #             break

        #         elif sentence in links_list:
        #             print("sentence in links_list")

        #             message_found = True
        #             break
        #         else:
        #             message_found = False
        #             print(sentence,"\n",link)
        #             print("GGGGGGGG",message_found)
                    
        #             return message_found
        
        for sentence in sentences:
            # print(sentence)
            # print(sentences)
            # print("################")
            if "/" in sentence:
                end_ = sentence.split("/")[-1]
                if end_.isdigit():
                    stsrt_ = sentence.split("/")[:-1]
                    stsrt_ = ("/").join(stsrt_)
                else:
                    stsrt_ = sentence

                # print("stsrt_ : ",stsrt_)
                if stsrt_ in links_list:
                    message_found = True
                    # break
                else:
                    message_found = False
                    # print("1111111",message_found)
                    return message_found

            else:
                if sentence in links_list:
                    message_found = True
                else:
                    message_found = False
                    return message_found

            # for link in links_list:
            #     if link in sentence:
            #         message_found = True
            #         break

            #     elif sentence in links_list:
            #         print("sentence in links_list")
            #         message_found = True                    
            #         break

            #     else:
            #         message_found = False
            #         print(sentence,"\n",link)
            #         print("GGGGGGGG",message_found)
                    
            #         return message_found
        
        return message_found
    
    if (list_domain == []) and (links_list != []):
        return message_found
    if (list_domain != []) and (links_list == []):
        message_found = False
        return message_found

    else:
        return message_found
    

#?تحذير الاعضاء
def wrong_member(safeCounter,chat_id,user_id,data,full_name):
    safeCounter += 1
    new_data={
        "safeCounter":safeCounter
    }
    data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"].update(new_data)
    with open('backend/Chat_Data.json', 'w') as f:
        json.dump(data, f)

    worning = f"[{full_name}](tg://user?id={user_id})"
    mesg_worning =f"""
{worning}
ممنوع ارسال الروابط 

الإنذار رقم: {safeCounter}
العقوبة: تقييد لمدة: {safeCounter} ساعة
"""

    time_mute = int(time.time()) + safeCounter * 60 * 60
    bot.restrict_chat_member(chat_id,user_id,time_mute)
    bot.send_message(chat_id=chat_id,text=mesg_worning,parse_mode="markdown")

    return data

#?التحقق من خيارات الروابط مثل اذا كانت الروابط والتحذير والروابط المحددة مفتوحة \ مغلقة
def option_group(chat_title,link_Chat,
                 chat_id,chat_username,
                 chat_members_count,full_name,
                 user_id,username,user_stat,text,
                 Admin_list,OK_Link,some_link,warning,
                 links_list,Moderators_list,message,
                 list_fowrword,data,safeCounter
                 ):

    found_message = True
    message_id = message.id

    messagee_link =f"""
المجموعة اللتي تم ارسال الرابط فيها :

الاسم : [{chat_title}]({link_Chat})
أيدي المجموعة: {chat_id}
اسم المستخدم للمجموعة: @{chat_username}
رابط المجموعة : [انقر هنا للانتقال]({link_Chat})
عدد الاعضاء: {chat_members_count}
--------------------------------------------------

مرسل الرابط:

الاسم : [{full_name}](tg://user?id={user_id})
الايدي: {user_id}
اسم المستخدم : @{username}
حالة العضو: {user_stat}
--------------------------------------------------

رابط تم ارسالة: 

{text}
"""

    message_wrong_user = f"([{full_name}](tg://user?id={user_id}))\n ممنوع ارسال الروابط"

    link_type_message = ""
    if ("entities" in message.json) or ("caption_entities" in message.json) :
        if message.text:
            # print("hhhhh")
            link_type_message = message.json["entities"][0]["type"]#للرسائل النصية        
        elif message.document:
            # print("nnnnnn")
            link_type_message = message.json["caption_entities"][0]["type"]#للرسائل النصية

    #?يبعت رسالة للمشرفين في الخاص
    if text == "@admin":
        addmi = Admin_list + Moderators_list
        for i in addmi:
            state_admin = bot.get_chat_member(chat_id,i)
            if state_admin.user.is_bot:
                pass
            else:
                # f"[{"full_name"}](tg://user?id={user_id})"[{chat_title}]
                m_to_admin= f"""
تم ارسال [@admin]({link_Chat}) داخل المجموعة :
---------------------------------------
اسم المجموعة :
------------- ( [{chat_title}]({link_Chat}) ) -------------
---------------------------------------
تم الارسال بواسطة :
------------- <  < [{full_name}](tg://user?id={user_id}) > > -------------
---------------------------------------
اذهب الان للتحقق"""
                
                bot.send_message(i,m_to_admin,parse_mode="markdown")

        return found_message ,data

    #?اذا ادمن بوت
    elif user_id in Admin_list:
        return found_message ,data

    elif link_type_message == "text_link":
        bot.delete_message(chat_id,message_id)
        bot.send_message(chat_id,f"([{full_name}](tg://user?id={user_id})) \nممنوع ارسال هذا النوع من الروابط",parse_mode="markdown")

    #?اذا مسموح بالروابط واللروابط المحددة مقفولة
    elif (OK_Link == "True") and (some_link == "False"):
        return found_message ,data

    #?اذا مسموح بالروابط واللروابط المحددة مفتوحة و لتحذير مغلق
    elif (OK_Link == "True") and (some_link == "True") and (warning == "False"):
        islink = check_in_links(text,links_list,chat_id,message_id)
        isuser = link_ceack(message,chat_id,list_fowrword)
        if islink and isuser:
            return found_message ,data
        else:
            bot.send_message(chat_id,message_wrong_user,parse_mode="markdown")
            bot.delete_message(chat_id,message_id)
            Admins = [1814696703,5176738408]
            for i in Admins:
                bot.send_message(i,messagee_link,parse_mode="markdown")
            found_message = False
            return found_message ,data
    
    #?اذا مسموح بالروابط واللروابط المحددة مفتوحة و لتحذير مفتوح
    elif (OK_Link == "True") and (some_link == "True") and (warning == "True"):
        islink = check_in_links(text,links_list,chat_id,message_id)
        isuser = link_ceack(message,chat_id,list_fowrword)
        if islink and isuser:
            return found_message ,data
        else:
            if user_id in Moderators_list:
                bot.send_message(chat_id,message_wrong_user,parse_mode="markdown")
            else:
                data = wrong_member(safeCounter,chat_id,user_id,data,full_name)
            
            bot.delete_message(chat_id,message_id)
            Admins = [1814696703,5176738408]
            for i in Admins:
                bot.send_message(i,messagee_link,parse_mode="markdown")
            found_message = False

            return found_message ,data
        
        
    #?اذا الروابط مغلقة
    elif (OK_Link == "False") and (warning == "False"):
        islink = check_in_links(text,links_list,chat_id,message_id)
        isuser = link_ceack(message,chat_id,list_fowrword)
        if user_id in Moderators_list:
            if islink and isuser:
                return found_message ,data
            else:
                bot.delete_message(chat_id,message_id)
                Admins = [1814696703,5176738408]
                for i in Admins:
                    bot.send_message(i,messagee_link,parse_mode="markdown")
                found_message = False
                return found_message ,data

        else:
            if "entities" in message.json:
                bot.send_message(chat_id,message_wrong_user,parse_mode="markdown")
                bot.delete_message(chat_id,message_id)
                Admins = [1814696703,5176738408]
                for i in Admins:
                    bot.send_message(i,messagee_link,parse_mode="markdown")
                found_message = False
                return found_message ,data
            return found_message ,data
            
    elif (OK_Link == "False") and (warning == "True"):
        islink = check_in_links(text,links_list,chat_id,message_id)
        isuser = link_ceack(message,chat_id,list_fowrword)
        if user_id in Moderators_list:
            if islink and isuser:
                return found_message ,data
            else:
                bot.send_message(chat_id,message_wrong_user,parse_mode="markdown")
                bot.delete_message(chat_id,message_id)
                Admins = [1814696703,5176738408]
                for i in Admins:
                    bot.send_message(i,messagee_link,parse_mode="markdown")
                found_message = False
                return found_message ,data

        else:
            if "entities" in message.json:
                wrong_member(safeCounter,chat_id,user_id,data,full_name)
                bot.delete_message(chat_id,message_id)
                Admins = [1814696703,5176738408]
                for i in Admins:
                    bot.send_message(i,messagee_link,parse_mode="markdown")
                found_message = False
                return found_message ,data
            
            return found_message ,data
        
    return found_message ,data
    

#?التعامل مع الروابط
def About_links(message,chat_id,Admin_list,
                user_id,Moderators_list,data,
                user_stat,list_fowrword):
    #?جزء مسح الروابط
    links_list = list(data["Groups"][f"{chat_id}"]["linkes"])
    OK_Link = data["Groups"][f"{chat_id}"]["OK_Link"]
    some_link = data["Groups"][f"{chat_id}"]["Specific links"]

    warning = data["Groups"][f"{chat_id}"]["warning"]
    
    safeCounter = data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"]["safeCounter"]

    chat_username = message.chat.username
    chat_stat = bot.get_chat(chat_id)
    link_Chat = chat_stat.invite_link    
    # message_id = message.id
    # type_Links = ["mention","text_mention","url","text_link"]
    full_name = message.from_user.full_name
    username = message.from_user.username
    chat_title = message.chat.title
    message_text = message.text
    # awnar = data['Groups'][f'{chat_id}']['owner']
    
    chat_members_count = bot.get_chat_members_count(chat_id=chat_id)
    
    found_message = True

    # all_admin =  Moderators_list + Admin_list

    #?الجزء الخاص بالروابط او اسم المستخدم للملف اذا موجودد في وصف الملف
    if message.caption:
        text_caption = message.caption
        try:
            found_message,data = option_group(chat_title,link_Chat,
                chat_id,chat_username,
                chat_members_count,full_name,
                user_id,username,user_stat,text_caption,
                Admin_list,OK_Link,some_link,warning,
                links_list,Moderators_list,message,
                list_fowrword,data,safeCounter
                )
               
            return found_message ,data
        except:
            found_message = False
            return found_message ,data

    #?الجزء الخاص بالروابط او اسم المستخدم للرسالة النصية           
    elif message_text:
        try:
            found_message,data = option_group(chat_title,link_Chat,
                chat_id,chat_username,
                chat_members_count,full_name,
                user_id,username,user_stat,message_text,
                Admin_list,OK_Link,some_link,warning,
                links_list,Moderators_list,message,
                list_fowrword,data,safeCounter
                )
            return found_message ,data
        except:
            found_message = False
            return found_message ,data

    return found_message ,data

