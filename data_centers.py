# data_centers.py
# Contains all the central learning libraries for the Japanese ecosystem

VERB_CENTER = {
    "intro": "Verbs in Japanese are the core of the sentence. Unlike English, verbs always come at the very end of the sentence. Japanese verbs conjugate (change form) based on tense (present/future vs past) and politeness (formal vs casual). To conjugate any verb, you must first know which of the 3 Groups it belongs to.",
    "groups": [
        {
            "name": "Group 1: U-Verbs (五段動詞 Godan Doushi)",
            "rules": "Group 1 verbs are the most common. In their dictionary form, they end in a 'u' sound (u, tsu, ru, nu, bu, mu, ku, gu, su). To make the formal 'Masu' form, drop the 'u' sound and change it to the 'i' sound of the same consonant column, then add 'masu'.",
            "example": "書く (kaku) → かき (kaki) + ます (masu) = 書きます (kakimasu)",
            "verbs": [
                ("書く (kaku, write)", "かきます (kakimasu)", "かきません (kakimasen)", "かきました (kakimashita)", "かきませんでした (kakimasendeshita)"),
                ("飲む (nomu, drink)", "のみます (nomimasu)", "のみません (nomimasen)", "のみました (nomimashita)", "のみませんでした (nomimasendeshita)"),
                ("話す (hanasu, speak)", "はなします (hanashimasu)", "はなしません (hanashimasen)", "はなしました (hanashimashita)", "はなしませんでした (hanashimasendeshita)"),
            ]
        },
        {
            "name": "Group 2: Ru-Verbs (一段動詞 Ichidan Doushi)",
            "rules": "Group 2 verbs always end in 'ru' (る). Furthermore, the vowel sound right before the 'ru' is always an 'i' or 'e' sound. Conjugating Group 2 is extremely easy: just chop off the 'ru' and attach the ending.",
            "example": "食べる (taberu) → たべ (tabe) + ます (masu) = 食べます (tabemasu)",
            "verbs": [
                ("食べる (taberu, eat)", "たべます (tabemasu)", "たべません (tabemasen)", "たべました (tabemashita)", "たべませんでした (tabemasendeshita)"),
                ("見る (miru, see)", "みます (mimasu)", "みません (mimasen)", "みました (mimashita)", "みませんでした (mimasendeshita)"),
                ("寝る (neru, sleep)", "ねます (nemasu)", "ねません (nemasen)", "ねました (nemashita)", "ねませんでした (nemasendeshita)"),
            ]
        },
        {
            "name": "Group 3: Irregular Verbs (不規則動詞 Fukisoku Doushi)",
            "rules": "There are only two irregular verbs in the entire Japanese language! You just have to memorize them.",
            "example": "する (suru, do) → します (shimasu). くる (kuru, come) → きます (kimasu).",
            "verbs": [
                ("する (suru, do)", "します (shimasu)", "しません (shimasen)", "しました (shimashita)", "しませんでした (shimasendeshita)"),
                ("くる (kuru, come)", "きます (kimasu)", "きません (kimasen)", "きました (kimashita)", "きませんでした (kimasendeshita)"),
            ]
        }
    ],
    "te_form": {
        "title": "The Te-Form (て形) Master Guide",
        "explanation": "The Te-form is the most important conjugation you will learn. By itself, it means nothing, but it acts like a 'connector'. It allows you to link verbs together, make requests ('Please do...'), express permission ('May I...?'), and show ongoing actions ('I am doing...').",
        "rules": [
            ("Group 2 (RU-verbs)", "Chop off る and add て", "たべる → たべて, みる → みて"),
            ("Group 3 (Irregular)", "する → して, くる → きて", "べんきょうする → べんきょうして"),
            ("Group 1: う, つ, る", "Drop the ending, add って (small tsu + te)", "あう → あって, まつ → まって, とる → とって"),
            ("Group 1: む, ぶ, ぬ", "Drop the ending, add んで (n + de)", "のむ → のんで, あそぶ → あそんで, しぬ → しんで"),
            ("Group 1: く", "Drop く, add いて", "かく → かいて. EXCEPTION: いく (to go) → いって (NOT いいて)"),
            ("Group 1: ぐ", "Drop ぐ, add いで", "およぐ → およいで"),
            ("Group 1: す", "Drop す, add して", "はなす → はなして"),
        ]
    }
}

PARTICLES = [

{
"particle": "は",
"romaji": "wa",
"core": "Topic Marker",
"difficulty": "N5",
"origin": "Written as は but pronounced わ when used as a particle.",
"meanings": [
("Topic", "私は学生です。"),
("Contrast", "肉は食べますが、魚は食べません。"),
("General Statement", "日本はきれいです。")
],
"compare_with": ["が"],
"common_mistakes": [
"Using は when emphasizing a specific subject.",
"Confusing topic and grammatical subject."
],
"jlpt_traps": [
"は = topic",
"が = specific subject"
]
},

{
"particle": "が",
"romaji": "ga",
"core": "Subject Marker",
"difficulty": "N5",
"meanings": [
("Subject", "猫がいます。"),
("New Information", "だれが来ましたか。"),
("Like / Skill", "日本語が好きです。"),
("Ability", "日本語がわかります。"),
("Existence", "机の上に本があります。")
],
"compare_with": ["は", "を"],
"jlpt_traps": [
"好き requires が",
"嫌い requires が",
"上手 requires が",
"下手 requires が",
"わかる requires が",
"できる requires が"
]
},

{
"particle": "を",
"romaji": "o",
"core": "Direct Object Marker",
"meanings": [
("Direct Object", "りんごを食べます。"),
("Thing Being Studied", "日本語を勉強します。"),
("Thing Being Watched", "映画を見ます。"),
("Path Traversed", "こうえんを散歩します。")
],
"compare_with": ["が"],
"jlpt_traps": [
"Do not use を with 好きです.",
"Do not use を with わかります."
]
},

{
"particle": "に",
"romaji": "ni",
"core": "Target / Point",
"meanings": [
("Time", "７時に起きます。"),
("Destination", "学校に行きます。"),
("Existence Location", "部屋に猫がいます。"),
("Receiver", "友達にプレゼントをあげます。"),
("Purpose", "映画を見に行きます。"),
("Result", "医者になります。")
],
"compare_with": ["へ", "で"],
"jlpt_traps": [
"Do not use に with 今日.",
"Do not use に with 明日.",
"Do not use に with 毎日."
]
},

{
"particle": "へ",
"romaji": "e",
"core": "Direction",
"meanings": [
("Direction", "東京へ行きます。"),
("Movement", "日本へ来ました。")
],
"compare_with": ["に"],
"jlpt_traps": [
"へ focuses on direction.",
"に focuses on destination."
]
},

{
"particle": "で",
"romaji": "de",
"core": "Place of Action / Means",
"meanings": [
("Action Location", "図書館で勉強します。"),
("Transportation", "バスで行きます。"),
("Tool", "はしで食べます。"),
("Language", "日本語で話します。"),
("Reason", "病気で休みました。")
],
"compare_with": ["に"],
"jlpt_traps": [
"Action location = で",
"Existence location = に"
]
},

{
"particle": "と",
"romaji": "to",
"core": "And / With",
"meanings": [
("Complete List", "肉と魚"),
("Together With", "友達と行きます。"),
("Quotation", "『はい』と言いました。")
]
},

{
"particle": "や",
"romaji": "ya",
"core": "Partial List",
"meanings": [
("A and B among others", "本やペンがあります。")
],
"compare_with": ["と"]
},

{
"particle": "も",
"romaji": "mo",
"core": "Also",
"meanings": [
("Also", "私も学生です。"),
("Too", "彼も来ます。")
]
},

{
"particle": "から",
"romaji": "kara",
"core": "From",
"meanings": [
("Starting Time", "９時からです。"),
("Starting Place", "東京から来ました。"),
("Reason", "忙しいから行きません。")
]
},

{
"particle": "まで",
"romaji": "made",
"core": "Until / To",
"meanings": [
("Ending Time", "５時までです。"),
("Ending Place", "駅まで歩きます。")
]
},

{
"particle": "より",
"romaji": "yori",
"core": "Than",
"meanings": [
("Comparison", "父より母のほうが若いです。")
]
},

{
"particle": "だけ",
"romaji": "dake",
"core": "Only",
"meanings": [
("Only", "水だけ飲みます。")
],
"compare_with": ["しか"]
},

{
"particle": "しか",
"romaji": "shika",
"core": "Only (with negative)",
"meanings": [
("Nothing but", "水しか飲みません。")
],
"compare_with": ["だけ"],
"jlpt_traps": [
"しか MUST be followed by a negative verb."
]
},

{
"particle": "か",
"romaji": "ka",
"core": "Question Marker",
"meanings": [
("Question", "学生ですか。"),
("Or", "コーヒーかお茶")
]
},

{
"particle": "ね",
"romaji": "ne",
"core": "Agreement Tag",
"meanings": [
("Right?", "いい天気ですね。")
]
},

{
"particle": "よ",
"romaji": "yo",
"core": "Assertion Tag",
"meanings": [
("New Information", "おいしいですよ。")
]
}

]


ADJECTIVES = {
    "intro": "Japanese has two types of adjectives. They are named based on what you have to do to attach them directly to a noun. They conjugate similarly to verbs.",
    "i_adj": {
        "name": "い-Adjectives (i-keiyoushi)",
        "rules": "They always end in the hiragana character い (i). To conjugate them, you alter the final い.",
        "examples": "大きい (ookii, big), 高い (takai, expensive), 新しい (atarashii, new).",
        "conjugations": [
            ("Present Affirmative", "大きいです", "(It is big) - Leave it alone, just add です"),
            ("Present Negative", "大きくないです / 大きくありません", "(It is not big) - Drop い, add くないです"),
            ("Past Affirmative", "大きかったです", "(It was big) - Drop い, add かったです"),
            ("Past Negative", "大きくなかったです / 大きくありませんでした", "(It was not big) - Drop い, add くなかったです"),
        ],
        "traps": "EXCEPTION: いい (good). It conjugates as よい. Present: いいです. Negative: よくないです. Past: よかったです."
    },
    "na_adj": {
        "name": "な-Adjectives (na-keiyoushi)",
        "rules": "They act almost exactly like nouns. When putting them directly before a noun, you must insert 'な' (na).",
        "examples": "静か (shizuka, quiet), きれい (kirei, beautiful), 便利 (benri, convenient).",
        "conjugations": [
            ("Present Affirmative", "静かです", "(It is quiet) - Just add です"),
            ("Present Negative", "静かではありません / 静かじゃありません", "(It is not quiet) - Same as noun negation"),
            ("Past Affirmative", "静かでした", "(It was quiet) - Same as noun past tense"),
            ("Past Negative", "静かではありませんでした", "(It was not quiet) - Same as noun past negative"),
        ],
        "traps": "TRAP: きれい (beautiful) and 有名 (famous) end in 'i', but they are NA-adjectives. Do NOT say きれいくないです. It is きれいではありません."
    }
}

EXPRESSIONS = [

("Daily Greetings", [
("おはようございます", "Ohayou gozaimasu", "Good morning."),
("こんにちは", "Konnichiwa", "Hello / Good afternoon."),
("こんばんは", "Konbanwa", "Good evening."),
("おやすみなさい", "Oyasuminasai", "Good night."),
("おやすみ", "Oyasumi", "Good night (casual)."),
("さようなら", "Sayounara", "Goodbye."),
("またあした", "Mata ashita", "See you tomorrow."),
("またらいしゅう", "Mata raishuu", "See you next week."),
("じゃあまた", "Jaa mata", "See you later."),
]),

("Home Expressions", [
("いってきます", "Ittekimasu", "I'm leaving and will come back."),
("いってらっしゃい", "Itterasshai", "Please go and come back safely."),
("ただいま", "Tadaima", "I'm home."),
("おかえりなさい", "Okaerinasai", "Welcome home."),
]),

("School & Classroom Expressions", [
("よろしくおねがいします", "Yoroshiku onegaishimasu", "Please take care of me / Nice to meet you."),
("しつれいします", "Shitsurei shimasu", "Excuse me."),
("しつれいしました", "Shitsurei shimashita", "Excuse me for what I did."),
("わかりました", "Wakarimashita", "Understood."),
("わかりません", "Wakarimasen", "I don't understand."),
("もういちどおねがいします", "Mou ichido onegaishimasu", "Please say it again."),
("ゆっくりおねがいします", "Yukkuri onegaishimasu", "Please speak slowly."),
("もうすこしおおきなこえで", "Mou sukoshi ookina koe de", "Please speak a little louder."),
]),

("Work Expressions", [
("おつかれさまです", "Otsukaresama desu", "Thank you for your hard work."),
("おさきにしつれいします", "Osaki ni shitsurei shimasu", "Excuse me for leaving before you."),
("よろしくおねがいします", "Yoroshiku onegaishimasu", "Please take care of me."),
]),

("Apologies & Thank Yous", [
("ありがとうございます", "Arigatou gozaimasu", "Thank you very much."),
("どうもありがとうございます", "Doumo arigatou gozaimasu", "Thank you very much indeed."),
("どういたしまして", "Douitashimashite", "You're welcome."),
("すみません", "Sumimasen", "Excuse me / Sorry."),
("ごめんなさい", "Gomen nasai", "I'm sorry."),
("もうしわけありません", "Moushiwake arimasen", "I sincerely apologize."),
]),

("Agreement & Reactions", [
("はい", "Hai", "Yes."),
("いいえ", "Iie", "No."),
("そうです", "Sou desu", "That's right."),
("そうですね", "Sou desu ne", "That's true / Let me think."),
("そうですか", "Sou desu ka", "I see."),
("なるほど", "Naruhodo", "I see / Indeed."),
("いいですね", "Ii desu ne", "That sounds good."),
("だいじょうぶです", "Daijoubu desu", "It's okay."),
("けっこうです", "Kekkou desu", "No thank you / That's sufficient."),
("もちろん", "Mochiron", "Of course."),
("ぜひ", "Zehi", "Definitely."),
("たぶん", "Tabun", "Probably."),
]),

("Restaurant & Table Manners", [
("いただきます", "Itadakimasu", "Said before eating."),
("ごちそうさまでした", "Gochisousama deshita", "Said after eating."),
("ごちそうさま", "Gochisousama", "Casual version of 'Thank you for the meal'."),
("いただけますか", "Itadakemasu ka", "Could I receive it?"),
("おかわり", "Okawari", "Another serving / Refill."),
("おかわりください", "Okawari kudasai", "Please give me another serving."),
("みずをください", "Mizu o kudasai", "Please give me water."),
("おちゃをください", "Ocha o kudasai", "Please give me tea."),
("メニューをください", "Menyuu o kudasai", "Please give me the menu."),
("おすすめはなんですか", "Osusume wa nan desu ka", "What do you recommend?"),
("これをください", "Kore o kudasai", "I'll take this one."),
("おかいけいおねがいします", "Okaikei onegaishimasu", "The bill, please."),
("おなかがいっぱいです", "Onaka ga ippai desu", "I'm full."),
("おいしいです", "Oishii desu", "It's delicious."),
("とてもおいしいです", "Totemo oishii desu", "It's very delicious."),
("あまりたべられません", "Amari taberaremasen", "I can't eat much."),
]),

("Shopping Expressions", [
("いらっしゃいませ", "Irasshaimase", "Welcome to our store."),
("いかがですか", "Ikaga desu ka", "How about this?"),
("こちらへどうぞ", "Kochira e douzo", "This way please."),
("これをください", "Kore o kudasai", "I'll take this."),
("もうすこしやすいのがありますか", "Mou sukoshi yasui no ga arimasu ka", "Do you have a cheaper one?"),
]),

("Telephone Expressions", [
("もしもし", "Moshi moshi", "Hello (telephone)."),
("しょうしょうおまちください", "Shoushou omachi kudasai", "Please wait a moment."),
("〜さんをおねがいします", "~san o onegaishimasu", "May I speak to ~?"),
]),

("Travel & Directions", [
("どこですか", "Doko desu ka", "Where is it?"),
("どうやっていきますか", "Dou yatte ikimasu ka", "How do I get there?"),
("きっぷをください", "Kippu o kudasai", "Please give me a ticket."),
("えきはどこですか", "Eki wa doko desu ka", "Where is the station?"),
("ちずをかいてください", "Chizu o kaite kudasai", "Please draw a map."),
]),

("Visitor & Politeness Expressions", [
("おじゃまします", "Ojama shimasu", "Excuse me for disturbing you."),
("おじゃましました", "Ojama shimashita", "Thank you for having me."),
("どうぞ", "Douzo", "Here you are / Please."),
("どうも", "Doumo", "Thanks / Hello."),
]),

("Emergency & Health", [
("だいじょうぶですか", "Daijoubu desu ka", "Are you okay?"),
("だいじょうぶです", "Daijoubu desu", "I'm okay."),
("びょういんはどこですか", "Byouin wa doko desu ka", "Where is the hospital?"),
("きぶんがわるいです", "Kibun ga warui desu", "I feel sick."),
]),

]

