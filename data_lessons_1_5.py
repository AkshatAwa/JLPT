# data_lessons_1_5.py
# Contains first-principles detailed data for Lessons 1 through 5

LESSONS_1_5 = [
    {
        "num": 1,
        "title": "Introductions and Identity",
        "jp_title": "はじめまして",
        "overview": "In this foundational lesson, you will learn how to introduce yourself, state your nationality and occupation, and ask questions. We will master the concept of the 'Copula' (the Japanese equivalent of 'is/am/are').",
        "objectives": [
            "Understand the concept of the Topic Marker は",
            "State your identity using です",
            "Negate your identity using ではありません",
            "Ask questions by appending か",
            "Connect nouns using the possessive particle の"
        ],
        "vocab": [
            ("私", "わたし", "I / me", "Noun", "N5", "私は学生です。", "Watashi wa gakusei desu.", "I am a student."),
            ("あなた", "あなた", "You", "Noun", "N5", "あなたは先生ですか。", "Anata wa sensei desu ka.", "Are you a teacher? (Note: Native speakers rarely use 'anata'. Use their name instead)."),
            ("先生", "せんせい", "Teacher", "Noun", "N5", "彼は先生です。", "Kare wa sensei desu.", "He is a teacher."),
            ("学生", "がくせい", "Student", "Noun", "N5", "私は学生ではありません。", "Watashi wa gakusei dewa arimasen.", "I am not a student."),
            ("会社員", "かいしゃいん", "Company Employee", "Noun", "N5", "父は会社員です。", "Chichi wa kaishain desu.", "My father is a company employee."),
        ],
        "grammar": [
            {
                "pattern": "N1 は N2 です",
                "meaning": "N1 is N2 (A is B)",
                "structure": "[Noun 1] は (wa) [Noun 2] です (desu)。",
                "formation": "Take a topic (N1), mark it with the particle は. State what it is (N2), and end the sentence with the polite copula です.",
                "why": "Japanese is an SOV (Subject-Object-Verb) language. The verb/copula ALWAYS goes at the absolute end. 'は' tells the listener what we are talking about.",
                "formal": "です is formal/polite.",
                "casual": "In casual speech with friends, です is replaced by だ (da).",
                "native": "Native speakers often drop 'Watashi wa' if it is obvious from context. Just saying 'Gakusei desu' is perfectly natural.",
                "examples": [
                    ("私はマリアです。", "I am Maria."),
                    ("マイクさんはアメリカ人です。", "Mike is American."),
                ],
                "mistakes": "Pronouncing は as 'ha' instead of 'wa'. Remember, when used as a grammar particle, it is ALWAYS pronounced 'wa'.",
                "jlpt": "The foundation of N5 reading comprehension."
            },
            {
                "pattern": "N1 は N2 ではありません",
                "meaning": "N1 is NOT N2",
                "structure": "[Noun 1] は [Noun 2] ではありません (dewa arimasen)。",
                "formation": "Replace です with ではありません to make a sentence negative.",
                "why": "ではありません literally means 'it does not exist as...'.",
                "formal": "ではありません is formal and suitable for business/writing.",
                "casual": "In casual speech, use じゃない (ja nai) or じゃありません (ja arimasen).",
                "native": "In spoken Japanese, 'dewa' often contracts to 'ja'. So 'ja arimasen' is highly common in daily polite conversation.",
                "examples": [
                    ("私は先生ではありません。", "I am not a teacher."),
                    ("サントスさんは学生じゃありません。", "Santos is not a student (spoken form)."),
                ],
                "mistakes": "Saying ではないです. While sometimes heard, ではありません is the grammatically correct formal standard taught in JLPT.",
                "jlpt": "Tested heavily in listening. Listen carefully to the very end of the sentence to catch the negative."
            },
            {
                "pattern": "N1 の N2",
                "meaning": "N1's N2 (Possession / Association)",
                "structure": "[Noun 1] の (no) [Noun 2]",
                "formation": "Place の between two nouns. The first noun modifies or owns the second noun.",
                "why": "Japanese modifies from front to back. N1 acts like an adjective describing N2.",
                "formal": "Used in all levels of speech.",
                "casual": "Used in all levels of speech.",
                "native": "Can be chained multiple times: わたしの ほんの なか (Inside of my book).",
                "examples": [
                    ("私の本です。", "It is my book."),
                    ("IMCの社員です。", "I am an employee of IMC."),
                ],
                "mistakes": "Trying to use の to connect adjectives to nouns. の ONLY connects NOUN to NOUN.",
                "jlpt": "Very common reading trap. Translate backwards: 'N2 of N1'."
            }
        ],
        "kanji": [
            ("私", "わたし", "シ", "7", "I, private", "Looks like a tree and a private elbow.", [("私", "わたし", "I"), ("私立", "しりつ", "Private (school)")]),
            ("人", "ひと", "ジン / ニン", "2", "Person", "Looks like a person walking sideways.", [("人", "ひと", "Person"), ("アメリカ人", "あめりかじん", "American person")]),
        ],
        "quiz": [
            {"q": "What is the correct pronunciation of the topic marker 'は'?", "opts": ["A. ha", "B. wa", "C. pa", "D. ba"], "ans": "B", "exp": "When used as a particle, the hiragana は is pronounced 'wa'."},
            {"q": "How do you say 'I am not a student' formally?", "opts": ["A. 学生ではないです", "B. 学生ではありません", "C. 学生じゃありません", "D. 学生ですない"], "ans": "B", "exp": "ではありません is the standard formal negative of です."},
        ]
    },
    {
        "num": 2,
        "title": "Demonstratives: This and That",
        "jp_title": "これ・それ・あれ",
        "overview": "Learn how to point to objects in space relative to you and the listener using the Ko-So-A-Do system.",
        "objectives": [
            "Master the Ko-So-A-Do distance system",
            "Use これ, それ, あれ as standalone nouns",
            "Use この, その, あの as noun modifiers",
            "Ask 'what' using 何 (なん/なに)"
        ],
        "vocab": [
            ("これ", "これ", "This (near speaker)", "Pronoun", "N5", "これは本です。", "Kore wa hon desu.", "This is a book."),
            ("それ", "それ", "That (near listener)", "Pronoun", "N5", "それは辞書ですか。", "Sore wa jisho desu ka.", "Is that a dictionary?"),
            ("あれ", "あれ", "That over there", "Pronoun", "N5", "あれは私の車です。", "Are wa watashi no kuruma desu.", "That over there is my car."),
            ("本", "ほん", "Book", "Noun", "N5", "この本は面白いです。", "Kono hon wa omoshiroi desu.", "This book is interesting."),
            ("何", "なん/なに", "What", "Interrogative", "N5", "これは何ですか。", "Kore wa nan desu ka.", "What is this?"),
        ],
        "grammar": [
            {
                "pattern": "これ / それ / あれ は N です",
                "meaning": "This / That / That over there is N",
                "structure": "[これ/それ/あれ] は [Noun] です。",
                "formation": "The demonstrative pronoun acts as the subject (N1).",
                "why": "Japanese defines spatial relationships strictly. 'Ko' = speaker's domain. 'So' = listener's domain. 'A' = outside both domains.",
                "formal": "Standard polite.",
                "casual": "Standard casual.",
                "native": "If you are holding an object, use これ. If the listener is holding it, use それ. If it's across the room, use あれ.",
                "examples": [
                    ("これは水です。", "This is water."),
                    ("あれは学校です。", "That over there is a school."),
                ],
                "mistakes": "Mixing up the distances. Memorize the 'Ko-So-A-Do' chart.",
                "jlpt": "Visual questions in listening often test if you know who is holding the object based on Ko/So/A."
            },
            {
                "pattern": "この / その / あの N",
                "meaning": "This N / That N",
                "structure": "[この/その/あの] [Noun] は [Noun/Adj] です。",
                "formation": "Unlike これ which stands alone, この MUST be attached directly to a noun.",
                "why": "The 'no' ending indicates it is modifying a noun (like the possession particle).",
                "formal": "Standard.",
                "casual": "Standard.",
                "native": "Often used to specify ownership: 'Kono hon wa watashi no desu' (This book is mine).",
                "examples": [
                    ("この本は私のです。", "This book is mine."),
                    ("あの人はだれですか。", "Who is that person over there?"),
                ],
                "mistakes": "Saying 'これ 本です' (WRONG). You must use 'この 本です' or 'これは 本です'.",
                "jlpt": "Choosing between これ and この is a guaranteed N5 grammar question."
            }
        ],
        "kanji": [
            ("本", "ほん", "ホン", "5", "Book, Origin", "A tree (木) with a mark at its base (root/origin). Books come from trees.", [("本", "ほん", "Book"), ("日本", "にほん", "Japan (Origin of Sun)")]),
            ("何", "なに/なん", "カ", "7", "What", "A person (亻) carrying a box, asking 'what is in here?'.", [("何", "なに", "What"), ("何時", "なんじ", "What time")]),
        ],
        "quiz": [
            {"q": "If the listener is holding a pen, how should you refer to it?", "opts": ["A. これ (kore)", "B. それ (sore)", "C. あれ (are)", "D. どれ (dore)"], "ans": "B", "exp": "それ refers to objects near the listener."},
            {"q": "Which is grammatically correct?", "opts": ["A. これ かばんです", "B. その は かばんです", "C. この かばんは わたしのです", "D. あの は わたしのです"], "ans": "C", "exp": "この/その/あの MUST be followed directly by a noun. これ/それ/あれ stand alone."},
        ]
    },
    {
        "num": 3,
        "title": "Locations and Existence",
        "jp_title": "ここ・そこ・あそこ",
        "overview": "Learn how to point out locations, ask where things are, and use the existence verbs Arimasu and Imasu.",
        "objectives": [
            "Use ここ, そこ, あそこ to indicate locations",
            "Ask where something is using どこ",
            "Understand the massive difference between あります and います",
            "Use the に particle to mark location of existence"
        ],
        "vocab": [
            ("ここ", "ここ", "Here (near speaker)", "Pronoun", "N5", "ここは食堂です。", "Koko wa shokudou desu.", "This place here is the cafeteria."),
            ("そこ", "そこ", "There (near listener)", "Pronoun", "N5", "そこはトイレですか。", "Soko wa toire desu ka.", "Is that place there the restroom?"),
            ("あそこ", "あそこ", "Over there", "Pronoun", "N5", "あそこは学校です。", "Asoko wa gakkou desu.", "That place over there is the school."),
            ("どこ", "どこ", "Where", "Interrogative", "N5", "トイレはどこですか。", "Toire wa doko desu ka.", "Where is the restroom?"),
            ("上", "うえ", "Above/On", "Noun", "N5", "机の上にあります。", "Tsukue no ue ni arimasu.", "It is on the desk."),
            ("下", "した", "Below/Under", "Noun", "N5", "ベッドの下にいます。", "Beddo no shita ni imasu.", "They are under the bed."),
        ],
        "grammar": [
            {
                "pattern": "N1 は どこ ですか",
                "meaning": "Where is N1?",
                "structure": "[Noun 1] は どこ ですか。",
                "formation": "Set the item as the topic with は, then ask 'where' using 'doko desu ka'.",
                "why": "This is the standard formula for asking location. Very direct and polite.",
                "formal": "トイレはどこですか。 (Standard polite).",
                "casual": "トイレ、どこ？ (Drop the particles and copula, raise intonation).",
                "native": "Often native speakers will just say the noun with a questioning tone: 'Toire wa?'",
                "examples": [
                    ("先生はどこですか。", "Where is the teacher?"),
                    ("駅はどこですか。", "Where is the station?"),
                ],
                "mistakes": "Do not overcomplicate this. Just N1 は どこ ですか.",
                "jlpt": "Often tested in listening. 'Where is the object?' questions."
            },
            {
                "pattern": "N に あります / います",
                "meaning": "Exists at N / Is at N",
                "structure": "[Location] に [Object] が あります/います。",
                "formation": "Use 'ni' to mark the location like a dart on a map. Then use 'ga' to mark the subject that exists there. Finally, use 'arimasu' for inanimate objects or 'imasu' for living things.",
                "why": "Japanese strictly divides existence between things that move/breathe (people, animals) and things that don't (plants, objects, concepts).",
                "formal": "あります / います are the polite forms.",
                "casual": "ある / いる are the dictionary casual forms.",
                "native": "Using 'imasu' for inanimate things sounds extremely weird to native speakers, like you believe the object is alive.",
                "examples": [
                    ("部屋に猫がいます。", "There is a cat in the room. (Cat = living = imasu)."),
                    ("机の上に本があります。", "There is a book on the desk. (Book = inanimate = arimasu)."),
                ],
                "mistakes": "CRITICAL MISTAKE: Swapping arimasu and imasu. Remember: Imasu = I move (living).",
                "jlpt": "This is guaranteed to be tested. Look out for trick questions about plants (they don't move, so they use あります)."
            }
        ],
        "kanji": [
            ("上", "うえ", "ジョウ", "3", "Above, Up", "A line pointing upward from a base.", [("上", "うえ", "Up"), ("上手", "じょうず", "Skilled (Upper hand)")]),
            ("下", "した", "カ / ゲ", "3", "Below, Down", "A line pointing downward from a base.", [("下", "した", "Down"), ("下手", "へた", "Unskilled (Lower hand)")]),
        ],
        "quiz": [
            {"q": "Which existence verb should you use for a tree (木)?", "opts": ["A. います (imasu)", "B. あります (arimasu)", "C. です (desu)", "D. します (shimasu)"], "ans": "B", "exp": "Trees and plants are inanimate in Japanese grammar because they do not move independently. Use あります."},
            {"q": "How do you ask 'Where is the station?'", "opts": ["A. 駅はここですか。", "B. 駅はなんですか。", "C. 駅はどこですか。", "D. 駅はだれですか。"], "ans": "C", "exp": "どこ (doko) means 'where'."},
        ]
    },
    {
        "num": 4,
        "title": "Time, Days, and Schedules",
        "jp_title": "いま なんじですか",
        "overview": "Learn how to read the clock, state the days of the week, and describe when actions take place using specific time markers and boundaries.",
        "objectives": [
            "Tell the time using じ and ふん",
            "State the days of the week",
            "Use the に particle for specific times",
            "Use から and まで to set start and end boundaries"
        ],
        "vocab": [
            ("今", "いま", "Now", "Noun", "N5", "今は何時ですか。", "Ima wa nanji desu ka.", "What time is it now?"),
            ("時", "じ", "O'clock", "Counter", "N5", "三時です。", "San-ji desu.", "It is 3 o'clock."),
            ("半", "はん", "Half past", "Noun", "N5", "四時半に帰ります。", "Yo-ji han ni kaerimasu.", "I will return at 4:30."),
            ("月曜日", "げつようび", "Monday", "Noun", "N5", "月曜日に働きます。", "Getsuyoubi ni hatarakimasu.", "I work on Monday."),
            ("毎日", "まいにち", "Every day", "Noun", "N5", "毎日勉強します。", "Mainichi benkyou shimasu.", "I study every day."),
        ],
        "grammar": [
            {
                "pattern": "[Time] に [Verb]",
                "meaning": "Do action AT [Time]",
                "structure": "[Specific Time] に [Verb]ます。",
                "formation": "Place the time word first, add the に particle, then the verb.",
                "why": "The に particle pinpoints a specific spot on the timeline, just like it pinpoints a spot on a map.",
                "formal": "Polite verbs end in ます.",
                "casual": "Casual verbs use dictionary form.",
                "native": "Native speakers strictly enforce the rule about *when* to use に.",
                "examples": [
                    ("6時に起きます。", "I wake up at 6:00."),
                    ("日曜日にテニスをします。", "I play tennis on Sunday."),
                ],
                "mistakes": "CRITICAL TRAP: Do NOT use に with relative time words. Today (きょう), tomorrow (あした), every day (まいにち) DO NOT take に.",
                "jlpt": "They will try to trick you by writing 'あしたに...'. This is grammatically wrong."
            },
            {
                "pattern": "〜から 〜まで",
                "meaning": "From 〜 Until 〜",
                "structure": "[Start] から (kara) [End] まで (made)",
                "formation": "Marks the start boundary and end boundary of time or space.",
                "why": "から means 'from/origin'. まで means 'until/limit'.",
                "formal": "Can be used alone or with verbs.",
                "casual": "Same in casual speech.",
                "native": "Can be used independently. You don't need both. '9時から働きます' (I work from 9).",
                "examples": [
                    ("9時から5時まで働きます。", "I work from 9:00 to 5:00."),
                    ("東京から大阪まで行きます。", "I go from Tokyo to Osaka."),
                ],
                "mistakes": "Confusing から with the particle で.",
                "jlpt": "Very common in schedule reading comprehension questions."
            }
        ],
        "kanji": [
            ("今", "いま", "コン", "4", "Now", "A clock pendulum swinging under a roof.", [("今", "いま", "Now"), ("今日", "きょう", "Today")]),
            ("時", "じ", "ジ", "10", "Time", "Sun (日) + Temple (寺). Keeping time by the sun at the temple.", [("時間", "じかん", "Time"), ("何時", "なんじ", "What time")]),
        ],
        "quiz": [
            {"q": "Which sentence is grammatically CORRECT?", "opts": ["A. 明日に行きます。", "B. 明日行きます。", "C. 毎日に寝ます。", "D. 今日に帰ります。"], "ans": "B", "exp": "Relative time words like 明日 (tomorrow) do NOT take the に particle."},
            {"q": "How do you say 'From 1 to 3'?", "opts": ["A. 1から3に", "B. 1まで3から", "C. 1から3まで", "D. 1に3へ"], "ans": "C", "exp": "から means from, まで means until."},
        ]
    },
    {
        "num": 5,
        "title": "Motion and Transport",
        "jp_title": "いきます・きます・かえります",
        "overview": "Learn how to describe moving from place to place, how you got there, and who you went with.",
        "objectives": [
            "Master the motion verbs 行きます, 来ます, and 帰ります",
            "Use へ and に to indicate destination",
            "Use で to indicate means of transportation",
            "Use と to indicate accompanying people"
        ],
        "vocab": [
            ("行く", "いく", "To go", "Verb (U)", "N5", "学校へ行きます。", "Gakkou e ikimasu.", "I go to school."),
            ("来る", "くる", "To come", "Verb (Irregular)", "N5", "日本へ来ました。", "Nihon e kimashita.", "I came to Japan."),
            ("帰る", "かえる", "To return/go home", "Verb (U)", "N5", "うちへ帰ります。", "Uchi e kaerimasu.", "I will return home."),
            ("電車", "でんしゃ", "Train", "Noun", "N5", "電車で行きます。", "Densha de ikimasu.", "I go by train."),
            ("友達", "ともだち", "Friend", "Noun", "N5", "友達と来ました。", "Tomodachi to kimashita.", "I came with a friend."),
        ],
        "grammar": [
            {
                "pattern": "[Place] へ/に 行きます",
                "meaning": "Go to [Place]",
                "structure": "[Destination] へ (e) / に (ni) 行きます/来ます/帰ります。",
                "formation": "Use へ (pronounced 'e' as a particle) to emphasize the *direction* of travel. Use に to emphasize the final *destination* point.",
                "why": "Historically, へ meant direction, に meant point. In modern Japanese, they are often interchangeable for destinations.",
                "formal": "行きます (ikimasu).",
                "casual": "行く (iku).",
                "native": "Native speakers use both. へ is slightly more 'flowy'.",
                "examples": [
                    ("京都へ行きます。", "I will go to Kyoto."),
                    ("国に帰ります。", "I will return to my country."),
                ],
                "mistakes": "Pronouncing へ as 'he'. As a particle, it is 'e'.",
                "jlpt": "Remember: 行く is moving *away* from the speaker. 来る is moving *towards* the speaker."
            },
            {
                "pattern": "[Vehicle] で 行きます",
                "meaning": "Go BY means of [Vehicle]",
                "structure": "[Transport Noun] で [Verb]",
                "formation": "The で particle marks the method or means of an action.",
                "why": "で defines the boundary or context of the action. You are acting *within* the context of a train.",
                "formal": "電車で行きます。",
                "casual": "電車で行く。",
                "native": "Very straightforward and widely used.",
                "examples": [
                    ("バスで来ました。", "I came by bus."),
                    ("タクシーで帰ります。", "I will return by taxi."),
                ],
                "mistakes": "CRITICAL TRAP: 'Walking' (歩いて) is an adverbial form, NOT a noun. Do NOT say '歩いてで行きます'. It is just '歩いて行きます' (I go walking).",
                "jlpt": "Walking (歩いて) never takes the で particle. Highly tested."
            },
            {
                "pattern": "[Person] と 行きます",
                "meaning": "Go WITH [Person]",
                "structure": "[Person] と [Verb]",
                "formation": "The と particle means 'with' or 'and'.",
                "why": "It links you and another entity together in the action.",
                "formal": "家族と来ました。 (I came with my family).",
                "casual": "家族と来た。 (I came with my family).",
                "native": "If you are alone, use 一人で (hitori de) — NOT hitori to.",
                "examples": [
                    ("友達と映画を見ます。", "I watch a movie with a friend."),
                ],
                "mistakes": "Using と for transportation (WRONG). Use で for vehicles, と for people.",
                "jlpt": "Distinguishing で (means) and と (companion)."
            }
        ],
        "kanji": [
            ("行", "い", "コウ / ギョウ", "6", "Go", "A crossroads or intersection.", [("行く", "いく", "To go"), ("旅行", "りょこう", "Travel")]),
            ("来", "き / く", "ライ", "7", "Come", "A grain of wheat dropping down. Represents things coming.", [("来る", "くる", "To come"), ("来年", "らいねん", "Next year")]),
        ],
        "quiz": [
            {"q": "Which is the correct way to say 'I walk to school'?", "opts": ["A. 歩いてで行きます", "B. 歩いて行きます", "C. 歩いてと行きます", "D. 歩いてに行きます"], "ans": "B", "exp": "歩いて (aruite) is a te-form verb acting as an adverb ('walking'). It does NOT take any particles like で."},
            {"q": "What is the difference between 行きます and 来ます?", "opts": ["A. 行きます is past tense", "B. 来ます means moving away from speaker", "C. 行きます means moving away from speaker", "D. They are identical"], "ans": "C", "exp": "行く (go) implies motion away from the speaker. 来る (come) implies motion towards the speaker or listener's focus."},
        ]
    }
]

# Add dummy lessons to reach 25
for i in range(6, 26):
    LESSONS_1_5.append({
        "num": i,
        "title": f"Lesson {i} Mastery Module",
        "jp_title": f"第{i}課",
        "overview": f"In-depth analysis and grammatical derivations for Lesson {i}. (Content expansion in next block).",
        "objectives": ["Master vocabulary", "Understand structural rules", "Pass JLPT mock exams"],
        "vocab": [("例文", "れいぶん", "Example sentence", "Noun", "N5", "例文を読みます。", "Reibun o yomimasu.", "I read the example sentence.")],
        "grammar": [{
            "pattern": f"Lesson {i} Core Grammar",
            "meaning": "Advanced application",
            "structure": "[Verb] + Context",
            "formation": "First principles derivation of the rule.",
            "why": "Linguistic origin.",
            "formal": "Used in business.",
            "casual": "Used with friends.",
            "native": "Real world application.",
            "examples": [("先生に聞きます。", "I ask the teacher.")],
            "mistakes": "Common error warning.",
            "jlpt": "Exam strategy."
        }],
        "kanji": [("学", "がく", "ガク", "8", "Study", "Child under a school roof.", [("学生", "がくせい", "Student")])],
        "quiz": [{"q": f"Lesson {i} review question", "opts": ["A. Right", "B. Wrong", "C. Wrong", "D. Wrong"], "ans": "A", "exp": "Explanation."}]
    })
