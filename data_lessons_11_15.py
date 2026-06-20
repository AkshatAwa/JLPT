# data_lessons_11_15.py
# Contains first-principles detailed data for Lessons 11 through 15

LESSONS_11_15 = [
    {
        "num": 11,
        "title": "Counting People and Things",
        "jp_title": "りんごをいくつ買いましたか",
        "overview": "Learn how to ask 'how many' and 'how long' using counters and periods of time.",
        "objectives": [
            "Ask 'How many' using いくつ",
            "State periods of time (hours, days, weeks)",
            "Ask 'How long does it take' using どのくらい",
            "Use the particle に to express frequency (e.g., 3 times a week)"
        ],
        "vocab": [
            ("いくつ", "いくつ", "How many (general objects)", "Interrogative", "N5", "みかんをいくつ買いましたか。", "Mikan o ikutsu kaimashita ka.", "How many tangerines did you buy?"),
            ("どのくらい", "どのくらい", "How long / How much", "Interrogative", "N5", "どのくらいかかりますか。", "Dono kurai kakarimasu ka.", "How long does it take?"),
            ("かかる", "かかる", "To take (time or money)", "Verb (U)", "N5", "一時間かかります。", "Ichijikan kakarimasu.", "It takes one hour."),
            ("回", "かい", "Times (frequency)", "Counter", "N5", "一週間に二回行きます。", "Isshuukan ni nikai ikimasu.", "I go twice a week."),
            ("だけ", "だけ", "Only", "Particle", "N5", "少しだけ食べました。", "Sukoshi dake tabemashita.", "I ate only a little."),
        ],
        "grammar": [
            {
                "pattern": "[Period of time] に [Number] 回 V",
                "meaning": "Do V [Number] times per [Period]",
                "structure": "[Time Period] に (ni) [Number] 回 (kai) [Verb]",
                "formation": "The に particle here means 'per' or 'within the span of'.",
                "why": "This is a highly structured, mathematical way of expressing frequency.",
                "formal": "一ヶ月に二回映画を見ます。",
                "casual": "一ヶ月に二回映画を見る。",
                "native": "Very common. 'Ichi-nichi ni san-kai' = 3 times a day.",
                "examples": [
                    ("一年に一回旅行します。", "I travel once a year."),
                    ("一日に三回薬を飲みます。", "I take medicine three times a day."),
                ],
                "mistakes": "Forgetting the に. '一週間三回' is WRONG. It must be '一週間に三回'.",
                "jlpt": "They love testing this exact structure in reading questions."
            },
            {
                "pattern": "[Quantity/Time] かかります",
                "meaning": "It takes [Time/Money]",
                "structure": "[Number + Counter] かかります。",
                "formation": "かかります acts as the verb indicating expenditure of time or money.",
                "why": "The verb かかる has many meanings in Japanese, but here it implies 'hanging' or 'requiring' resources.",
                "formal": "東京から大阪まで二時間半かかります。",
                "casual": "二時間半かかる。",
                "native": "Just like other counters, do NOT use a particle before かかります.",
                "examples": [
                    ("一万円かかりました。", "It cost ten thousand yen."),
                    ("毎日、二時間かかります。", "It takes two hours every day."),
                ],
                "mistakes": "Saying '二時間がかかります'. WRONG. The counter floats: '二時間かかります'.",
                "jlpt": "Often paired with 'どのくらい' (how much/long) in listening tests."
            }
        ],
        "kanji": [
            ("百", "ひゃく", "ヒャク", "6", "Hundred", "One (一) over white (白).", [("百", "ひゃく", "100"), ("三百", "さんびゃく", "300")]),
            ("千", "せん", "セン", "3", "Thousand", "A drop (ten) on top of ten (十). Ten tens equals a thousand (almost).", [("千", "せん", "1000"), ("三千", "さんぜん", "3000")]),
        ],
        "quiz": [
            {"q": "How do you say 'twice a week'?", "opts": ["A. 一週間二回", "B. 一週間に二回", "C. 二回に一週間", "D. 一週間で二回"], "ans": "B", "exp": "You must use the に particle after the time period to mean 'per'. 一週間に (Per week) 二回 (two times)."},
            {"q": "Which is correct?", "opts": ["A. 五時間かかります", "B. 五時間がかかります", "C. 五時間をかかります", "D. 五時間でかかります"], "ans": "A", "exp": "Time lengths are counters. Counters act like adverbs and do not take particles before the verb かかります."},
        ]
    },
    {
        "num": 12,
        "title": "Comparisons and Superlatives",
        "jp_title": "カレーのほうが好きです",
        "overview": "Learn how to compare two items and state which is the best among three or more items.",
        "objectives": [
            "Describe the past tense of Adjectives and Nouns",
            "Compare two things using より and ほうが",
            "State the superlative (best/most) using 一番",
            "Ask 'Which is more' using どちら"
        ],
        "vocab": [
            ("より", "より", "Than", "Particle", "N5", "肉は魚より高いです。", "Niku wa sakana yori takai desu.", "Meat is more expensive than fish."),
            ("ほうが", "ほうが", "More (side/alternative)", "Noun Phrase", "N5", "私のほうが強いです。", "Watashi no hou ga tsuyoi desu.", "I am stronger (My side is stronger)."),
            ("どちら", "どちら", "Which (of two)", "Interrogative", "N5", "どちらが好きですか。", "Dochira ga suki desu ka.", "Which (of the two) do you like?"),
            ("一番", "いちばん", "Number one / Most", "Adverb", "N5", "これが一番美味しいです。", "Kore ga ichiban oishii desu.", "This is the most delicious."),
            ("ずっと", "ずっと", "By far", "Adverb", "N5", "今日のほうがずっと暑いです。", "Kyou no hou ga zutto atsui desu.", "Today is by far hotter."),
        ],
        "grammar": [
            {
                "pattern": "A は B より [Adjective] です",
                "meaning": "A is more [Adjective] than B",
                "structure": "[Noun A] は [Noun B] より [Adjective] です。",
                "formation": "A is the topic. より attaches to B to mean 'than B'.",
                "why": "より indicates the baseline for comparison. 'Compared to B, A is...'",
                "formal": "中国は日本より大きいです。",
                "casual": "中国は日本より大きい。",
                "native": "Highly structured comparison form.",
                "examples": [
                    ("今日は昨日より暑いです。", "Today is hotter than yesterday."),
                    ("車は自転車より速いです。", "A car is faster than a bicycle."),
                ],
                "mistakes": "Swapping the order. 'A yori B wa' means B is greater than A.",
                "jlpt": "Reading comprehension trap. Pay close attention to which noun has the より."
            },
            {
                "pattern": "A と B と どちらが [Adjective] ですか",
                "meaning": "Between A and B, which is more [Adjective]?",
                "structure": "[Noun A] と [Noun B] と どちらが [Adjective] ですか。",
                "formation": "You explicitly state A and B, linking them with と (and), then ask 'dochira ga' (which side).",
                "why": "Japanese requires you to explicitly bracket the two options being compared.",
                "formal": "サッカーと野球とどちらが好きですか。",
                "casual": "サッカーと野球、どっちが好き？ (Dochira becomes dotchi).",
                "native": "The response must use ほうが.",
                "examples": [
                    ("肉と魚とどちらがいいですか。", "Between meat and fish, which is better?"),
                ],
                "mistakes": "Using どれ (which of 3+) instead of どちら (which of 2).",
                "jlpt": "If the options are two things, you MUST use どちら."
            },
            {
                "pattern": "〜のなかで [X] が 一番 [Adjective] です",
                "meaning": "Among ~, [X] is the most [Adjective]",
                "structure": "[Category Noun] のなかで [Noun X] が 一番 (ichiban) [Adjective] です。",
                "formation": "Set the category with 'no naka de' (inside of/among). Then state the subject X with 'ga', and use 'ichiban' (number one) to show it is the superlative.",
                "why": "This is how you compare 3 or more things.",
                "formal": "果物のなかでりんごが一番好きです。",
                "casual": "果物のなかでりんごが一番好き。",
                "native": "You can drop the category if it's obvious from context.",
                "examples": [
                    ("一年で夏が一番好きです。", "In a year, I like summer the best."),
                    ("クラスで誰が一番背が高いですか。", "Who is the tallest in the class?"),
                ],
                "mistakes": "Using ほうが instead of 一番. ほうが is ONLY for comparing two things.",
                "jlpt": "Distinguishing between どちら (2 things) and どれ/だれ/一番 (3+ things)."
            }
        ],
        "kanji": [
            ("万", "まん", "マン / バン", "3", "Ten Thousand", "A very large number.", [("一万", "いちまん", "10,000"), ("万年筆", "まんねんひつ", "Fountain pen")]),
            ("円", "えん", "エン", "4", "Yen / Circle", "Looks like a window. Originally meant round.", [("百円", "ひゃくえん", "100 Yen"), ("円い", "まるい", "Round")]),
        ],
        "quiz": [
            {"q": "If I want to say 'Dogs are cuter than cats', what is the correct sentence?", "opts": ["A. 犬は猫よりかわいいです", "B. 猫は犬よりかわいいです", "C. 犬より猫はかわいいです", "D. 猫と犬とどちらがかわいいです"], "ans": "A", "exp": "犬 (dogs) is the topic (は). 猫 (cats) is the baseline (より). So, dogs are cuter than cats."},
            {"q": "When comparing three or more things, which word must you use to say 'the most'?", "opts": ["A. ほうが (hou ga)", "B. どちら (dochira)", "C. 一番 (ichiban)", "D. より (yori)"], "ans": "C", "exp": "一番 means 'number one' or 'the most'. ほうが and どちら are strictly used for comparing only two things."},
        ]
    },
    {
        "num": 13,
        "title": "Desires and Purpose",
        "jp_title": "日本へ遊びに行きます",
        "overview": "Learn how to express what you want, what you want to do, and your purpose for going somewhere.",
        "objectives": [
            "Express desire for an object using が ほしい",
            "Express desire to do an action using Verb-たい",
            "State the purpose of movement using [Verb-stem] に 行きます"
        ],
        "vocab": [
            ("ほしい", "ほしい", "Want (an object)", "I-Adj", "N5", "車がほしいです。", "Kuruma ga hoshii desu.", "I want a car."),
            ("〜たい", "たい", "Want to (do an action)", "Suffix", "N5", "日本へ行きたいです。", "Nihon e ikitai desu.", "I want to go to Japan."),
            ("遊びます", "あそびます", "To play / visit", "Verb (U)", "N5", "友達と遊びます。", "Tomodachi to asobimasu.", "I play with my friend."),
            ("買い物", "かいもの", "Shopping", "Noun", "N5", "買い物に行きます。", "Kaimono ni ikimasu.", "I go shopping."),
            ("広い", "ひろい", "Spacious / Wide", "I-Adj", "N5", "広い家がほしいです。", "Hiroi ie ga hoshii desu.", "I want a spacious house."),
        ],
        "grammar": [
            {
                "pattern": "N が ほしいです",
                "meaning": "I want N",
                "structure": "[Noun] が ほしいです。",
                "formation": "Similar to 好き (like), ほしい is an ADJECTIVE describing a state of desire. Therefore, the object takes the が particle.",
                "why": "You do not 'action' a want in Japanese. An object is 'desirable' to you.",
                "formal": "私は新しいパソコンがほしいです。",
                "casual": "新しいパソコンがほしい。",
                "native": "You CANNOT use ほしい to describe what a third person (he/she) wants. It is strictly for first-person (I) or asking second-person questions.",
                "examples": [
                    ("お金がほしいです。", "I want money."),
                    ("今、何が一番ほしいですか。", "Right now, what do you want the most?"),
                ],
                "mistakes": "Using を ほしい. It MUST be が ほしい.",
                "jlpt": "Particle test: identifying that ほしい takes が."
            },
            {
                "pattern": "V ます-stem + たいです",
                "meaning": "I want to do V",
                "structure": "[Verb stem] + たいです。",
                "formation": "Take the formal ます form, drop the ます, and attach たい. The resulting word acts exactly like an い-adjective.",
                "why": "This transforms the verb into an adjective of desire.",
                "formal": "私は日本へ行きたいです。",
                "casual": "日本へ行きたい。",
                "native": "Because it becomes an i-adjective, you conjugate it like one: 行きたくない (don't want to go), 行きたかった (wanted to go).",
                "examples": [
                    ("すしを食べたいです。", "I want to eat sushi."),
                    ("今日は何もしたくないです。", "I don't want to do anything today."),
                ],
                "mistakes": "Conjugating it like a verb. Remember, V-たい is an i-ADJECTIVE. Negative is たくない, NOT たいではありません.",
                "jlpt": "Conjugation trap. V-たくない is highly tested."
            },
            {
                "pattern": "[Place] へ [Purpose] に 行きます",
                "meaning": "Go to [Place] in order to do [Purpose]",
                "structure": "[Destination] へ [Verb stem OR Verbal Noun] に 行きます/来ます/帰ります",
                "formation": "Take a verb stem (e.g., 買い) or a verbal noun (e.g., 買い物), attach the に particle, and follow with a motion verb.",
                "why": "The に particle here represents the 'target' or 'purpose' of the movement.",
                "formal": "デパートへ買い物をしに行きます。",
                "casual": "デパートへ買い物に行く。",
                "native": "You can drop the 'shini' and just use the verbal noun: デパートへ買い物に行きます。",
                "examples": [
                    ("日本へ日本語を勉強しに来ました。", "I came to Japan in order to study Japanese."),
                    ("プールへ泳ぎに行きます。", "I go to the pool to swim."),
                ],
                "mistakes": "Putting the full dictionary verb before に. '泳ぐに行きます' is WRONG. It must be the STEM: '泳ぎに行きます'.",
                "jlpt": "Tested heavily. Ensure you use the Masu-stem without the Masu."
            }
        ],
        "kanji": [
            ("買", "か", "バイ", "12", "Buy", "A net/eye over a shell (ancient currency).", [("買う", "かう", "To buy"), ("買い物", "かいもの", "Shopping")]),
            ("物", "もの", "ブツ / モツ", "8", "Thing", "Cow (牛) + Flag/Blood. Physical objects.", [("物", "もの", "Thing"), ("飲み物", "のみもの", "Beverage")]),
        ],
        "quiz": [
            {"q": "How do you conjugate 'want to eat' into the negative 'do not want to eat'?", "opts": ["A. 食べたいではありません", "B. 食べたくないです", "C. 食べたいないです", "D. 食べないたいです"], "ans": "B", "exp": "V-たい is an i-adjective. To negate an i-adjective, drop the 'i' and add 'kunai'. 食べたい → 食べたくない."},
            {"q": "Which sentence correctly says 'I go to Kyoto to take pictures'?", "opts": ["A. 京都へ写真を撮るに行きます", "B. 京都へ写真を撮ってに行きます", "C. 京都へ写真を撮りに行きます", "D. 京都へ写真が撮ります"], "ans": "C", "exp": "Purpose of motion requires the MASU-STEM of the verb. 撮ります → 撮り. So, 撮りに行きます."},
        ]
    },
    {
        "num": 14,
        "title": "The Te-Form and Requests",
        "jp_title": "ちょっと待ってください",
        "overview": "Learn the most critical verb conjugation in Japanese: The Te-Form. This allows you to link actions, make requests, and offer help.",
        "objectives": [
            "Master the Te-Form conjugation rules for all 3 Verb Groups",
            "Make polite requests using 〜てください",
            "Describe ongoing actions using 〜ています",
            "Offer assistance using 〜ましょうか"
        ],
        "vocab": [
            ("待つ", "まつ", "To wait", "Verb (U)", "N5", "ちょっと待ってください。", "Chotto matte kudasai.", "Please wait a moment."),
            ("持つ", "もつ", "To hold / have", "Verb (U)", "N5", "荷物を持ちましょうか。", "Nimotsu o mochimashou ka.", "Shall I carry your bags?"),
            ("呼ぶ", "よぶ", "To call", "Verb (U)", "N5", "タクシーを呼びましょう。", "Takushii o yobimashou.", "Let's call a taxi."),
            ("急ぐ", "いそぐ", "To hurry", "Verb (U)", "N5", "急いでください。", "Isoide kudasai.", "Please hurry."),
            ("ちょっと", "ちょっと", "A little / A moment", "Adverb", "N5", "ちょっと待って。", "Chotto matte.", "Wait a sec."),
        ],
        "grammar": [
            {
                "pattern": "V-て ください",
                "meaning": "Please do V",
                "structure": "[Verb Te-Form] + ください",
                "formation": "Conjugate the verb into the Te-Form and attach ください (Please give me the favor of...).",
                "why": "By itself, the Te-Form is just a connector. Adding ください turns it into a direct request.",
                "formal": "ここに名前を書いてください。",
                "casual": "ここに名前を書いて。 (Drop kudasai).",
                "native": "This is a direct instruction/order. It is NOT polite enough for bosses or customers. It is used for instructions or between peers.",
                "examples": [
                    ("ドアを閉めてください。", "Please close the door."),
                    ("ゆっくり話してください。", "Please speak slowly."),
                ],
                "mistakes": "Using the dictionary form instead of the Te-form.",
                "jlpt": "Te-form conjugation is the most heavily tested N5 mechanic."
            },
            {
                "pattern": "V-て います",
                "meaning": "Is currently doing V / Is in a state of V",
                "structure": "[Verb Te-Form] + います",
                "formation": "Te-Form + the animate existence verb います.",
                "why": "It shows that an action is currently existing/ongoing right now.",
                "formal": "今、雨が降っています。",
                "casual": "今、雨が降っている。",
                "native": "Can mean an ongoing action (I am eating) OR a continuous state (I am married / I live in Tokyo).",
                "examples": [
                    ("ミラーさんは今、電話をかけています。", "Mr. Miller is making a phone call right now."),
                    ("私は結婚しています。", "I am married. (State of being)."),
                ],
                "mistakes": "Thinking it ONLY means 'action in progress'. It also means 'resulting state'.",
                "jlpt": "Understanding that '住んでいます' (I live) is a state, not an action in progress."
            },
            {
                "pattern": "V-ましょうか",
                "meaning": "Shall I do V? (Offering help)",
                "structure": "[Verb Masu-stem] + ましょうか",
                "formation": "Takes the 'Let's' form and adds the question particle か.",
                "why": "Literally 'Shall we do...?' but effectively used to say 'Let me do that for you.'",
                "formal": "窓を開けましょうか。",
                "casual": "窓を開けようか。 (Volitional form).",
                "native": "A highly polite and considerate way to offer assistance.",
                "examples": [
                    ("傘を貸しましょうか。", "Shall I lend you an umbrella?"),
                    ("手伝いましょうか。", "Shall I help you?"),
                ],
                "mistakes": "Confusing it with ませんか (invitation). ましょうか is offering YOUR service. ませんか is asking someone to join you.",
                "jlpt": "Common listening test: Someone looks troubled. What do you say? -> ましょうか."
            }
        ],
        "kanji": [
            ("待", "ま", "タイ", "9", "Wait", "A line of people stepping at a temple, waiting their turn.", [("待つ", "まつ", "To wait"), ("招待", "しょうたい", "Invitation")]),
            ("持", "も", "ジ", "9", "Hold", "Hand (手) + Temple (寺). Holding hands at the temple.", [("持つ", "もつ", "To hold"), ("お金持ち", "おかねもち", "Rich person (money holder)")]),
        ],
        "quiz": [
            {"q": "What is the correct Te-Form of 急ぐ (Isogu - to hurry)?", "opts": ["A. いそいて", "B. いそって", "C. いそいで", "D. いそんで"], "ans": "C", "exp": "Group 1 verbs ending in 'gu' change to 'ide'. ぐ → いで."},
            {"q": "If you see someone carrying a heavy box, what should you say?", "opts": ["A. 持ちませんか", "B. 持ちましょうか", "C. 待ってください", "D. 持ちますか"], "ans": "B", "exp": "持ちましょうか (Shall I hold it?) is the standard polite way to offer assistance."},
        ]
    },
    {
        "num": 15,
        "title": "Permissions and Prohibitions",
        "jp_title": "写真を撮ってもいいですか",
        "overview": "Learn how to ask for permission, grant permission, and firmly state prohibitions using the Te-Form.",
        "objectives": [
            "Ask for permission using 〜てもいいですか",
            "Grant permission using 〜てもいいです",
            "State prohibitions using 〜てはいけません",
            "Describe habitual actions or states using 〜ています"
        ],
        "vocab": [
            ("写真を撮る", "しゃしんをとる", "To take a picture", "Verb Phrase", "N5", "ここで写真を撮ってもいいですか。", "Koko de shashin o totte mo ii desu ka.", "May I take a picture here?"),
            ("吸う", "すう", "To smoke / breathe", "Verb (U)", "N5", "タバコを吸ってはいけません。", "Tabako o sutte wa ikemasen.", "You must not smoke."),
            ("入る", "はいる", "To enter", "Verb (U)", "N5", "ここに入ってはいけません。", "Koko ni haitte wa ikemasen.", "You must not enter here."),
            ("売る", "うる", "To sell", "Verb (U)", "N5", "スーパーで売っています。", "Suupaa de utte imasu.", "They are selling it at the supermarket."),
            ("知る", "しる", "To know", "Verb (U)", "N5", "私はその人を知っています。", "Watashi wa sono hito o shitte imasu.", "I know that person."),
        ],
        "grammar": [
            {
                "pattern": "V-ても いいです(か)",
                "meaning": "May I do V? / You may do V",
                "structure": "[Verb Te-Form] + も いいです",
                "formation": "Te-form + mo (even if) + ii desu (it is good).",
                "why": "Literally means 'Even if you do V, it is good.'",
                "formal": "このカタログをもらってもいいですか。",
                "casual": "これ、もらってもいい？",
                "native": "This is the universal way to ask for permission in Japanese.",
                "examples": [
                    ("ここに座ってもいいですか。", "May I sit here?"),
                    ("ええ、いいですよ。", "Yes, you may (it's good)."),
                ],
                "mistakes": "Forgetting the 'mo' particle. 'Te ii desu' sounds unnatural.",
                "jlpt": "Identifying permission structures."
            },
            {
                "pattern": "V-ては いけません",
                "meaning": "You must NOT do V (Prohibition)",
                "structure": "[Verb Te-Form] + は (wa) いけません",
                "formation": "Te-form + wa + ikemasen (it cannot go).",
                "why": "Literally 'As for doing V, it cannot go (it is bad)'.",
                "formal": "ここに車を止めてはいけません。",
                "casual": "ここに車を止めてはだめだ。 / 止めちゃだめだ。",
                "native": "This is very strong and direct. It is used for rules, laws, and reprimanding children. It is too strong to use to politely decline a request.",
                "examples": [
                    ("タバコを吸ってはいけません。", "You must not smoke."),
                    ("ここで写真を撮ってはいけません。", "You must not take pictures here."),
                ],
                "mistakes": "Using it to politely say 'no'. If someone asks 'May I smoke?', replying '吸ってはいけません' is incredibly rude and aggressive. Say 'すみません、ちょっと...' instead.",
                "jlpt": "Understanding that this expresses absolute rules/laws."
            },
            {
                "pattern": "V-て います (States)",
                "meaning": "Know / Live / Married (Continuous State)",
                "structure": "[Verb Te-Form] + います",
                "formation": "Certain verbs in Japanese describe instantaneous changes (like getting married, finding out information, moving to a city). To say you currently ARE in that state, you use Te-imasu.",
                "why": "In English 'I know' is present tense. In Japanese, 'shiru' means 'to discover/find out'. So you must say 'I discovered it and am currently in the state of knowing' (shitte imasu).",
                "formal": "私は大阪に住んでいます。",
                "casual": "大阪に住んでいる。",
                "native": "The negative of 'shitte imasu' is the massive exception: 'shirimasen' (NOT shitte imasen).",
                "examples": [
                    ("IMCで働いています。", "I work at IMC. (Habitual employment)."),
                    ("ミラーさんを知っていますか。", "Do you know Mr. Miller?"),
                    ("いいえ、知りません。", "No, I do not know him. (EXCEPTION!)."),
                ],
                "mistakes": "CRITICAL EXCEPTION: To say 'I don't know', you NEVER say 知っていません. You MUST say 知りません.",
                "jlpt": "知っています vs 知りません is guaranteed to be tested."
            }
        ],
        "kanji": [
            ("入", "はい / い", "ニュウ", "2", "Enter", "A person walking into an opening.", [("入る", "はいる", "To enter"), ("入口", "いりぐち", "Entrance")]),
            ("出", "で / だ", "シュツ", "5", "Exit / Take out", "Two mountains, climbing out.", [("出る", "でる", "To exit"), ("出口", "でぐち", "Exit")]),
        ],
        "quiz": [
            {"q": "What is the correct negative response to '知っていますか' (Do you know)?", "opts": ["A. 知っていません", "B. 知りません", "C. 知らなくない", "D. 知るじゃない"], "ans": "B", "exp": "This is a major grammatical exception in Japanese. The positive is 知っています, but the negative is strictly 知りません."},
            {"q": "Which sentence means 'You must not smoke'?", "opts": ["A. 吸ってもいいですか", "B. 吸っていません", "C. 吸ってはいけません", "D. 吸いません"], "ans": "C", "exp": "〜てはいけません is the strict prohibition form meaning 'must not'."},
        ]
    }
]
