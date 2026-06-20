# data_lessons_6_10.py
# Contains first-principles detailed data for Lessons 6 through 10

LESSONS_6_10 = [
    {
        "num": 6,
        "title": "Verbs, Objects, and Invitations",
        "jp_title": "ごはんをたべます",
        "overview": "Learn how to use transitive verbs to perform actions on objects, and how to invite friends to do things with you.",
        "objectives": [
            "Use the を particle to mark direct objects",
            "Use the で particle for the location of action",
            "Offer invitations using 〜ませんか",
            "Suggest actions using 〜ましょう"
        ],
        "vocab": [
            ("食べる", "たべる", "To eat", "Verb (Ru)", "N5", "りんごを食べます。", "Ringo o tabemasu.", "I eat an apple."),
            ("飲む", "のむ", "To drink", "Verb (U)", "N5", "水を飲みます。", "Mizu o nomimasu.", "I drink water."),
            ("見る", "みる", "To see/watch", "Verb (Ru)", "N5", "映画を見ます。", "Eiga o mimasu.", "I watch a movie."),
            ("する", "する", "To do", "Verb (Irregular)", "N5", "テニスをします。", "Tenisu o shimasu.", "I play tennis."),
            ("一緒に", "いっしょに", "Together", "Adverb", "N5", "一緒に働きましょう。", "Issho ni hatarakimashou.", "Let's work together."),
        ],
        "grammar": [
            {
                "pattern": "N を V",
                "meaning": "Perform an action (V) on a direct object (N)",
                "structure": "[Object Noun] を (o) [Transitive Verb]",
                "formation": "Place the object first, mark it with the を particle, and end with the verb.",
                "why": "The を particle explicitly marks the target that receives the action of the verb.",
                "formal": "パンを食べます。 (I eat bread.)",
                "casual": "パン、食べる。 (In casual speech, the を particle is frequently dropped).",
                "native": "You can string multiple nouns with 'to' (and), but the final noun takes the を. (Pan to mizu o nomimasu).",
                "examples": [
                    ("テレビを見ます。", "I watch TV."),
                    ("手紙を書きます。", "I write a letter."),
                ],
                "mistakes": "Using を with existence verbs (います/あります) or ability verbs (わかります). ONLY use を with verbs where you take direct action on an object.",
                "jlpt": "Pronunciation note: It is typed as 'wo' but pronounced as 'o'."
            },
            {
                "pattern": "[Place] で [Verb]",
                "meaning": "Do [Verb] at [Place]",
                "structure": "[Location] で (de) [Action Verb]",
                "formation": "Use the で particle to indicate the location where an action takes place.",
                "why": "Unlike に (which marks a pinpoint location of existence), で defines the 'contextual boundary' in which an action happens.",
                "formal": "レストランで食べます。",
                "casual": "レストランで食べる。",
                "native": "Highly flexible. Can be combined with other particles: レストランで友達とパンを食べます。",
                "examples": [
                    ("部屋で勉強します。", "I study in the room."),
                    ("デパートで靴を買いました。", "I bought shoes at the department store."),
                ],
                "mistakes": "CRITICAL: Saying '部屋に勉強します'. You cannot use に for the location of an action. You must use で.",
                "jlpt": "The に vs で distinction is heavily tested in N5 grammar."
            },
            {
                "pattern": "〜ませんか / 〜ましょう",
                "meaning": "Won't you...? / Let's...!",
                "structure": "[Verb Masu-stem] + ませんか / ましょう",
                "formation": "Drop 'masu' and add 'masen ka' to invite. Add 'mashou' to suggest or accept.",
                "why": "ませんか is literally 'do you not...?'. Offering the negative gives the listener a polite 'out' to decline.",
                "formal": "一緒に映画を見ませんか。 ええ、見ましょう！",
                "casual": "To say 'Let's' casually, use the Volitional form (taught later).",
                "native": "ません is considered much more polite and considerate than ましょう when inviting someone for the first time.",
                "examples": [
                    ("お茶を飲みませんか。", "Won't you drink some tea?"),
                    ("行きましょう。", "Let's go."),
                ],
                "mistakes": "Translating ませんか strictly as a negative. In English, it means 'Would you like to...?'",
                "jlpt": "Common response patterns in the listening section."
            }
        ],
        "kanji": [
            ("見", "み", "ケン", "7", "See", "An eye (目) with legs, running to see something.", [("見る", "みる", "To see"), ("見せる", "みせる", "To show")]),
            ("食", "た", "ショク", "9", "Eat", "A person assembling good things under a roof.", [("食べる", "たべる", "To eat"), ("食堂", "しょくどう", "Cafeteria")]),
        ],
        "quiz": [
            {"q": "Which particle marks the location where an action (like reading) takes place?", "opts": ["A. に (ni)", "B. で (de)", "C. へ (e)", "D. を (o)"], "ans": "B", "exp": "で marks the location of an action. に marks the location of existence (with います/あります)."},
            {"q": "How do you politely invite someone to eat?", "opts": ["A. 食べますか", "B. 食べません", "C. 食べましょう", "D. 食べませんか"], "ans": "D", "exp": "ませんか is the polite invitation form ('Won't you eat?')."},
        ]
    },
    {
        "num": 7,
        "title": "Tools, Languages, and Giving/Receiving",
        "jp_title": "あげる・もらう",
        "overview": "Learn how to describe the tools you use, the language you speak in, and the complex system of giving and receiving gifts.",
        "objectives": [
            "Use the で particle for tools and languages",
            "Express giving using あげます",
            "Express receiving using もらいます",
            "Understand the direction of transaction using に/から"
        ],
        "vocab": [
            ("あげる", "あげる", "To give", "Verb (Ru)", "N5", "友達に花をあげます。", "Tomodachi ni hana o agemasu.", "I give flowers to my friend."),
            ("もらう", "もらう", "To receive", "Verb (U)", "N5", "父から時計をもらいました。", "Chichi kara tokei o moraimashita.", "I received a watch from my dad."),
            ("手", "て", "Hand", "Noun", "N5", "手で食べます。", "Te de tabemasu.", "I eat with my hands."),
            ("箸", "はし", "Chopsticks", "Noun", "N5", "箸で食べます。", "Hashi de tabemasu.", "I eat with chopsticks."),
            ("日本語", "にほんご", "Japanese language", "Noun", "N5", "日本語で話します。", "Nihongo de hanashimasu.", "I speak in Japanese."),
        ],
        "grammar": [
            {
                "pattern": "[Tool/Language] で V",
                "meaning": "Do by means of / using [Tool]",
                "structure": "[Noun] で (de) [Verb]",
                "formation": "Use the で particle after a physical tool, a method, or a language.",
                "why": "で defines the 'means' or 'context'. You are acting within the framework of that tool.",
                "formal": "日本語でレポートを書きます。",
                "casual": "スマホで写真(しゃしん)を撮(と)る。",
                "native": "Highly common. 'Kore wa Nihongo de nan desu ka?' (What is this in Japanese?)",
                "examples": [
                    ("はさみで紙を切ります。", "I cut paper with scissors."),
                    ("英語で話します。", "I speak in English."),
                ],
                "mistakes": "Using に for tools. Tools ALWAYS take で.",
                "jlpt": "Identifying the method of action."
            },
            {
                "pattern": "[Giver] は [Receiver] に [Object] を あげます",
                "meaning": "Giver gives Object to Receiver",
                "structure": "[Giver] は [Receiver] に [Object] を あげます。",
                "formation": "The Giver is the topic (は). The Receiver is the target (に).",
                "why": "あげます represents outward motion from the speaker's perspective.",
                "formal": "私は木村さんに花をあげました。",
                "casual": "木村さんに花をあげた。",
                "native": "You CANNOT use あげます when someone gives something to YOU. You must use くれます (taught later).",
                "examples": [
                    ("マリアさんに本をあげます。", "I will give a book to Maria."),
                ],
                "mistakes": "CRITICAL: '私は 友達に もらいました' is receiving. '私は 友達に あげました' is giving. The 'ni' particle stays the same, only the verb changes!",
                "jlpt": "Heavily tested. Understanding the direction of giving based on the verb."
            },
            {
                "pattern": "[Receiver] は [Giver] に/から [Object] を もらいます",
                "meaning": "Receiver receives Object from Giver",
                "structure": "[Receiver] は [Giver] に (or から) [Object] を もらいます。",
                "formation": "The Receiver is the topic (は). The Giver is marked with に (from/target) or から (from).",
                "why": "もらいます represents inward motion towards the subject.",
                "formal": "私は山田さんに辞書をもらいました。",
                "casual": "山田さんに辞書をもらった。",
                "native": "Using から instead of に makes the source very clear and avoids confusion.",
                "examples": [
                    ("先生から本をもらいました。", "I received a book from the teacher."),
                ],
                "mistakes": "Confusing the subject. The person marked with は is the one who ends up with the item.",
                "jlpt": "Reading comprehension trap: Who actually has the book at the end of the sentence?"
            }
        ],
        "kanji": [
            ("手", "て", "シュ", "4", "Hand", "Looks like a hand with fingers.", [("手", "て", "Hand"), ("上手", "じょうず", "Skilled (upper hand)")]),
            ("紙", "かみ", "シ", "10", "Paper", "Thread (糸) + Family/Name. Documents were made of threaded paper.", [("紙", "かみ", "Paper"), ("手紙", "てがみ", "Letter (hand paper)")]),
        ],
        "quiz": [
            {"q": "What does '日本語で話します' mean?", "opts": ["A. I speak to Japan", "B. I speak about Japanese", "C. I speak in Japanese", "D. Japanese speaks to me"], "ans": "C", "exp": "The で particle indicates the tool/means of the action. Speaking 'by means of' Japanese."},
            {"q": "If Tanaka gives a book to Sato, who is the subject (は) of the verb もらいます (receive)?", "opts": ["A. 田中 (Tanaka)", "B. 佐藤 (Sato)", "C. 本 (Book)", "D. No subject"], "ans": "B", "exp": "Sato is the receiver, so the sentence would be: 佐藤は田中から本をもらいました。"},
        ]
    },
    {
        "num": 8,
        "title": "Adjectives: Describing the World",
        "jp_title": "ハンサムですね",
        "overview": "Learn how to use adjectives to describe nouns, and how to conjugate them to say things are NOT or WERE NOT a certain way.",
        "objectives": [
            "Distinguish between い-Adjectives and な-Adjectives",
            "Use adjectives to modify nouns directly",
            "Conjugate adjectives into negative and past forms",
            "Use the intensifier とても and the negator あまり"
        ],
        "vocab": [
            ("大きい", "おおきい", "Big", "I-Adj", "N5", "大きい犬です。", "Ookii inu desu.", "It is a big dog."),
            ("小さい", "ちいさい", "Small", "I-Adj", "N5", "小さい車です。", "Chiisai kuruma desu.", "It is a small car."),
            ("静か", "しずか", "Quiet", "Na-Adj", "N5", "静かな町です。", "Shizuka na machi desu.", "It is a quiet town."),
            ("きれい", "きれい", "Beautiful/Clean", "Na-Adj", "N5", "きれいな花です。", "Kirei na hana desu.", "It is a beautiful flower."),
            ("とても", "とても", "Very", "Adverb", "N5", "とても暑いです。", "Totemo atsui desu.", "It is very hot."),
            ("あまり", "あまり", "Not very (requires negative)", "Adverb", "N5", "あまり寒くないです。", "Amari samukunai desu.", "It is not very cold."),
        ],
        "grammar": [
            {
                "pattern": "N は [Adjective] です",
                "meaning": "N is [Adjective]",
                "structure": "Noun は [i-Adj or na-Adj] です。",
                "formation": "Both types of adjectives can sit right before 'desu'. Do NOT add 'na' when using a na-adjective at the end of a sentence.",
                "why": "Adjectives act as the predicate. 'Desu' acts as a polite wrapper.",
                "formal": "富士山は高いです。 / この町は静かです。",
                "casual": "富士山は高い。 / この町は静かだ。 (i-adj drop desu, na-adj replace with da).",
                "native": "Native speakers drop 'desu' entirely in casual speech for i-adjectives.",
                "examples": [
                    ("東京は大きいです。", "Tokyo is big."),
                    ("そのカメラは新しいです。", "That camera is new."),
                ],
                "mistakes": "Saying 静かなです. (WRONG). 'Na' is ONLY used when putting the adjective directly before a noun.",
                "jlpt": "Identifying sentence-ending adjectives."
            },
            {
                "pattern": "[Adjective] N",
                "meaning": "The [Adjective] Noun",
                "structure": "[i-Adj] + [Noun] OR [na-Adj] + な + [Noun]",
                "formation": "i-Adjectives attach directly to nouns. na-Adjectives MUST have 'na' inserted between them and the noun.",
                "why": "na-Adjectives are essentially nouns themselves. They need a copular bridge ('na') to connect to another noun.",
                "formal": "高い山です。 / 静かな町です。",
                "casual": "Same.",
                "native": "Same.",
                "examples": [
                    ("美味しいパンを食べます。", "I eat delicious bread."),
                    ("きれいな女の人です。", "She is a beautiful woman."),
                ],
                "mistakes": "CRITICAL TRAP: きれい (beautiful) and 有名 (famous) end in the 'i' sound, but they are NA-ADJECTIVES. They must take 'na': きれいな花.",
                "jlpt": "They will try to trick you into treating きれい as an i-adjective."
            },
            {
                "pattern": "あまり + [Negative]",
                "meaning": "Not very...",
                "structure": "あまり (amari) + [Negative Adjective/Verb]",
                "formation": "Amari must ALWAYS be followed by a negative conjugation.",
                "why": "It acts as a degree modifier that softens a negative statement.",
                "formal": "この車はあまり大きくないです。",
                "casual": "この車はあまり大きくない。",
                "native": "Used constantly to be polite instead of saying a flat 'no' or 'it is bad'.",
                "examples": [
                    ("今日はあまり寒くありません。", "Today is not very cold."),
                    ("英語があまりわかりません。", "I don't understand English very well."),
                ],
                "mistakes": "Using あまり with a positive verb. 'あまり暑いです' is strictly forbidden.",
                "jlpt": "If you see あまり in the question, the answer MUST be negative."
            }
        ],
        "kanji": [
            ("大", "おお / ダイ", "ダイ / タイ", "3", "Big", "A person stretching their arms out wide to show how big something is.", [("大きい", "おおきい", "Big"), ("大学", "だいがく", "University (Big study)")]),
            ("小", "ちい", "ショウ", "3", "Small", "Three small drops/pieces.", [("小さい", "ちいさい", "Small"), ("小学校", "しょうがっこう", "Elementary school")]),
        ],
        "quiz": [
            {"q": "Which is the correct way to say 'It is a beautiful flower'?", "opts": ["A. きれいい花です", "B. きれいな花です", "C. きれい花です", "D. きれく花です"], "ans": "B", "exp": "きれい is a na-adjective (despite ending in 'i'), so it requires 'na' before a noun."},
            {"q": "If you see the word あまり (amari) in a sentence, the verb/adjective MUST be:", "opts": ["A. Past tense", "B. Positive", "C. Negative", "D. Polite"], "ans": "C", "exp": "あまり (not very) is a grammatical rule that dictates the end of the sentence must be negative."},
        ]
    },
    {
        "num": 9,
        "title": "Likes, Dislikes, and Ability",
        "jp_title": "わかります・すきです",
        "overview": "Learn how to express your preferences, your skills, and the reasons for your actions.",
        "objectives": [
            "Use the が particle to mark the object of desire/ability",
            "Express likes (好き) and dislikes (嫌い)",
            "Express ability (わかります / できます)",
            "Explain reasons using から"
        ],
        "vocab": [
            ("好き", "すき", "Like", "Na-Adj", "N5", "犬が好きです。", "Inu ga suki desu.", "I like dogs."),
            ("嫌い", "きらい", "Dislike", "Na-Adj", "N5", "野菜が嫌いです。", "Yasai ga kirai desu.", "I dislike vegetables."),
            ("上手", "じょうず", "Skilled / Good at", "Na-Adj", "N5", "歌が上手です。", "Uta ga jouzu desu.", "She is good at singing."),
            ("下手", "へた", "Unskilled / Bad at", "Na-Adj", "N5", "スポーツが下手です。", "Supootsu ga heta desu.", "I am bad at sports."),
            ("わかる", "わかる", "To understand", "Verb (U)", "N5", "日本語がわかります。", "Nihongo ga wakarimasu.", "I understand Japanese."),
        ],
        "grammar": [
            {
                "pattern": "N が 好き / わかる / 上手",
                "meaning": "Like N / Understand N / Good at N",
                "structure": "[Noun] が (ga) [Preference/Ability Word]",
                "formation": "Unlike English where 'like' is an action verb taking a direct object, in Japanese, 'suki' is an ADJECTIVE. The literal translation is 'As for me, dogs ARE LIKABLE'. Therefore, dogs are the subject, marked by が.",
                "why": "This is a fundamental difference in Japanese psychology. Preferences and abilities are states of being, not actions you perform on an object.",
                "formal": "私はスポーツが好きです。",
                "casual": "スポーツが好き。",
                "native": "Never use を with these words.",
                "examples": [
                    ("漢字がわかります。", "I understand Kanji. (Literally: Kanji is understandable to me)."),
                    ("マリアさんはダンスが上手です。", "Maria is good at dancing."),
                ],
                "mistakes": "CRITICAL TRAP: Saying '肉を好きです' (WRONG). You must use が.",
                "jlpt": "Identifying that 好き, 嫌い, 上手, 下手, わかる, and できる strictly require the が particle."
            },
            {
                "pattern": "[Reason] から",
                "meaning": "Because [Reason]...",
                "structure": "[Sentence 1 (Reason)] から (kara)、[Sentence 2 (Result)]",
                "formation": "Place から at the end of the sentence stating the reason.",
                "why": "から means 'origin'. The reason is the 'origin' of the result.",
                "formal": "時間がありませんから、新聞を読みません。",
                "casual": "時間がないから、新聞を読まない。",
                "native": "You can state the result first, and add the reason later: '新聞を読みません。時間がありませんから。'",
                "examples": [
                    ("お金がありませんから、カメラを買いません。", "Because I have no money, I won't buy a camera."),
                    ("おいしいですから、たくさん食べました。", "Because it was delicious, I ate a lot."),
                ],
                "mistakes": "Putting から at the BEGINNING of the reason like English 'because'. It must go at the END of the reason.",
                "jlpt": "Ordering sentences correctly."
            }
        ],
        "kanji": [
            ("好", "す / コウ", "コウ", "6", "Like", "A woman (女) holding a child (子). A universal symbol of fondness.", [("好き", "すき", "Like"), ("大好物", "だいこうぶつ", "Favorite food")]),
            ("歌", "うた", "カ", "14", "Song", "Looks complex, but contains characters indicating breath/yawning. Singing out loud.", [("歌", "うた", "Song"), ("歌手", "かしゅ", "Singer")]),
        ],
        "quiz": [
            {"q": "Which particle is required when saying 'I like apples' (りんご___好きです)?", "opts": ["A. を (o)", "B. で (de)", "C. に (ni)", "D. が (ga)"], "ans": "D", "exp": "好き (like) is an adjective in Japanese. The object of preference must take the が particle."},
            {"q": "How do you correctly say 'Because it is hot, I will drink water'?", "opts": ["A. から暑いですよ、水を飲みます", "B. 暑いですから、水を飲みます", "C. 水を飲みますから、暑いです", "D. 暑い水を飲みますから"], "ans": "B", "exp": "から (because) goes at the END of the reason clause. Reason (暑いです) + から, Result (水を飲みます)."},
        ]
    },
    {
        "num": 10,
        "title": "Counters and Positions",
        "jp_title": "そこにいます",
        "overview": "Learn the complex Japanese counting system, and how to describe the exact spatial positioning of objects.",
        "objectives": [
            "Use basic Japanese counters (〜つ, 〜枚, 〜台, 〜人)",
            "Ask 'How many?'",
            "Describe exact locations (In, On, Next to, Between)"
        ],
        "vocab": [
            ("前", "まえ", "Front / Before", "Noun", "N5", "家の前に車があります。", "Ie no mae ni kuruma ga arimasu.", "There is a car in front of the house."),
            ("後ろ", "うしろ", "Behind", "Noun", "N5", "木の後ろに猫がいます。", "Ki no ushiro ni neko ga imasu.", "There is a cat behind the tree."),
            ("隣", "となり", "Next to (same category)", "Noun", "N5", "銀行の隣に郵便局があります。", "Ginkou no tonari ni yuubinkyoku ga arimasu.", "There is a post office next to the bank."),
            ("間", "あいだ", "Between", "Noun", "N5", "AとBの間にあります。", "A to B no aida ni arimasu.", "It is between A and B."),
            ("中", "なか", "Inside", "Noun", "N5", "箱の中にりんごがあります。", "Hako no naka ni ringo ga arimasu.", "There is an apple in the box."),
        ],
        "grammar": [
            {
                "pattern": "[Noun] の [Position] に",
                "meaning": "At the [Position] of [Noun]",
                "structure": "[Reference Object] の [Position Word] に",
                "formation": "Use the possessive の to link the object to the spatial concept. 'The desk's top'.",
                "why": "In Japanese, spatial concepts (top, inside, front) are treated as physical nouns.",
                "formal": "机の上に本があります。",
                "casual": "机の上にある。",
                "native": "Highly structured and logical.",
                "examples": [
                    ("本屋は駅の前にあります。", "The bookstore is in front of the station."),
                    ("犬はドアの後ろにいます。", "The dog is behind the door."),
                ],
                "mistakes": "Using the wrong existence verb. Even if you get the location right, you must use います for living things.",
                "jlpt": "Classic listening test: 'Where is the dog?' (Next to the TV, behind the sofa, etc)."
            },
            {
                "pattern": "Counters",
                "meaning": "Counting objects based on their shape/type",
                "structure": "[Noun] が [Counter Number] あります",
                "formation": "The counter acts like an adverb modifying the verb. It does NOT take a particle itself.",
                "why": "Japanese categorizes objects by shape. Flat things (paper, shirts) take 枚 (mai). Machines (cars, computers) take 台 (dai). People take 人 (nin). Small/general objects take the native Japanese counting system (一つ, 二つ...).",
                "formal": "切手を三枚買いました。",
                "casual": "切手を三枚買った。",
                "native": "You do not say '三枚の切手'. You say '切手を三枚'. The counter floats free.",
                "examples": [
                    ("りんごを二つ食べました。", "I ate two apples. (General counter)."),
                    ("車が四台あります。", "There are four cars. (Machine counter)."),
                    ("男の人が五人います。", "There are five men. (Person counter)."),
                ],
                "mistakes": "Putting a particle after the counter: 'りんごが二つがあります' is WRONG. The counter floats: 'りんごが二つあります'.",
                "jlpt": "Knowing the correct counter for the correct object type (枚 vs 台)."
            }
        ],
        "kanji": [
            ("中", "なか", "チュウ", "4", "Inside / Middle", "A box with a line striking right through the middle.", [("中", "なか", "Inside"), ("中国", "ちゅうごく", "China (Middle Country)")]),
            ("前", "まえ", "ゼン", "9", "Front / Before", "Contains the radicals for moon/flesh and knife. Originally meant to cut something in front of you.", [("前", "まえ", "Front/Before"), ("午前", "ごぜん", "A.M. (Before noon)")]),
        ],
        "quiz": [
            {"q": "If you buy 3 shirts, which counter should you use?", "opts": ["A. 三つ (Mitsu)", "B. 三台 (Sandai)", "C. 三枚 (Sanmai)", "D. 三人 (Sannin)"], "ans": "C", "exp": "Shirts are flat, thin objects, so they take the 枚 (mai) counter."},
            {"q": "Which sentence has the correct placement for the counter?", "opts": ["A. 二つのりんごが食べました", "B. りんごを二つを食べました", "C. りんごが二つを食べました", "D. りんごを二つ食べました"], "ans": "D", "exp": "The counter (二つ) acts like an adverb and directly modifies the verb without taking a particle."},
        ]
    }
]

# Dummy lessons for 11-25
for i in range(11, 26):
    LESSONS_6_10.append({
        "num": i,
        "title": f"Lesson {i} Mastery Module",
        "jp_title": f"第{i}課",
        "overview": f"In-depth analysis for Lesson {i}. (To be built in next block).",
        "objectives": ["Master vocabulary", "Understand structural rules"],
        "vocab": [("例文", "れいぶん", "Example", "Noun", "N5", "例文を読む。", "Reibun o yomu.", "Read example.")],
        "grammar": [{"pattern": f"Rule {i}", "meaning": "App", "structure": "[X]", "formation": "Logic", "why": "Origin", "formal": "Polite", "casual": "Casual", "native": "Native", "examples": [("例", "Example")], "mistakes": "Trap", "jlpt": "Test"}],
        "kanji": [("学", "がく", "ガク", "8", "Study", "Tip", [("学生", "がくせい", "Student")])],
        "quiz": [{"q": f"Q{i}", "opts": ["A. 1", "B. 2", "C. 3", "D. 4"], "ans": "A", "exp": "Exp"}]
    })
