# data_lessons_21_25.py
# Contains first-principles detailed data for Lessons 21 through 25 (The final N5 lessons)

LESSONS_21_25 = [
    {
        "num": 21,
        "title": "Thoughts and Quotations",
        "jp_title": "明日雨が降ると思います",
        "overview": "Learn how to express your own opinions, state your thoughts, and directly quote what other people have said.",
        "objectives": [
            "Express thoughts and opinions using 〜と思います",
            "Quote direct and indirect speech using 〜と言いました",
            "Seek agreement from the listener using 〜でしょう",
            "Understand that quotation clauses require the Plain Form"
        ],
        "vocab": [
            ("思う", "おもう", "To think", "Verb (U)", "N5", "高いと思います。", "Takai to omoimasu.", "I think it is expensive."),
            ("言う", "いう", "To say", "Verb (U)", "N5", "彼は行くと言いました。", "Kare wa iku to iimashita.", "He said he will go."),
            ("足りる", "たりる", "To be enough", "Verb (Ru)", "N5", "時間が足りないと思います。", "Jikan ga tarinai to omoimasu.", "I think there is not enough time."),
            ("勝つ", "かつ", "To win", "Verb (U)", "N5", "日本が勝つと思います。", "Nihon ga katsu to omoimasu.", "I think Japan will win."),
            ("負ける", "まける", "To lose", "Verb (Ru)", "N5", "試合に負けました。", "Shiai ni makemashita.", "We lost the match."),
        ],
        "grammar": [
            {
                "pattern": "[Plain Form] と 思います",
                "meaning": "I think that...",
                "structure": "[Plain Form Sentence] と (to) 思います",
                "formation": "You construct a complete sentence in the Plain (casual) style, attach the quotation particle と, and end with 思います.",
                "why": "The particle と acts like quotation marks in Japanese. You are literally saying: '(Quote) -> I think.'",
                "formal": "明日雨が降ると思います。",
                "casual": "明日雨が降ると思う。",
                "native": "When asking someone's opinion, you cannot just say 'Do you think?'. You must ask 'どう思いますか' (How do you think?).",
                "examples": [
                    ("日本の物価は高いと思います。", "I think prices in Japan are high."),
                    ("ミラーさんは来ないと思います。", "I think Mr. Miller will not come."),
                ],
                "mistakes": "Using the polite form before と. '高いですと思います' is WRONG. It must be '高いと思います'.",
                "jlpt": "Identifying that the clause before と must be in Plain Form."
            },
            {
                "pattern": "「Sentence」と 言いました",
                "meaning": "Said '...'",
                "structure": "「[Direct Quote]」と 言いました",
                "formation": "Enclose the exact phrase in Japanese quotation marks 「 」 and follow with と言いました.",
                "why": "This is direct quotation.",
                "formal": "先生は「明日テストがあります」と言いました。",
                "casual": "先生は「明日テストがある」と言った。",
                "native": "For indirect quotation (He said that he will go), you drop the brackets and use the plain form: 先生は明日テストがあると言いました。",
                "examples": [
                    ("寝る前に「おやすみなさい」と言います。", "Before sleeping, we say 'Good night'."),
                ],
                "mistakes": "Using indirect quotation rules for direct quotes.",
                "jlpt": "Testing the difference between direct quotes (allows polite form) and indirect quotes (requires plain form)."
            },
            {
                "pattern": "[Plain Form] でしょう？",
                "meaning": "...right? / ...isn't it?",
                "structure": "[Plain Form] でしょう",
                "formation": "Attach でしょう to the end of a plain sentence. Note: For Nouns and Na-adjectives, drop the 'da' before attaching 'deshou'.",
                "why": "This is used when the speaker is confident the listener agrees with them and is seeking confirmation.",
                "formal": "明日パーティーに行くでしょう？",
                "casual": "明日パーティーに行くでしょ？ (Drop the long 'u').",
                "native": "The intonation must rise at the end. If it falls, it means 'It probably will' instead of 'Right?'.",
                "examples": [
                    ("北海道は寒かったでしょう？", "Hokkaido was cold, wasn't it?"),
                ],
                "mistakes": "Leaving 'da' on a noun. '学生だでしょう' is WRONG. It must be '学生でしょう'.",
                "jlpt": "Intonation and grammatical connection rules for でしょう."
            }
        ],
        "kanji": [
            ("思", "おも", "シ", "9", "Think", "A field (田) over a heart (心). The mind working over the heart.", [("思う", "おもう", "To think"), ("思い出す", "おもいだす", "To remember")]),
            ("言", "い / こと", "ゲン", "7", "Say", "Words coming out of a mouth (口).", [("言う", "いう", "To say"), ("言葉", "ことば", "Word")]),
        ],
        "quiz": [
            {"q": "Which is the correct way to say 'I think it is quiet'?", "opts": ["A. 静かですと思います", "B. 静かだだと思います", "C. 静かだと思います", "D. 静かと思います"], "ans": "C", "exp": "The clause before と思います must be in Plain Form. The plain form of 静かです is 静かだ."},
            {"q": "What is the function of the と (to) particle in '〜と言いました'?", "opts": ["A. It means 'and'", "B. It means 'with'", "C. It acts as a quotation marker", "D. It indicates a destination"], "ans": "C", "exp": "In the context of thinking or speaking, と functions like quotation marks to denote the content of the thought/speech."},
        ]
    },
    {
        "num": 22,
        "title": "Noun Modifiers",
        "jp_title": "私が作ったケーキです",
        "overview": "Learn how to use entire sentences to describe a single noun. This is one of the most powerful and fundamentally different structures in Japanese compared to English.",
        "objectives": [
            "Use Plain Form sentences to modify nouns",
            "Understand that Japanese lacks relative pronouns (who, which, that)",
            "Identify the subject of a modifying clause using が"
        ],
        "vocab": [
            ("着る", "きる", "To wear (upper body)", "Verb (Ru)", "N5", "シャツを着ています。", "Shatsu o kite imasu.", "I am wearing a shirt."),
            ("履く", "はく", "To wear (lower body)", "Verb (U)", "N5", "靴を履きます。", "Kutsu o hakimasu.", "I wear shoes."),
            ("被る", "かぶる", "To wear (head)", "Verb (U)", "N5", "帽子を被ります。", "Boushi o kaburimasu.", "I wear a hat."),
            ("掛ける", "かける", "To wear (glasses)", "Verb (Ru)", "N5", "眼鏡を掛けています。", "Megane o kakete imasu.", "I am wearing glasses."),
            ("生まれる", "うまれる", "To be born", "Verb (Ru)", "N5", "東京で生まれました。", "Toukyou de umaremashita.", "I was born in Tokyo."),
        ],
        "grammar": [
            {
                "pattern": "[Plain Form Clause] + Noun",
                "meaning": "The Noun that [Clause]",
                "structure": "[Plain Form Sentence] + [Noun]",
                "formation": "In English, you say 'The book THAT I bought'. The modifier ('that I bought') comes AFTER the noun. In Japanese, the modifier ALWAYS comes BEFORE the noun. 'I bought book' -> 買った本.",
                "why": "Japanese strictly modifies from front-to-back. An entire sentence can act like a giant adjective.",
                "formal": "これは私が撮った写真です。",
                "casual": "これ、私が撮った写真。",
                "native": "Inside a modifying clause, the subject is marked with が, NEVER は.",
                "examples": [
                    ("ミラーさんが住んでいる家は古いです。", "The house that Mr. Miller lives in is old."),
                    ("昨日買ったケーキを食べました。", "I ate the cake that I bought yesterday."),
                ],
                "mistakes": "CRITICAL TRAP: Using は inside the modifier. '私は買った本' is WRONG. It must be '私が買った本' (The book that I bought). は sets the topic for the WHOLE sentence, not the mini-clause.",
                "jlpt": "Identifying what the clause is actually modifying, and the が vs は rule."
            },
            {
                "pattern": "Dictionary vs Ta-Form Modifiers",
                "meaning": "Time frames of modifiers",
                "structure": "Dictionary = Future/Habitual. Ta-Form = Past/Completed.",
                "formation": "You can change the meaning entirely just by the tense of the modifying verb.",
                "why": "Because Japanese modifiers are full sentences, they carry their own tense.",
                "formal": "明日会う人 (The person I will meet tomorrow) vs 昨日会った人 (The person I met yesterday).",
                "casual": "N/A",
                "native": "Very compact and efficient way to convey complex information.",
                "examples": [
                    ("中国で買ったお茶を飲みます。", "I drink the tea that I bought in China."),
                ],
                "mistakes": "Using polite verbs to modify. '買いました本' is strictly broken grammar. Modifiers MUST be in Plain Form.",
                "jlpt": "Choosing the correct verb tense for the modifying clause."
            }
        ],
        "kanji": [
            ("着", "き / つ", "チャク", "12", "Wear / Arrive", "A sheep (羊) over an eye (目). Wool covering the body.", [("着る", "きる", "To wear"), ("到着", "とうちゃく", "Arrival")]),
            ("生", "う / い", "セイ / ショウ", "5", "Life / Born", "A plant sprouting from the ground.", [("生まれる", "うまれる", "To be born"), ("先生", "せんせい", "Teacher")]),
        ],
        "quiz": [
            {"q": "How do you translate: 'The bag that Mr. Yamada bought'?", "opts": ["A. 山田さんは買ったかばん", "B. 買った山田さんのかばん", "C. 山田さんが買ったかばん", "D. かばんは山田さんが買った"], "ans": "C", "exp": "The modifying clause comes first (山田さんが買った), followed directly by the noun (かばん). The subject inside the clause must take が."},
            {"q": "Which verb form CANNOT be used to directly modify a noun?", "opts": ["A. The Dictionary Form (行く)", "B. The Ta-Form (行った)", "C. The Nai-Form (行かない)", "D. The Masu-Form (行きます)"], "ans": "D", "exp": "You can only use Plain Forms (Dictionary, Ta, Nai) to modify nouns. Formal forms like Masu cannot connect to nouns."},
        ]
    },
    {
        "num": 23,
        "title": "Time Clauses (When / If)",
        "jp_title": "図書館へ行くとき、カードが要ります",
        "overview": "Learn how to describe exactly *when* an action happens using とき, and how to create conditional 'If/When' statements using と.",
        "objectives": [
            "Use 〜とき to specify when something happens",
            "Understand the tense rules before とき",
            "Use the dictionary form + と for natural consequences (If A, then B)"
        ],
        "vocab": [
            ("道", "みち", "Road / Street", "Noun", "N5", "道を渡ります。", "Michi o watarimasu.", "I cross the street."),
            ("交差点", "こうさてん", "Intersection", "Noun", "N5", "交差点を右へ曲がります。", "Kousaten o migi e magarimasu.", "Turn right at the intersection."),
            ("渡る", "わたる", "To cross", "Verb (U)", "N5", "橋を渡ります。", "Hashi o watarimasu.", "I cross the bridge."),
            ("曲がる", "まがる", "To turn", "Verb (U)", "N5", "右へ曲がると、あります。", "Migi e magaru to, arimasu.", "If you turn right, it is there."),
            ("音", "おと", "Sound", "Noun", "N5", "音が聞こえます。", "Oto ga kikoemasu.", "I can hear a sound."),
        ],
        "grammar": [
            {
                "pattern": "[Plain Form] とき",
                "meaning": "When...",
                "structure": "[Verb Plain Form / Noun+の / Na-Adj+な / I-Adj] + とき (toki)",
                "formation": "とき acts as a noun meaning 'the time of'. Therefore, all the rules of noun modification (Lesson 22) apply here.",
                "why": "By modifying 'toki', you define the exact time frame of the main action.",
                "formal": "図書館で本を借りるとき、カードが要ります。",
                "casual": "本を借りるとき、カードが要る。",
                "native": "Notice that 'hima na toki' (when I am free) requires 'na' because 'hima' is a na-adjective.",
                "examples": [
                    ("子供のとき、よく川で泳ぎました。", "When I was a child, I often swam in the river."),
                    ("頭が痛いとき、この薬を飲みます。", "When my head hurts, I take this medicine."),
                ],
                "mistakes": "Forgetting the particles for nouns and na-adjs. '子供とき' is wrong. It must be '子供のとき'.",
                "jlpt": "Knowing the correct connection: Noun+の, Na-Adj+な."
            },
            {
                "pattern": "V-る/V-ない と、〜",
                "meaning": "If / When V happens, (natural consequence)",
                "structure": "[Dictionary or Nai-Form] + と (to)、[Consequence]",
                "formation": "Attach the particle と to the plain present tense of a verb.",
                "why": "This 'to' means 'whenever A happens, B inevitably follows'. It is used for natural facts, machine operations, and directions.",
                "formal": "このボタンを押すと、お釣りが出ます。",
                "casual": "このボタンを押すと、お釣りが出る。",
                "native": "You CANNOT use this structure for personal desires or requests. (e.g. 'If I have money, I want to buy a car' CANNOT use と).",
                "examples": [
                    ("右へ曲がると、郵便局があります。", "If you turn right, there is a post office. (Giving directions)."),
                ],
                "mistakes": "Using と for personal commands. '春になると、花見をしましょう' is WRONG. と is only for inevitable facts.",
                "jlpt": "Distinguishing the 'natural consequence と' from other conditionals."
            }
        ],
        "kanji": [
            ("道", "みち", "ドウ", "12", "Road / Path", "A head (首) moving along a path (辶).", [("道", "みち", "Road"), ("水道", "すいどう", "Water supply / Pipe")]),
            ("音", "おと", "オン", "9", "Sound", "To stand (立) under the sun (日) and make noise.", [("音", "おと", "Sound"), ("音楽", "おんがく", "Music")]),
        ],
        "quiz": [
            {"q": "How do you correctly say 'When I am free (暇 - hima)'?", "opts": ["A. 暇のとき", "B. 暇とき", "C. 暇なとき", "D. 暇でとき"], "ans": "C", "exp": "暇 is a Na-adjective, so it must take な before a noun like とき."},
            {"q": "The conditional と (e.g., ボタンを押すと...) is used for:", "opts": ["A. Inviting someone", "B. Expressing personal desires", "C. Inevitable facts and machine operations", "D. Apologizing"], "ans": "C", "exp": "The と conditional means 'Whenever A happens, B invariably happens'. It is used for facts, directions, and mechanics."},
        ]
    },
    {
        "num": 24,
        "title": "Giving and Receiving (Advanced)",
        "jp_title": "私に花をくれました",
        "overview": "Expand your knowledge of giving and receiving. Learn the crucial difference between 'Ageru' (giving outward) and 'Kureru' (giving inward to me).",
        "objectives": [
            "Use くれます to express someone giving something to YOU",
            "Express doing favors for others using 〜てあげます",
            "Express receiving favors using 〜てもらいます",
            "Express someone doing a favor for you using 〜てくれます"
        ],
        "vocab": [
            ("くれる", "くれる", "To give (to me)", "Verb (Ru)", "N5", "彼が私にくれました。", "Kare ga watashi ni kuremashita.", "He gave it to me."),
            ("手伝う", "てつだう", "To help", "Verb (U)", "N5", "仕事を手伝ってくれました。", "Shigoto o tetsudatte kuremashita.", "He helped me with my work."),
            ("直す", "なおす", "To fix / correct", "Verb (U)", "N5", "自転車を直してもらいました。", "Jitensha o naoshite moraimashita.", "I had my bicycle fixed (received the favor)."),
            ("連れて行く", "つれていく", "To take (someone)", "Verb (U)", "N5", "子供を病院へ連れて行きます。", "Kodomo o byouin e tsurete ikimasu.", "I will take my child to the hospital."),
            ("おじいさん", "おじいさん", "Grandfather / Old man", "Noun", "N5", "おじいさんに道を教えました。", "Ojiisan ni michi o oshiemashita.", "I taught the old man the way."),
        ],
        "grammar": [
            {
                "pattern": "[Giver] は/が 私 に [Object] を くれます",
                "meaning": "Giver gives [Object] to ME",
                "structure": "[Giver] は (wa) 私に (to me) くれます (kuremasu)",
                "formation": "Use くれます ONLY when the receiver is the speaker (or the speaker's in-group/family).",
                "why": "Japanese verbs encode the *direction* of the action. あげます goes outward (away from speaker). くれます goes inward (toward the speaker).",
                "formal": "佐藤さんが（私に）クリスマスカードをくれました。",
                "casual": "佐藤さんがくれた。",
                "native": "Because 'kuremasu' inherently means 'gave to me', native speakers almost always drop 'watashi ni'. It is implied by the verb itself.",
                "examples": [
                    ("誰がこの本をくれましたか。", "Who gave you this book? (Speaker is receiver)."),
                ],
                "mistakes": "CRITICAL: '友達にプレゼントをくれました' is WRONG if you are giving it to the friend. If you are the giver, you MUST use あげます.",
                "jlpt": "Ageru vs Kureru is heavily tested to see if you understand the direction of the transaction."
            },
            {
                "pattern": "V-て あげます / もらいます / くれます",
                "meaning": "Giving/Receiving FAVORS (Actions)",
                "structure": "[Verb Te-Form] + [Giving/Receiving Verb]",
                "formation": "Instead of giving physical objects, you put an action verb in the Te-form to give/receive the 'favor' of an action.",
                "why": "This is how Japanese expresses gratitude or the interpersonal dynamics of doing things for others.",
                "formal": "私は木村さんに本を貸してあげました。 (I did the favor of lending...).",
                "casual": "本を貸してあげた。",
                "native": "Using '〜てあげます' directly to a superior sounds arrogant ('I will do you the favor of...'). Better to offer with '〜ましょうか'.",
                "examples": [
                    ("私は山田さんに旅行の写真を見せてもらいました。", "I received the favor of Yamada showing me his photos (Yamada showed me)."),
                    ("母がセーターを送ってくれました。", "My mother did me the favor of sending a sweater (My mother sent me)."),
                ],
                "mistakes": "Misidentifying the subject. In '見せてもらいました', the subject (は) is the RECEIVER of the favor (I). In '見せてくれました', the subject is the GIVER of the favor (Mother).",
                "jlpt": "Parsing who did the action based on the trailing verb."
            }
        ],
        "kanji": [
            ("手", "て", "シュ", "4", "Hand", "A hand.", [("手伝う", "てつだう", "To help"), ("手紙", "てがみ", "Letter")]),
            ("連", "つ", "レン", "10", "Link / Take along", "A vehicle (車) moving along a path (辶).", [("連れて行く", "つれていく", "To take someone along")]),
        ],
        "quiz": [
            {"q": "If Tanaka gives YOU a pen, which verb should you use?", "opts": ["A. あげます (Agemasu)", "B. くれます (Kuremasu)", "C. もらいます (Moraimasu)", "D. 貸します (Kashimasu)"], "ans": "B", "exp": "When someone gives something inward to the speaker, you must use くれます (kuremasu). あげます is for giving outward."},
            {"q": "What does '先生が教えてくれました' mean?", "opts": ["A. I taught the teacher", "B. The teacher received teaching", "C. The teacher kindly taught me", "D. I want to teach the teacher"], "ans": "C", "exp": "教えて (teach) + くれました (gave inward to me). The teacher did me the favor of teaching me."},
        ]
    },
    {
        "num": 25,
        "title": "Conditionals and Concessions",
        "jp_title": "雨が降ったら、行きません",
        "overview": "Learn how to express 'If' (hypotheticals) and 'Even if' (concessions) to master the final, most advanced N5 concepts.",
        "objectives": [
            "Use the Ta-form to create 'If / When' conditional statements (〜たら)",
            "Use the Te-form to create 'Even if' statements (〜ても)",
            "Understand the Nuance of もし (Suppose/If) and いくら (No matter how)"
        ],
        "vocab": [
            ("もし", "もし", "If / In case", "Adverb", "N5", "もし雨が降ったら...", "Moshi ame ga futtara...", "If it happens to rain..."),
            ("いくら", "いくら", "No matter how (much)", "Adverb", "N5", "いくら高くても、買います。", "Ikura takakutemo, kaimasu.", "No matter how expensive it is, I will buy it."),
            ("考える", "かんがえる", "To think / consider", "Verb (Ru)", "N5", "よく考えてください。", "Yoku kangaete kudasai.", "Please consider it carefully."),
            ("頑張る", "がんばる", "To do one's best", "Verb (U)", "N5", "最後まで頑張ります。", "Saigo made ganbarimasu.", "I will do my best until the end."),
            ("お世話になる", "おせわになる", "To be indebted", "Verb Phrase", "N5", "お世話になりました。", "Osewa ni narimashita.", "Thank you for taking care of me."),
        ],
        "grammar": [
            {
                "pattern": "V-たら、〜",
                "meaning": "If / When V happens...",
                "structure": "[Verb Ta-Form] + ら (ra)",
                "formation": "Conjugate the verb into the past tense plain form (Ta-Form) and attach 'ra'.",
                "why": "This is the most versatile conditional in Japanese. It handles both hypotheticals ('If I have money...') and future certainties ('When I get home...').",
                "formal": "お金があったら、旅行します。",
                "casual": "お金があったら、旅行する。",
                "native": "You can add the adverb 'moshi' at the beginning of the sentence to explicitly flag that it is a hypothetical 'if' statement.",
                "examples": [
                    ("もし雨が降ったら、行きません。", "If it rains, I won't go."),
                    ("駅に着いたら、電話してください。", "When you arrive at the station, please call me. (Future certainty)."),
                ],
                "mistakes": "Attaching 'ra' to the present tense (降るら is WRONG). It MUST attach to the past tense (降ったら).",
                "jlpt": "Understanding that 〜たら can mean both 'If' and 'When'."
            },
            {
                "pattern": "V-ても、〜",
                "meaning": "Even if V happens...",
                "structure": "[Verb Te-Form] + も (mo)",
                "formation": "Conjugate the verb into the Te-form and attach 'mo'. For i-adjectives: くて+も. For na-adjs/nouns: で+も.",
                "why": "The particle も means 'also/even'. So literally, 'Even doing V, the result is...'",
                "formal": "雨が降っても、行きます。",
                "casual": "雨が降っても、行く。",
                "native": "Can be paired with the adverb 'ikura' (no matter how much) to strengthen the concession.",
                "examples": [
                    ("いくら考えても、わかりません。", "No matter how much I think about it, I don't understand."),
                    ("安くても、買いません。", "Even if it is cheap, I won't buy it."),
                    ("日曜日でも、働きます。", "Even if it's Sunday, I work."),
                ],
                "mistakes": "Confusing it with the conditional. 〜たら means IF. 〜ても means EVEN IF.",
                "jlpt": "Reading comprehension logic traps. Will they do the action or not?"
            }
        ],
        "kanji": [
            ("考", "かんが", "コウ", "6", "Consider / Think", "An old person (老) leaning on a cane, pondering deeply.", [("考える", "かんがえる", "To consider")]),
            ("終", "おわ", "シュウ", "11", "End / Finish", "Thread (糸) + Winter (冬). The end of the year, tying the thread.", [("終わる", "おわる", "To end/finish"), ("終電", "しゅうでん", "Last train")]),
        ],
        "quiz": [
            {"q": "What is the correct way to say 'If I have time'?", "opts": ["A. 時間があるら", "B. 時間があったら", "C. 時間がありたら", "D. 時間であら"], "ans": "B", "exp": "The Tara-conditional requires the Ta-form (past tense plain form). ある -> あった -> あったら."},
            {"q": "How do you translate 'Even if it is expensive, I will buy it'?", "opts": ["A. 高かったら、買います", "B. 高くても、買います", "C. 高いでも、買います", "D. 高いくても、買います"], "ans": "B", "exp": "The 'even if' form uses the Te-form + mo. For i-adjectives, it is 〜くても. So, 高くても (Takakutemo)."},
        ]
    }
]
