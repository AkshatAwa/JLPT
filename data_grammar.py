"""
Complete JLPT N5 Grammar Encyclopedia Data
All grammar points, Te-Form master data, relationship map, and revision sets.
"""

# ==============================================================
# GRAMMAR ENCYCLOPEDIA DATA
# Each entry is a fully-documented grammar point.
# ==============================================================

GRAMMAR_DATA = [

    # =============================================
    # CATEGORY: BASIC SENTENCES
    # =============================================
    {
        "id": "desu",
        "pattern": "〜です",
        "category": "Basic Sentences",
        "meaning": "Is / Am / Are (copula)",
        "structure": "Noun / Na-Adj + です",
        "formation": "Simply attach です to a noun or na-adjective. It does NOT attach to い-adjectives for present affirmative (they stand alone). です is the formal copula — the Japanese equivalent of 'to be'.",
        "formal": "私は学生です。(Watashi wa gakusei desu.) — I am a student.",
        "casual": "Replace です with だ. 私は学生だ。(Watashi wa gakusei da.) — very casual/plain form.",
        "common_mistakes": "Learners often attach です directly to い-adjectives (e.g., ✗ 高いです — this is actually acceptable and common in polite speech, but the base adjective is complete without it). Do NOT say ✗ です alone without a subject.",
        "jlpt_traps": "On the JLPT, です follows na-adjectives (きれいです) but note that い-adjectives like 大きい already carry tense/negation within themselves. Don't confuse です as the only way to form a sentence.",
        "related": ["〜ではありません", "〜でした", "〜ではありませんでした"],
        "differences": "です (formal) vs だ (casual plain). In writing, だ is common. です is always polite.",
        "examples": [
            {"jp": "これは本です。", "kana": "これはほんです。", "romaji": "Kore wa hon desu.", "eng": "This is a book."},
            {"jp": "山田さんは先生です。", "kana": "やまださんはせんせいです。", "romaji": "Yamada-san wa sensei desu.", "eng": "Mr. Yamada is a teacher."},
            {"jp": "あの店はきれいです。", "kana": "あのみせはきれいです。", "romaji": "Ano mise wa kirei desu.", "eng": "That store is beautiful."},
            {"jp": "今日は月曜日です。", "kana": "きょうはげつようびです。", "romaji": "Kyou wa getsuyoubi desu.", "eng": "Today is Monday."},
            {"jp": "私はアクシャットです。", "kana": "わたしはアクシャットです。", "romaji": "Watashi wa Akshat desu.", "eng": "I am Akshat."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "お仕事は何ですか。", "kana": "おしごとはなんですか。", "romaji": "Oshigoto wa nan desu ka.", "eng": "What is your job?"},
            {"speaker": "B", "jp": "医者です。", "kana": "いしゃです。", "romaji": "Isha desu.", "eng": "I am a doctor."},
        ]
    },
    {
        "id": "dewa_arimasen",
        "pattern": "〜ではありません",
        "category": "Basic Sentences",
        "meaning": "Is not / Am not / Are not (formal negative copula)",
        "structure": "Noun / Na-Adj + ではありません",
        "formation": "Take the plain copula だ and replace it with ではありません. The short form じゃありません is also widely used in both formal and casual contexts. ではありません is slightly more formal/emphatic.",
        "formal": "私は学生ではありません。— I am not a student.",
        "casual": "私は学生じゃない。(Watashi wa gakusei ja nai.) — very casual.",
        "common_mistakes": "✗ 私は学生ではないです (grammatically acceptable but redundant). Use either ではありません (formal) or じゃない (casual). Don't mix registers randomly.",
        "jlpt_traps": "JLPT often tests ではありません vs じゃありません. They are interchangeable but register differs. ではありません is stiffer/more formal.",
        "related": ["〜です", "〜でした"],
        "differences": "ではありません (formal, emphatic) = じゃありません (semi-formal) = じゃない (casual).",
        "examples": [
            {"jp": "これはペンではありません。", "kana": "これはペンではありません。", "romaji": "Kore wa pen dewa arimasen.", "eng": "This is not a pen."},
            {"jp": "田中さんは医者ではありません。", "kana": "たなかさんはいしゃではありません。", "romaji": "Tanaka-san wa isha dewa arimasen.", "eng": "Tanaka-san is not a doctor."},
            {"jp": "ここは学校ではありません。", "kana": "ここはがっこうではありません。", "romaji": "Koko wa gakkou dewa arimasen.", "eng": "This is not a school."},
            {"jp": "あれは私の車じゃありません。", "kana": "あれはわたしのくるまじゃありません。", "romaji": "Are wa watashi no kuruma ja arimasen.", "eng": "That is not my car."},
            {"jp": "彼は先生ではありません。学生です。", "kana": "かれはせんせいではありません。がくせいです。", "romaji": "Kare wa sensei dewa arimasen. Gakusei desu.", "eng": "He is not a teacher. He is a student."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "あの方はスミスさんですか。", "kana": "あのかたはスミスさんですか。", "romaji": "Ano kata wa Sumisu-san desu ka.", "eng": "Is that person Mr. Smith?"},
            {"speaker": "B", "jp": "いいえ、スミスさんではありません。ジョーンズさんです。", "kana": "いいえ、スミスさんではありません。ジョーンズさんです。", "romaji": "Iie, Sumisu-san dewa arimasen. Joonzu-san desu.", "eng": "No, that is not Mr. Smith. It is Mr. Jones."},
        ]
    },
    {
        "id": "deshita",
        "pattern": "〜でした",
        "category": "Basic Sentences",
        "meaning": "Was / Were (past tense copula)",
        "structure": "Noun / Na-Adj + でした",
        "formation": "でした is the past tense of です. It expresses that something *was* something in the past. For い-adjectives, the past tense is formed differently (remove い, add かった).",
        "formal": "昨日は月曜日でした。— Yesterday was Monday.",
        "casual": "昨日は月曜日だった。(Kinou wa getsuyoubi datta.) — casual past.",
        "common_mistakes": "Do not use でした with い-adjectives. ✗ 暑いでした. Correct: 暑かったです (Atsukatta desu).",
        "jlpt_traps": "JLPT frequently tests past tense adjectives. い-adj past: 〜かった, na-adj past: 〜でした.",
        "related": ["〜です", "〜ではありませんでした"],
        "differences": "でした (past formal) vs だった (past casual). でした sounds like だった + さ.",
        "examples": [
            {"jp": "昨日は休みでした。", "kana": "きのうはやすみでした。", "romaji": "Kinou wa yasumi deshita.", "eng": "Yesterday was a holiday."},
            {"jp": "子供のころ、夢は医者でした。", "kana": "こどものころ、ゆめはいしゃでした。", "romaji": "Kodomo no koro, yume wa isha deshita.", "eng": "When I was a child, my dream was to be a doctor."},
            {"jp": "あのレストランはとてもにぎやかでした。", "kana": "あのレストランはとてもにぎやかでした。", "romaji": "Ano resutoran wa totemo nigiyaka deshita.", "eng": "That restaurant was very lively."},
            {"jp": "田中さんはむかし学生でした。", "kana": "たなかさんはむかしがくせいでした。", "romaji": "Tanaka-san wa mukashi gakusei deshita.", "eng": "Tanaka-san used to be a student."},
            {"jp": "映画はとても面白かったです。", "kana": "えいがはとてもおもしろかったです。", "romaji": "Eiga wa totemo omoshirokatta desu.", "eng": "The movie was very interesting. (い-adj example for contrast)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "子供のころ、どんな子でしたか。", "kana": "こどものころ、どんなこでしたか。", "romaji": "Kodomo no koro, donna ko deshita ka.", "eng": "What kind of child were you?"},
            {"speaker": "B", "jp": "元気な子でした。", "kana": "げんきなこでした。", "romaji": "Genki na ko deshita.", "eng": "I was an energetic child."},
        ]
    },
    {
        "id": "dewa_arimasen_deshita",
        "pattern": "〜ではありませんでした",
        "category": "Basic Sentences",
        "meaning": "Was not / Were not (past negative copula)",
        "structure": "Noun / Na-Adj + ではありませんでした",
        "formation": "Combine the negative (ではありません) with the past (でした) → ではありませんでした. Casual: じゃなかった.",
        "formal": "昨日は休みではありませんでした。— Yesterday was not a holiday.",
        "casual": "昨日は休みじゃなかった。— casual past negative.",
        "common_mistakes": "This is a long form. In speech, じゃなかったです or じゃありませんでした is much more natural. ではありませんでした sounds very formal.",
        "jlpt_traps": "This is a classic JLPT fill-in-the-blank target. Know all four forms: +pres, -pres, +past, -past.",
        "related": ["〜です", "〜でした", "〜ではありません"],
        "differences": "Formal-polite past negative. Casual equivalent: じゃなかった.",
        "examples": [
            {"jp": "昨日の天気は晴れではありませんでした。", "kana": "きのうのてんきははれではありませんでした。", "romaji": "Kinou no tenki wa hare dewa arimasen deshita.", "eng": "Yesterday's weather was not sunny."},
            {"jp": "彼は最初から友達ではありませんでした。", "kana": "かれははじめからともだちではありませんでした。", "romaji": "Kare wa hajime kara tomodachi dewa arimasen deshita.", "eng": "He was not a friend from the beginning."},
            {"jp": "その映画は面白くありませんでした。", "kana": "そのえいがはおもしろくありませんでした。", "romaji": "Sono eiga wa omoshiroku arimasen deshita.", "eng": "That movie was not interesting. (い-adj negative past)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "パーティーはにぎやかでしたか。", "kana": "パーティーはにぎやかでしたか。", "romaji": "Paatii wa nigiyaka deshita ka.", "eng": "Was the party lively?"},
            {"speaker": "B", "jp": "いいえ、あまりにぎやかではありませんでした。", "kana": "いいえ、あまりにぎやかではありませんでした。", "romaji": "Iie, amari nigiyaka dewa arimasen deshita.", "eng": "No, it was not very lively."},
        ]
    },

    # =============================================
    # CATEGORY: QUESTIONS
    # =============================================
    {
        "id": "desu_ka",
        "pattern": "〜ですか",
        "category": "Questions",
        "meaning": "Is it...? / Are you...? (yes/no question)",
        "structure": "Statement + か",
        "formation": "Add か to the end of any polite statement to turn it into a yes/no question. No subject inversion needed (unlike English). In casual speech, rising intonation alone forms questions without か.",
        "formal": "これは本ですか。(Is this a book?) — Formal.",
        "casual": "これは本？ — with rising intonation. Dropping か entirely is natural in casual speech.",
        "common_mistakes": "✗ Adding a question mark in formal Japanese writing (redundant with か). In writing, か serves as the question mark. Also, do NOT use ですか with casual だ forms → sounds strange.",
        "jlpt_traps": "JLPT tests embedded questions (indirect questions). Don't confuse ですか (direct question) with かどうか (whether or not) which appears in N4.",
        "related": ["〜ましたか", "〜ませんか"],
        "differences": "か makes any sentence a question. In casual speech, intonation alone or の か is used.",
        "examples": [
            {"jp": "あなたは学生ですか。", "kana": "あなたはがくせいですか。", "romaji": "Anata wa gakusei desu ka.", "eng": "Are you a student?"},
            {"jp": "これは日本語の本ですか。", "kana": "これはにほんごのほんですか。", "romaji": "Kore wa nihongo no hon desu ka.", "eng": "Is this a Japanese book?"},
            {"jp": "田中さんは来ますか。", "kana": "たなかさんはきますか。", "romaji": "Tanaka-san wa kimasu ka.", "eng": "Is Tanaka-san coming?"},
            {"jp": "明日は休みですか。", "kana": "あしたはやすみですか。", "romaji": "Ashita wa yasumi desu ka.", "eng": "Is tomorrow a holiday?"},
            {"jp": "日本語が分かりますか。", "kana": "にほんごがわかりますか。", "romaji": "Nihongo ga wakarimasu ka.", "eng": "Do you understand Japanese?"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "すみません、トイレはどこですか。", "kana": "すみません、トイレはどこですか。", "romaji": "Sumimasen, toire wa doko desu ka.", "eng": "Excuse me, where is the bathroom?"},
            {"speaker": "B", "jp": "あそこです。", "kana": "あそこです。", "romaji": "Asoko desu.", "eng": "It's over there."},
        ]
    },

    # =============================================
    # CATEGORY: EXISTENCE
    # =============================================
    {
        "id": "ga_arimasu",
        "pattern": "〜があります",
        "category": "Existence",
        "meaning": "There is / There exists (for inanimate things)",
        "structure": "Noun が + あります",
        "formation": "あります is the polite form of ある. Use it to state that something NON-LIVING exists, is present, or you have it. The subject is marked with が (not は for pure existence statements).",
        "formal": "テーブルの上に本があります。— There is a book on the table.",
        "casual": "本がある。— There is a book. (plain form: ある)",
        "common_mistakes": "✗ Using あります for people or animals. Correct: 人/動物 → います. Also, a very common mistake is using は instead of が: 本はあります is about contrast ('as for the book, it exists'), が marks the pure subject.",
        "jlpt_traps": "あります vs います is one of the most tested items on the JLPT N5. Animals always use います. Plants use あります. Robots/machines: usually あります.",
        "related": ["〜がいます", "〜にあります"],
        "differences": "あります = non-living, います = living. Exception: nouns like 'friends/family' use います because people are living.",
        "examples": [
            {"jp": "机の上に本があります。", "kana": "つくえのうえにほんがあります。", "romaji": "Tsukue no ue ni hon ga arimasu.", "eng": "There is a book on the desk."},
            {"jp": "銀行の近くにコンビニがあります。", "kana": "ぎんこうのちかくにコンビニがあります。", "romaji": "Ginkou no chikaku ni konbini ga arimasu.", "eng": "There is a convenience store near the bank."},
            {"jp": "冷蔵庫の中にジュースがあります。", "kana": "れいぞうこのなかにジュースがあります。", "romaji": "Reizouko no naka ni juusu ga arimasu.", "eng": "There is juice inside the refrigerator."},
            {"jp": "今日は時間がありません。", "kana": "きょうはじかんがありません。", "romaji": "Kyou wa jikan ga arimasen.", "eng": "I don't have time today."},
            {"jp": "明日、テストがあります。", "kana": "あした、テストがあります。", "romaji": "Ashita, tesuto ga arimasu.", "eng": "There is a test tomorrow."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "すみません、ATMはありますか。", "kana": "すみません、ATMはありますか。", "romaji": "Sumimasen, ATM wa arimasu ka.", "eng": "Excuse me, is there an ATM?"},
            {"speaker": "B", "jp": "はい、あそこにあります。", "kana": "はい、あそこにあります。", "romaji": "Hai, asoko ni arimasu.", "eng": "Yes, it's over there."},
        ]
    },
    {
        "id": "ga_imasu",
        "pattern": "〜がいます",
        "category": "Existence",
        "meaning": "There is / There exists (for living things)",
        "structure": "Noun が + います",
        "formation": "います is the polite form of いる. Use it for LIVING THINGS — people, animals, insects. Even fictional living characters use います. います can also describe ongoing actions (〜ています).",
        "formal": "部屋に子供がいます。— There is a child in the room.",
        "casual": "子供がいる。— There is a child. (plain form: いる)",
        "common_mistakes": "✗ 犬があります (wrong). Correct: 犬がいます. Animals are living! ✗ テレビがいます (wrong). TVs are not living — use あります.",
        "jlpt_traps": "Plants are debatable — in everyday Japanese, あります is standard for plants. Stuffed animals: usually あります.",
        "related": ["〜があります", "〜にいます"],
        "differences": "います = living (people/animals). あります = non-living (things, events, abstract concepts).",
        "examples": [
            {"jp": "公園に子供たちがいます。", "kana": "こうえんにこどもたちがいます。", "romaji": "Kouen ni kodomotachi ga imasu.", "eng": "There are children in the park."},
            {"jp": "庭に犬がいます。", "kana": "にわにいぬがいます。", "romaji": "Niwa ni inu ga imasu.", "eng": "There is a dog in the garden."},
            {"jp": "教室に先生がいません。", "kana": "きょうしつにせんせいがいません。", "romaji": "Kyoushitsu ni sensei ga imasen.", "eng": "There is no teacher in the classroom."},
            {"jp": "彼女がいます。", "kana": "かのじょがいます。", "romaji": "Kanojo ga imasu.", "eng": "I have a girlfriend. / She is here."},
            {"jp": "池に魚がいますか。", "kana": "いけにさかながいますか。", "romaji": "Ike ni sakana ga imasu ka.", "eng": "Are there fish in the pond?"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "山田さんはいますか。", "kana": "やまださんはいますか。", "romaji": "Yamada-san wa imasu ka.", "eng": "Is Yamada-san here?"},
            {"speaker": "B", "jp": "はい、います。ちょっと待ってください。", "kana": "はい、います。ちょっとまってください。", "romaji": "Hai, imasu. Chotto matte kudasai.", "eng": "Yes, they are. Please wait a moment."},
        ]
    },

    # =============================================
    # CATEGORY: LOCATION
    # =============================================
    {
        "id": "ni_arimasu",
        "pattern": "〜にあります / 〜にいます",
        "category": "Location",
        "meaning": "Is located at / Is at (for things/people)",
        "structure": "Place に + Noun が + あります / います",
        "formation": "Use に to mark the LOCATION of existence. The structure 'Place に Thing が あります/います' answers the question 'Where is X?' When describing location, に is the location particle, while あります/います follow the living/non-living rule.",
        "formal": "駅の前にコンビニがあります。— There is a convenience store in front of the station.",
        "casual": "駅の前にコンビニがある。— casual.",
        "common_mistakes": "Confusing で and に for location. に marks the LOCATION OF EXISTENCE (something IS there), while で marks the LOCATION OF ACTION (something HAPPENS there). ✗ 図書館で本があります → ✓ 図書館に本があります.",
        "jlpt_traps": "で vs に for location is one of the most tested particle distinctions at N5. に = where something exists, で = where something happens.",
        "related": ["〜があります", "〜がいます", "Location words"],
        "differences": "に (location of existence) vs で (location of action). 'The book is at the library' → 図書館に. 'I study at the library' → 図書館で.",
        "examples": [
            {"jp": "駅はどこにありますか。", "kana": "えきはどこにありますか。", "romaji": "Eki wa doko ni arimasu ka.", "eng": "Where is the station?"},
            {"jp": "駅は銀行の隣にあります。", "kana": "えきはぎんこうのとなりにあります。", "romaji": "Eki wa ginkou no tonari ni arimasu.", "eng": "The station is next to the bank."},
            {"jp": "猫はどこにいますか。", "kana": "ねこはどこにいますか。", "romaji": "Neko wa doko ni imasu ka.", "eng": "Where is the cat?"},
            {"jp": "猫はテーブルの下にいます。", "kana": "ねこはテーブルのしたにいます。", "romaji": "Neko wa teeburr no shita ni imasu.", "eng": "The cat is under the table."},
            {"jp": "田中さんは今どこにいますか。", "kana": "たなかさんはいまどこにいますか。", "romaji": "Tanaka-san wa ima doko ni imasu ka.", "eng": "Where is Tanaka-san right now?"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "郵便局はどこにありますか。", "kana": "ゆうびんきょくはどこにありますか。", "romaji": "Yuubinkyoku wa doko ni arimasu ka.", "eng": "Where is the post office?"},
            {"speaker": "B", "jp": "公園の右にあります。", "kana": "こうえんのみぎにあります。", "romaji": "Kouen no migi ni arimasu.", "eng": "It is to the right of the park."},
        ]
    },

    # =============================================
    # CATEGORY: MOVEMENT
    # =============================================
    {
        "id": "e_ikimasu",
        "pattern": "〜へいきます / 〜にいきます",
        "category": "Movement",
        "meaning": "Go to (a place)",
        "structure": "Place へ / に + verb of movement",
        "formation": "Both へ and に can mark the destination of movement. へ (pronounced 'e') emphasizes DIRECTION (toward). に emphasizes the ARRIVAL POINT (destination). For general 'going to', they are largely interchangeable, but に is more common in modern speech.",
        "formal": "学校へ行きます。/ 学校に行きます。— I go to school.",
        "casual": "学校へ行く。/ 学校に行く。",
        "common_mistakes": "✗ Using で for destinations. ✗ 学校で行きます. で marks location of action, not destination of movement. Destination = へ or に.",
        "jlpt_traps": "へ vs に: Both can be used for destinations of movement. The nuance: へ implies direction/journey, に implies arrival. In practice on JLPT, both are often accepted unless context dictates.",
        "related": ["〜へきます", "〜からきます", "〜に帰ります"],
        "differences": "行きます (go) / 来ます (come) / 帰ります (return home) — all use に or へ for destination.",
        "examples": [
            {"jp": "明日、東京へ行きます。", "kana": "あした、とうきょうへいきます。", "romaji": "Ashita, Toukyou e ikimasu.", "eng": "I will go to Tokyo tomorrow."},
            {"jp": "友達の家に行きました。", "kana": "ともだちのいえにいきました。", "romaji": "Tomodachi no ie ni ikimashita.", "eng": "I went to my friend's house."},
            {"jp": "どこへ行きますか。", "kana": "どこへいきますか。", "romaji": "Doko e ikimasu ka.", "eng": "Where are you going?"},
            {"jp": "スーパーへ買い物に行きます。", "kana": "スーパーへかいものにいきます。", "romaji": "Suupaa e kaimono ni ikimasu.", "eng": "I'm going to the supermarket to shop."},
            {"jp": "毎朝、会社へ行きます。", "kana": "まいあさ、かいしゃへいきます。", "romaji": "Maiasa, kaisha e ikimasu.", "eng": "Every morning, I go to the company."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "週末、どこかへ行きますか。", "kana": "しゅうまつ、どこかへいきますか。", "romaji": "Shuumatsu, dokoka e ikimasu ka.", "eng": "Are you going anywhere this weekend?"},
            {"speaker": "B", "jp": "はい、山へ行きます。", "kana": "はい、やまへいきます。", "romaji": "Hai, yama e ikimasu.", "eng": "Yes, I'm going to the mountains."},
        ]
    },

    # =============================================
    # CATEGORY: TIME EXPRESSIONS
    # =============================================
    {
        "id": "mae_ni",
        "pattern": "〜まえに",
        "category": "Time Expressions",
        "meaning": "Before doing ~ / Before ~",
        "structure": "Verb (dictionary form) + まえに | Noun + のまえに",
        "formation": "For verbs: Use the DICTIONARY (plain non-past) form before まえに — regardless of the tense of the main clause. For nouns: Noun + の + まえに. 'まえ' literally means 'front/before'.",
        "formal": "寝るまえに、歯を磨きます。— I brush my teeth before sleeping.",
        "casual": "寝るまえに歯を磨く。",
        "common_mistakes": "✗ Using the た-form before まえに (寝たまえに). Wrong! Before = dictionary form. After = てから / たあとで (ta-form). The main verb tense handles the overall time frame.",
        "jlpt_traps": "まえに always takes DICTIONARY form verb. This is directly tested. Contrast with あとで which takes た-form.",
        "related": ["〜あとで", "〜てから"],
        "differences": "まえに (before) vs あとで (after, takes た-form) vs てから (sequential actions, uses te-form).",
        "examples": [
            {"jp": "食べるまえに手を洗います。", "kana": "たべるまえにてをあらいます。", "romaji": "Taberu mae ni te o araimasu.", "eng": "I wash my hands before eating."},
            {"jp": "寝るまえに本を読みます。", "kana": "ねるまえにほんをよみます。", "romaji": "Neru mae ni hon o yomimasu.", "eng": "I read a book before sleeping."},
            {"jp": "授業のまえに単語を勉強しました。", "kana": "じゅぎょうのまえにたんごをべんきょうしました。", "romaji": "Jugyou no mae ni tango o benkyou shimashita.", "eng": "I studied vocabulary before class."},
            {"jp": "出かけるまえに鍵を確認してください。", "kana": "でかけるまえにかぎをかくにんしてください。", "romaji": "Dekakeru mae ni kagi o kakunin shite kudasai.", "eng": "Please check your keys before going out."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "毎朝、何をしますか。", "kana": "まいあさ、なにをしますか。", "romaji": "Maiasa, nani o shimasu ka.", "eng": "What do you do every morning?"},
            {"speaker": "B", "jp": "シャワーを浴びるまえに、コーヒーを飲みます。", "kana": "シャワーをあびるまえに、コーヒーをのみます。", "romaji": "Shawaa o abiru mae ni, koohii o nomimasu.", "eng": "I drink coffee before taking a shower."},
        ]
    },
    {
        "id": "ato_de",
        "pattern": "〜あとで",
        "category": "Time Expressions",
        "meaning": "After doing ~",
        "structure": "Verb (た-form) + あとで | Noun + のあとで",
        "formation": "For verbs: Use the た-form (past plain) before あとで. This is the opposite of まえに. For nouns: Noun + の + あとで. 'あと' literally means 'after/behind'.",
        "formal": "ご飯を食べたあとで、散歩しました。— After eating, I took a walk.",
        "casual": "ご飯食べたあと、散歩した。",
        "common_mistakes": "✗ Using dictionary form with あとで (食べるあとで). Wrong! After = た-form. Contrast with まえに = dictionary form.",
        "jlpt_traps": "Classic exam question: fill in the correct verb form before あとで (always た-form) or まえに (always dictionary form).",
        "related": ["〜まえに", "〜てから"],
        "differences": "あとで (general 'after') vs てから (immediate sequential action). てから implies the second action follows directly. あとで allows a time gap.",
        "examples": [
            {"jp": "学校が終わったあとで、友達と遊びます。", "kana": "がっこうがおわったあとで、ともだちとあそびます。", "romaji": "Gakkou ga owatta ato de, tomodachi to asobimasu.", "eng": "After school ends, I'll play with friends."},
            {"jp": "宿題をしたあとで、テレビを見ます。", "kana": "しゅくだいをしたあとで、テレビをみます。", "romaji": "Shukudai o shita ato de, terebi o mimasu.", "eng": "After doing homework, I watch TV."},
            {"jp": "昼ごはんのあとで、昼寝をします。", "kana": "ひるごはんのあとで、ひるねをします。", "romaji": "Hirugohan no ato de, hirune o shimasu.", "eng": "After lunch, I take a nap."},
            {"jp": "シャワーを浴びたあとで、寝ます。", "kana": "シャワーをあびたあとで、ねます。", "romaji": "Shawaa o abita ato de, nemasu.", "eng": "After taking a shower, I go to sleep."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "この仕事が終わったあとで、食事しましょう。", "kana": "このしごとがおわったあとで、しょくじしましょう。", "romaji": "Kono shigoto ga owatta ato de, shokuji shimashou.", "eng": "After this work is done, let's have a meal."},
            {"speaker": "B", "jp": "いいですね。どこへ行きますか。", "kana": "いいですね。どこへいきますか。", "romaji": "Ii desu ne. Doko e ikimasu ka.", "eng": "Sounds good. Where shall we go?"},
        ]
    },
    {
        "id": "te_kara",
        "pattern": "〜てから",
        "category": "Time Expressions",
        "meaning": "After doing ~ (then...)",
        "structure": "Verb (te-form) + から",
        "formation": "Attach から directly to the te-form of a verb. Unlike あとで, てから implies a direct sequential cause-effect or immediate sequence: do A, THEN do B. The second action often depends on or follows from the first.",
        "formal": "卒業してから、就職します。— After graduating, I will get a job.",
        "casual": "卒業してから就職する。",
        "common_mistakes": "✗ Using てから to mean 'because'. から alone at the end of a clause means 'because', but てから means 'after'. Don't confuse the two uses of から.",
        "jlpt_traps": "てから vs あとで: てから emphasizes the sequence and that the second action depends on the first. あとで is more loosely 'at some later time after'.",
        "related": ["〜あとで", "〜まえに"],
        "differences": "てから = direct sequence (B immediately follows A). あとで = general 'after' (may have time gap). てから implies dependency.",
        "examples": [
            {"jp": "手を洗ってから、ご飯を食べます。", "kana": "てをあらってから、ごはんをたべます。", "romaji": "Te o aratte kara, gohan o tabemasu.", "eng": "After washing my hands, I will eat."},
            {"jp": "確認してから、送ります。", "kana": "かくにんしてから、おくります。", "romaji": "Kakunin shite kara, okurimasu.", "eng": "After confirming, I will send it."},
            {"jp": "日本に来てから、三年が経ちました。", "kana": "にほんにきてから、さんねんがたちました。", "romaji": "Nihon ni kite kara, sannen ga tachimashita.", "eng": "It has been three years since I came to Japan."},
            {"jp": "考えてから、返事します。", "kana": "かんがえてから、へんじします。", "romaji": "Kangaete kara, henji shimasu.", "eng": "After thinking about it, I will respond."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "いつ出発しますか。", "kana": "いつしゅっぱつしますか。", "romaji": "Itsu shuppatsu shimasu ka.", "eng": "When will you depart?"},
            {"speaker": "B", "jp": "準備ができてから出発します。", "kana": "じゅんびができてからしゅっぱつします。", "romaji": "Junbi ga dekite kara shuppatsu shimasu.", "eng": "I will depart after I am ready."},
        ]
    },

    # =============================================
    # CATEGORY: REQUESTS
    # =============================================
    {
        "id": "te_kudasai",
        "pattern": "〜てください",
        "category": "Requests",
        "meaning": "Please do ~ (polite request)",
        "structure": "Verb (te-form) + ください",
        "formation": "Attach ください to the te-form of any verb. This is the standard polite request. ください alone means 'please give me (something)'. When added to a te-form verb, it becomes a request for an action.",
        "formal": "ここに名前を書いてください。— Please write your name here.",
        "casual": "ここに名前書いて。— (drop ください, use te-form alone as casual request)",
        "common_mistakes": "✗ 書くください — must use te-form. ✓ 書いてください. Also, for stronger requests: 〜てくださいませんか (even more polite, asking 'would you please').",
        "jlpt_traps": "てください is a KEY grammar point. Know all te-form conversions. ましょうか is an offer, ませんか is an invitation — different from ください which is a direct request.",
        "related": ["〜をください", "〜てもいいですか", "〜てくれますか"],
        "differences": "てください (polite request) vs てくれますか (asking a favor, slightly softer) vs てくださいませんか (very polite request).",
        "examples": [
            {"jp": "もう一度言ってください。", "kana": "もういちどいってください。", "romaji": "Mou ichido itte kudasai.", "eng": "Please say it one more time."},
            {"jp": "ゆっくり話してください。", "kana": "ゆっくりはなしてください。", "romaji": "Yukkuri hanashite kudasai.", "eng": "Please speak slowly."},
            {"jp": "窓を閉めてください。", "kana": "まどをしめてください。", "romaji": "Mado o shimete kudasai.", "eng": "Please close the window."},
            {"jp": "ちょっと待ってください。", "kana": "ちょっとまってください。", "romaji": "Chotto matte kudasai.", "eng": "Please wait a moment."},
            {"jp": "ここに座ってください。", "kana": "ここにすわってください。", "romaji": "Koko ni suwatte kudasai.", "eng": "Please sit here."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "すみません、もう少し大きい声で話してください。", "kana": "すみません、もうすこしおおきいこえではなしてください。", "romaji": "Sumimasen, mou sukoshi ookii koe de hanashite kudasai.", "eng": "Excuse me, please speak a little louder."},
            {"speaker": "B", "jp": "あ、すみません。これでいいですか。", "kana": "あ、すみません。これでいいですか。", "romaji": "A, sumimasen. Kore de ii desu ka.", "eng": "Oh, sorry. Is this okay?"},
        ]
    },

    # =============================================
    # CATEGORY: INVITATIONS
    # =============================================
    {
        "id": "masen_ka",
        "pattern": "〜ませんか",
        "category": "Invitations",
        "meaning": "Won't you ~? / Would you like to ~? (invitation)",
        "structure": "Verb (masu-stem) + ませんか",
        "formation": "Take the ます-form of the verb, replace ます with ませんか. This is a soft invitation or suggestion. The negative question form creates a more indirect, polite invitation.",
        "formal": "一緒に映画を見ませんか。— Would you like to watch a movie together?",
        "casual": "映画見ない？— (using plain negative with rising intonation for casual invitation)",
        "common_mistakes": "✗ Confusing ませんか (invitation) with ましょうか (offer to do something). 一緒に行きませんか = 'Shall we go?' (invitation). 荷物を持ちましょうか = 'Shall I carry the luggage?' (offer).",
        "jlpt_traps": "ませんか (invitation to listener) vs ましょうか (offer from speaker). Know the difference.",
        "related": ["〜ましょう", "〜ましょうか"],
        "differences": "ませんか = invitation ('won't you join me?'). ましょう = 'let's do it together' (speaker already decided). ましょうか = 'shall I do it for you?' (offer).",
        "examples": [
            {"jp": "一緒に昼ごはんを食べませんか。", "kana": "いっしょにひるごはんをたべませんか。", "romaji": "Issho ni hirugohan o tabemasen ka.", "eng": "Won't you eat lunch with me?"},
            {"jp": "公園を散歩しませんか。", "kana": "こうえんをさんぽしませんか。", "romaji": "Kouen o sanpo shimasen ka.", "eng": "Would you like to take a walk in the park?"},
            {"jp": "コーヒーでも飲みませんか。", "kana": "コーヒーでものみませんか。", "romaji": "Koohii demo nomimasen ka.", "eng": "How about drinking some coffee?"},
            {"jp": "今度、うちへ来ませんか。", "kana": "こんど、うちへきませんか。", "romaji": "Kondo, uchi e kimasen ka.", "eng": "Won't you come to my place sometime?"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "この後、カラオケに行きませんか。", "kana": "このあと、カラオケにいきませんか。", "romaji": "Kono ato, karaoke ni ikimasen ka.", "eng": "Won't you go to karaoke after this?"},
            {"speaker": "B", "jp": "いいですね！ぜひ行きましょう。", "kana": "いいですね！ぜひいきましょう。", "romaji": "Ii desu ne! Zehi ikimashou.", "eng": "That sounds great! Let's definitely go."},
        ]
    },
    {
        "id": "mashou",
        "pattern": "〜ましょう",
        "category": "Invitations",
        "meaning": "Let's ~ / Shall we ~",
        "structure": "Verb (masu-stem) + ましょう",
        "formation": "Replace ます with ましょう. This is the volitional form in polite speech, used to: (1) suggest doing something together, (2) express one's own strong intention.",
        "formal": "出発しましょう。— Let's depart.",
        "casual": "行こう！— Let's go! (plain volitional form: replace る→よう, Group 1: change final u to ou)",
        "common_mistakes": "✗ Using ましょう for something only the speaker does (use つもりです for personal intention). ましょう always implies mutual action.",
        "jlpt_traps": "ましょうか (shall I? = offer) vs ましょう (let's = mutual suggestion).",
        "related": ["〜ませんか", "〜ましょうか"],
        "differences": "ましょう = 'let's do X'. ませんか = 'won't you do X with me?' (softer, still an invitation). ましょう is more decisive.",
        "examples": [
            {"jp": "さあ、始めましょう。", "kana": "さあ、はじめましょう。", "romaji": "Saa, hajimemashou.", "eng": "Well then, let's begin."},
            {"jp": "一緒に勉強しましょう。", "kana": "いっしょにべんきょうしましょう。", "romaji": "Issho ni benkyou shimashou.", "eng": "Let's study together."},
            {"jp": "もう帰りましょう。", "kana": "もうかえりましょう。", "romaji": "Mou kaerimashou.", "eng": "Let's go home already."},
            {"jp": "ここで休みましょう。", "kana": "ここでやすみましょう。", "romaji": "Koko de yasumimashou.", "eng": "Let's rest here."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "もう遅いですね。", "kana": "もうおそいですね。", "romaji": "Mou osoi desu ne.", "eng": "It's already late, isn't it?"},
            {"speaker": "B", "jp": "そうですね。帰りましょう。", "kana": "そうですね。かえりましょう。", "romaji": "Sou desu ne. Kaerimashou.", "eng": "You're right. Let's go home."},
        ]
    },

    # =============================================
    # CATEGORY: PERMISSION
    # =============================================
    {
        "id": "te_mo_ii_desu",
        "pattern": "〜てもいいです",
        "category": "Permission",
        "meaning": "It's okay to ~ / You may ~ (giving permission)",
        "structure": "Verb (te-form) + もいいです",
        "formation": "Attach もいいです to the te-form. To ask for permission: 〜てもいいですか (may I...?). To deny permission: 〜てはいけません (must not). もいいです literally means 'even doing X is fine'.",
        "formal": "ここで写真を撮ってもいいです。— You may take photos here.",
        "casual": "ここで写真撮っていいよ。",
        "common_mistakes": "Confusing giving permission (〜てもいいです) with asking for it (〜てもいいですか). The question form is critical.",
        "jlpt_traps": "〜てもいいですか (may I?) is a very common JLPT question structure. Know how to form it from any verb's te-form.",
        "related": ["〜てはいけません", "〜てください"],
        "differences": "てもいいです (permission given/OK) vs てはいけません (prohibition/must not) vs なければなりません (obligation/must do).",
        "examples": [
            {"jp": "ここに座ってもいいですか。", "kana": "ここにすわってもいいですか。", "romaji": "Koko ni suwatte mo ii desu ka.", "eng": "May I sit here?"},
            {"jp": "はい、座ってもいいですよ。", "kana": "はい、すわってもいいですよ。", "romaji": "Hai, suwatte mo ii desu yo.", "eng": "Yes, you may sit."},
            {"jp": "窓を開けてもいいですか。", "kana": "まどをあけてもいいですか。", "romaji": "Mado o akete mo ii desu ka.", "eng": "May I open the window?"},
            {"jp": "もう帰ってもいいです。", "kana": "もうかえってもいいです。", "romaji": "Mou kaette mo ii desu.", "eng": "You may go home now."},
            {"jp": "質問してもいいですか。", "kana": "しつもんしてもいいですか。", "romaji": "Shitsumon shite mo ii desu ka.", "eng": "May I ask a question?"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "先生、辞書を使ってもいいですか。", "kana": "せんせい、じしょをつかってもいいですか。", "romaji": "Sensei, jisho o tsukatte mo ii desu ka.", "eng": "Teacher, may I use a dictionary?"},
            {"speaker": "B", "jp": "いいえ、テストの間は使ってはいけません。", "kana": "いいえ、テストのあいだはつかってはいけません。", "romaji": "Iie, tesuto no aida wa tsukatte wa ikemasen.", "eng": "No, you must not use one during the test."},
        ]
    },

    # =============================================
    # CATEGORY: PROHIBITION
    # =============================================
    {
        "id": "te_wa_ikemasen",
        "pattern": "〜てはいけません",
        "category": "Prohibition",
        "meaning": "Must not ~ / It is not allowed to ~",
        "structure": "Verb (te-form) + はいけません",
        "formation": "Attach はいけません to the te-form. This is the standard way to express prohibition in polite speech. いけない (casual) is very common too. A stronger form: 〜てはならない (must not, stronger/literary).",
        "formal": "ここでタバコを吸ってはいけません。— You must not smoke here.",
        "casual": "ここでタバコ吸っちゃダメ。/ 吸ってはダメ。",
        "common_mistakes": "✗ Using ていけません without は (the は is required). Also, don't confuse with 〜てもいいです. These are opposites.",
        "jlpt_traps": "てはいけません is DIRECTLY tested. Know that: te-form + はいけません = prohibition. Negation of permission.",
        "related": ["〜てもいいです", "〜なければなりません"],
        "differences": "てはいけません (prohibition: don't do X) vs なければなりません (obligation: must do X). These are conceptual opposites.",
        "examples": [
            {"jp": "試験中に話してはいけません。", "kana": "しけんちゅうにはなしてはいけません。", "romaji": "Shiken chuu ni hanashite wa ikemasen.", "eng": "You must not talk during the exam."},
            {"jp": "ここで食べてはいけません。", "kana": "ここでたべてはいけません。", "romaji": "Koko de tabete wa ikemasen.", "eng": "You must not eat here."},
            {"jp": "遅刻してはいけません。", "kana": "ちこくしてはいけません。", "romaji": "Chikoku shite wa ikemasen.", "eng": "You must not be late."},
            {"jp": "嘘をついてはいけません。", "kana": "うそをついてはいけません。", "romaji": "Uso o tsuite wa ikemasen.", "eng": "You must not tell lies."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "携帯電話を使ってもいいですか。", "kana": "けいたいでんわをつかってもいいですか。", "romaji": "Keitai denwa o tsukatte mo ii desu ka.", "eng": "May I use my cell phone?"},
            {"speaker": "B", "jp": "授業中は使ってはいけません。", "kana": "じゅぎょうちゅうはつかってはいけません。", "romaji": "Jugyou chuu wa tsukatte wa ikemasen.", "eng": "You must not use it during class."},
        ]
    },

    # =============================================
    # CATEGORY: OBLIGATION
    # =============================================
    {
        "id": "nakereba_narimasen",
        "pattern": "〜なければなりません / 〜なくてはいけません",
        "category": "Obligation",
        "meaning": "Must ~ / Have to ~",
        "structure": "Verb (nai-form, replace い with ければ) + なりません | Verb (nai-form, replace い with くては) + いけません",
        "formation": "Two main patterns for obligation:\n1. Verb (neg stem) + なければなりません\n2. Verb (neg stem) + なくてはいけません\nBoth mean 'must do'. Formation: take the nai-form (ない form), remove the い, then add either ければなりません or くてはいけません.\nExample: 食べる → 食べない → 食べなければなりません (must eat).",
        "formal": "毎日薬を飲まなければなりません。— I must take medicine every day.",
        "casual": "毎日薬飲まなきゃ。/ 飲まなくちゃ。(Very casual contractions)",
        "common_mistakes": "The formation is complex. Remember: ない → drop い → add ければ/くては. Don't say ✗ 飲むなければ.",
        "jlpt_traps": "JLPT tests this heavily. Four forms to know: なければなりません / なくてはいけません / なきゃ / なくちゃ. All mean 'must'. なきゃ and なくちゃ are casual contractions.",
        "related": ["〜てもいいです", "〜てはいけません"],
        "differences": "なければなりません (formal, must) vs なくてはいけません (also formal, slightly softer nuance) vs なきゃ (very casual).\n\nNote on nuance: なりません = 'will not do' (emphasizing the consequence), いけません = 'not good' (emphasizing the moral/rule aspect). In practice, interchangeable.",
        "examples": [
            {"jp": "明日、早く起きなければなりません。", "kana": "あした、はやくおきなければなりません。", "romaji": "Ashita, hayaku okinakereba narimasen.", "eng": "I must wake up early tomorrow."},
            {"jp": "宿題を出さなくてはいけません。", "kana": "しゅくだいをださなくてはいけません。", "romaji": "Shukudai o dasanakute wa ikemasen.", "eng": "I must submit the homework."},
            {"jp": "毎日練習しなければなりません。", "kana": "まいにちれんしゅうしなければなりません。", "romaji": "Mainichi renshuu shinakereba narimasen.", "eng": "I must practice every day."},
            {"jp": "レポートを書かなきゃ。", "kana": "レポートをかかなきゃ。", "romaji": "Repooto o kakanakya.", "eng": "I gotta write the report. (casual)"},
            {"jp": "もっと野菜を食べなくちゃ。", "kana": "もっとやさいをたべなくちゃ。", "romaji": "Motto yasai o tabenakucha.", "eng": "I gotta eat more vegetables. (casual)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "なんで急いでいるの？", "kana": "なんでいそいでいるの？", "romaji": "Nande isoide iru no?", "eng": "Why are you in a hurry?"},
            {"speaker": "B", "jp": "５時までに会社に戻らなければなりません。", "kana": "ごじまでにかいしゃにもどらなければなりません。", "romaji": "Goji made ni kaisha ni modorana kereba narimasen.", "eng": "I have to return to the office by 5 o'clock."},
        ]
    },

    # =============================================
    # CATEGORY: DESIRE
    # =============================================
    {
        "id": "tai_desu",
        "pattern": "〜たいです",
        "category": "Desire",
        "meaning": "Want to ~ (speaker's own desire)",
        "structure": "Verb (masu-stem) + たいです",
        "formation": "Remove ます from the masu-form. Add たいです. たい is an い-adjective, so it conjugates like one: たい → たくない (not want), たかった (wanted), たくなかった (didn't want).",
        "formal": "日本に行きたいです。— I want to go to Japan.",
        "casual": "日本に行きたい。",
        "common_mistakes": "✗ Using たいです for OTHERS' desires. For third person, use 〜たがっています (he seems to want to). ✗ 彼は行きたいです (sounds odd — use 行きたがっています). Exception: questions are fine: 何を食べたいですか (what do you want to eat?).",
        "jlpt_traps": "たい is treated as an い-adjective. So negative is たくない, past is たかった. This conjugation is tested.",
        "related": ["〜ほしいです", "〜たいと思います"],
        "differences": "たいです (want to DO something — verb). ほしいです (want to HAVE something — noun).",
        "examples": [
            {"jp": "寿司を食べたいです。", "kana": "すしをたべたいです。", "romaji": "Sushi o tabetai desu.", "eng": "I want to eat sushi."},
            {"jp": "日本語が上手になりたいです。", "kana": "にほんごがじょうずになりたいです。", "romaji": "Nihongo ga jouzu ni naritai desu.", "eng": "I want to become good at Japanese."},
            {"jp": "もっと早く帰りたかったです。", "kana": "もっとはやくかえりたかったです。", "romaji": "Motto hayaku kaeritakatta desu.", "eng": "I wanted to go home earlier."},
            {"jp": "何を飲みたいですか。", "kana": "なにをのみたいですか。", "romaji": "Nani o nomitai desu ka.", "eng": "What do you want to drink?"},
            {"jp": "旅行したいです。でもお金がありません。", "kana": "りょこうしたいです。でもおかねがありません。", "romaji": "Ryokou shitai desu. Demo okane ga arimasen.", "eng": "I want to travel. But I have no money."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "将来、何になりたいですか。", "kana": "しょうらい、なになりたいですか。", "romaji": "Shourai, nani ni naritai desu ka.", "eng": "What do you want to become in the future?"},
            {"speaker": "B", "jp": "医者になりたいです。", "kana": "いしゃになりたいです。", "romaji": "Isha ni naritai desu.", "eng": "I want to become a doctor."},
        ]
    },
    {
        "id": "hoshii_desu",
        "pattern": "〜ほしいです",
        "category": "Desire",
        "meaning": "Want (to have) ~ (desire for a noun/thing)",
        "structure": "Noun + が + ほしいです",
        "formation": "ほしい is an い-adjective. Used with nouns (things you want to possess/have). Subject is always the speaker. For third person desire for a noun: ほしがっています.",
        "formal": "新しいパソコンがほしいです。— I want a new computer.",
        "casual": "新しいパソコンがほしい。",
        "common_mistakes": "✗ Using ほしいです for verbs (use たいです). ✗ 泳ぐほしいです → ✓ 泳ぎたいです. ほしい = want to HAVE a thing.",
        "jlpt_traps": "ほしい (adjective) vs たい (desire for action). Mix them up and you make a fundamental error.",
        "related": ["〜たいです"],
        "differences": "ほしいです + NOUN (want to have). たいです + VERB (want to do). 'I want a car' = 車がほしい. 'I want to drive' = 運転したい.",
        "examples": [
            {"jp": "新しい車がほしいです。", "kana": "あたらしいくるまがほしいです。", "romaji": "Atarashii kuruma ga hoshii desu.", "eng": "I want a new car."},
            {"jp": "友達がほしいです。", "kana": "ともだちがほしいです。", "romaji": "Tomodachi ga hoshii desu.", "eng": "I want friends."},
            {"jp": "何がほしいですか。", "kana": "なにがほしいですか。", "romaji": "Nani ga hoshii desu ka.", "eng": "What do you want?"},
            {"jp": "時間がほしかったです。", "kana": "じかんがほしかったです。", "romaji": "Jikan ga hoshikatta desu.", "eng": "I wanted time."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "誕生日プレゼントは何がほしいですか。", "kana": "たんじょうびプレゼントはなにがほしいですか。", "romaji": "Tanjoubi purezento wa nani ga hoshii desu ka.", "eng": "What do you want for a birthday present?"},
            {"speaker": "B", "jp": "新しい本がほしいです。", "kana": "あたらしいほんがほしいです。", "romaji": "Atarashii hon ga hoshii desu.", "eng": "I want a new book."},
        ]
    },

    # =============================================
    # CATEGORY: ABILITY
    # =============================================
    {
        "id": "koto_ga_dekimasu",
        "pattern": "〜ことができます",
        "category": "Ability",
        "meaning": "Can ~ / Is able to ~",
        "structure": "Verb (dictionary form) + ことができます",
        "formation": "Dictionary form + こと (nominalizer) + が + できます. The こと turns the verb phrase into a noun ('the act of doing'). A simpler alternative for many verbs: Verb-stem + ます form → potential form (e.g., 食べる → 食べられる). Both mean 'can'.",
        "formal": "日本語を話すことができます。— I can speak Japanese.",
        "casual": "日本語が話せる。— (Using potential verb form, which is more natural in casual speech)",
        "common_mistakes": "✗ Using the te-form with ことができます. Always use the DICTIONARY form. Also, the potential form (食べられる) is more natural in casual speech than ことができます.",
        "jlpt_traps": "Both ことができます AND the potential form (-られる/-える) express ability. JLPT may test transforming between them.",
        "related": ["〜たいです", "Potential Verb Forms"],
        "differences": "ことができます (more formal/emphatic) vs potential verb (more natural/casual). ピアノを弾くことができます = ピアノが弾けます.",
        "examples": [
            {"jp": "日本語を読むことができます。", "kana": "にほんごをよむことができます。", "romaji": "Nihongo o yomu koto ga dekimasu.", "eng": "I can read Japanese."},
            {"jp": "ここで駐車することができません。", "kana": "ここでちゅうしゃすることができません。", "romaji": "Koko de chuusha suru koto ga dekimasen.", "eng": "You cannot park here."},
            {"jp": "泳ぐことができますか。", "kana": "およぐことができますか。", "romaji": "Oyogu koto ga dekimasu ka.", "eng": "Can you swim?"},
            {"jp": "子供のころ、ピアノを弾くことができました。", "kana": "こどものころ、ピアノをひくことができました。", "romaji": "Kodomo no koro, piano o hiku koto ga dekimashita.", "eng": "When I was a child, I could play the piano."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "車の運転ができますか。", "kana": "くるまのうんてんができますか。", "romaji": "Kuruma no unten ga dekimasu ka.", "eng": "Can you drive a car?"},
            {"speaker": "B", "jp": "はい、できます。でも自転車の方が好きです。", "kana": "はい、できます。でもじてんしゃのほうがすきです。", "romaji": "Hai, dekimasu. Demo jitensha no hou ga suki desu.", "eng": "Yes, I can. But I prefer bicycles."},
        ]
    },

    # =============================================
    # CATEGORY: COMPARISON
    # =============================================
    {
        "id": "comparison",
        "pattern": "〜より / 〜のほうが / 〜いちばん",
        "category": "Comparison",
        "meaning": "More than ~ / ~ is more ~ / The most ~",
        "structure": "A より B のほうが (quality) | A が いちばん (quality)",
        "formation": "Comparison: 'A より B のほうが 〜です' → 'B is more ~ than A'. Note the order: A (the lesser one) comes with より, B (the winner) comes with のほうが.\n\nSuperlative: 'A が いちばん 〜です' → 'A is the most ~' (among some group, often stated with の中で).",
        "formal": "東京は大阪より大きいです。— Tokyo is bigger than Osaka.",
        "casual": "東京の方が大きい。",
        "common_mistakes": "✗ Putting のほうが on the LESSER item (opposite of English). In English 'A is bigger than B' — A is the winner. In Japanese, 'A より B の方が大きい' — B is the winner. The item after より is the baseline comparison (the lesser one).",
        "jlpt_traps": "AよりBのほうが is tested heavily. Know which item comes with より (the inferior) and which with のほうが (the superior). Also, いちばん for superlatives.",
        "related": ["Question: AとBとどちらが〜ですか"],
        "differences": "より (than) + のほうが (the one that is more). いちばん (the most/best - superlative).",
        "examples": [
            {"jp": "夏より冬のほうが好きです。", "kana": "なつよりふゆのほうがすきです。", "romaji": "Natsu yori fuyu no hou ga suki desu.", "eng": "I like winter more than summer."},
            {"jp": "電車はバスより速いです。", "kana": "でんしゃはバスよりはやいです。", "romaji": "Densha wa basu yori hayai desu.", "eng": "The train is faster than the bus."},
            {"jp": "日本語の中で、漢字がいちばん難しいです。", "kana": "にほんごのなかで、かんじがいちばんむずかしいです。", "romaji": "Nihongo no naka de, kanji ga ichiban muzukashii desu.", "eng": "Among Japanese, kanji is the hardest."},
            {"jp": "このクラスでだれがいちばん背が高いですか。", "kana": "このクラスでだれがいちばんせがたかいですか。", "romaji": "Kono kurasu de dare ga ichiban se ga takai desu ka.", "eng": "Who is the tallest in this class?"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "肉と魚とどちらが好きですか。", "kana": "にくとさかなとどちらがすきですか。", "romaji": "Niku to sakana to dochira ga suki desu ka.", "eng": "Which do you prefer, meat or fish?"},
            {"speaker": "B", "jp": "魚のほうが好きです。", "kana": "さかなのほうがすきです。", "romaji": "Sakana no hou ga suki desu.", "eng": "I prefer fish."},
        ]
    },

    # =============================================
    # CATEGORY: EXPERIENCE & HABITS (TE-IRU)
    # =============================================
    {
        "id": "te_imasu",
        "pattern": "〜ています",
        "category": "Experience & Habits",
        "meaning": "Is doing ~ / Does ~ (habitually) / Is in a state of ~",
        "structure": "Verb (te-form) + います",
        "formation": "Attach います to the te-form. This is one of the most versatile and important grammar patterns in Japanese. It has FOUR main meanings — context determines which applies.",
        "formal": "Depends on meaning. See examples below.",
        "casual": "〜ている → contracted to 〜てる in casual speech.",
        "common_mistakes": "✗ Thinking 〜ています always means 'currently doing'. It often means a RESULTING STATE or HABIT. '結婚しています' = 'I am married (resultant state)', NOT 'I am currently getting married'.",
        "jlpt_traps": "The FOUR meanings are critical:\n1. 現在進行 (Current action): 今、本を読んでいます。(I am reading a book right now.)\n2. 習慣 (Habit): 毎朝ジョギングしています。(I jog every morning.)\n3. 結果状態 (Resulting state): 窓が開いています。(The window is open [as a result of opening].)\n4. 職業・状態 (Occupation/State): 会社で働いています。(I work at a company.)",
        "related": ["〜たり〜たりします", "〜ながら"],
        "differences": "ています (ongoing/habitual/state) vs ました (completed action, past tense) vs ます (simple habitual/future polite).",
        "examples": [
            {"jp": "今、テレビを見ています。", "kana": "いま、テレビをみています。", "romaji": "Ima, terebi o mite imasu.", "eng": "(1) CURRENT ACTION: I am watching TV right now."},
            {"jp": "毎日英語を勉強しています。", "kana": "まいにちえいごをべんきょうしています。", "romaji": "Mainichi eigo o benkyou shite imasu.", "eng": "(2) HABIT: I study English every day."},
            {"jp": "結婚しています。", "kana": "けっこんしています。", "romaji": "Kekkon shite imasu.", "eng": "(3) RESULTING STATE: I am married."},
            {"jp": "銀行で働いています。", "kana": "ぎんこうではたらいています。", "romaji": "Ginkou de hataraite imasu.", "eng": "(4) OCCUPATION: I work at a bank."},
            {"jp": "電気がついています。", "kana": "でんきがついています。", "romaji": "Denki ga tsuite imasu.", "eng": "(3) STATE: The light is on."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "今、何をしていますか。", "kana": "いま、なにをしていますか。", "romaji": "Ima, nani o shite imasu ka.", "eng": "What are you doing right now?"},
            {"speaker": "B", "jp": "日本語を勉強しています。", "kana": "にほんごをべんきょうしています。", "romaji": "Nihongo o benkyou shite imasu.", "eng": "I am studying Japanese."},
        ]
    },

    # =============================================
    # CATEGORY: SEQUENTIAL ACTIONS
    # =============================================
    {
        "id": "tari_tari",
        "pattern": "〜たり〜たりします",
        "category": "Sequential Actions",
        "meaning": "Do things like ~ and ~ (among other things)",
        "structure": "Verb (ta-form) + り + Verb (ta-form) + り + します",
        "formation": "Take the た-form (past plain form) of verbs and add り to each. The final verb します closes the pattern. It expresses a non-exhaustive list of actions — implying there are other things too. Can also express alternating states.",
        "formal": "週末は映画を見たり、本を読んだりします。— On weekends, I do things like watching movies and reading books.",
        "casual": "週末、映画見たり本読んだりする。",
        "common_mistakes": "✗ Using the て-form instead of た-form + り. 食べてり (wrong) → 食べたり (correct). Also, ✗ stopping after one たり. You need at least two たり phrases (A たり B たり), OR one たり + する which implies 'sometimes'.",
        "jlpt_traps": "たり〜たり is about a NON-EXHAUSTIVE list. 'I do things like A and B'. It does NOT mean 'I only do A and B'.",
        "related": ["〜て (sequential)", "〜や〜など"],
        "differences": "〜て (sequential actions, ordered: A then B) vs 〜たり〜たり (listing activities without order, implying more exist).",
        "examples": [
            {"jp": "休みの日は、音楽を聴いたり、散歩したりします。", "kana": "やすみのひは、おんがくをきいたり、さんぽしたりします。", "romaji": "Yasumi no hi wa, ongaku o kiitari, sanpo shitari shimasu.", "eng": "On my days off, I do things like listen to music and take walks."},
            {"jp": "授業中に寝たり、話したりしないでください。", "kana": "じゅぎょうちゅうにねたり、はなしたりしないでください。", "romaji": "Jugyou chuu ni netari, hanashitari shinaide kudasai.", "eng": "Please don't do things like sleep and talk during class."},
            {"jp": "彼は来たり来なかったりします。", "kana": "かれはきたりこなかったりします。", "romaji": "Kare wa kitari konakattari shimasu.", "eng": "He sometimes comes and sometimes doesn't. (alternating states)"},
            {"jp": "子供のころ、公園で走ったり、自転車に乗ったりしていました。", "kana": "こどものころ、こうえんではしったり、じてんしゃにのったりしていました。", "romaji": "Kodomo no koro, kouen de hashittari, jitensha ni nottari shite imashita.", "eng": "When I was a child, I used to do things like run in the park and ride my bicycle."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "旅行で何をしましたか。", "kana": "りょこうでなにをしましたか。", "romaji": "Ryokou de nani o shimashita ka.", "eng": "What did you do on the trip?"},
            {"speaker": "B", "jp": "観光したり、美味しいものを食べたりしました。", "kana": "かんこうしたり、おいしいものをたべたりしました。", "romaji": "Kankou shitari, oishii mono o tabetari shimashita.", "eng": "I did things like sightseeing and eating delicious food."},
        ]
    },

    # =============================================
    # CATEGORY: REASONS
    # =============================================
    {
        "id": "kara_node",
        "pattern": "〜から / 〜ので",
        "category": "Reasons",
        "meaning": "Because ~ / So ~ (giving reasons)",
        "structure": "Clause + から / Clause + ので + Result clause",
        "formation": "Both から and ので attach to the end of a reason clause to connect it to the result/conclusion. The reason comes FIRST in Japanese (opposite emphasis from English sometimes).\n\nFrom PLAIN form or polite form:\n- から: attaches to both plain and polite forms\n- ので: typically attaches to plain forms (な-adj and nouns need なので)",
        "formal": "体が悪いので、今日は休みます。— Because I am not feeling well, I will rest today.",
        "casual": "体が悪いから今日休む。",
        "common_mistakes": "✗ Using から/ので at the start of a sentence (they mark reason clauses, not starters). Also, ✗ だから at the end (だから is a sentence-initial connector 'so...').",
        "jlpt_traps": "KEY DIFFERENCE: から sounds more direct/assertive. ので sounds softer and more objective (implying 'naturally, given this reason...'). ので is more polite. ので is preferred in formal speech.",
        "related": ["〜けど/けれど", "〜のに"],
        "differences": "から (direct reason, subjective, slightly demanding/assertive) vs ので (objective reason, softer, more polite/formal). When asking for favors: ので sounds better. When making excuses: either works.",
        "examples": [
            {"jp": "疲れているから、早く寝ます。", "kana": "つかれているから、はやくねます。", "romaji": "Tsukarete iru kara, hayaku nemasu.", "eng": "Because I am tired, I will go to sleep early."},
            {"jp": "明日試験があるので、今日は勉強します。", "kana": "あしたしけんがあるので、きょうはべんきょうします。", "romaji": "Ashita shiken ga aru node, kyou wa benkyou shimasu.", "eng": "Because there is an exam tomorrow, I will study today."},
            {"jp": "雨が降っているから、外出しません。", "kana": "あめがふっているから、がいしゅつしません。", "romaji": "Ame ga futte iru kara, gaishutsu shimasen.", "eng": "Because it is raining, I will not go out."},
            {"jp": "体の具合が悪いので、休ませてください。", "kana": "からだのぐあいがわるいので、やすませてください。", "romaji": "Karada no guai ga warui node, yasumasete kudasai.", "eng": "Because I am not feeling well, please let me rest. (ので = softer/more polite)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "どうして日本語を勉強していますか。", "kana": "どうしてにほんごをべんきょうしていますか。", "romaji": "Doushite nihongo o benkyou shite imasu ka.", "eng": "Why are you studying Japanese?"},
            {"speaker": "B", "jp": "日本が大好きなので、日本語を学んでいます。", "kana": "にほんがだいすきなので、にほんごをまなんでいます。", "romaji": "Nihon ga daisuki na node, nihongo o manande imasu.", "eng": "Because I love Japan very much, I am learning Japanese."},
        ]
    },

    # =============================================
    # CATEGORY: OPINIONS
    # =============================================
    {
        "id": "to_omoimasu",
        "pattern": "〜とおもいます",
        "category": "Opinions",
        "meaning": "I think that ~",
        "structure": "Clause (plain form) + とおもいます",
        "formation": "The clause before と must be in PLAIN form (not polite ます/です). とおもいます = 'I think that...'. The と is a quotation particle. To ask for an opinion: 〜とおもいますか. For negative thought: 〜とはおもいません.",
        "formal": "日本語はむずかしいとおもいます。— I think Japanese is difficult.",
        "casual": "日本語はむずかしいと思う。",
        "common_mistakes": "✗ Using polite form before と: 日本語はむずかしいですとおもいます → Wrong. Must use plain form: むずかしい (い-adj stays same), 好きだとおもいます (na-adj + だ), 学生だとおもいます (noun + だ).",
        "jlpt_traps": "The plain form requirement before とおもいます is tested. Also know: 〜ないとおもいます (I don't think that) vs 〜とはおもいません (more emphatic: I don't think so).",
        "related": ["〜とはおもいません", "〜つもりです"],
        "differences": "とおもいます (I think...) vs でしょう (probably/conjecture) vs かもしれません (might be).",
        "examples": [
            {"jp": "彼は来ないとおもいます。", "kana": "かれはこないとおもいます。", "romaji": "Kare wa konai to omoimasu.", "eng": "I think he won't come."},
            {"jp": "この問題はむずかしいとおもいます。", "kana": "このもんだいはむずかしいとおもいます。", "romaji": "Kono mondai wa muzukashii to omoimasu.", "eng": "I think this problem is difficult."},
            {"jp": "彼女は学生だとおもいます。", "kana": "かのじょはがくせいだとおもいます。", "romaji": "Kanojo wa gakusei da to omoimasu.", "eng": "I think she is a student."},
            {"jp": "日本は安全だとおもいます。", "kana": "にほんはあんぜんだとおもいます。", "romaji": "Nihon wa anzen da to omoimasu.", "eng": "I think Japan is safe."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "この映画、どうおもいますか。", "kana": "このえいが、どうおもいますか。", "romaji": "Kono eiga, dou omoimasu ka.", "eng": "What do you think about this movie?"},
            {"speaker": "B", "jp": "すごくおもしろいとおもいます。", "kana": "すごくおもしろいとおもいます。", "romaji": "Sugoku omoshiroi to omoimasu.", "eng": "I think it is very interesting."},
        ]
    },

    # =============================================
    # CATEGORY: INTENTIONS
    # =============================================
    {
        "id": "tsumori_desu",
        "pattern": "〜つもりです",
        "category": "Intentions",
        "meaning": "Intend to ~ / Plan to ~",
        "structure": "Verb (dictionary form) + つもりです",
        "formation": "Dictionary form + つもりです. Negative: 〜ないつもりです (I intend not to do). つもり is a noun meaning 'intention/expectation'. So this literally means 'it is my intention to...'.",
        "formal": "来年、日本語能力試験を受けるつもりです。— I intend to take the JLPT next year.",
        "casual": "来年、日本語の試験受けるつもり。",
        "common_mistakes": "✗ Confusing つもりです with 予定です. つもりです = personal intention (may not have concrete plans). 予定です = scheduled plan (more concrete, 'I have plans to').",
        "jlpt_traps": "つもりです vs 予定です: つもり is vague intention, 予定 is a concrete schedule. 来年、日本に行くつもりです = I intend to go (my intention). 来年３月に日本へ行く予定です = I am scheduled to go in March (concrete).",
        "related": ["〜とおもいます", "〜予定です"],
        "differences": "つもりです (intention — internal decision). 予定です (plan/schedule — external arrangement). とおもいます (think/conjecture — opinion). だろうと思っています (thinking of doing, most uncertain).",
        "examples": [
            {"jp": "大学を卒業したら、就職するつもりです。", "kana": "だいがくをそつぎょうしたら、しゅうしょくするつもりです。", "romaji": "Daigaku o sotsugyou shitara, shuushoku suru tsumori desu.", "eng": "After graduating from university, I intend to get a job."},
            {"jp": "今年の夏は旅行するつもりです。", "kana": "ことしのなつはりょこうするつもりです。", "romaji": "Kotoshi no natsu wa ryokou suru tsumori desu.", "eng": "I intend to travel this summer."},
            {"jp": "タバコはやめるつもりです。", "kana": "タバコはやめるつもりです。", "romaji": "Tabako wa yameru tsumori desu.", "eng": "I intend to quit smoking."},
            {"jp": "二度と遅刻しないつもりです。", "kana": "にどとちこくしないつもりです。", "romaji": "Nido to chikoku shinai tsumori desu.", "eng": "I intend to never be late again."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "将来、どこに住むつもりですか。", "kana": "しょうらい、どこにすむつもりですか。", "romaji": "Shourai, doko ni sumu tsumori desu ka.", "eng": "Where do you intend to live in the future?"},
            {"speaker": "B", "jp": "日本に住むつもりです。", "kana": "にほんにすむつもりです。", "romaji": "Nihon ni sumu tsumori desu.", "eng": "I intend to live in Japan."},
        ]
    },

    # =============================================
    # CATEGORY: SIMULTANEOUS ACTIONS
    # =============================================
    {
        "id": "nagara",
        "pattern": "〜ながら",
        "category": "Simultaneous Actions",
        "meaning": "While doing ~ (simultaneously)",
        "structure": "Verb (masu-stem) + ながら + Main verb",
        "formation": "Remove ます from the masu-form, add ながら. The action marked by ながら is the SECONDARY action. The main (more important) action is the second verb. Both actions are performed by the SAME subject simultaneously.",
        "formal": "音楽を聴きながら勉強します。— I study while listening to music.",
        "casual": "音楽聴きながら勉強する。",
        "common_mistakes": "✗ Using ながら when subjects are DIFFERENT. ながら requires same subject doing both actions. ✗ Using it for unrelated sequential actions (use て-form for sequential). ✗ Using て-form of the verb before ながら (must be masu-stem).",
        "jlpt_traps": "ながら = same subject, simultaneous. 〜ているとき = 'when ~ is happening' (can be different subjects). 〜あいだ = 'while/during a duration' (different subjects possible).",
        "related": ["〜ているとき", "〜あいだ"],
        "differences": "ながら (two actions simultaneously, same person) vs ているとき (when/at the time of). ながら implies genuine multitasking.",
        "examples": [
            {"jp": "歩きながら電話をします。", "kana": "あるきながらでんわをします。", "romaji": "Aruki nagara denwa o shimasu.", "eng": "I talk on the phone while walking."},
            {"jp": "テレビを見ながら、ご飯を食べます。", "kana": "テレビをみながら、ごはんをたべます。", "romaji": "Terebi o mi nagara, gohan o tabemasu.", "eng": "I eat while watching TV."},
            {"jp": "笑いながら話しました。", "kana": "わらいながらはなしました。", "romaji": "Warai nagara hanashimashita.", "eng": "I spoke while laughing."},
            {"jp": "働きながら大学に通っています。", "kana": "はたらきながらだいがくにかよっています。", "romaji": "Hataraki nagara daigaku ni kayotte imasu.", "eng": "I commute to university while working."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "よく音楽を聴きながら走りますか。", "kana": "よくおんがくをきながらはしりますか。", "romaji": "Yoku ongaku o ki nagara hashirimasu ka.", "eng": "Do you often run while listening to music?"},
            {"speaker": "B", "jp": "はい、ジョギングしながらよく聴きます。", "kana": "はい、ジョギングしながらよくきます。", "romaji": "Hai, jogingu shi nagara yoku kikimasu.", "eng": "Yes, I often listen while jogging."},
        ]
    },

    # =============================================
    # CATEGORY: CONJECTURE
    # =============================================
    {
        "id": "deshou",
        "pattern": "〜でしょう / 〜だろう",
        "category": "Conjecture",
        "meaning": "Probably ~ / I suppose ~ (conjecture/probability)",
        "structure": "Plain form + でしょう (formal) / だろう (casual)",
        "formation": "でしょう is the conjectural copula. Attach to plain form verbs, adjectives, nouns. Expresses the speaker's REASONABLE GUESS or expectation about something uncertain. With rising intonation (でしょう↗), it asks for confirmation ('isn't it?').",
        "formal": "明日は雨でしょう。— It will probably rain tomorrow.",
        "casual": "明日は雨だろう。/ 雨だろうね。",
        "common_mistakes": "✗ Using でしょう for confirmed facts. It implies uncertainty/guess. Don't use it for things you know for certain.",
        "jlpt_traps": "でしょう (reasonable guess, fairly confident) vs かもしれません (might be, more uncertain). でしょう = ~70%+ confident. かもしれません = ~50% or lower.",
        "related": ["〜かもしれません", "〜とおもいます"],
        "differences": "でしょう (probably, fairly confident, logical inference) vs かもしれません (might be, less certain) vs とおもいます (I think, based on opinion).",
        "examples": [
            {"jp": "明日は晴れでしょう。", "kana": "あしたははれでしょう。", "romaji": "Ashita wa hare deshou.", "eng": "It will probably be sunny tomorrow."},
            {"jp": "彼はもう知っているでしょう。", "kana": "かれはもうしっているでしょう。", "romaji": "Kare wa mou shitte iru deshou.", "eng": "He probably already knows."},
            {"jp": "そこは高いでしょう。", "kana": "そこはたかいでしょう。", "romaji": "Soko wa takai deshou.", "eng": "That place is probably expensive."},
            {"jp": "難しいでしょうが、がんばってください。", "kana": "むずかしいでしょうが、がんばってください。", "romaji": "Muzukashii deshou ga, ganbatte kudasai.", "eng": "It will probably be difficult, but please do your best."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "山田さんは来ますか。", "kana": "やまださんはきますか。", "romaji": "Yamada-san wa kimasu ka.", "eng": "Will Yamada-san come?"},
            {"speaker": "B", "jp": "来るでしょう。たぶん。", "kana": "くるでしょう。たぶん。", "romaji": "Kuru deshou. Tabun.", "eng": "They'll probably come. I think."},
        ]
    },
    {
        "id": "kamoshiremasen",
        "pattern": "〜かもしれません",
        "category": "Conjecture",
        "meaning": "Might ~ / May ~ (possibility, less certain)",
        "structure": "Plain form + かもしれません",
        "formation": "Attach かもしれません directly to the plain form. For nouns and na-adjectives: Noun/Na-adj (no だ needed) + かもしれません. This expresses a POSSIBILITY that the speaker is unsure about.",
        "formal": "彼は来ないかもしれません。— He might not come.",
        "casual": "彼は来ないかも。(Very common casual contraction: かも alone)",
        "common_mistakes": "✗ Using で after nouns before かもしれません. Correct: 学生かもしれません (NOT 学生でかもしれません).",
        "jlpt_traps": "かもしれません = possibility (speaker not sure). でしょう = more confident guess. JLPT tests the difference.",
        "related": ["〜でしょう", "〜とおもいます"],
        "differences": "かもしれません (might, ~50% or uncertain) vs でしょう (probably, ~70%+ confident). 'It might rain' = 雨かもしれません. 'It will probably rain' = 雨でしょう.",
        "examples": [
            {"jp": "彼女は病気かもしれません。", "kana": "かのじょはびょうきかもしれません。", "romaji": "Kanojo wa byouki kamoshiremasen.", "eng": "She might be sick."},
            {"jp": "明日は雨かもしれません。傘を持って行って。", "kana": "あしたはあめかもしれません。かさをもっていって。", "romaji": "Ashita wa ame kamoshiremasen. Kasa o motte itte.", "eng": "It might rain tomorrow. Take an umbrella."},
            {"jp": "電車が遅れているかもしれません。", "kana": "でんしゃがおくれているかもしれません。", "romaji": "Densha ga okurete iru kamoshiremasen.", "eng": "The train might be late."},
            {"jp": "これは本物じゃないかも。", "kana": "これはほんものじゃないかも。", "romaji": "Kore wa honmono ja nai kamo.", "eng": "This might not be real. (casual)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "田中さんはどこですか。", "kana": "たなかさんはどこですか。", "romaji": "Tanaka-san wa doko desu ka.", "eng": "Where is Tanaka-san?"},
            {"speaker": "B", "jp": "まだ外かもしれません。", "kana": "まだそとかもしれません。", "romaji": "Mada soto kamoshiremasen.", "eng": "They might still be outside."},
        ]
    },

    # =============================================
    # CATEGORY: LIMITS
    # =============================================
    {
        "id": "dake_shika",
        "pattern": "〜だけ / 〜しか〜ません",
        "category": "Limits",
        "meaning": "Only ~ / Nothing but ~ (limiting expressions)",
        "structure": "Noun + だけ (です/が/etc.) | Noun + しか + Negative verb",
        "formation": "Two ways to express 'only':\n1. だけ: Neutral 'only'. 'I ate only sushi' = 寿司だけ食べました. No negative verb required.\n2. しか〜ない: Exclusive 'only' — implies there is nothing else / it is insufficient. ALWAYS requires a NEGATIVE predicate. '寿司しか食べませんでした' = 'I ate nothing but sushi' (implying disappointment or that it was the only option).",
        "formal": "今日は百円しかありません。— I only have 100 yen (and that's all / it's not enough).",
        "casual": "百円しかない。",
        "common_mistakes": "✗ Using しか with a POSITIVE verb. Correct: しか + NEGATIVE. 水しか飲みません (✓) vs ✗ 水しか飲みます. だけ has no such restriction.",
        "jlpt_traps": "しか ALWAYS requires negative verb. だけ does not. These are directly tested. The nuance: だけ is neutral ('I just have 100 yen'), しか〜ない implies insufficiency or limitation ('I only have 100 yen — that's all I have').",
        "related": ["〜しかない", "〜ばかり"],
        "differences": "だけ (neutral 'only', positive or negative OK) vs しか〜ない (emphatic 'nothing but', always negative, nuance of insufficiency or exclusivity).",
        "examples": [
            {"jp": "一つだけください。", "kana": "ひとつだけください。", "romaji": "Hitotsu dake kudasai.", "eng": "Please give me just one."},
            {"jp": "水しか飲みませんでした。", "kana": "みずしかのみませんでした。", "romaji": "Mizu shika nomimasen deshita.", "eng": "I drank nothing but water. (implied: only water, perhaps disappointed)"},
            {"jp": "彼女だけが知っている。", "kana": "かのじょだけがしっている。", "romaji": "Kanojo dake ga shitte iru.", "eng": "Only she knows."},
            {"jp": "三人しか来ませんでした。", "kana": "さんにんしかきませんでした。", "romaji": "San nin shika kimasen deshita.", "eng": "Only three people came. (implied: fewer than expected)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "お金はありますか。", "kana": "おかねはありますか。", "romaji": "Okane wa arimasu ka.", "eng": "Do you have money?"},
            {"speaker": "B", "jp": "五百円しかありません。", "kana": "ごひゃくえんしかありません。", "romaji": "Gohyaku en shika arimasen.", "eng": "I only have 500 yen. (It's not enough)"},
        ]
    },

    # =============================================
    # CATEGORY: LISTING
    # =============================================
    {
        "id": "ya_nado",
        "pattern": "〜や〜など",
        "category": "Listing",
        "meaning": "~ and ~ and so on / things like ~",
        "structure": "Noun + や + Noun + など",
        "formation": "や is used to list nouns in a NON-EXHAUSTIVE way (implies there are more items). など (etcetera) is often added at the end to reinforce this. Contrast with と which lists ALL items exhaustively.",
        "formal": "冷蔵庫にりんごやバナナなどがあります。— There are things like apples and bananas in the refrigerator.",
        "casual": "冷蔵庫にりんごやバナナとかある。(とか is a more casual equivalent of や〜など)",
        "common_mistakes": "✗ Using や when you want to list EVERYTHING exactly (use と). 'I bought a pen AND a notebook (and nothing else)' = ペンとノートを買いました. 'I bought things like pens and notebooks' = ペンやノートなどを買いました.",
        "jlpt_traps": "や (non-exhaustive list) vs と (exhaustive list). This is a crucial particle distinction tested on JLPT.",
        "related": ["〜と (exhaustive list)", "〜たり〜たりします"],
        "differences": "や〜など (non-exhaustive list of nouns: 'A, B, and so on') vs と (exhaustive: 'A and B, that's it') vs たり〜たり (non-exhaustive list of ACTIONS).",
        "examples": [
            {"jp": "スーパーでりんごやみかんなどを買いました。", "kana": "スーパーでりんごやみかんなどをかいました。", "romaji": "Suupaa de ringo ya mikan nado o kaimashita.", "eng": "I bought things like apples and mandarin oranges at the supermarket."},
            {"jp": "趣味は料理や読書などです。", "kana": "しゅみはりょうりやどくしょなどです。", "romaji": "Shumi wa ryouri ya dokusho nado desu.", "eng": "My hobbies include things like cooking and reading."},
            {"jp": "日本では桜や富士山などが有名です。", "kana": "にほんではさくらやふじさんなどがゆうめいです。", "romaji": "Nihon dewa sakura ya Fujisan nado ga yuumei desu.", "eng": "In Japan, things like cherry blossoms and Mt. Fuji are famous."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "冷蔵庫に何がありますか。", "kana": "れいぞうこになにがありますか。", "romaji": "Reizouko ni nani ga arimasu ka.", "eng": "What is in the refrigerator?"},
            {"speaker": "B", "jp": "牛乳や卵などがあります。", "kana": "ぎゅうにゅうやたまごなどがあります。", "romaji": "Gyuunyuu ya tamago nado ga arimasu.", "eng": "There are things like milk and eggs."},
        ]
    },

    # =============================================
    # CATEGORY: GIVING & RECEIVING
    # =============================================
    {
        "id": "ageru_morau_kureru",
        "pattern": "あげます / もらいます / くれます",
        "category": "Giving & Receiving",
        "meaning": "Give / Receive / Give (to me)",
        "structure": "A が B に (thing) を あげます | A が B に (thing) を もらいます | A が (私に) (thing) を くれます",
        "formation": "These three verbs are the core of Japanese giving-receiving expressions. The DIRECTION of the giving determines which verb to use:\n\n• あげます (ageru): I/someone GIVES to another (outward direction). 'I give to you/him/her'.\n• もらいます (morau): I/someone RECEIVES from another (inward direction). 'I receive from him/her'.\n• くれます (kureru): Someone GIVES TO ME (or my in-group). Special verb — subject is always the giver, the recipient is always the speaker or someone close.",
        "formal": "先生に本をもらいました。— I received a book from the teacher.",
        "casual": "先生に本もらった。",
        "common_mistakes": "✗ Using あげます when someone gives TO YOU (use くれます). 友達が本をあげました → Wrong if the friend gave it to you! Correct: 友達が本をくれました. あげます for outgoing giving. くれます for incoming giving (to me/in-group).",
        "jlpt_traps": "The あげます/もらいます/くれます distinction is one of the MOST TESTED N5 grammar points. Draw the direction: あげます = → (away from speaker). くれます = → (toward speaker). もらいます = speaker receives.",
        "related": ["〜てあげます", "〜てもらいます", "〜てくれます"],
        "differences": "あげます: giver is speaker or 3rd person, recipient is NOT the speaker. くれます: giver is 3rd person, recipient IS the speaker. もらいます: receiver is speaker, giver is 3rd person.",
        "examples": [
            {"jp": "友達に誕生日プレゼントをあげました。", "kana": "ともだちにたんじょうびプレゼントをあげました。", "romaji": "Tomodachi ni tanjoubi purezento o agemashita.", "eng": "I gave a birthday present to my friend. (I → friend)"},
            {"jp": "友達が誕生日プレゼントをくれました。", "kana": "ともだちがたんじょうびプレゼントをくれました。", "romaji": "Tomodachi ga tanjoubi purezento o kuremashita.", "eng": "My friend gave me a birthday present. (friend → me)"},
            {"jp": "先生に本をもらいました。", "kana": "せんせいにほんをもらいました。", "romaji": "Sensei ni hon o moraimashita.", "eng": "I received a book from the teacher. (I receive ← teacher)"},
            {"jp": "母にお菓子をあげました。", "kana": "ははにおかしをあげました。", "romaji": "Haha ni okashi o agemashita.", "eng": "I gave sweets to my mother. (I → mom)"},
            {"jp": "彼女がカードをくれました。", "kana": "かのじょがカードをくれました。", "romaji": "Kanojo ga kaado o kuremashita.", "eng": "My girlfriend gave me a card. (girlfriend → me)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "その辞書は誰にもらいましたか。", "kana": "そのじしょはだれにもらいましたか。", "romaji": "Sono jisho wa dare ni moraimashita ka.", "eng": "Who did you receive that dictionary from?"},
            {"speaker": "B", "jp": "先生がくれました。", "kana": "せんせいがくれました。", "romaji": "Sensei ga kuremashita.", "eng": "My teacher gave it to me."},
        ]
    },

    # =============================================
    # CATEGORY: ADVICE
    # =============================================
    {
        "id": "ta_hou_ga_ii",
        "pattern": "〜たほうがいいです",
        "category": "Advice",
        "meaning": "You should ~ / It's better to ~",
        "structure": "Verb (ta-form) + ほうがいいです | Verb (nai-form) + ほうがいいです",
        "formation": "Positive advice: た-form + ほうがいいです (you should do X). Negative advice: ない-form + ほうがいいです (you should not do X). ほう means 'direction/side', so literally 'the doing-X direction is better'.",
        "formal": "もっと野菜を食べたほうがいいですよ。— You should eat more vegetables.",
        "casual": "もっと野菜食べたほうがいいよ。",
        "common_mistakes": "✗ Using dictionary form before ほうがいいです (a common error): 食べるほうがいいです — this is actually used for COMPARING options, not advice. For advice to someone, use the た-form.",
        "jlpt_traps": "たほうがいいです vs ないほうがいいです. Know which form expresses 'should do' (た-form) and 'should not do' (ない-form).",
        "related": ["〜なければなりません", "〜てください"],
        "differences": "たほうがいいです (gentle advice/recommendation) vs なければなりません (strong obligation/must). The former is a suggestion, the latter is a rule/duty.",
        "examples": [
            {"jp": "早く寝たほうがいいです。", "kana": "はやくねたほうがいいです。", "romaji": "Hayaku neta hou ga ii desu.", "eng": "You should go to bed early."},
            {"jp": "タバコを吸わないほうがいいです。", "kana": "タバコをすわないほうがいいです。", "romaji": "Tabako o suwanai hou ga ii desu.", "eng": "You should not smoke."},
            {"jp": "雨が降りそうですよ。傘を持って行ったほうがいいです。", "kana": "あめがふりそうですよ。かさをもっていったほうがいいです。", "romaji": "Ame ga furi sou desu yo. Kasa o motte itta hou ga ii desu.", "eng": "It looks like it's going to rain. You should take an umbrella."},
            {"jp": "もっと練習したほうがいいとおもいます。", "kana": "もっとれんしゅうしたほうがいいとおもいます。", "romaji": "Motto renshuu shita hou ga ii to omoimasu.", "eng": "I think you should practice more."},
        ],
        "conversation": [
            {"speaker": "A", "jp": "最近、体の調子が悪くて。", "kana": "さいきん、からだのちょうしがわるくて。", "romaji": "Saikin, karada no choushi ga warukute.", "eng": "Recently I haven't been feeling well."},
            {"speaker": "B", "jp": "早めに病院に行ったほうがいいですよ。", "kana": "はやめにびょういんにいったほうがいいですよ。", "romaji": "Hayame ni byouin ni itta hou ga ii desu yo.", "eng": "You should go to the hospital soon."},
        ]
    },

    # =============================================
    # CATEGORY: NOUN MODIFICATION
    # =============================================
    {
        "id": "no_modifier",
        "pattern": "〜の (Noun Modifier)",
        "category": "Noun Modification",
        "meaning": "Possessive / Attribute / Connecting nouns",
        "structure": "Noun1 + の + Noun2 (Noun1 modifies Noun2)",
        "formation": "の is the possessive/connecting particle. It links two nouns: 'Noun1's Noun2' or 'Noun2 of/from/at Noun1'. It creates noun phrases. Unlike English, the modifier always comes BEFORE the main noun.",
        "formal": "山田さんの本です。— It is Yamada-san's book.",
        "casual": "山田さんの本。",
        "common_mistakes": "✗ の attaches nouns to nouns, not to verbs/adjectives directly. For verb clauses modifying nouns, the verb must be in plain form directly before the noun (no の needed in most cases).",
        "jlpt_traps": "の has many uses: (1) possessive, (2) appositive/descriptor (東京の大学 = university in Tokyo), (3) pronoun replacing a noun (これは山田さんのです = This is Yamada-san's [one]).",
        "related": ["Relative clauses (plain form + noun)"],
        "differences": "の (noun-noun connection, possessive) vs が (subject marker) vs は (topic marker). These are three different functions.",
        "examples": [
            {"jp": "これは私の本です。", "kana": "これはわたしのほんです。", "romaji": "Kore wa watashi no hon desu.", "eng": "This is my book."},
            {"jp": "東京の大学で勉強しています。", "kana": "とうきょうのだいがくでべんきょうしています。", "romaji": "Toukyou no daigaku de benkyou shite imasu.", "eng": "I study at a university in Tokyo."},
            {"jp": "日本語の勉強は楽しいです。", "kana": "にほんごのべんきょうはたのしいです。", "romaji": "Nihongo no benkyou wa tanoshii desu.", "eng": "Japanese study is fun."},
            {"jp": "その赤いのをください。", "kana": "そのあかいのをください。", "romaji": "Sono akai no o kudasai.", "eng": "Please give me that red one. (の as pronoun)"},
        ],
        "conversation": [
            {"speaker": "A", "jp": "これは誰の傘ですか。", "kana": "これはだれのかさですか。", "romaji": "Kore wa dare no kasa desu ka.", "eng": "Whose umbrella is this?"},
            {"speaker": "B", "jp": "私のです。", "kana": "わたしのです。", "romaji": "Watashi no desu.", "eng": "It is mine."},
        ]
    },
]

# ==============================================================
# TE-FORM MASTER SECTION
# ==============================================================

TE_FORM_DATA = {
    "title": "Te-Form Master Guide",
    "intro": "The Te-form (〜て form) is the MOST IMPORTANT form in Japanese. It is used in 6+ grammar patterns. Mastering Te-form unlocks requests, permissions, prohibitions, sequential actions, ongoing actions, and more.",
    "groups": [
        {
            "name": "Group 1 Verbs (U-verbs / Godan)",
            "description": "Verbs ending in any う-column sound. The te-form depends on the LAST character of the dictionary form.",
            "rules": [
                {"ending": "く", "te_form": "いて", "example_dict": "書く", "example_te": "書いて", "example_eng": "write"},
                {"ending": "ぐ", "te_form": "いで", "example_dict": "泳ぐ", "example_te": "泳いで", "example_eng": "swim"},
                {"ending": "む", "te_form": "んで", "example_dict": "読む", "example_te": "読んで", "example_eng": "read"},
                {"ending": "ぶ", "te_form": "んで", "example_dict": "遊ぶ", "example_te": "遊んで", "example_eng": "play"},
                {"ending": "ぬ", "te_form": "んで", "example_dict": "死ぬ", "example_te": "死んで", "example_eng": "die"},
                {"ending": "す", "te_form": "して", "example_dict": "話す", "example_te": "話して", "example_eng": "speak"},
                {"ending": "つ", "te_form": "って", "example_dict": "待つ", "example_te": "待って", "example_eng": "wait"},
                {"ending": "る", "te_form": "って", "example_dict": "帰る", "example_te": "帰って", "example_eng": "return (home)"},
                {"ending": "う", "te_form": "って", "example_dict": "買う", "example_te": "買って", "example_eng": "buy"},
            ],
            "exceptions": [
                {"dict": "行く", "te": "行って", "note": "Exception! く normally → いて, but 行く (iku) → 行って (itte). Must memorize!"},
            ]
        },
        {
            "name": "Group 2 Verbs (RU-verbs / Ichidan)",
            "description": "Verbs ending in る where the preceding syllable is in the い-row or え-row. Drop る, add て.",
            "rules": [
                {"ending": "る (after i/e sound)", "te_form": "て", "example_dict": "食べる", "example_te": "食べて", "example_eng": "eat"},
                {"ending": "る (after i/e sound)", "te_form": "て", "example_dict": "見る", "example_te": "見て", "example_eng": "see"},
                {"ending": "る (after i/e sound)", "te_form": "て", "example_dict": "起きる", "example_te": "起きて", "example_eng": "wake up"},
                {"ending": "る (after i/e sound)", "te_form": "て", "example_dict": "できる", "example_te": "できて", "example_eng": "can do"},
            ],
            "exceptions": []
        },
        {
            "name": "Group 3 Verbs (Irregular)",
            "description": "Only two irregular verbs. MUST be memorized.",
            "rules": [
                {"ending": "する", "te_form": "して", "example_dict": "勉強する", "example_te": "勉強して", "example_eng": "study"},
                {"ending": "くる", "te_form": "きて", "example_dict": "来る", "example_te": "来て", "example_eng": "come"},
            ],
            "exceptions": []
        }
    ],
    "usages": [
        {
            "title": "① Request (〜てください)",
            "pattern": "Te-form + ください",
            "meaning": "Please do ~",
            "example_jp": "ゆっくり話してください。",
            "example_eng": "Please speak slowly."
        },
        {
            "title": "② Permission (〜てもいいです)",
            "pattern": "Te-form + もいいです",
            "meaning": "It's okay to ~ / May I ~?",
            "example_jp": "ここに座ってもいいですか。",
            "example_eng": "May I sit here?"
        },
        {
            "title": "③ Prohibition (〜てはいけません)",
            "pattern": "Te-form + はいけません",
            "meaning": "Must not ~",
            "example_jp": "ここで話してはいけません。",
            "example_eng": "You must not talk here."
        },
        {
            "title": "④ Sequential Action (〜て、〜)",
            "pattern": "Te-form + next clause",
            "meaning": "Do A, then do B",
            "example_jp": "手を洗って、ご飯を食べます。",
            "example_eng": "I wash my hands and then eat."
        },
        {
            "title": "⑤ Ongoing Action (〜ています)",
            "pattern": "Te-form + います",
            "meaning": "Is doing ~ / Has done ~ (ongoing state)",
            "example_jp": "今、本を読んでいます。",
            "example_eng": "I am reading a book right now."
        },
        {
            "title": "⑥ Giving/Receiving Favors",
            "pattern": "Te-form + あげます/くれます/もらいます",
            "meaning": "Do ~ for someone / Have someone do ~",
            "example_jp": "荷物を持ってあげました。",
            "example_eng": "I carried the luggage for them."
        },
    ]
}

# ==============================================================
# GRAMMAR RELATIONSHIP MAP
# ==============================================================

GRAMMAR_MAP = [
    {
        "title": "The Core Verb Forms & Their Grammar",
        "nodes": [
            {"level": 0, "name": "Dictionary Form (plain non-past)", "color": "#3B82F6"},
            {"level": 1, "name": "Masu Form (polite present/future)", "color": "#8B5CF6", "connects_from": "Drop る/u sound + ます"},
            {"level": 2, "name": "Te Form", "color": "#10B981", "connects_from": "Complex te-form rules →"},
            {"level": 3, "name": "→ Request (〜てください)", "color": "#34D399", "connects_from": "Te + ください"},
            {"level": 3, "name": "→ Permission (〜てもいいです)", "color": "#34D399", "connects_from": "Te + もいいです"},
            {"level": 3, "name": "→ Prohibition (〜てはいけません)", "color": "#EF4444", "connects_from": "Te + はいけません"},
            {"level": 3, "name": "→ Progressive (〜ています)", "color": "#34D399", "connects_from": "Te + います"},
            {"level": 3, "name": "→ Sequential Actions (〜て、〜)", "color": "#34D399", "connects_from": "Te + next clause"},
            {"level": 2, "name": "Nai Form (plain negative)", "color": "#F59E0B", "connects_from": "Replace u → anai"},
            {"level": 3, "name": "→ Obligation (〜なければなりません)", "color": "#FCD34D", "connects_from": "Nai stem + ければなりません"},
            {"level": 3, "name": "→ Negative Advice (〜ないほうがいいです)", "color": "#FCD34D", "connects_from": "Nai + ほうがいいです"},
            {"level": 2, "name": "Ta Form (past plain)", "color": "#EC4899", "connects_from": "Same rule as te-form, replace て/で → た/だ"},
            {"level": 3, "name": "→ Experience (〜たことがあります)", "color": "#F9A8D4", "connects_from": "Ta + ことがあります"},
            {"level": 3, "name": "→ Advice (〜たほうがいいです)", "color": "#F9A8D4", "connects_from": "Ta + ほうがいいです"},
            {"level": 3, "name": "→ After (〜たあとで)", "color": "#F9A8D4", "connects_from": "Ta + あとで"},
            {"level": 1, "name": "Volitional Form (let's / intend)", "color": "#8B5CF6", "connects_from": "Masu stem + ましょう"},
            {"level": 3, "name": "→ Invitation (〜ましょう)", "color": "#C4B5FD", "connects_from": "Masu stem + ましょう"},
        ]
    }
]

# ==============================================================
# REVISION SETS
# ==============================================================

REVISION_SETS = {
    "top25": [
        "desu", "dewa_arimasen", "deshita", "desu_ka",
        "ga_arimasu", "ga_imasu", "ni_arimasu",
        "e_ikimasu", "te_kudasai", "masen_ka", "mashou",
        "te_mo_ii_desu", "te_wa_ikemasen", "nakereba_narimasen",
        "tai_desu", "hoshii_desu", "koto_ga_dekimasu",
        "te_imasu", "kara_node", "to_omoimasu", "tsumori_desu",
        "ageru_morau_kureru", "ta_hou_ga_ii", "comparison", "dake_shika"
    ],
    "top50": "all",  # All grammar points listed above
    "exam_focus": [
        "te_wa_ikemasen", "te_mo_ii_desu", "nakereba_narimasen",
        "ta_hou_ga_ii", "te_imasu", "kara_node",
        "ageru_morau_kureru", "comparison", "dake_shika",
        "mae_ni", "ato_de", "te_kara", "tsumori_desu",
        "tari_tari", "nagara", "deshou", "kamoshiremasen",
        "koto_ga_dekimasu", "ya_nado"
    ],
    "one_day_sheet": [
        "desu", "dewa_arimasen", "desu_ka",
        "ga_arimasu", "ga_imasu", "e_ikimasu",
        "te_kudasai", "masen_ka", "te_mo_ii_desu",
        "te_wa_ikemasen", "nakereba_narimasen",
        "tai_desu", "te_imasu", "kara_node",
        "ageru_morau_kureru", "comparison"
    ]
}

# ==============================================================
# QUESTION WORDS REFERENCE
# ==============================================================

QUESTION_WORDS = [
    {"word": "何（なに）", "romaji": "nani", "meaning": "What (before ga, o, ni, etc.)", "example_jp": "何がありますか。", "example_eng": "What is there?"},
    {"word": "何（なん）", "romaji": "nan", "meaning": "What (before desu, counter, d/n/t sounds)", "example_jp": "何ですか。", "example_eng": "What is it?"},
    {"word": "だれ", "romaji": "dare", "meaning": "Who", "example_jp": "だれですか。", "example_eng": "Who is it?"},
    {"word": "どこ", "romaji": "doko", "meaning": "Where", "example_jp": "どこへ行きますか。", "example_eng": "Where are you going?"},
    {"word": "いつ", "romaji": "itsu", "meaning": "When", "example_jp": "いつ来ますか。", "example_eng": "When will you come?"},
    {"word": "なぜ", "romaji": "naze", "meaning": "Why (formal/literary)", "example_jp": "なぜ泣いていますか。", "example_eng": "Why are you crying?"},
    {"word": "どうして", "romaji": "doushite", "meaning": "Why (common spoken)", "example_jp": "どうして遅れましたか。", "example_eng": "Why were you late?"},
    {"word": "どう", "romaji": "dou", "meaning": "How (what way)", "example_jp": "日本語はどうですか。", "example_eng": "How is Japanese?"},
    {"word": "どんな", "romaji": "donna", "meaning": "What kind of (adjective)", "example_jp": "どんな映画が好きですか。", "example_eng": "What kind of movies do you like?"},
    {"word": "どれ", "romaji": "dore", "meaning": "Which one (of 3 or more)", "example_jp": "どれがいいですか。", "example_eng": "Which one is good?"},
    {"word": "どちら / どっち", "romaji": "dochira / docchi", "meaning": "Which (of two) / Which way (polite)", "example_jp": "どちらが好きですか。", "example_eng": "Which do you prefer?"},
    {"word": "いくつ", "romaji": "ikutsu", "meaning": "How many / How old", "example_jp": "りんごはいくつありますか。", "example_eng": "How many apples are there?"},
    {"word": "いくら", "romaji": "ikura", "meaning": "How much (price)", "example_jp": "これはいくらですか。", "example_eng": "How much is this?"},
]

# ==============================================================
# LOCATION WORDS REFERENCE
# ==============================================================

LOCATION_WORDS = [
    {"word": "うえ（上）", "romaji": "ue", "meaning": "Above / On top of", "example_jp": "机の上に本があります。", "example_eng": "There is a book on the desk."},
    {"word": "した（下）", "romaji": "shita", "meaning": "Below / Under", "example_jp": "椅子の下に猫がいます。", "example_eng": "There is a cat under the chair."},
    {"word": "なか（中）", "romaji": "naka", "meaning": "Inside / In", "example_jp": "箱の中に何がありますか。", "example_eng": "What is inside the box?"},
    {"word": "そと（外）", "romaji": "soto", "meaning": "Outside", "example_jp": "外で遊んでいます。", "example_eng": "Playing outside."},
    {"word": "まえ（前）", "romaji": "mae", "meaning": "In front of / Before", "example_jp": "駅の前で待っています。", "example_eng": "Waiting in front of the station."},
    {"word": "うしろ（後ろ）", "romaji": "ushiro", "meaning": "Behind / In back of", "example_jp": "後ろを見てください。", "example_eng": "Please look behind you."},
    {"word": "みぎ（右）", "romaji": "migi", "meaning": "Right", "example_jp": "右に曲がってください。", "example_eng": "Please turn right."},
    {"word": "ひだり（左）", "romaji": "hidari", "meaning": "Left", "example_jp": "左の建物が病院です。", "example_eng": "The building on the left is the hospital."},
    {"word": "となり（隣）", "romaji": "tonari", "meaning": "Next to / Adjacent", "example_jp": "銀行の隣に郵便局があります。", "example_eng": "There is a post office next to the bank."},
    {"word": "ちかく（近く）", "romaji": "chikaku", "meaning": "Near / Nearby", "example_jp": "駅の近くに住んでいます。", "example_eng": "I live near the station."},
    {"word": "むこう（向こう）", "romaji": "mukou", "meaning": "Over there / Across", "example_jp": "向こうに山があります。", "example_eng": "There is a mountain over there."},
    {"word": "あいだ（間）", "romaji": "aida", "meaning": "Between", "example_jp": "AとBの間にあります。", "example_eng": "It is between A and B."},
]
