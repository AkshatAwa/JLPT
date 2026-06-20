"""
JLPT N5 Practice Test Data
Genuine N5-level questions across grammar, vocabulary, kanji, and reading.
"""

N5_TESTS = [
    {
        "id": "grammar_test_1",
        "title": "Grammar & Particles",
        "icon": "📝",
        "color": "#3B82F6",
        "description": "Test your understanding of N5 grammar patterns and particles.",
        "questions": [
            {
                "q": "田中さんは毎朝コーヒー＿＿飲みます。",
                "opts": ["A. が", "B. を", "C. に", "D. は"],
                "ans": "B",
                "exp": "を is the direct object marker. Coffee (コーヒー) is the object being drunk. が marks subjects/ability, に marks targets/locations."
            },
            {
                "q": "私は昨日、友達＿＿手紙を書きました。",
                "opts": ["A. を", "B. が", "C. に", "D. で"],
                "ans": "C",
                "exp": "に marks the RECEIVER of an action. You write a letter TO a friend. 友達に手紙を書く = to write a letter to a friend."
            },
            {
                "q": "図書館＿＿本を読みます。",
                "opts": ["A. に", "B. を", "C. で", "D. が"],
                "ans": "C",
                "exp": "で marks the LOCATION OF AN ACTION. You 'do' something at/in a place. に marks existence (something IS there). Reading (action) → で."
            },
            {
                "q": "明日、東京＿＿行きます。",
                "opts": ["A. で", "B. に", "C. が", "D. も"],
                "ans": "B",
                "exp": "に (or へ) marks the DESTINATION of movement verbs like 行く, 来る, 帰る. 東京に行く = Go to Tokyo."
            },
            {
                "q": "寝る＿＿、歯を磨きます。",
                "opts": ["A. あとで", "B. まえに", "C. てから", "D. ながら"],
                "ans": "B",
                "exp": "まえに (before) takes the DICTIONARY FORM of the verb. 寝る (dictionary form) + まえに = before sleeping. Note: あとで takes the た-form."
            },
            {
                "q": "この仕事は＿＿なければなりません。",
                "opts": ["A. し", "B. しない", "C. して", "D. する"],
                "ans": "A",
                "exp": "なければなりません (must do) attaches to the NAI-stem. する → しない → し + なければなりません. So: しなければなりません (must do it)."
            },
            {
                "q": "もっとゆっくり話し＿＿ください。",
                "opts": ["A. て", "B. た", "C. で", "D. に"],
                "ans": "A",
                "exp": "〜てください (please do ~) uses the TE-FORM + ください. 話す → 話して → 話してください."
            },
            {
                "q": "ここで写真を撮っ＿＿もいいですか。",
                "opts": ["A. た", "B. て", "C. で", "D. に"],
                "ans": "B",
                "exp": "〜てもいいです (may I / it's okay to) uses the TE-FORM. 撮る → 撮って → 撮ってもいいですか = May I take a photo?"
            },
            {
                "q": "電車の中でタバコを吸っ＿＿いけません。",
                "opts": ["A. てで", "B. てに", "C. ては", "D. てを"],
                "ans": "C",
                "exp": "〜てはいけません (must not / prohibited) uses TE-FORM + は + いけません. 吸って + は + いけません = must not smoke."
            },
            {
                "q": "私は日本語を話す＿＿ができます。",
                "opts": ["A. の", "B. こと", "C. もの", "D. ところ"],
                "ans": "B",
                "exp": "〜ことができます (can do / ability) uses DICTIONARY FORM + こと + が + できます. こと nominalizes the verb phrase."
            },
            {
                "q": "夏＿＿冬のほうが好きです。",
                "opts": ["A. より", "B. ほど", "C. くらい", "D. まで"],
                "ans": "A",
                "exp": "AよりBのほうが好き = I like B more than A. より marks the item being compared against (the lesser one). So 夏より冬のほうが好き = I like winter more than summer."
            },
            {
                "q": "今、雨が降っ＿＿います。",
                "opts": ["A. た", "B. て", "C. で", "D. に"],
                "ans": "B",
                "exp": "〜ています (ongoing action/state) uses the TE-FORM + います. 降る → 降って → 降っています = It is raining right now."
            },
            {
                "q": "彼女に本を＿＿ました。（She gave me the book）",
                "opts": ["A. あげ", "B. もらい", "C. くれ", "D. やり"],
                "ans": "C",
                "exp": "くれる is used when someone GIVES TO THE SPEAKER. 彼女が（私に）本をくれた = She gave me the book. あげる = speaker gives outward. もらう = speaker receives."
            },
            {
                "q": "来年、日本に行く＿＿です。",
                "opts": ["A. はず", "B. つもり", "C. ため", "D. ので"],
                "ans": "B",
                "exp": "〜つもりです (intend to / plan to) uses DICTIONARY FORM + つもりです. Expresses the speaker's personal intention."
            },
            {
                "q": "音楽を聴き＿＿、勉強します。",
                "opts": ["A. ながら", "B. てから", "C. あとで", "D. まえに"],
                "ans": "A",
                "exp": "〜ながら (while doing ~) uses the MASU-STEM + ながら. 聴く → 聴き + ながら = while listening. Both actions happen simultaneously by the same person."
            },
        ]
    },
    {
        "id": "vocab_test_1",
        "title": "Vocabulary",
        "icon": "📚",
        "color": "#10B981",
        "description": "Test your N5 vocabulary knowledge.",
        "questions": [
            {
                "q": "「急ぐ」の意味は何ですか。\nWhat does 急ぐ mean?",
                "opts": ["A. To walk slowly", "B. To hurry / To rush", "C. To wait", "D. To stop"],
                "ans": "B",
                "exp": "急ぐ (いそぐ - isogu) means 'to hurry' or 'to rush'. Used as: 急いでください (Please hurry)."
            },
            {
                "q": "「電車」の読み方は？",
                "opts": ["A. でんきゃ", "B. でんちゃ", "C. でんしゃ", "D. てんしゃ"],
                "ans": "C",
                "exp": "電車 = でんしゃ (densha) = Train. 電 (den = electricity) + 車 (sha = vehicle)."
            },
            {
                "q": "「先週」はいつですか。",
                "opts": ["A. Next week", "B. This week", "C. Last week", "D. Every week"],
                "ans": "C",
                "exp": "先週 (せんしゅう - senshuu) = Last week. 先 means 'previous/before'. 来週 = next week, 今週 = this week, 毎週 = every week."
            },
            {
                "q": "「にぎやか」の反対は？\nThe opposite of にぎやか (lively)?",
                "opts": ["A. きれい", "B. しずか", "C. ゆうめい", "D. べんり"],
                "ans": "B",
                "exp": "しずか (静か - shizuka) = quiet / peaceful. The opposite of にぎやか (lively/bustling). Both are na-adjectives."
            },
            {
                "q": "「もらう」の丁寧形は？\nThe polite form of もらう?",
                "opts": ["A. もらいます", "B. くれます", "C. あげます", "D. おくります"],
                "ans": "A",
                "exp": "もらう → もらいます (masu-form). This means 'to receive'. 私は先生に本をもらいました = I received a book from the teacher."
            },
            {
                "q": "「暑い」vs「熱い」の違いは？\nDifference between 暑い and 熱い?",
                "opts": ["A. Both mean 'cold'", "B. 暑い = weather hot, 熱い = object hot", "C. 暑い = object hot, 熱い = weather hot", "D. Same meaning, different kanji only"],
                "ans": "B",
                "exp": "暑い (あつい) = hot weather / hot day. 熱い (あつい) = hot to touch (food, liquid, object). Same reading, different meaning!"
            },
            {
                "q": "「〜ています」の用法ではないものは？\nWhich is NOT a use of 〜ています?",
                "opts": ["A. Current ongoing action (今、食べています)", "B. Habitual action (毎日走っています)", "C. Future action (明日行っています)", "D. Resulting state (結婚しています)"],
                "ans": "C",
                "exp": "〜ています is NOT used for future actions. Future is expressed with the plain ます-form. ています has 4 uses: current action, habit, resulting state, occupation."
            },
            {
                "q": "「〜たことがあります」 means?",
                "opts": ["A. I am doing ~", "B. I will do ~", "C. I have done ~ before (experience)", "D. I must do ~"],
                "ans": "C",
                "exp": "〜たことがあります = 'I have ~ before' (experience). Uses TA-FORM + こと + が + あります. 日本に行ったことがあります = I have been to Japan before."
            },
        ]
    },
    {
        "id": "kanji_test_1",
        "title": "Kanji Reading",
        "icon": "🈶",
        "color": "#8B5CF6",
        "description": "Test your JLPT N5 kanji reading ability.",
        "questions": [
            {
                "q": "「山」の読み方は？\nHow do you read 山?",
                "opts": ["A. かわ", "B. やま", "C. うみ", "D. はな"],
                "ans": "B",
                "exp": "山 = やま (yama) = Mountain. ON reading: さん (san) as in 富士山 (ふじさん). KUN reading: やま used alone."
            },
            {
                "q": "「日曜日」の読み方は？",
                "opts": ["A. げつようび", "B. にちようび", "C. かようび", "D. もくようび"],
                "ans": "B",
                "exp": "日曜日 = にちようび (nichiyoubi) = Sunday. 日 = sun/day, 曜 = day of week, 日 = day."
            },
            {
                "q": "「百」は何ですか？",
                "opts": ["A. 10", "B. 1,000", "C. 100", "D. 10,000"],
                "ans": "C",
                "exp": "百 (ひゃく - hyaku) = 100. 千 (せん - sen) = 1,000. 万 (まん - man) = 10,000."
            },
            {
                "q": "「食べる」の kanji の読み方は？",
                "opts": ["A. のむ", "B. かく", "C. たべる", "D. みる"],
                "ans": "C",
                "exp": "食べる = たべる (taberu) = To eat. The kanji 食 has ON reading: ショク (shoku) as in 食事 (meal), 食堂 (cafeteria)."
            },
            {
                "q": "「何時に起きますか」\nWhat does this sentence ask?",
                "opts": ["A. Where do you wake up?", "B. What time do you wake up?", "C. When did you sleep?", "D. Who woke up?"],
                "ans": "B",
                "exp": "何時 (なんじ - nanji) = What time. 起きます = wake up. So: What time do you wake up? 何時 uses 何 (what) + 時 (o'clock)."
            },
            {
                "q": "「大学生」を正しく読んでください。",
                "opts": ["A. ちゅうがくせい", "B. しょうがくせい", "C. だいがくせい", "D. こうこうせい"],
                "ans": "C",
                "exp": "大学生 = だいがくせい (daigakusei) = University student. 大 (大きい = big) + 学 (gaku = study) + 生 (sei = person/student)."
            },
            {
                "q": "「右」と「左」— which means RIGHT?",
                "opts": ["A. 左", "B. 右", "C. Both are the same", "D. Neither"],
                "ans": "B",
                "exp": "右 (みぎ - migi) = Right. 左 (ひだり - hidari) = Left. Memory trick: 右 has a shorter left stroke = right is shorter stroke side."
            },
            {
                "q": "「今月」はいつですか？",
                "opts": ["A. Last month", "B. Next month", "C. This month", "D. Every month"],
                "ans": "C",
                "exp": "今月 (こんげつ - kongetsu) = This month. 今 (ima/kon = now/this) + 月 (tsuki/getsu = month). 先月 = last month, 来月 = next month."
            },
        ]
    },
    {
        "id": "sentence_test_1",
        "title": "Sentence Comprehension",
        "icon": "💬",
        "color": "#F59E0B",
        "description": "Choose the correct sentence or fill in the blank — N5 level comprehension.",
        "questions": [
            {
                "q": "Which sentence is CORRECT?",
                "opts": [
                    "A. 私は日本語が好きです。",
                    "B. 私は日本語を好きです。",
                    "C. 私は日本語に好きです。",
                    "D. 私は日本語で好きです。"
                ],
                "ans": "A",
                "exp": "好き (like) requires the particle が for the thing you like. 私は日本語が好きです = I like Japanese. NEVER を with 好き."
            },
            {
                "q": "「水しか飲みません」の意味は？",
                "opts": [
                    "A. I drink only water (neutral)",
                    "B. I drink only water (implying nothing else, perhaps disappointment)",
                    "C. I don't drink water",
                    "D. I also drink water"
                ],
                "ans": "B",
                "exp": "しか〜ない = 'nothing but, only' with an implication of insufficiency or exclusivity. It ALWAYS requires a negative verb. Contrast: 水だけ飲みます (neutral 'only water')."
            },
            {
                "q": "Choose the sentence with the correct verb form:\n友達に本を___もらいました。",
                "opts": ["A. あげて", "B. くれて", "C. もらって", "D. かして"],
                "ans": "A",
                "exp": "Wait — this is actually a tricky question! 友達に本をあげてもらいました = I had my friend give me a book (I received the favor of giving). The te-form of あげる + もらいます = to have someone do something for you."
            },
            {
                "q": "「田中さんは来ないかもしれません」means?",
                "opts": [
                    "A. Tanaka-san will definitely come",
                    "B. Tanaka-san probably won't come (certain)",
                    "C. Tanaka-san might not come (uncertain)",
                    "D. Tanaka-san must not come"
                ],
                "ans": "C",
                "exp": "かもしれません = 'might / may' expressing possibility and uncertainty. It's less certain than でしょう. 来ない + かもしれません = might not come."
            },
            {
                "q": "Which particle correctly completes: バス＿＿学校まで行きます。",
                "opts": ["A. を", "B. に", "C. で", "D. が"],
                "ans": "C",
                "exp": "で marks the MEANS OF TRANSPORTATION. バスで = by bus. バスを is wrong (を is for direct object/path walked). バスに = on the bus (location), not means."
            },
            {
                "q": "「毎朝、ジョギングしています」means?",
                "opts": [
                    "A. I am jogging right now",
                    "B. I jog every morning (habitual)",
                    "C. I jogged this morning (past)",
                    "D. I will jog every morning"
                ],
                "ans": "B",
                "exp": "毎朝 (every morning) + 〜ています = habitual action. When 〜ています is used with frequency words like 毎日, 毎朝, it means a HABIT, not a current ongoing action."
            },
            {
                "q": "Pick the correct sentence for 'I want to go to Japan':",
                "opts": [
                    "A. 日本へ行きたいです。",
                    "B. 日本へ行きほしいです。",
                    "C. 日本へ行くほしいです。",
                    "D. 日本へ行きたがります。"
                ],
                "ans": "A",
                "exp": "たいです (want to DO) = masu-stem + たいです. 行く → 行き + たいです = want to go. ほしいです is for THINGS (nouns), not actions. たがります is for third-person desire."
            },
            {
                "q": "「宿題をしたあとで、ゲームをします」— What happens first?",
                "opts": [
                    "A. Playing games",
                    "B. Doing homework",
                    "C. Both at the same time",
                    "D. Neither clearly stated"
                ],
                "ans": "B",
                "exp": "〜たあとで (after doing ~) = た-form + あとで. The action before あとで happens FIRST. 宿題をしたあとで = after doing homework → then games."
            },
        ]
    },
]
