# data_lessons_16_20.py
# Contains first-principles detailed data for Lessons 16 through 20

LESSONS_16_20 = [
    {
        "num": 16,
        "title": "Linking Actions and Adjectives",
        "jp_title": "朝ジョギングをして、シャワーを浴びます",
        "overview": "Learn how to link multiple actions in chronological order and how to combine multiple adjectives to describe something in detail.",
        "objectives": [
            "Link verbs sequentially using the Te-form",
            "Explain the sequence of actions using 〜てから",
            "Combine い-adjectives by dropping い and adding くて",
            "Combine な-adjectives by adding で"
        ],
        "vocab": [
            ("乗る", "のる", "To ride / get on", "Verb (U)", "N5", "電車に乗ります。", "Densha ni norimasu.", "I ride the train."),
            ("降りる", "おりる", "To get off", "Verb (Ru)", "N5", "バスを降ります。", "Basu o orimasu.", "I get off the bus."),
            ("乗り換える", "のりかえる", "To transfer", "Verb (Ru)", "N5", "地下鉄に乗り換えます。", "Chikatetsu ni norikaemasu.", "I transfer to the subway."),
            ("浴びる", "あびる", "To take (a shower)", "Verb (Ru)", "N5", "シャワーを浴びます。", "Shawaa o abimasu.", "I take a shower."),
            ("若い", "わかい", "Young", "I-Adj", "N5", "彼は若くて元気です。", "Kare wa wakakute genki desu.", "He is young and energetic."),
        ],
        "grammar": [
            {
                "pattern": "V1-て、V2-て、V3ます",
                "meaning": "Do V1, then V2, then V3",
                "structure": "[Verb 1 Te-Form]、[Verb 2 Te-Form]、[Verb 3 Tense]",
                "formation": "To list sequential actions, put all verbs in the Te-form except the final one. The final verb determines the tense (past/present/future) of the entire sentence.",
                "why": "The Te-form acts as an 'and then' connector for verbs.",
                "formal": "朝起きて、朝ごはんを食べて、学校へ行きます。",
                "casual": "朝起きて、朝ごはんを食べて、学校へ行く。",
                "native": "You can string as many verbs as you want, but practically native speakers rarely string more than three.",
                "examples": [
                    ("昨日、神戸へ行って、映画を見て、お茶を飲みました。", "Yesterday, I went to Kobe, watched a movie, and drank tea."),
                ],
                "mistakes": "Conjugating the middle verbs into the past tense. DO NOT do this. Only the very last verb gets the past tense: 行きました.",
                "jlpt": "Sequence of events in reading/listening."
            },
            {
                "pattern": "V1-て から、V2ます",
                "meaning": "After doing V1, do V2",
                "structure": "[Verb 1 Te-Form] から、[Verb 2]",
                "formation": "Attach から directly to the Te-form.",
                "why": "から means 'from'. So literally, 'From the point of doing V1, I do V2'.",
                "formal": "仕事が終わってから、飲みに行きます。",
                "casual": "仕事が終わってから、飲みに行く。",
                "native": "This strongly emphasizes that V2 CANNOT happen until V1 is completely finished.",
                "examples": [
                    ("手を洗ってから、ごはんを食べます。", "After washing my hands, I eat a meal."),
                ],
                "mistakes": "Confusing it with the 'Reason' から. If から is attached to a Te-form verb, it means 'After'. If it's attached to a normal sentence end (like ですから), it means 'Because'.",
                "jlpt": "Differentiating Te-kara (after) vs Desu-kara (because)."
            },
            {
                "pattern": "A1-くて / A1-で、A2",
                "meaning": "Is A1 and A2",
                "structure": "[i-Adj minus 'i' + くて] OR [na-Adj + で] + [Next Adjective]",
                "formation": "To link adjectives with 'and', you cannot use 'と'. For い-adjectives, drop the い and add くて. For な-adjectives, attach で.",
                "why": "Just like verbs need the Te-form to connect, adjectives have their own 'Te-form' connectors (くて/で).",
                "formal": "東京は大きくて、にぎやかです。",
                "casual": "東京は大きくて、にぎやかだ。",
                "native": "The adjectives should generally match in tone. Don't link a highly positive adjective with a highly negative one this way (use が/but instead).",
                "examples": [
                    ("この部屋は狭くて、暗いです。", "This room is narrow and dark."),
                    ("ミラーさんはハンサムで、親切です。", "Mr. Miller is handsome and kind."),
                ],
                "mistakes": "Using と to link adjectives. '大きいと高いです' is strictly WRONG. It must be '大きくて、高いです'.",
                "jlpt": "Adjective conjunction is a guaranteed N5 grammar question."
            }
        ],
        "kanji": [
            ("朝", "あさ", "チョウ", "12", "Morning", "Sun/Moon rising over the mist.", [("朝", "あさ", "Morning"), ("毎朝", "まいあさ", "Every morning")]),
            ("昼", "ひる", "チュウ", "9", "Noon / Daytime", "A sun with rays shining down.", [("昼休み", "ひるやすみ", "Lunch break"), ("昼ごはん", "ひるごはん", "Lunch")]),
        ],
        "quiz": [
            {"q": "How do you link 'It is cheap (安い) and delicious (美味しい)'?", "opts": ["A. 安いと美味しいです", "B. 安いて美味しいです", "C. 安くて美味しいです", "D. 安いで美味しいです"], "ans": "C", "exp": "安い is an i-adjective. To link i-adjectives, drop the 'i' and add 'kute' (安くて)."},
            {"q": "What does 終わってから mean?", "opts": ["A. Because it finished", "B. After finishing", "C. Even if it finishes", "D. Before finishing"], "ans": "B", "exp": "Te-form + から means 'after doing' the action."},
        ]
    },
    {
        "num": 17,
        "title": "The Nai-Form and Obligations",
        "jp_title": "ここで写真を撮らないでください",
        "overview": "Learn how to construct the Nai-form (the negative dictionary form), and use it to ask people not to do things, or to state what you must do.",
        "objectives": [
            "Master the Nai-Form conjugation rules for all 3 Verb Groups",
            "Politely ask someone not to do something using 〜ないでください",
            "Express obligation (must do) using 〜なければなりません",
            "Express lack of obligation (don't have to) using 〜なくてもいいです"
        ],
        "vocab": [
            ("忘れる", "わすれる", "To forget", "Verb (Ru)", "N5", "パスポートを忘れないでください。", "Pasupooto o wasurenaide kudasai.", "Please do not forget your passport."),
            ("払う", "はらう", "To pay", "Verb (U)", "N5", "お金を払わなければなりません。", "Okane o harawanakereba narimasen.", "I must pay the money."),
            ("返す", "かえす", "To return (an object)", "Verb (U)", "N5", "本を返さなければなりません。", "Hon o kaesanakereba narimasen.", "I must return the book."),
            ("脱ぐ", "ぬぐ", "To take off (shoes/clothes)", "Verb (U)", "N5", "靴を脱いでください。", "Kutsu o nuide kudasai.", "Please take off your shoes."),
            ("薬", "くすり", "Medicine", "Noun", "N5", "薬を飲まなければなりません。", "Kusuri o nomanakereba narimasen.", "I must take medicine."),
        ],
        "grammar": [
            {
                "pattern": "V-ないで ください",
                "meaning": "Please don't do V",
                "structure": "[Verb Nai-Form] + で + ください",
                "formation": "To make the Nai-form: For Group 2, change る to ない. For Group 3, する→しない, くる→こない. For Group 1, change the final 'u' sound to the 'a' sound of the same column, and add ない. Example: かく→かかない.",
                "why": "This is the negative equivalent of V-て ください.",
                "formal": "ここでタバコを吸わないでください。",
                "casual": "ここでタバコを吸わないで。 (Drop kudasai).",
                "native": "Remember the Group 1 'U' exception: 買う (kau) becomes 買わない (kawanai), NOT kaanai.",
                "examples": [
                    ("心配しないでください。", "Please don't worry."),
                    ("あの部屋に入らないでください。", "Please do not enter that room."),
                ],
                "mistakes": "Conjugating Group 1 verbs ending in う into あ. It MUST become わ.",
                "jlpt": "Group 1 Nai-form conjugation is a massive test target."
            },
            {
                "pattern": "V-なければ なりません",
                "meaning": "Must do V",
                "structure": "[Verb Nai-Form minus 'i'] + ければ なりません",
                "formation": "Drop the 'i' from the Nai-form, and attach 'kereba narimasen'.",
                "why": "This is a massive double negative. 'Nakereba' = If I don't do it. 'Narimasen' = It will not become/go well. Literally: 'If I don't do it, things will be bad' -> I must do it.",
                "formal": "明日、病院へ行かなければなりません。",
                "casual": "明日、病院へ行かなきゃ。 (Shortened native spoken form).",
                "native": "In textbooks it is long and rigid, but in real life natives shorten it to 'nakya' or 'nakucha'.",
                "examples": [
                    ("薬を飲まなければなりません。", "I must take my medicine."),
                    ("宿題をしなければなりません。", "I must do my homework."),
                ],
                "mistakes": "Forgetting the double negative structure. It feels very long to English speakers.",
                "jlpt": "Tested heavily in reading to see if you understand what the subject is forced to do."
            },
            {
                "pattern": "V-なくても いいです",
                "meaning": "Don't have to do V",
                "structure": "[Verb Nai-Form minus 'i'] + くても いいです",
                "formation": "Drop the 'i' from the Nai-form, and attach 'kutemo ii desu'.",
                "why": "Literally: 'Even if I don't do it, it is good/fine.'",
                "formal": "明日来なくてもいいです。",
                "casual": "明日来なくてもいいよ。",
                "native": "The direct opposite of なければなりません.",
                "examples": [
                    ("急がなくてもいいです。", "You don't have to hurry."),
                    ("靴を脱がなくてもいいですか。", "Is it okay if I don't take off my shoes?"),
                ],
                "mistakes": "Mixing up the endings. なければ = MUST. なくても = DON'T HAVE TO.",
                "jlpt": "Classic listening trap: The boss tells the worker they 'don't have to' do something today. The question asks what the worker will do today."
            }
        ],
        "kanji": [
            ("夜", "よる", "ヤ", "8", "Night", "A person under a roof at night.", [("夜", "よる", "Night"), ("今夜", "こんや", "Tonight")]),
            ("勉", "べん", "ベン", "10", "Exertion / Study", "Contains the radical for power/strength (力). Study requires exertion.", [("勉強", "べんきょう", "Study")]),
        ],
        "quiz": [
            {"q": "What is the correct Nai-form of 買う (kau - to buy)?", "opts": ["A. かあない", "B. かうない", "C. かわない", "D. かえない"], "ans": "C", "exp": "Group 1 verbs ending in う (u) are the big exception. They change to わ (wa), not あ (a)."},
            {"q": "Which phrase means 'I don't have to go'?", "opts": ["A. 行かなければなりません", "B. 行かなくてもいいです", "C. 行かないでください", "D. 行ってはいけません"], "ans": "B", "exp": "〜なくてもいいです literally means 'even if I don't, it is fine', which translates to 'don't have to'."},
        ]
    },
    {
        "num": 18,
        "title": "The Dictionary Form and Potential",
        "jp_title": "漢字を読むことができます",
        "overview": "Learn how to use the raw Dictionary Form of verbs to express hobbies, abilities, and actions before a specific time.",
        "objectives": [
            "Use the Dictionary Form to express potential (can do) with 〜ことができます",
            "State your hobby using 趣味は 〜ことです",
            "Express actions done *before* something else using 〜前に"
        ],
        "vocab": [
            ("できる", "できる", "To be able to / can", "Verb (Ru)", "N5", "日本語ができます。", "Nihongo ga dekimasu.", "I can do Japanese."),
            ("弾く", "ひく", "To play (a stringed instrument)", "Verb (U)", "N5", "ピアノを弾くことができます。", "Piano o hiku koto ga dekimasu.", "I can play the piano."),
            ("歌う", "うたう", "To sing", "Verb (U)", "N5", "歌を歌います。", "Uta o utaimasu.", "I sing a song."),
            ("趣味", "しゅみ", "Hobby", "Noun", "N5", "趣味は読書です。", "Shumi wa dokusho desu.", "My hobby is reading."),
            ("前", "まえ", "Before", "Noun", "N5", "寝る前に本を読みます。", "Neru mae ni hon o yomimasu.", "I read a book before sleeping."),
        ],
        "grammar": [
            {
                "pattern": "V-る ことが できます",
                "meaning": "Can do V / Able to do V",
                "structure": "[Verb Dictionary Form] + ことが できます",
                "formation": "You must use the raw dictionary form (e.g., 食べる, 読む, 書く). The word こと turns the verb phrase into a noun ('the act of'). Then you add ができます (is doable).",
                "why": "In Japanese, you cannot attach 'dekimasu' directly to a verb. You must nounify the verb first using こと.",
                "formal": "私は漢字を読むことができます。",
                "casual": "漢字を読むことができる。 (Or just use the short potential form taught in N4).",
                "native": "For nouns that inherently imply action (like 運転 - driving, or スキー - skiing), you can skip the こと and just say: 運転ができます。",
                "examples": [
                    ("ミラーさんは日本語を話すことができます。", "Mr. Miller can speak Japanese."),
                    ("ここで写真を撮ることができますか。", "Can I take pictures here? (Permission/Ability)."),
                ],
                "mistakes": "Trying to say '読みますことができます'. WRONG. You MUST use the raw dictionary form before こと.",
                "jlpt": "Knowing to use the dictionary form."
            },
            {
                "pattern": "趣味は V-る ことです",
                "meaning": "My hobby is doing V",
                "structure": "趣味 (shumi) は [Verb Dictionary Form] + ことです。",
                "formation": "Again, こと acts as a nominalizer (noun-maker).",
                "why": "You cannot say 'My hobby is to read' directly. You must say 'My hobby is the ACT OF reading'.",
                "formal": "私の趣味は映画を見ることです。",
                "casual": "趣味は映画を見ること。",
                "native": "If your hobby is just a noun (like Sports), you do not need こと: 趣味はスポーツです。",
                "examples": [
                    ("趣味は写真を撮ることです。", "My hobby is taking pictures."),
                ],
                "mistakes": "Forgetting the こと. '趣味は映画を見ます' is grammatically broken.",
                "jlpt": "Nounification concepts."
            },
            {
                "pattern": "V1-る 前に、V2",
                "meaning": "Before doing V1, do V2",
                "structure": "[Verb 1 Dictionary Form] 前に (mae ni)、[Verb 2]",
                "formation": "Dictionary form + mae ni.",
                "why": "Before (前) is a noun. Verbs modifying nouns must be in the plain/dictionary form.",
                "formal": "日本へ来る前に、日本語を勉強しました。",
                "casual": "日本へ来る前に、日本語を勉強した。",
                "native": "You can also use nouns with 'no' (食事の前に = before the meal) or specific time quantities (5年前に = 5 years ago).",
                "examples": [
                    ("寝る前に、本を読みます。", "Before sleeping, I read a book."),
                ],
                "mistakes": "Using the past tense before 前に. '来た前に' is WRONG. It must always be the dictionary form: '来る前に'.",
                "jlpt": "Contrasting 〜てから (after) with 〜前に (before)."
            }
        ],
        "kanji": [
            ("書", "か", "ショ", "10", "Write", "A hand holding a brush over a document.", [("書く", "かく", "To write"), ("辞書", "じしょ", "Dictionary")]),
            ("読", "よ", "ドク", "14", "Read", "Words (言) being sold (売) -> reading out loud.", [("読む", "よむ", "To read"), ("読書", "どくしょ", "Reading as a hobby")]),
        ],
        "quiz": [
            {"q": "What is the purpose of the word こと (koto) in '食べる ことができます'?", "opts": ["A. It means 'because'", "B. It means 'after'", "C. It turns the verb into a noun ('the act of')", "D. It is a polite filler word"], "ans": "C", "exp": "こと is a nominalizer. It turns 'to eat' into 'the act of eating' so it can act as the subject of the sentence."},
            {"q": "Which sentence is grammatically correct?", "opts": ["A. 寝た前に本を読む", "B. 寝て前に本を読む", "C. 寝る前に本を読む", "D. 寝ます前に本を読む"], "ans": "C", "exp": "前に MUST be preceded by the raw Dictionary Form of the verb (寝る)."},
        ]
    },
    {
        "num": 19,
        "title": "The Ta-Form and Experiences",
        "jp_title": "相撲を見たことがあります",
        "overview": "Learn how to use the Ta-Form (the past tense dictionary form) to talk about your life experiences and give advice.",
        "objectives": [
            "Conjugate verbs into the Ta-Form",
            "Talk about life experiences using 〜たことがあります",
            "List non-sequential examples of actions using 〜たり 〜たり します",
            "Give advice using 〜たほうがいいです (Bonus)"
        ],
        "vocab": [
            ("相撲", "すもう", "Sumo", "Noun", "N5", "相撲を見たことがありますか。", "Sumou o mita koto ga arimasu ka.", "Have you ever seen sumo?"),
            ("登る", "のぼる", "To climb", "Verb (U)", "N5", "山に登りました。", "Yama ni noborimashita.", "I climbed the mountain."),
            ("泊まる", "とまる", "To stay (at a hotel)", "Verb (U)", "N5", "ホテルに泊まります。", "Hoteru ni tomarimasu.", "I stay at a hotel."),
            ("掃除する", "そうじする", "To clean", "Verb (Irregular)", "N5", "部屋を掃除します。", "Heya o souji shimasu.", "I clean the room."),
            ("洗濯する", "せんたくする", "To wash clothes", "Verb (Irregular)", "N5", "服を洗濯します。", "Fuku o sentaku shimasu.", "I wash the clothes."),
        ],
        "grammar": [
            {
                "pattern": "V-た ことが あります",
                "meaning": "Have the experience of doing V",
                "structure": "[Verb Ta-Form] + ことが あります",
                "formation": "To make the Ta-form, just apply the exact same conjugation rules as the Te-form, but replace 'te/de' with 'ta/da'. Example: たべて→たべた, のんで→のんだ. Then attach ことがあります.",
                "why": "Literally: 'The act of having done V exists.'",
                "formal": "私は日本へ行ったことがあります。",
                "casual": "日本へ行ったことがある。",
                "native": "Only used for distinct life experiences. Do not use this for things you did yesterday. ('I have the experience of eating breakfast yesterday' sounds insane in Japanese).",
                "examples": [
                    ("馬に乗ったことがありますか。", "Have you ever ridden a horse?"),
                    ("一度もありません。", "Not even once."),
                ],
                "mistakes": "Using the present tense. '行くことがあります' means 'There are times when I go'. '行ったことがあります' means 'I have the experience of going'.",
                "jlpt": "Differentiating between daily actions and life experiences."
            },
            {
                "pattern": "V1-たり、V2-たり します",
                "meaning": "Do things like V1 and V2",
                "structure": "[Verb 1 Ta-Form] り、[Verb 2 Ta-Form] り します",
                "formation": "Ta-form + ri. You must ALWAYS end the sentence with 'shimasu' (to do).",
                "why": "Unlike the Te-form (which lists actions in chronological order), the Tari-form implies 'I did various things, such as V1 and V2, among others, in no particular order'.",
                "formal": "日曜日は買い物をしたり、映画を見たりします。",
                "casual": "日曜日は買い物をしたり、映画を見たりする。",
                "native": "The final 'shimasu' defines the tense. To say you DID these things yesterday, use 'shimashita'.",
                "examples": [
                    ("昨日、本を読んだり、手紙を書いたりしました。", "Yesterday, I did things like read a book and write a letter."),
                ],
                "mistakes": "Forgetting the final 'shimasu'. '読んだり、書いたり。' is incomplete and grammatically dangling.",
                "jlpt": "Te-form (chronological sequence) vs Tari-form (random examples)."
            }
        ],
        "kanji": [
            ("山", "やま", "サン", "3", "Mountain", "A pictogram of three mountain peaks.", [("山", "やま", "Mountain"), ("富士山", "ふじさん", "Mt. Fuji")]),
            ("川", "かわ", "セン", "3", "River", "A pictogram of a flowing river.", [("川", "かわ", "River"), ("小川", "おがわ", "Stream")]),
        ],
        "quiz": [
            {"q": "What is the Ta-form of 飲む (nomu - to drink)?", "opts": ["A. のんで", "B. のんだ", "C. のった", "D. のまた"], "ans": "B", "exp": "The Ta-form is identical to the Te-form, just swap 'te/de' with 'ta/da'. のむ → のんで → のんだ."},
            {"q": "Which structure should you use to talk about what you did on the weekend in no particular order?", "opts": ["A. 〜て、〜て", "B. 〜たり、〜たりします", "C. 〜たことがあります", "D. 〜てから"], "ans": "B", "exp": "The Tari-form is used to list representative, non-sequential examples of actions."},
        ]
    },
    {
        "num": 20,
        "title": "Plain Style and Casual Speech",
        "jp_title": "明日東京へ行く？",
        "overview": "Learn how to drop the polite 'Masu/Desu' and speak in the Plain Style (dictionary/casual forms) used with friends and family.",
        "objectives": [
            "Understand the difference between Polite Style and Plain Style",
            "Convert Desu into Da",
            "Convert Masu into Dictionary Form",
            "Convert Masen into Nai-Form",
            "Convert Mashita into Ta-Form",
            "Convert Masendeshita into Nakatta-Form"
        ],
        "vocab": [
            ("言葉", "ことば", "Word / Language", "Noun", "N5", "言葉がわかりません。", "Kotoba ga wakarimasen.", "I don't understand the word."),
            ("物価", "ぶっか", "Prices (of goods)", "Noun", "N5", "日本の物価は高いです。", "Nihon no bukka wa takai desu.", "Prices in Japan are high."),
            ("ビザ", "ビザ", "Visa", "Noun", "N5", "ビザが要ります。", "Biza ga irimasu.", "I need a visa."),
            ("要る", "いる", "To need", "Verb (U)", "N5", "お金が要ります。", "Okane ga irimasu.", "I need money."),
            ("ううん", "ううん", "No (Casual)", "Interjection", "N5", "ううん、行かない。", "Uun, ikanai.", "Nah, I won't go."),
            ("うん", "うん", "Yes (Casual)", "Interjection", "N5", "うん、行く。", "Un, iku.", "Yeah, I'll go."),
        ],
        "grammar": [
            {
                "pattern": "Polite vs Plain Style",
                "meaning": "Using dictionary forms instead of Masu/Desu",
                "structure": "Replacing the formal wrapper with raw grammatical forms.",
                "formation": "1. Present (+): ます → Dictionary Form. \n2. Present (-): ません → Nai-Form. \n3. Past (+): ました → Ta-Form. \n4. Past (-): ませんでした → Nakatta-Form. \n5. Noun/Na-Adj: です → だ.",
                "why": "Polite style builds a social wall of respect. Plain style drops the wall for intimacy and speed.",
                "formal": "明日、東京へ行きますか。 (Are you going to Tokyo tomorrow?)",
                "casual": "明日、東京へ行く？ (You going to Tokyo tomorrow?)",
                "native": "In Plain style questions, the particle 'か' is entirely dropped. You simply raise your intonation at the end of the sentence.",
                "examples": [
                    ("Polite: 毎日忙しいですか。 -> Plain: 毎日忙しい？", "Are you busy every day?"),
                    ("Polite: 食べませんでした。 -> Plain: 食べなかった。", "I didn't eat."),
                ],
                "mistakes": "Mixing polite and plain styles in the same sentence. It sounds extremely unnatural.",
                "jlpt": "Reading comprehension passages are almost always written in the Plain Style."
            },
            {
                "pattern": "Noun/Na-Adj Past Tense (Plain)",
                "meaning": "Was / Was not",
                "structure": "Polite: でした -> Plain: だった \n Polite: ではありませんでした -> Plain: じゃなかった",
                "formation": "This is how you casually state the past tense of nouns and na-adjectives.",
                "why": "This is foundational for advanced grammar in N4, where you must attach plain-form sentences to other grammatical structures.",
                "formal": "昨日は休みでした。",
                "casual": "昨日は休みだった。",
                "native": "Often followed by particle 'yo' or 'ne' to soften it: 休みだったよ。",
                "examples": [
                    ("Polite: 静かではありませんでした。 -> Plain: 静かじゃなかった。", "It wasn't quiet."),
                ],
                "mistakes": "Applying 'katta' to nouns. '休みかった' is WRONG. It must be '休みだった'.",
                "jlpt": "Recognizing 'datta' as the past tense of 'da/desu'."
            }
        ],
        "kanji": [
            ("言", "い / こと", "ゲン / ゴン", "7", "Say / Word", "Lines coming out of a mouth (口).", [("言う", "いう", "To say"), ("言葉", "ことば", "Word/Language")]),
            ("休", "やす", "キュウ", "6", "Rest", "A person (亻) leaning against a tree (木) to rest.", [("休む", "やすむ", "To rest"), ("休み", "やすみ", "Holiday/Break")]),
        ],
        "quiz": [
            {"q": "What is the Plain (casual) form of 食べませんでした (Did not eat)?", "opts": ["A. 食べない", "B. 食べた", "C. 食べなかった", "D. 食べだ"], "ans": "C", "exp": "The Nai-form of taberu is tabenai. The past tense of the Nai-form drops 'i' and adds 'katta' -> tabenakatta."},
            {"q": "How do you turn a Plain sentence into a question?", "opts": ["A. Add か at the end", "B. Add だ at the end", "C. Drop the particle and raise your intonation", "D. Add ですか at the end"], "ans": "C", "exp": "In casual speech, the question particle か is dropped, and the sentence ends with a rising intonation (e.g., 食べる？)."},
        ]
    }
]

# Dummy lessons for 21-25
for i in range(21, 26):
    LESSONS_16_20.append({
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
