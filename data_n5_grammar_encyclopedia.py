"""Data for Complete N5 Grammar Encyclopedia."""

N5_GRAMMAR_ENCYCLOPEDIA = [
    {
        "category": "Basic Sentences",
        "jlpt_category": "Core Sentence Endings",
        "pattern": "〜です / 〜ではありません / 〜でした / 〜ではありませんでした",
        "meaning": "Polite copula forms: is, is not, was, was not",
        "english_concept": "Identity and state",
        "structure": "Noun/Na-adjective + です/ではありません/でした/ではありませんでした",
        "formation": "Attach copula to nouns and na-adjectives. Use でした for past, and ではありません for negation.",
        "conjugation": "Present affirmative: です; Present negative: ではありません; Past affirmative: でした; Past negative: ではありませんでした",
        "formal": "こちらは図書館です。",
        "casual": "ここ、図書館だよ。",
        "mistakes": "Using these forms with i-adjectives directly (e.g. たかいですでした) is incorrect.",
        "traps": "N5 often tests noun/na-adjective copula vs i-adjective past (〜かったです).",
        "related": "〜ですか, noun modification 〜の",
        "differences": "です-family is for noun/na-adjective predicates, not direct verb conjugation.",
        "examples": [
            ("私は学生です。", "わたしはがくせいです。", "watashi wa gakusei desu", "I am a student."),
            ("この町は静かではありません。", "このまちはしずかではありません。", "kono machi wa shizuka dewa arimasen", "This town is not quiet."),
            ("昨日は休みでした。", "きのうはやすみでした。", "kinou wa yasumi deshita", "Yesterday was a day off."),
            ("その店は有名ではありませんでした。", "そのみせはゆうめいではありませんでした。", "sono mise wa yuumei dewa arimasen deshita", "That shop was not famous."),
            ("今日は土曜日です。", "きょうはどようびです。", "kyou wa doyoubi desu", "Today is Saturday.")
        ],
        "conversation": [
            ("A: 田中さんは先生ですか。", "A: たなかさんはせんせいですか。", "A: Tanaka-san wa sensei desu ka?", "A: Is Mr. Tanaka a teacher?"),
            ("B: いいえ、先生ではありません。", "B: いいえ、せんせいではありません。", "B: Iie, sensei dewa arimasen.", "B: No, he is not a teacher.")
        ]
    },
    {
        "category": "Questions",
        "jlpt_category": "Question Forms",
        "pattern": "〜ですか / Question Words",
        "meaning": "Polite yes-no and WH questions",
        "english_concept": "Asking information",
        "structure": "Sentence + か; WH-word + predicate + か",
        "formation": "Add か at sentence end. Use question words: なに/なん, だれ, どこ, いつ, なぜ, どうして, どう, どんな, どれ, どちら, いくつ, いくら.",
        "conjugation": "Plain form can drop か in casual speech, but this point focuses on polite N5 standard.",
        "formal": "これは何ですか。",
        "casual": "これ、なに？",
        "mistakes": "Confusing なに and なん before counters/classifiers and copula structures.",
        "traps": "JLPT often tests subtle WH-word choice: どれ vs どちら, どう vs どうして.",
        "related": "〜と思います, 〜でしょう",
        "differences": "〜ですか asks directly; 〜でしょうか is softer/politer speculation request.",
        "examples": [
            ("これは何ですか。", "これはなんですか。", "kore wa nan desu ka", "What is this?"),
            ("だれが来ますか。", "だれがきますか。", "dare ga kimasu ka", "Who will come?"),
            ("どこで昼ご飯を食べますか。", "どこでひるごはんをたべますか。", "doko de hirugohan o tabemasu ka", "Where will you eat lunch?"),
            ("いつ日本へ行きますか。", "いつにほんへいきますか。", "itsu nihon e ikimasu ka", "When will you go to Japan?"),
            ("このかばんはいくらですか。", "このかばんはいくらですか。", "kono kaban wa ikura desu ka", "How much is this bag?")
        ],
        "conversation": [
            ("A: どうして日本語を勉強しますか。", "A: どうしてにほんごをべんきょうしますか。", "A: Doushite nihongo o benkyou shimasu ka?", "A: Why do you study Japanese?"),
            ("B: 日本へ行きたいからです。", "B: にほんへいきたいからです。", "B: Nihon e ikitai kara desu.", "B: Because I want to go to Japan.")
        ]
    },
    {
        "category": "Existence",
        "jlpt_category": "Existence Verbs",
        "pattern": "〜があります / 〜います",
        "meaning": "Existence of inanimate vs animate entities",
        "english_concept": "There is/are",
        "structure": "Place に Noun が あります/います",
        "formation": "Use あります for objects/events; use います for people/animals.",
        "conjugation": "Polite negative: ありません/いません; past: ありました/いました.",
        "formal": "教室に先生がいます。",
        "casual": "教室に先生いる。",
        "mistakes": "Using あります for people or animals.",
        "traps": "Plant/tree questions in JLPT are usually treated as あります.",
        "related": "〜にあります, 〜にいます",
        "differences": "あります = non-living presence; います = living presence.",
        "examples": [
            ("机の上に本があります。", "つくえのうえにほんがあります。", "tsukue no ue ni hon ga arimasu", "There is a book on the desk."),
            ("公園に犬がいます。", "こうえんにいぬがいます。", "kouen ni inu ga imasu", "There is a dog in the park."),
            ("駅の前に銀行があります。", "えきのまえにぎんこうがあります。", "eki no mae ni ginkou ga arimasu", "There is a bank in front of the station."),
            ("部屋にだれもいません。", "へやにだれもいません。", "heya ni dare mo imasen", "There is no one in the room."),
            ("時間がありますか。", "じかんがありますか。", "jikan ga arimasu ka", "Do you have time?")
        ],
        "conversation": [
            ("A: 近くにコンビニがありますか。", "A: ちかくにコンビニがありますか。", "A: Chikaku ni konbini ga arimasu ka?", "A: Is there a convenience store nearby?"),
            ("B: はい、あそこにあります。", "B: はい、あそこにあります。", "B: Hai, asoko ni arimasu.", "B: Yes, there is one over there.")
        ]
    },
    {
        "category": "Location",
        "jlpt_category": "Location Expressions",
        "pattern": "〜にあります / 〜にいます + Place Expressions",
        "meaning": "Specify exact location",
        "english_concept": "Position in space",
        "structure": "Noun の place-expression に Noun が あります/います",
        "formation": "Use relative position words: うえ, した, なか, そと, まえ, うしろ, みぎ, ひだり, となり, ちかく.",
        "conjugation": "Location nouns behave as normal nouns before に.",
        "formal": "郵便局は駅のとなりにあります。",
        "casual": "猫はいすの下にいる。",
        "mistakes": "Mixing action location で and existence location に.",
        "traps": "Question may include action verb; then use で, not に.",
        "related": "あります/います, particles に and で",
        "differences": "に marks static existence location; で marks action location.",
        "examples": [
            ("ねこはテーブルの下にいます。", "ねこはテーブルのしたにいます。", "neko wa teeburu no shita ni imasu", "The cat is under the table."),
            ("かばんはつくえの上にあります。", "かばんはつくえのうえにあります。", "kaban wa tsukue no ue ni arimasu", "The bag is on the desk."),
            ("銀行はスーパーのとなりにあります。", "ぎんこうはスーパーのとなりにあります。", "ginkou wa suupaa no tonari ni arimasu", "The bank is next to the supermarket."),
            ("本は箱の中にあります。", "ほんははこのなかにあります。", "hon wa hako no naka ni arimasu", "The book is inside the box."),
            ("駅は学校の近くにあります。", "えきはがっこうのちかくにあります。", "eki wa gakkou no chikaku ni arimasu", "The station is near the school.")
        ],
        "conversation": [
            ("A: トイレはどこにありますか。", "A: トイレはどこにありますか。", "A: Toire wa doko ni arimasu ka?", "A: Where is the restroom?"),
            ("B: エレベーターのうしろにあります。", "B: エレベーターのうしろにあります。", "B: Erebeetaa no ushiro ni arimasu.", "B: It is behind the elevator.")
        ]
    },
    {
        "category": "Movement",
        "jlpt_category": "Movement Patterns",
        "pattern": "〜へいきます / 〜にいきます / 〜へきます / 〜からきます",
        "meaning": "Movement toward/from destination",
        "english_concept": "Go/come movement",
        "structure": "Place へ/に 行きます; Place へ 来ます; Place から 来ます",
        "formation": "へ emphasizes direction, に emphasizes destination point.",
        "conjugation": "Applies with 行きます, 来ます, 帰ります.",
        "formal": "大阪から東京へ来ました。",
        "casual": "学校に行く。",
        "mistakes": "Confusing from-source から with destination particles に/へ.",
        "traps": "In JLPT, both に and へ can be correct; nuance is tested with context.",
        "related": "time particle に, transport で",
        "differences": "へ = direction, に = destination target.",
        "examples": [
            ("毎日学校に行きます。", "まいにちがっこうにいきます。", "mainichi gakkou ni ikimasu", "I go to school every day."),
            ("来週京都へ行きます。", "らいしゅうきょうとへいきます。", "raishuu kyouto e ikimasu", "I will go to Kyoto next week."),
            ("友だちがうちへ来ます。", "ともだちがうちへきます。", "tomodachi ga uchi e kimasu", "My friend will come to my house."),
            ("私はインドから来ました。", "わたしはインドからきました。", "watashi wa indo kara kimashita", "I came from India."),
            ("駅まで歩いて行きます。", "えきまであるいていきます。", "eki made aruite ikimasu", "I walk to the station.")
        ],
        "conversation": [
            ("A: どこへ行きますか。", "A: どこへいきますか。", "A: Doko e ikimasu ka?", "A: Where are you going?"),
            ("B: 図書館に行きます。", "B: としょかんにいきます。", "B: Toshokan ni ikimasu.", "B: I am going to the library.")
        ]
    },
    {
        "category": "Time Expressions",
        "jlpt_category": "Time Sequence",
        "pattern": "〜まえに / 〜あとで / 〜てから",
        "meaning": "Before, after, and after doing",
        "english_concept": "Time order",
        "structure": "Dictionary form + 前に; た-form + 後で; て-form + から",
        "formation": "前に uses dictionary form; 後で uses past form; てから links completed action to next action.",
        "conjugation": "Use verb forms precisely; this is a major N5 test point.",
        "formal": "食事の前に手を洗います。",
        "casual": "ご飯食べたあとで行く。",
        "mistakes": "Using た-form before 前に (wrong in standard N5 grammar).",
        "traps": "てから implies sequence with dependency, not just simple time after.",
        "related": "〜て (sequential), 〜ながら",
        "differences": "後で is broad after-time; てから is action-A then action-B.",
        "examples": [
            ("寝る前に歯をみがきます。", "ねるまえにはをみがきます。", "neru mae ni ha o migakimasu", "I brush my teeth before sleeping."),
            ("授業の後で図書館へ行きます。", "じゅぎょうのあとでとしょかんへいきます。", "jugyou no ato de toshokan e ikimasu", "I go to the library after class."),
            ("朝ご飯を食べてから会社へ行きます。", "あさごはんをたべてからかいしゃへいきます。", "asagohan o tabete kara kaisha e ikimasu", "I go to work after eating breakfast."),
            ("日本へ行く前に日本語を勉強しました。", "にほんへいくまえににほんごをべんきょうしました。", "nihon e iku mae ni nihongo o benkyou shimashita", "I studied Japanese before going to Japan."),
            ("映画を見た後でご飯を食べます。", "えいがをみたあとでごはんをたべます。", "eiga o mita ato de gohan o tabemasu", "I will eat after watching a movie.")
        ],
        "conversation": [
            ("A: 宿題の前に何をしますか。", "A: しゅくだいのまえになにをしますか。", "A: Shukudai no mae ni nani o shimasu ka?", "A: What do you do before homework?"),
            ("B: おふろに入ってから勉強します。", "B: おふろにはいってからべんきょうします。", "B: Ofuro ni haitte kara benkyou shimasu.", "B: I study after taking a bath.")
        ]
    },
    {
        "category": "Requests",
        "jlpt_category": "Request Forms",
        "pattern": "〜てください / 〜をください",
        "meaning": "Please do / Please give",
        "english_concept": "Polite requesting",
        "structure": "Vて + ください; Noun + をください",
        "formation": "Use て-form for action requests and をください for item requests.",
        "conjugation": "Verb must be in correct て-form.",
        "formal": "この書類を見てください。",
        "casual": "これ、ください。",
        "mistakes": "Using をください with verbs.",
        "traps": "てください is stronger than てもらえますか (not in N5 core but appears in conversation).",
        "related": "Permission/prohibition via て-form",
        "differences": "をください asks for things; てください asks for actions.",
        "examples": [
            ("名前を書いてください。", "なまえをかいてください。", "namae o kaite kudasai", "Please write your name."),
            ("ドアを開けてください。", "ドアをあけてください。", "doa o akete kudasai", "Please open the door."),
            ("水をください。", "みずをください。", "mizu o kudasai", "Please give me water."),
            ("りんごを二つください。", "りんごをふたつください。", "ringo o futatsu kudasai", "Please give me two apples."),
            ("ゆっくり話してください。", "ゆっくりはなしてください。", "yukkuri hanashite kudasai", "Please speak slowly.")
        ],
        "conversation": [
            ("A: すみません、メニューをください。", "A: すみません、メニューをください。", "A: Sumimasen, menyuu o kudasai.", "A: Excuse me, please give me the menu."),
            ("B: はい、少々お待ちください。", "B: はい、しょうしょうおまちください。", "B: Hai, shoushou omachi kudasai.", "B: Yes, please wait a moment.")
        ]
    },
    {
        "category": "Invitations",
        "jlpt_category": "Invitation Forms",
        "pattern": "〜ませんか / 〜ましょう",
        "meaning": "Won't you...? / Let's ...",
        "english_concept": "Invitation and proposal",
        "structure": "Vます-stem + ませんか / ましょう",
        "formation": "Take verb stem from ます form and attach invitation ending.",
        "conjugation": "Both forms are polite and common in N5 dialogs.",
        "formal": "一緒に昼ご飯を食べませんか。",
        "casual": "行こう。 (N4-ish plain equivalent)",
        "mistakes": "Confusing listener invitation (ませんか) with speaker proposal (ましょう).",
        "traps": "JLPT listens for polite refusal patterns after ませんか invitations.",
        "related": "〜たいです, 〜つもりです",
        "differences": "ませんか is softer and gives listener choice; ましょう is stronger shared decision.",
        "examples": [
            ("映画を見ませんか。", "えいがをみませんか。", "eiga o mimasen ka", "Won't you watch a movie?"),
            ("土曜日に勉強しませんか。", "どようびにべんきょうしませんか。", "doyoubi ni benkyou shimasen ka", "Won't you study on Saturday?"),
            ("一緒に帰りましょう。", "いっしょにかえりましょう。", "issho ni kaerimashou", "Let's go home together."),
            ("まず自己紹介をしましょう。", "まずじこしょうかいをしましょう。", "mazu jikoshoukai o shimashou", "Let's introduce ourselves first."),
            ("ここで少し休みましょう。", "ここですこしやすみましょう。", "koko de sukoshi yasumimashou", "Let's rest here for a while.")
        ],
        "conversation": [
            ("A: コーヒーを飲みませんか。", "A: コーヒーをのみませんか。", "A: Koohii o nomimasen ka?", "A: Would you like to drink coffee?"),
            ("B: いいですね。飲みましょう。", "B: いいですね。のみましょう。", "B: Ii desu ne. Nomimashou.", "B: Sounds good. Let's drink.")
        ]
    },
    {
        "category": "Permission and Prohibition",
        "jlpt_category": "Rules",
        "pattern": "〜てもいいです / 〜てはいけません",
        "meaning": "May do / Must not do",
        "english_concept": "Allowed vs prohibited actions",
        "structure": "Vて + もいいです; Vて + はいけません",
        "formation": "Use verb て-form as base for both patterns.",
        "conjugation": "Question form: 〜てもいいですか for asking permission.",
        "formal": "ここで写真を撮ってもいいですか。",
        "casual": "入っていい？ / 入っちゃだめ。",
        "mistakes": "Missing て-form before もいい and はいけません.",
        "traps": "Similar options in exam differ only by particle or te-form ending.",
        "related": "〜てください, obligation forms",
        "differences": "てもいい grants allowance; てはいけません gives prohibition.",
        "examples": [
            ("ここで座ってもいいです。", "ここですわってもいいです。", "koko de suwatte mo ii desu", "You may sit here."),
            ("窓を開けてもいいですか。", "まどをあけてもいいですか。", "mado o akete mo ii desu ka", "May I open the window?"),
            ("この部屋で食べてはいけません。", "このへやでたべてはいけません。", "kono heya de tabete wa ikemasen", "You must not eat in this room."),
            ("授業中に話してはいけません。", "じゅぎょうちゅうにはなしてはいけません。", "jugyouchuu ni hanashite wa ikemasen", "You must not talk during class."),
            ("ここで泳いではいけません。", "ここでおよいではいけません。", "koko de oyoide wa ikemasen", "You must not swim here.")
        ],
        "conversation": [
            ("A: このペンを使ってもいいですか。", "A: このペンをつかってもいいですか。", "A: Kono pen o tsukatte mo ii desu ka?", "A: May I use this pen?"),
            ("B: はい、使ってもいいです。", "B: はい、つかってもいいです。", "B: Hai, tsukatte mo ii desu.", "B: Yes, you may use it.")
        ]
    },
    {
        "category": "Obligation",
        "jlpt_category": "Must/Haves",
        "pattern": "〜なければなりません / 〜なくてはいけません / 〜なきゃ / 〜なくちゃ",
        "meaning": "Must do / have to do",
        "english_concept": "Obligation register levels",
        "structure": "Vない stem + ければなりません / くてはいけません / casual short forms",
        "formation": "Convert to ない-form, then apply obligation ending. い of ない changes depending on pattern.",
        "conjugation": "Formal: なければなりません; standard spoken: なくてはいけません; casual: なきゃ/なくちゃ.",
        "formal": "明日早く起きなければなりません。",
        "casual": "もう行かなきゃ。",
        "mistakes": "Using dictionary form directly before obligation endings.",
        "traps": "Double negative meaning can confuse beginners: literally 'if not do, it won't become'.",
        "related": "〜なくてもいいです (no need)",
        "differences": "なければなりません is most formal; なきゃ/なくちゃ are casual spoken contractions.",
        "examples": [
            ("薬を飲まなければなりません。", "くすりをのまなければなりません。", "kusuri o nomanakereba narimasen", "I must take medicine."),
            ("レポートを出さなくてはいけません。", "レポートをださなくてはいけません。", "repooto o dasanakute wa ikemasen", "I must submit the report."),
            ("今日は早く帰らなきゃ。", "きょうははやくかえらなきゃ。", "kyou wa hayaku kaeranakya", "I gotta go home early today."),
            ("宿題をしなくちゃ。", "しゅくだいをしなくちゃ。", "shukudai o shinakucha", "I have to do homework."),
            ("明日までに払わなくてはいけません。", "あしたまでにはらわなくてはいけません。", "ashita made ni harawanakute wa ikemasen", "I must pay by tomorrow.")
        ],
        "conversation": [
            ("A: 今日の会議に出ますか。", "A: きょうのかいぎにでますか。", "A: Kyou no kaigi ni demasu ka?", "A: Will you attend today's meeting?"),
            ("B: はい、出なければなりません。", "B: はい、でなければなりません。", "B: Hai, denakereba narimasen.", "B: Yes, I have to attend.")
        ]
    },
    {
        "category": "Desire and Ability",
        "jlpt_category": "Wants and Can",
        "pattern": "〜たいです / 〜ほしいです / 〜ことができます",
        "meaning": "Want to do, want noun, can do",
        "english_concept": "Desire and ability expression",
        "structure": "Vます-stem + たい; N がほしい; Dict V + ことができます",
        "formation": "たい attaches to verb stem, ほしい works like i-adjective, ことができます nominalizes action.",
        "conjugation": "たい behaves like i-adjective (e.g., たくない).",
        "formal": "日本語を話すことができます。",
        "casual": "ラーメン食べたい。",
        "mistakes": "Using を with ほしい in basic N5 contexts where が is expected.",
        "traps": "たい for your own desire; avoid directly stating another person's desire in plain factual way at N5.",
        "related": "invitation forms and intentions",
        "differences": "たい = want to do action; ほしい = want thing; ことができます = ability.",
        "examples": [
            ("日本へ行きたいです。", "にほんへいきたいです。", "nihon e ikitai desu", "I want to go to Japan."),
            ("新しいパソコンがほしいです。", "あたらしいパソコンがほしいです。", "atarashii pasokon ga hoshii desu", "I want a new computer."),
            ("私はピアノを弾くことができます。", "わたしはピアノをひくことができます。", "watashi wa piano o hiku koto ga dekimasu", "I can play the piano."),
            ("今日は何も食べたくないです。", "きょうはなにもたべたくないです。", "kyou wa nani mo tabetakunai desu", "I don't want to eat anything today."),
            ("ここで切符を買うことができます。", "ここできっぷをかうことができます。", "koko de kippu o kau koto ga dekimasu", "You can buy tickets here.")
        ],
        "conversation": [
            ("A: 何がほしいですか。", "A: なにがほしいですか。", "A: Nani ga hoshii desu ka?", "A: What do you want?"),
            ("B: 日本語の辞書がほしいです。", "B: にほんごのじしょがほしいです。", "B: Nihongo no jisho ga hoshii desu.", "B: I want a Japanese dictionary.")
        ]
    },
    {
        "category": "Comparison",
        "jlpt_category": "Comparative Grammar",
        "pattern": "〜より / 〜のほうが / 〜いちばん",
        "meaning": "More than / comparatively more / most",
        "english_concept": "Comparison and superlative",
        "structure": "A は B より ...; B のほうが ...; Category で N がいちばん ...",
        "formation": "Use より as benchmark, のほうが for preferred side, いちばん for top rank.",
        "conjugation": "Works with adjectives and preference verbs like 好きです.",
        "formal": "電車はバスより速いです。",
        "casual": "こっちのほうがいい。",
        "mistakes": "Using both sides with が incorrectly in one clause.",
        "traps": "JLPT often asks with どちらが〜 and expects のほうが/いちばん logic.",
        "related": "question words どちら/どれ",
        "differences": "より marks standard; のほうが marks stronger side; いちばん marks maximum.",
        "examples": [
            ("今日は昨日より暑いです。", "きょうはきのうよりあついです。", "kyou wa kinou yori atsui desu", "Today is hotter than yesterday."),
            ("犬より猫のほうが好きです。", "いぬよりねこのほうがすきです。", "inu yori neko no hou ga suki desu", "I like cats more than dogs."),
            ("クラスで山田さんがいちばん背が高いです。", "クラスでやまださんがいちばんせがたかいです。", "kurasu de yamada-san ga ichiban se ga takai desu", "Yamada is the tallest in the class."),
            ("日本語と英語とどちらが難しいですか。", "にほんごとえいごとどちらがむずかしいですか。", "nihongo to eigo to dochira ga muzukashii desu ka", "Which is harder, Japanese or English?"),
            ("この店のラーメンがいちばんおいしいです。", "このみせのラーメンがいちばんおいしいです。", "kono mise no raamen ga ichiban oishii desu", "The ramen at this shop is the most delicious.")
        ],
        "conversation": [
            ("A: 紅茶とコーヒーとどちらが好きですか。", "A: こうちゃとコーヒーとどちらがすきですか。", "A: Koucha to koohii to dochira ga suki desu ka?", "A: Which do you like more, tea or coffee?"),
            ("B: コーヒーのほうが好きです。", "B: コーヒーのほうがすきです。", "B: Koohii no hou ga suki desu.", "B: I like coffee more.")
        ]
    },
    {
        "category": "Experience and Habits",
        "jlpt_category": "Te-iru Meanings",
        "pattern": "〜ています",
        "meaning": "Current action, habit, resulting state, occupation",
        "english_concept": "Progressive and state",
        "structure": "Vて + います",
        "formation": "Create verb te-form and attach います.",
        "conjugation": "Negative: 〜ていません; past: 〜ていました.",
        "formal": "今、勉強しています。",
        "casual": "今、勉強してる。",
        "mistakes": "Overusing English-style progressive; some verbs indicate resulting state.",
        "traps": "結婚しています means 'is married' (state), not currently marrying.",
        "related": "sequential 〜て, request/permission patterns",
        "differences": "Action in progress vs habitual repeated action vs resulting state depends on verb semantics.",
        "examples": [
            ("今、本を読んでいます。", "いま、ほんをよんでいます。", "ima, hon o yonde imasu", "I am reading a book now."),
            ("毎朝ジョギングしています。", "まいあさジョギングしています。", "maiasa jogingu shite imasu", "I jog every morning."),
            ("窓が開いています。", "まどがあいています。", "mado ga aite imasu", "The window is open."),
            ("父は銀行で働いています。", "ちちはぎんこうではたらいています。", "chichi wa ginkou de hataraite imasu", "My father works at a bank."),
            ("田中さんは結婚しています。", "たなかさんはけっこんしています。", "tanaka-san wa kekkon shite imasu", "Mr. Tanaka is married.")
        ],
        "conversation": [
            ("A: 今、何をしていますか。", "A: いま、なにをしていますか。", "A: Ima, nani o shite imasu ka?", "A: What are you doing now?"),
            ("B: レポートを書いています。", "B: レポートをかいています。", "B: Repooto o kaite imasu.", "B: I am writing a report.")
        ]
    },
    {
        "category": "Sequential Actions",
        "jlpt_category": "Action Chains",
        "pattern": "〜て / 〜たり〜たりします",
        "meaning": "Do A and then B / do things like A and B",
        "english_concept": "Sequencing and representative listing",
        "structure": "Vて、V; Vたり Vたり します",
        "formation": "Use te-form for strict sequence; use たり-form for non-exhaustive examples.",
        "conjugation": "たり-form is made from past plain + り.",
        "formal": "朝ご飯を食べて、学校へ行きます。",
        "casual": "休みの日は本を読んだりする。",
        "mistakes": "Using たり without final します in N5 pattern.",
        "traps": "て can also indicate reason/method in broader grammar; N5 mostly tests sequence.",
        "related": "〜てから, 〜ながら",
        "differences": "て = actual sequence; たりたり = representative habitual set.",
        "examples": [
            ("手を洗って、ご飯を食べます。", "てをあらって、ごはんをたべます。", "te o aratte, gohan o tabemasu", "I wash my hands and eat."),
            ("家に帰って、宿題をします。", "いえにかえって、しゅくだいをします。", "ie ni kaette, shukudai o shimasu", "I go home and do homework."),
            ("週末は映画を見たり、本を読んだりします。", "しゅうまつはえいがをみたり、ほんをよんだりします。", "shuumatsu wa eiga o mitari, hon o yondari shimasu", "On weekends I do things like watch movies and read books."),
            ("休みの日は買い物したり、料理したりします。", "やすみのひはかいものしたり、りょうりしたりします。", "yasumi no hi wa kaimono shitari, ryouri shitari shimasu", "On days off I do things like shop and cook."),
            ("音楽を聞いて勉強します。", "おんがくをきいてべんきょうします。", "ongaku o kiite benkyou shimasu", "I study while listening to music.")
        ],
        "conversation": [
            ("A: 休みの日は何をしますか。", "A: やすみのひはなにをしますか。", "A: Yasumi no hi wa nani o shimasu ka?", "A: What do you do on your days off?"),
            ("B: 走ったり、友だちと話したりします。", "B: はしったり、ともだちとはなしたりします。", "B: Hashittari, tomodachi to hanashitari shimasu.", "B: I do things like run and chat with friends.")
        ]
    },
    {
        "category": "Reasons",
        "jlpt_category": "Reason Connectors",
        "pattern": "〜から / 〜ので",
        "meaning": "Because",
        "english_concept": "Cause and reason",
        "structure": "Reason clause + から/ので + Result",
        "formation": "Attach reason connector after reason statement.",
        "conjugation": "ので sounds softer and more objective than から.",
        "formal": "雨なので、出かけません。",
        "casual": "疲れたから寝る。",
        "mistakes": "Adding both から and ので in same clause.",
        "traps": "Polite announcements often prefer ので; personal blunt reason favors から.",
        "related": "〜んです explanatory tone",
        "differences": "から = direct personal reason; ので = softer, objective, polite reason.",
        "examples": [
            ("雨が降っているから、行きません。", "あめがふっているから、いきません。", "ame ga futte iru kara, ikimasen", "Because it is raining, I won't go."),
            ("時間がないので、急ぎます。", "じかんがないので、いそぎます。", "jikan ga nai node, isogimasu", "Because I don't have time, I hurry."),
            ("頭が痛いから、薬を飲みます。", "あたまがいたいから、くすりをのみます。", "atama ga itai kara, kusuri o nomimasu", "Because my head hurts, I take medicine."),
            ("静かなので、ここで勉強します。", "しずかなので、ここでべんきょうします。", "shizuka na node, koko de benkyou shimasu", "Because it's quiet, I study here."),
            ("安いから、この店で買います。", "やすいから、このみせでかいます。", "yasui kara, kono mise de kaimasu", "Because it's cheap, I buy at this shop.")
        ],
        "conversation": [
            ("A: どうして遅れましたか。", "A: どうしておくれましたか。", "A: Doushite okuremashita ka?", "A: Why were you late?"),
            ("B: 電車が遅れたので、遅れました。", "B: でんしゃがおくれたので、おくれました。", "B: Densha ga okureta node, okuremashita.", "B: Because the train was delayed, I was late.")
        ]
    },
    {
        "category": "Opinions and Intentions",
        "jlpt_category": "Thought and Plan",
        "pattern": "〜とおもいます / 〜つもりです",
        "meaning": "I think / intend to",
        "english_concept": "Opinion and intention",
        "structure": "Plain clause + と思います; Dictionary/Past negative + つもりです",
        "formation": "Use plain form before と; つもり marks deliberate plan.",
        "conjugation": "つもり can be negated: 〜ないつもりです.",
        "formal": "来年日本へ行くつもりです。",
        "casual": "たぶん大丈夫だと思う。",
        "mistakes": "Using polite です form before と思います in strict grammar contexts.",
        "traps": "Thought in present can be plain non-past; intention may be tested against desire.",
        "related": "〜たいです, conjecture forms",
        "differences": "と思います = belief/opinion; つもりです = plan/intent.",
        "examples": [
            ("この映画は面白いと思います。", "このえいがはおもしろいとおもいます。", "kono eiga wa omoshiroi to omoimasu", "I think this movie is interesting."),
            ("明日は雨だと思います。", "あしたはあめだとおもいます。", "ashita wa ame da to omoimasu", "I think it will rain tomorrow."),
            ("来月引っ越すつもりです。", "らいげつひっこすつもりです。", "raigetsu hikkosu tsumori desu", "I intend to move next month."),
            ("今年は車を買わないつもりです。", "ことしはくるまをかわないつもりです。", "kotoshi wa kuruma o kawanai tsumori desu", "I do not intend to buy a car this year."),
            ("田中さんは来ると思います。", "たなかさんはくるとおもいます。", "tanaka-san wa kuru to omoimasu", "I think Mr. Tanaka will come.")
        ],
        "conversation": [
            ("A: 週末は何をするつもりですか。", "A: しゅうまつはなにをするつもりですか。", "A: Shuumatsu wa nani o suru tsumori desu ka?", "A: What do you intend to do this weekend?"),
            ("B: 家でゆっくり休むつもりです。", "B: いえでゆっくりやすむつもりです。", "B: Ie de yukkuri yasumu tsumori desu.", "B: I intend to rest at home.")
        ]
    },
    {
        "category": "Simultaneous and Conjecture",
        "jlpt_category": "Guessing and While",
        "pattern": "〜ながら / 〜でしょう / 〜かもしれません",
        "meaning": "While doing / probably / maybe",
        "english_concept": "Simultaneous action and uncertainty",
        "structure": "Vます-stem + ながら; Plain + でしょう/かもしれません",
        "formation": "ながら connects two actions by same subject; conjecture endings attach to plain form.",
        "conjugation": "かもしれません expresses weaker certainty than でしょう.",
        "formal": "雨が降るでしょう。",
        "casual": "彼は来るかも。",
        "mistakes": "Using different subjects with ながら in basic N5 pattern.",
        "traps": "でしょう often sounds more likely/confident than かもしれません.",
        "related": "〜と思います, sequence patterns",
        "differences": "ながら = simultaneous action; でしょう = probable; かもしれません = possible/uncertain.",
        "examples": [
            ("音楽を聞きながら勉強します。", "おんがくをききながらべんきょうします。", "ongaku o kikinagara benkyou shimasu", "I study while listening to music."),
            ("歩きながら電話しないでください。", "あるきながらでんわしないでください。", "arukinagara denwa shinaide kudasai", "Please don't talk on the phone while walking."),
            ("明日は晴れるでしょう。", "あしたははれるでしょう。", "ashita wa hareru deshou", "It will probably be sunny tomorrow."),
            ("彼は今、忙しいかもしれません。", "かれはいま、いそがしいかもしれません。", "kare wa ima, isogashii kamoshiremasen", "He might be busy now."),
            ("この答えは正しいでしょう。", "このこたえはただしいでしょう。", "kono kotae wa tadashii deshou", "This answer is probably correct.")
        ],
        "conversation": [
            ("A: 山田さんは来ますか。", "A: やまださんはきますか。", "A: Yamada-san wa kimasu ka?", "A: Will Mr. Yamada come?"),
            ("B: 来るでしょう。でも遅れるかもしれません。", "B: くるでしょう。でもおくれるかもしれません。", "B: Kuru deshou. Demo okureru kamoshiremasen.", "B: He probably will, but he might be late.")
        ]
    },
    {
        "category": "Limits and Listing",
        "jlpt_category": "Only and Examples",
        "pattern": "〜だけ / 〜しか〜ません / 〜や / 〜など",
        "meaning": "Only / only with negative / and such / etc.",
        "english_concept": "Restriction and non-exhaustive listing",
        "structure": "N + だけ; N + しか + negative; NやNなど",
        "formation": "だけ works with positive or negative; しか requires negative predicate.",
        "conjugation": "しか always pairs with ません/ない forms.",
        "formal": "会議には部長だけ来ました。",
        "casual": "百円しかない。",
        "mistakes": "Using しか with positive verbs.",
        "traps": "Both mean 'only', but polarity of verb determines correctness.",
        "related": "quantities and particles",
        "differences": "だけ is neutral only; しか〜ない emphasizes limitation/insufficiency.",
        "examples": [
            ("今日は水だけ飲みます。", "きょうはみずだけのみます。", "kyou wa mizu dake nomimasu", "Today I will drink only water."),
            ("財布に千円しかありません。", "さいふにせんえんしかありません。", "saifu ni sen-en shika arimasen", "I only have 1000 yen in my wallet."),
            ("机の上に本やノートがあります。", "つくえのうえにほんやノートがあります。", "tsukue no ue ni hon ya nooto ga arimasu", "There are books, notebooks, and so on on the desk."),
            ("日曜日は掃除や洗濯などをします。", "にちようびはそうじやせんたくなどをします。", "nichiyoubi wa souji ya sentaku nado o shimasu", "On Sundays I do things like cleaning and laundry."),
            ("パンだけ食べました。", "パンだけたべました。", "pan dake tabemashita", "I ate only bread.")
        ],
        "conversation": [
            ("A: お金はどのくらいありますか。", "A: おかねはどのくらいありますか。", "A: Okane wa dono kurai arimasu ka?", "A: How much money do you have?"),
            ("B: 千円しかありません。", "B: せんえんしかありません。", "B: Sen-en shika arimasen.", "B: I only have 1000 yen.")
        ]
    },
    {
        "category": "Giving, Advice and Noun Modification",
        "jlpt_category": "Interaction Patterns",
        "pattern": "あげます / もらいます / くれます / 〜たほうがいいです / 〜の",
        "meaning": "Giving and receiving, advice, noun linker",
        "english_concept": "Perspective and recommendations",
        "structure": "A は B に N をあげます; A は B に/から N をもらいます; B は A に N をくれます; Vた + ほうがいい; N1 の N2",
        "formation": "Choose giving verb by direction of benefit. Use past short form before ほうがいい.",
        "conjugation": "Advice negative also appears: Vないほうがいい.",
        "formal": "先生は私に本をくれました。",
        "casual": "早く寝たほうがいいよ。",
        "mistakes": "Mixing speaker-centered くれます with neutral あげます/もらいます.",
        "traps": "Exam items test who gives to whom more than tense details.",
        "related": "particles に/から, possession with の",
        "differences": "あげる = give outward, もらう = receive, くれる = give to me/us side.",
        "examples": [
            ("私は友だちに本をあげました。", "わたしはともだちにほんをあげました。", "watashi wa tomodachi ni hon o agemashita", "I gave a book to my friend."),
            ("私は先生に辞書をもらいました。", "わたしはせんせいにじしょをもらいました。", "watashi wa sensei ni jisho o moraimashita", "I received a dictionary from my teacher."),
            ("母は私にケーキをくれました。", "はははわたしにケーキをくれました。", "haha wa watashi ni keeki o kuremashita", "My mother gave me a cake."),
            ("疲れているなら、休んだほうがいいです。", "つかれているなら、やすんだほうがいいです。", "tsukarete iru nara, yasunda hou ga ii desu", "If you are tired, you should rest."),
            ("これは日本語の本です。", "これはにほんごのほんです。", "kore wa nihongo no hon desu", "This is a Japanese-language book.")
        ],
        "conversation": [
            ("A: 風邪です。どうしたらいいですか。", "A: かぜです。どうしたらいいですか。", "A: Kaze desu. Dou shitara ii desu ka?", "A: I have a cold. What should I do?"),
            ("B: 薬を飲んだほうがいいです。", "B: くすりをのんだほうがいいです。", "B: Kusuri o nonda hou ga ii desu.", "B: You should take medicine.")
        ]
    }
]

REVISION_MODE_LISTS = {
    "top25": [
        "〜です", "〜ではありません", "〜でした", "〜ではありませんでした", "〜ですか",
        "〜があります", "〜います", "〜にあります", "〜にいます", "〜へいきます",
        "〜にいきます", "〜てください", "〜をください", "〜ませんか", "〜ましょう",
        "〜てもいいです", "〜てはいけません", "〜なければなりません", "〜たいです", "〜ほしいです",
        "〜ことができます", "〜より", "〜のほうが", "〜いちばん", "〜ています"
    ],
    "top50": [
        "〜です", "〜ではありません", "〜でした", "〜ではありませんでした", "〜ですか", "なに/なん", "だれ", "どこ", "いつ",
        "なぜ", "どうして", "どう", "どんな", "どれ", "どちら", "いくつ", "いくら", "〜があります", "〜います",
        "〜にあります", "〜にいます", "うえ", "した", "なか", "そと", "まえ", "うしろ", "みぎ", "ひだり", "となり", "ちかく",
        "〜へいきます", "〜にいきます", "〜へきます", "〜からきます", "〜まえに", "〜あとで", "〜てから", "〜てください", "〜をください",
        "〜ませんか", "〜ましょう", "〜てもいいです", "〜てはいけません", "〜なければなりません", "〜なくてはいけません", "〜だけ", "〜しか〜ません", "〜から", "〜ので"
    ],
    "exam": [
        "Te-form conversions (especially いく→いって)",
        "〜てもいいです vs 〜てはいけません",
        "〜だけ vs 〜しか〜ません",
        "〜から vs 〜ので",
        "あります vs います",
        "に (existence) vs で (action place)",
        "〜なければなりません family",
        "〜ています meanings (action/state/habit/occupation)",
        "Comparison trio: より / のほうが / いちばん",
        "Giving verbs: あげます / もらいます / くれます"
    ],
    "oneday": [
        "Morning 1h: Copula + Questions + Existence",
        "Midday 1h: Movement + Time expressions + Requests",
        "Afternoon 1h: Permission/Prohibition/Obligation",
        "Evening 1h: Desire/Ability/Comparison/Te-iru",
        "Night 1h: Reasons/Opinion/Intention/Conjecture/Limits",
        "Final 30m: Te-form table + top traps + mock sentence rewrite"
    ]
}
"""Structured data for the Complete N5 Grammar Encyclopedia."""

N5_GRAMMAR_ENCYCLOPEDIA = [
    {
        "category": "Basic Sentences",
        "jlpt_category": "Core Sentence Patterns",
        "points": [
            {
                "pattern": "〜です / 〜ではありません / 〜でした / 〜ではありませんでした",
                "meaning": "Copula (present/past, positive/negative)",
                "english_concept": "to be / was / is not / was not",
                "structure": "Noun/Na-adjective + です/ではありません/でした/ではありませんでした",
                "formation": "Attach polite copula endings to nouns and na-adjectives.",
                "conjugation": "です -> ではありません -> でした -> ではありませんでした",
                "formal": "こちらは私の先生です。",
                "casual": "これは先生だ。",
                "mistakes": "Using these forms with i-adjectives directly (e.g., たかいですでした).",
                "traps": "Nouns use でした, but i-adjectives use かったです for past polite.",
                "related": "〜ですか, plain form だ",
                "differences": "Polite copula differs from verb conjugation patterns.",
                "examples": [
                    ("私は学生です。", "わたしはがくせいです。", "watashi wa gakusei desu.", "I am a student."),
                    ("田中さんは先生ではありません。", "たなかさんはせんせいではありません。", "tanaka-san wa sensei dewa arimasen.", "Mr. Tanaka is not a teacher."),
                    ("きのうは日曜日でした。", "きのうはにちようびでした。", "kinou wa nichiyoubi deshita.", "Yesterday was Sunday."),
                    ("試験は簡単ではありませんでした。", "しけんはかんたんではありませんでした。", "shiken wa kantan dewa arimasen deshita.", "The exam was not easy."),
                    ("この町は静かです。", "このまちはしずかです。", "kono machi wa shizuka desu.", "This town is quiet.")
                ],
                "conversation": [
                    "A: あなたはエンジニアですか。",
                    "B: いいえ、エンジニアではありません。教師です。"
                ]
            }
        ]
    },
    {
        "category": "Questions",
        "jlpt_category": "Question Formation",
        "points": [
            {
                "pattern": "〜ですか + Question Words",
                "meaning": "Polite questions",
                "english_concept": "asking who/what/where/when/why/how/which/how many/how much",
                "structure": "Sentence + ですか / Question word + ですか",
                "formation": "Add か to a polite sentence, or place question word in target slot.",
                "conjugation": "No verb change required beyond normal tense/politeness.",
                "formal": "お名前はなんですか。",
                "casual": "名前、なに？",
                "mistakes": "Mixing なん and なに incorrectly before counters and sounds.",
                "traps": "なん is often used before です, じ, and counters (e.g., なんじ).",
                "related": "〜と思います (indirect question statements)",
                "differences": "Question words replace the unknown slot; particle usage stays important.",
                "examples": [
                    ("これはなんですか。", "これはなんですか。", "kore wa nan desu ka.", "What is this?"),
                    ("だれが来ましたか。", "だれがきましたか。", "dare ga kimashita ka.", "Who came?"),
                    ("どこで昼ご飯を食べますか。", "どこでひるごはんをたべますか。", "doko de hirugohan o tabemasu ka.", "Where do you eat lunch?"),
                    ("いつ日本へ行きますか。", "いつにほんへいきますか。", "itsu nihon e ikimasu ka.", "When will you go to Japan?"),
                    ("いくらですか。", "いくらですか。", "ikura desu ka.", "How much is it?")
                ],
                "conversation": [
                    "A: どちらが田中さんですか。",
                    "B: あの青いシャツの人です。"
                ],
                "question_words": ["なに", "なん", "だれ", "どこ", "いつ", "なぜ", "どうして", "どう", "どんな", "どれ", "どちら", "いくつ", "いくら"]
            }
        ]
    },
    {
        "category": "Existence",
        "jlpt_category": "Existence and Possession",
        "points": [
            {
                "pattern": "〜があります / 〜います",
                "meaning": "Existence of things vs living beings",
                "english_concept": "there is/are",
                "structure": "Place に Thing が あります / Place に Person/Animal が います",
                "formation": "Use あります for inanimate objects, います for animate beings.",
                "conjugation": "あります -> ありません -> ありました / います -> いません -> いました",
                "formal": "教室に学生がいます。",
                "casual": "教室に学生がいる。",
                "mistakes": "Using あります for people.",
                "traps": "Plants and robots are usually treated as あります in N5 contexts.",
                "related": "〜にあります / 〜にいます",
                "differences": "Animate vs inanimate distinction is the key exam test.",
                "examples": [
                    ("机の上に本があります。", "つくえのうえにほんがあります。", "tsukue no ue ni hon ga arimasu.", "There is a book on the desk."),
                    ("公園に子どもがいます。", "こうえんにこどもがいます。", "kouen ni kodomo ga imasu.", "There are children in the park."),
                    ("冷蔵庫に牛乳があります。", "れいぞうこにぎゅうにゅうがあります。", "reizouko ni gyuunyuu ga arimasu.", "There is milk in the fridge."),
                    ("駅の前に犬がいます。", "えきのまえにいぬがいます。", "eki no mae ni inu ga imasu.", "There is a dog in front of the station."),
                    ("この町に図書館があります。", "このまちにとしょかんがあります。", "kono machi ni toshokan ga arimasu.", "There is a library in this town.")
                ],
                "conversation": [
                    "A: 教室に先生がいますか。",
                    "B: はい、います。"
                ]
            }
        ]
    },
    {
        "category": "Location",
        "jlpt_category": "Place and Position",
        "points": [
            {
                "pattern": "〜にあります / 〜にいます",
                "meaning": "Location of existence",
                "english_concept": "is located at",
                "structure": "Noun は Place に あります/います",
                "formation": "Mark location with に and end with existence verb.",
                "conjugation": "Follows あります/います conjugation.",
                "formal": "銀行は駅の近くにあります。",
                "casual": "銀行は駅の近くにある。",
                "mistakes": "Using で instead of に for existence.",
                "traps": "に marks location of existence; で marks location of action.",
                "related": "あります/います, particles に and で",
                "differences": "Existence location and action location are separate grammar roles.",
                "examples": [
                    ("トイレは二階にあります。", "トイレはにかいにあります。", "toire wa nikai ni arimasu.", "The restroom is on the second floor."),
                    ("田中さんは会議室にいます。", "たなかさんはかいぎしつにいます。", "tanaka-san wa kaigishitsu ni imasu.", "Mr. Tanaka is in the meeting room."),
                    ("猫は箱の中にいます。", "ねこははこのなかにいます。", "neko wa hako no naka ni imasu.", "The cat is in the box."),
                    ("コンビニは学校の隣にあります。", "コンビニはがっこうのとなりにあります。", "konbini wa gakkou no tonari ni arimasu.", "The convenience store is next to the school."),
                    ("先生の車は外にあります。", "せんせいのくるまはそとにあります。", "sensei no kuruma wa soto ni arimasu.", "The teacher's car is outside.")
                ],
                "conversation": [
                    "A: 駅はどこにありますか。",
                    "B: あの建物のうしろにあります。"
                ],
                "place_expressions": ["うえ", "した", "なか", "そと", "まえ", "うしろ", "みぎ", "ひだり", "となり", "ちかく"]
            }
        ]
    },
    {
        "category": "Movement",
        "jlpt_category": "Direction and Movement",
        "points": [
            {
                "pattern": "〜へいきます / 〜にいきます / 〜へきます / 〜からきます",
                "meaning": "Movement destination and origin",
                "english_concept": "go/come to/from",
                "structure": "Place へ/に 行きます・来ます / Place から 来ます",
                "formation": "Use へ for direction, に for destination, から for starting point.",
                "conjugation": "行きます/来ます/帰ります standard polite conjugation",
                "formal": "大阪へ行きます。",
                "casual": "大阪に行く。",
                "mistakes": "Using を for destination.",
                "traps": "へ and に are often both acceptable with movement verbs at N5.",
                "related": "Time particles and transportation で",
                "differences": "から marks origin, while へ/に mark destination.",
                "examples": [
                    ("毎朝、学校へ行きます。", "まいあさ、がっこうへいきます。", "maiasa, gakkou e ikimasu.", "I go to school every morning."),
                    ("週末に図書館に行きます。", "しゅうまつにとしょかんにいきます。", "shuumatsu ni toshokan ni ikimasu.", "I go to the library on weekends."),
                    ("友達がうちへ来ます。", "ともだちがうちへきます。", "tomodachi ga uchi e kimasu.", "My friend comes to my house."),
                    ("インドから来ました。", "インドからきました。", "indo kara kimashita.", "I came from India."),
                    ("先生は教室に来ません。", "せんせいはきょうしつにきません。", "sensei wa kyoushitsu ni kimasen.", "The teacher will not come to the classroom.")
                ],
                "conversation": [
                    "A: どこへ行きますか。",
                    "B: 銀行に行きます。"
                ]
            }
        ]
    },
    {
        "category": "Time Expressions",
        "jlpt_category": "Time Relationship",
        "points": [
            {
                "pattern": "〜まえに / 〜あとで / 〜てから",
                "meaning": "Before/after sequence",
                "english_concept": "before doing, after doing",
                "structure": "Dictionary form + まえに / Ta-form + あとで / Te-form + から",
                "formation": "Use dictionary form before action, completed form after action.",
                "conjugation": "Verb form changes before each time marker.",
                "formal": "寝る前に勉強します。",
                "casual": "食べてから行く。",
                "mistakes": "Using ta-form with まえに.",
                "traps": "まえに needs uncompleted action form (dictionary form).",
                "related": "Sequential 〜て",
                "differences": "あとで can be loosely after; てから is direct sequence.",
                "examples": [
                    ("寝る前に日記を書きます。", "ねるまえににっきをかきます。", "neru mae ni nikki o kakimasu.", "I write a diary before sleeping."),
                    ("授業の後で友達に会います。", "じゅぎょうのあとでともだちにあいます。", "jugyou no ato de tomodachi ni aimasu.", "I meet my friend after class."),
                    ("手を洗ってからご飯を食べます。", "てをあらってからごはんをたべます。", "te o aratte kara gohan o tabemasu.", "I eat after washing my hands."),
                    ("出かける前にドアを閉めます。", "でかけるまえにドアをしめます。", "dekakeru mae ni doa o shimemasu.", "I close the door before going out."),
                    ("映画を見た後でコーヒーを飲みました。", "えいがをみたあとでコーヒーをのみました。", "eiga o mita ato de koohii o nomimashita.", "I drank coffee after watching a movie.")
                ],
                "conversation": [
                    "A: 何をしてから寝ますか。",
                    "B: 本を読んでから寝ます。"
                ]
            }
        ]
    },
    {
        "category": "Requests",
        "jlpt_category": "Requests and Asking",
        "points": [
            {
                "pattern": "〜てください / 〜をください",
                "meaning": "Please do / Please give",
                "english_concept": "requesting an action or item",
                "structure": "Te-form + ください / Noun + をください",
                "formation": "Choose verb request or noun request based on what you need.",
                "conjugation": "Requires correct te-form for verbs.",
                "formal": "ゆっくり話してください。",
                "casual": "ちょっと待って。",
                "mistakes": "Using をください with verbs.",
                "traps": "ください alone is not used after dictionary-form verbs.",
                "related": "〜てもいいですか (permission request)",
                "differences": "Action request vs item request.",
                "examples": [
                    ("ここに名前を書いてください。", "ここになまえをかいてください。", "koko ni namae o kaite kudasai.", "Please write your name here."),
                    ("もう一度言ってください。", "もういちどいってください。", "mou ichido itte kudasai.", "Please say it once more."),
                    ("水をください。", "みずをください。", "mizu o kudasai.", "Please give me water."),
                    ("切符を二枚ください。", "きっぷをにまいください。", "kippu o nimai kudasai.", "Two tickets, please."),
                    ("この漢字を教えてください。", "このかんじをおしえてください。", "kono kanji o oshiete kudasai.", "Please teach me this kanji.")
                ],
                "conversation": [
                    "A: すみません、メニューをください。",
                    "B: はい、どうぞ。"
                ]
            }
        ]
    },
    {
        "category": "Invitations",
        "jlpt_category": "Invitation and Suggestion",
        "points": [
            {
                "pattern": "〜ませんか / 〜ましょう",
                "meaning": "Won't you...? / Let's...",
                "english_concept": "invitation and suggestion",
                "structure": "Verb masu-stem + ませんか / ましょう",
                "formation": "Use ませんか for soft invitation; ましょう for proposal.",
                "conjugation": "Built from masu-form stem.",
                "formal": "いっしょに昼ご飯を食べませんか。",
                "casual": "いっしょに行こう。",
                "mistakes": "Translating ませんか as strict negative.",
                "traps": "Semantically positive invitation despite negative grammar form.",
                "related": "〜たいです, 〜ましょうか",
                "differences": "ませんか checks willingness; ましょう states group intention.",
                "examples": [
                    ("土曜日に映画を見ませんか。", "どようびにえいがをみませんか。", "doyoubi ni eiga o mimasen ka.", "Would you like to watch a movie on Saturday?"),
                    ("少し休みましょう。", "すこしやすみましょう。", "sukoshi yasumimashou.", "Let's rest a little."),
                    ("駅まで歩きませんか。", "えきまであるきませんか。", "eki made arukimasen ka.", "Shall we walk to the station?"),
                    ("先に始めましょう。", "さきにはじめましょう。", "saki ni hajimemashou.", "Let's start first."),
                    ("今夜、電話しませんか。", "こんや、でんわしませんか。", "konya, denwa shimasen ka.", "Would you like to talk on the phone tonight?")
                ],
                "conversation": [
                    "A: コーヒーを飲みませんか。",
                    "B: いいですね。飲みましょう。"
                ]
            }
        ]
    },
    {
        "category": "Permission",
        "jlpt_category": "Permission and Rules",
        "points": [
            {
                "pattern": "〜てもいいです",
                "meaning": "It is okay to do / may I do",
                "english_concept": "permission",
                "structure": "Te-form + もいいです(か)",
                "formation": "Attach もいいです after te-form.",
                "conjugation": "Depends on te-form conversion.",
                "formal": "ここで写真を撮ってもいいですか。",
                "casual": "これ使ってもいい？",
                "mistakes": "Using dictionary form before もいいです.",
                "traps": "Question intonation shifts statement to permission request.",
                "related": "〜てはいけません",
                "differences": "Permission opposite of prohibition.",
                "examples": [
                    ("この椅子に座ってもいいですか。", "このいすにすわってもいいですか。", "kono isu ni suwatte mo ii desu ka.", "May I sit on this chair?"),
                    ("辞書を借りてもいいです。", "じしょをかりてもいいです。", "jisho o karite mo ii desu.", "You may borrow the dictionary."),
                    ("ここで食べてもいいですか。", "ここでたべてもいいですか。", "koko de tabete mo ii desu ka.", "Can I eat here?"),
                    ("窓を開けてもいいですか。", "まどをあけてもいいですか。", "mado o akete mo ii desu ka.", "May I open the window?"),
                    ("今日は早く帰ってもいいです。", "きょうははやくかえってもいいです。", "kyou wa hayaku kaette mo ii desu.", "You can go home early today.")
                ],
                "conversation": [
                    "A: ここに荷物を置いてもいいですか。",
                    "B: はい、いいですよ。"
                ]
            }
        ]
    },
    {
        "category": "Prohibition",
        "jlpt_category": "Permission and Rules",
        "points": [
            {
                "pattern": "〜てはいけません",
                "meaning": "Must not / cannot",
                "english_concept": "prohibition",
                "structure": "Te-form + はいけません",
                "formation": "Attach はいけません to te-form.",
                "conjugation": "Depends on te-form conversion.",
                "formal": "ここでタバコを吸ってはいけません。",
                "casual": "ここで吸っちゃだめ。",
                "mistakes": "Using dictionary form + はいけません.",
                "traps": "Seen often in rules/signs and exam listening instructions.",
                "related": "〜てもいいです, obligation family",
                "differences": "Stronger than simple request not to do something.",
                "examples": [
                    ("図書館で大きい声で話してはいけません。", "としょかんでおおきいこえではなしてはいけません。", "toshokan de ookii koe de hanashite wa ikemasen.", "You must not speak loudly in the library."),
                    ("ここに車を止めてはいけません。", "ここにくるまをとめてはいけません。", "koko ni kuruma o tomete wa ikemasen.", "You must not park here."),
                    ("授業中に携帯を使ってはいけません。", "じゅぎょうちゅうにけいたいをつかってはいけません。", "jugyouchuu ni keitai o tsukatte wa ikemasen.", "You must not use your phone during class."),
                    ("病院で走ってはいけません。", "びょういんではしってはいけません。", "byouin de hashitte wa ikemasen.", "You must not run in the hospital."),
                    ("夜遅くまでゲームをしてはいけません。", "よるおそくまでゲームをしてはいけません。", "yoru osoku made geemu o shite wa ikemasen.", "You must not play games until late at night.")
                ],
                "conversation": [
                    "A: ここで写真を撮ってもいいですか。",
                    "B: すみません、撮ってはいけません。"
                ]
            }
        ]
    },
    {
        "category": "Obligation",
        "jlpt_category": "Necessity",
        "points": [
            {
                "pattern": "〜なければなりません / 〜なくてはいけません / 〜なきゃ / 〜なくちゃ",
                "meaning": "Must do / have to",
                "english_concept": "obligation",
                "structure": "Nai-form base + obligation ending",
                "formation": "Convert verb to nai-form, then add required ending.",
                "conjugation": "行く -> 行かなければなりません / 行かなくてはいけません / 行かなきゃ / 行かなくちゃ",
                "formal": "明日早く起きなければなりません。",
                "casual": "明日早く起きなきゃ。",
                "mistakes": "Confusing obligation with prohibition because both look negative.",
                "traps": "Double-negative logic means positive obligation.",
                "related": "〜てもいいです, 〜てはいけません",
                "differences": "なければなりません is formal; なきゃ/なくちゃ are casual spoken.",
                "examples": [
                    ("宿題をしなければなりません。", "しゅくだいをしなければなりません。", "shukudai o shinakereba narimasen.", "I must do homework."),
                    ("薬を飲まなくてはいけません。", "くすりをのまなくてはいけません。", "kusuri o nomanakute wa ikemasen.", "I have to take medicine."),
                    ("もう帰らなきゃ。", "もうかえらなきゃ。", "mou kaeranakya.", "I have to go home now."),
                    ("明日、早く起きなくちゃ。", "あした、はやくおきなくちゃ。", "ashita, hayaku okinakucha.", "I need to wake up early tomorrow."),
                    ("会社に連絡しなければなりません。", "かいしゃにれんらくしなければなりません。", "kaisha ni renraku shinakereba narimasen.", "I must contact the company.")
                ],
                "conversation": [
                    "A: もう出かけるの？",
                    "B: うん、会議だから行かなくちゃ。"
                ]
            }
        ]
    },
    {
        "category": "Desire",
        "jlpt_category": "Wants",
        "points": [
            {
                "pattern": "〜たいです / 〜ほしいです",
                "meaning": "Want to do / want something",
                "english_concept": "desire",
                "structure": "Verb masu-stem + たいです / Noun + がほしいです",
                "formation": "Use たい for actions and ほしい for nouns.",
                "conjugation": "たい behaves like i-adjective (negative: たくない).",
                "formal": "日本語をもっと勉強したいです。",
                "casual": "新しいカメラがほしい。",
                "mistakes": "Using を with ほしい in basic N5 context.",
                "traps": "たい attaches to verb stem, not dictionary form.",
                "related": "invitation patterns and intention つもり",
                "differences": "Action desire vs object desire.",
                "examples": [
                    ("日本へ行きたいです。", "にほんへいきたいです。", "nihon e ikitai desu.", "I want to go to Japan."),
                    ("冷たい水がほしいです。", "つめたいみずがほしいです。", "tsumetai mizu ga hoshii desu.", "I want cold water."),
                    ("今日は早く寝たいです。", "きょうははやくねたいです。", "kyou wa hayaku netai desu.", "I want to sleep early today."),
                    ("新しい辞書がほしいです。", "あたらしいじしょがほしいです。", "atarashii jisho ga hoshii desu.", "I want a new dictionary."),
                    ("友達と話したいです。", "ともだちとはなしたいです。", "tomodachi to hanashitai desu.", "I want to talk with my friend.")
                ],
                "conversation": [
                    "A: 何がほしいですか。",
                    "B: 日本語の文法本がほしいです。"
                ]
            }
        ]
    },
    {
        "category": "Ability",
        "jlpt_category": "Potential",
        "points": [
            {
                "pattern": "〜ことができます",
                "meaning": "Can do",
                "english_concept": "ability / possibility",
                "structure": "Dictionary form + ことができます",
                "formation": "Nominalize action with こと then mark ability.",
                "conjugation": "できます -> できません -> できました",
                "formal": "私は日本語を読むことができます。",
                "casual": "日本語が読める。",
                "mistakes": "Using masu-form before ことができます.",
                "traps": "Dictionary form must be used before こと.",
                "related": "好き/上手 and potential plain forms",
                "differences": "Formal and explicit ability expression.",
                "examples": [
                    ("私はピアノを弾くことができます。", "わたしはピアノをひくことができます。", "watashi wa piano o hiku koto ga dekimasu.", "I can play the piano."),
                    ("ここでカードで払うことができます。", "ここでカードではらうことができます。", "koko de kaado de harau koto ga dekimasu.", "You can pay by card here."),
                    ("日本語で話すことができます。", "にほんごではなすことができます。", "nihongo de hanasu koto ga dekimasu.", "I can speak in Japanese."),
                    ("この機械は予約することができます。", "このきかいはよやくすることができます。", "kono kikai wa yoyaku suru koto ga dekimasu.", "This machine can make reservations."),
                    ("私は泳ぐことができません。", "わたしはおよぐことができません。", "watashi wa oyogu koto ga dekimasen.", "I cannot swim.")
                ],
                "conversation": [
                    "A: 漢字を読むことができますか。",
                    "B: はい、少しできます。"
                ]
            }
        ]
    },
    {
        "category": "Comparison",
        "jlpt_category": "Comparison",
        "points": [
            {
                "pattern": "〜より / 〜のほうが / 〜いちばん",
                "meaning": "than / more / most",
                "english_concept": "comparative and superlative",
                "structure": "A は B より Adj / A のほうが Adj / Group で A がいちばん Adj",
                "formation": "Use より as baseline and ほうが for stronger compared item.",
                "conjugation": "Adjective stays in normal form.",
                "formal": "電車のほうがバスより速いです。",
                "casual": "これがいちばん好き。",
                "mistakes": "Using いちばん without group context in exam questions.",
                "traps": "Word order can flip; particle clues decide meaning.",
                "related": "どちらが〜 and preference questions",
                "differences": "より sets comparison base; ほうが marks preferred/stronger side.",
                "examples": [
                    ("新幹線はバスより速いです。", "しんかんせんはバスよりはやいです。", "shinkansen wa basu yori hayai desu.", "The bullet train is faster than the bus."),
                    ("日本語と英語では、日本語のほうが難しいです。", "にほんごとえいごでは、にほんごのほうがむずかしいです。", "nihongo to eigo dewa, nihongo no hou ga muzukashii desu.", "Between Japanese and English, Japanese is harder."),
                    ("果物でいちばん好きなのはりんごです。", "くだものでいちばんすきなのはりんごです。", "kudamono de ichiban sukina no wa ringo desu.", "My favorite fruit is apples."),
                    ("この店のほうが安いです。", "このみせのほうがやすいです。", "kono mise no hou ga yasui desu.", "This shop is cheaper."),
                    ("今日は昨日より寒いです。", "きょうはきのうよりさむいです。", "kyou wa kinou yori samui desu.", "Today is colder than yesterday.")
                ],
                "conversation": [
                    "A: コーヒーとお茶と、どちらが好きですか。",
                    "B: お茶のほうが好きです。"
                ]
            }
        ]
    },
    {
        "category": "Experience & Habits",
        "jlpt_category": "Te-iru Meanings",
        "points": [
            {
                "pattern": "〜ています",
                "meaning": "Current action, habit, resulting state, occupation",
                "english_concept": "progressive/habitual/state",
                "structure": "Te-form + います",
                "formation": "Convert verb to te-form then add います.",
                "conjugation": "〜ています / 〜ていません / 〜ていました",
                "formal": "今、勉強しています。",
                "casual": "今、勉強してる。",
                "mistakes": "Assuming 〜ています is always ""ing"" action.",
                "traps": "Some verbs indicate resulting state (結婚しています).",
                "related": "Te-form system",
                "differences": "Action-in-progress vs state depends on verb semantics.",
                "examples": [
                    ("今、レポートを書いています。", "いま、レポートをかいています。", "ima, repooto o kaite imasu.", "I am writing a report now."),
                    ("毎朝ジョギングしています。", "まいあさジョギングしています。", "maiasa jogingu shite imasu.", "I jog every morning."),
                    ("東京に住んでいます。", "とうきょうにすんでいます。", "toukyou ni sunde imasu.", "I live in Tokyo."),
                    ("私は先生をしています。", "わたしはせんせいをしています。", "watashi wa sensei o shite imasu.", "I work as a teacher."),
                    ("窓が開いています。", "まどがあいています。", "mado ga aite imasu.", "The window is open.")
                ],
                "conversation": [
                    "A: 今、何をしていますか。",
                    "B: 文法を復習しています。"
                ]
            }
        ]
    },
    {
        "category": "Sequential Actions",
        "jlpt_category": "Linking Actions",
        "points": [
            {
                "pattern": "〜て / 〜たり〜たりします",
                "meaning": "Do A and then B / do things like A and B",
                "english_concept": "sequence and representative listing",
                "structure": "Verb te-form + Verb / Verb ta-form + り ... + りします",
                "formation": "Use te-form for strict sequence; tari for non-exhaustive actions.",
                "conjugation": "たり uses ta-form + り",
                "formal": "朝ご飯を食べて学校へ行きます。",
                "casual": "週末は映画を見たりする。",
                "mistakes": "Using dictionary form + り.",
                "traps": "たり must appear at least twice in N5 pattern drills.",
                "related": "Time expressions and te-form",
                "differences": "て is direct chain, たり is example-list behavior.",
                "examples": [
                    ("手を洗って、食べます。", "てをあらって、たべます。", "te o aratte, tabemasu.", "I wash my hands and eat."),
                    ("朝起きて、シャワーを浴びます。", "あさおきて、シャワーをあびます。", "asa okite, shawaa o abimasu.", "I wake up and take a shower."),
                    ("日曜日は掃除したり、料理したりします。", "にちようびはそうじしたり、りょうりしたりします。", "nichiyoubi wa souji shitari, ryouri shitari shimasu.", "On Sundays I do things like cleaning and cooking."),
                    ("休みの日は本を読んだり、寝たりします。", "やすみのひはほんをよんだり、ねたりします。", "yasumi no hi wa hon o yondari, netari shimasu.", "On days off I do things like reading and sleeping."),
                    ("駅で友達に会って、一緒に帰りました。", "えきでともだちにあって、いっしょにかえりました。", "eki de tomodachi ni atte, issho ni kaerimashita.", "I met my friend at the station and we went home together.")
                ],
                "conversation": [
                    "A: 週末に何をしますか。",
                    "B: 買い物したり、映画を見たりします。"
                ]
            }
        ]
    },
    {
        "category": "Reasons",
        "jlpt_category": "Reason and Cause",
        "points": [
            {
                "pattern": "〜から / 〜ので",
                "meaning": "because",
                "english_concept": "reason and cause",
                "structure": "Reason + から/ので + Result",
                "formation": "Attach after plain/polite reason phrase depending context.",
                "conjugation": "Noun/Na-adj + なので; Verb/i-adj + ので",
                "formal": "時間がないので、急ぎます。",
                "casual": "雨だから行かない。",
                "mistakes": "Using から in very formal apologetic contexts where ので is expected.",
                "traps": "ので sounds softer and objective; から sounds direct.",
                "related": "〜んです explanation tone",
                "differences": "から is subjective/assertive; ので is polite/objective.",
                "examples": [
                    ("雨が降っているから、出かけません。", "あめがふっているから、でかけません。", "ame ga futte iru kara, dekakemasen.", "Because it's raining, I won't go out."),
                    ("静かなので、ここで勉強します。", "しずかなので、ここでべんきょうします。", "shizuka na node, koko de benkyou shimasu.", "Because it's quiet, I study here."),
                    ("今日は日曜日だから、銀行は休みです。", "きょうはにちようびだから、ぎんこうはやすみです。", "kyou wa nichiyoubi da kara, ginkou wa yasumi desu.", "Because today is Sunday, the bank is closed."),
                    ("駅が近いので、歩いて行きます。", "えきがちかいので、あるいていきます。", "eki ga chikai node, aruite ikimasu.", "Because the station is near, I will walk."),
                    ("疲れたから、もう寝ます。", "つかれたから、もうねます。", "tsukareta kara, mou nemasu.", "Because I'm tired, I'll sleep now.")
                ],
                "conversation": [
                    "A: どうして遅れましたか。",
                    "B: 電車が遅れたので、遅れました。"
                ]
            }
        ]
    },
    {
        "category": "Opinions",
        "jlpt_category": "Thought and Opinion",
        "points": [
            {
                "pattern": "〜とおもいます",
                "meaning": "I think that",
                "english_concept": "opinion",
                "structure": "Plain form sentence + と思います",
                "formation": "Use plain form before と.",
                "conjugation": "Noun/na-adj uses だ before と in plain style contexts.",
                "formal": "明日は雨だと思います。",
                "casual": "いいと思う。",
                "mistakes": "Using polite です directly before と思います in some structures.",
                "traps": "Learners overuse it; in Japanese it softens certainty.",
                "related": "でしょう, かもしれません",
                "differences": "Speaker opinion marker, not objective fact marker.",
                "examples": [
                    ("この本はおもしろいと思います。", "このほんはおもしろいとおもいます。", "kono hon wa omoshiroi to omoimasu.", "I think this book is interesting."),
                    ("明日は忙しいと思います。", "あしたはいそがしいとおもいます。", "ashita wa isogashii to omoimasu.", "I think tomorrow will be busy."),
                    ("田中さんは来ないと思います。", "たなかさんはこないとおもいます。", "tanaka-san wa konai to omoimasu.", "I think Mr. Tanaka won't come."),
                    ("日本語は難しいと思います。", "にほんごはむずかしいとおもいます。", "nihongo wa muzukashii to omoimasu.", "I think Japanese is difficult."),
                    ("この店は安いと思います。", "このみせはやすいとおもいます。", "kono mise wa yasui to omoimasu.", "I think this store is cheap.")
                ],
                "conversation": [
                    "A: この問題、難しいですか。",
                    "B: はい、少し難しいと思います。"
                ]
            }
        ]
    },
    {
        "category": "Intentions",
        "jlpt_category": "Plan and Intention",
        "points": [
            {
                "pattern": "〜つもりです",
                "meaning": "intend to do",
                "english_concept": "intention and plan",
                "structure": "Dictionary form / Nai form + つもりです",
                "formation": "Attach to plan in your mind.",
                "conjugation": "行くつもりです / 行かないつもりです",
                "formal": "来年、日本へ留学するつもりです。",
                "casual": "今日は外食しないつもり。",
                "mistakes": "Using this for decisions made just now.",
                "traps": "Shows decided intention, not vague wish.",
                "related": "〜たいです",
                "differences": "たい is desire; つもり is intention/plan.",
                "examples": [
                    ("今年、日本語能力試験を受けるつもりです。", "ことし、にほんごのうりょくしけんをうけるつもりです。", "kotoshi, nihongo nouryoku shiken o ukeru tsumori desu.", "I intend to take the JLPT this year."),
                    ("明日は早く起きるつもりです。", "あしたははやくおきるつもりです。", "ashita wa hayaku okiru tsumori desu.", "I intend to wake up early tomorrow."),
                    ("今月はお金を使わないつもりです。", "こんげつはおかねをつかわないつもりです。", "kongetsu wa okane o tsukawanai tsumori desu.", "I intend not to spend money this month."),
                    ("週末に部屋を掃除するつもりです。", "しゅうまつにへやをそうじするつもりです。", "shuumatsu ni heya o souji suru tsumori desu.", "I plan to clean my room this weekend."),
                    ("来年、車を買うつもりです。", "らいねん、くるまをかうつもりです。", "rainen, kuruma o kau tsumori desu.", "I intend to buy a car next year.")
                ],
                "conversation": [
                    "A: 夏休みに何をするつもりですか。",
                    "B: アルバイトをするつもりです。"
                ]
            }
        ]
    },
    {
        "category": "Simultaneous Actions",
        "jlpt_category": "Dual Action",
        "points": [
            {
                "pattern": "〜ながら",
                "meaning": "while doing",
                "english_concept": "simultaneous action",
                "structure": "Verb masu-stem + ながら + main action",
                "formation": "Secondary action + ながら + main action verb.",
                "conjugation": "Uses verb stem.",
                "formal": "音楽を聞きながら勉強します。",
                "casual": "歩きながら話す。",
                "mistakes": "Using dictionary form before ながら.",
                "traps": "Main action is the final verb in sentence.",
                "related": "〜て and 〜たり〜たり",
                "differences": "ながら is simultaneous, not sequence.",
                "examples": [
                    ("音楽を聞きながら勉強します。", "おんがくをききながらべんきょうします。", "ongaku o kiki nagara benkyou shimasu.", "I study while listening to music."),
                    ("コーヒーを飲みながら本を読みます。", "コーヒーをのみながらほんをよみます。", "koohii o nomi nagara hon o yomimasu.", "I read while drinking coffee."),
                    ("テレビを見ながらご飯を食べます。", "テレビをみながらごはんをたべます。", "terebi o mi nagara gohan o tabemasu.", "I eat while watching TV."),
                    ("歩きながら電話してはいけません。", "あるきながらでんわしてはいけません。", "aruki nagara denwa shite wa ikemasen.", "You must not talk on the phone while walking."),
                    ("歌いながら料理します。", "うたいながらりょうりします。", "utai nagara ryouri shimasu.", "I cook while singing.")
                ],
                "conversation": [
                    "A: 何をしながら通勤しますか。",
                    "B: 音楽を聞きながら通勤します。"
                ]
            }
        ]
    },
    {
        "category": "Conjecture",
        "jlpt_category": "Guess and Probability",
        "points": [
            {
                "pattern": "〜でしょう / 〜かもしれません",
                "meaning": "probably / maybe",
                "english_concept": "conjecture",
                "structure": "Plain/polite sentence + でしょう / plain sentence + かもしれません",
                "formation": "Attach after statement to soften certainty.",
                "conjugation": "No major verb change beyond base sentence form.",
                "formal": "明日は晴れるでしょう。",
                "casual": "たぶん来るかも。",
                "mistakes": "Treating both as equal certainty.",
                "traps": "かもしれません indicates lower confidence than でしょう.",
                "related": "〜と思います, たぶん",
                "differences": "でしょう = likely; かもしれません = maybe/possible.",
                "examples": [
                    ("明日は雨でしょう。", "あしたはあめでしょう。", "ashita wa ame deshou.", "It will probably rain tomorrow."),
                    ("田中さんはもう帰ったでしょう。", "たなかさんはもうかえったでしょう。", "tanaka-san wa mou kaetta deshou.", "Mr. Tanaka has probably already gone home."),
                    ("この答えは正しいかもしれません。", "このこたえはただしいかもしれません。", "kono kotae wa tadashii kamo shiremasen.", "This answer might be correct."),
                    ("彼は来ないかもしれません。", "かれはこないかもしれません。", "kare wa konai kamo shiremasen.", "He might not come."),
                    ("電車が遅れるでしょう。", "でんしゃがおくれるでしょう。", "densha ga okureru deshou.", "The train will probably be delayed.")
                ],
                "conversation": [
                    "A: 明日のテスト、難しいですか。",
                    "B: うーん、難しいかもしれません。"
                ]
            }
        ]
    },
    {
        "category": "Limits",
        "jlpt_category": "Restriction",
        "points": [
            {
                "pattern": "〜だけ / 〜しか〜ません",
                "meaning": "only",
                "english_concept": "limitation",
                "structure": "Noun + だけ + affirmative / Noun + しか + negative",
                "formation": "Choose positive-only (だけ) or negative-only (しか...ない).",
                "conjugation": "しか requires negative predicate.",
                "formal": "今日は水だけ飲みます。",
                "casual": "千円しかない。",
                "mistakes": "Using しか with affirmative verb.",
                "traps": "Exam loves switching だけ and しか with negation clues.",
                "related": "quantity expressions",
                "differences": "だけ is neutral focus; しか〜ない emphasizes scarcity.",
                "examples": [
                    ("私は日本語だけ勉強します。", "わたしはにほんごだけべんきょうします。", "watashi wa nihongo dake benkyou shimasu.", "I study only Japanese."),
                    ("今日は三時間だけ寝ました。", "きょうはさんじかんだけねました。", "kyou wa sanjikan dake nemashita.", "I slept only three hours today."),
                    ("財布に百円しかありません。", "さいふにひゃくえんしかありません。", "saifu ni hyakuen shika arimasen.", "I have only 100 yen in my wallet."),
                    ("水しか飲みません。", "みずしかのみません。", "mizu shika nomimasen.", "I drink only water."),
                    ("この店には日本語の本しかないです。", "このみせにはにほんごのほんしかないです。", "kono mise ni wa nihongo no hon shika nai desu.", "This shop has only Japanese books.")
                ],
                "conversation": [
                    "A: パンがありますか。",
                    "B: すみません、今日はケーキしかありません。"
                ]
            }
        ]
    },
    {
        "category": "Listing",
        "jlpt_category": "Non-exhaustive Listing",
        "points": [
            {
                "pattern": "〜や / 〜など",
                "meaning": "A and B and so on",
                "english_concept": "example listing",
                "structure": "Noun や Noun など",
                "formation": "List representative examples rather than complete set.",
                "conjugation": "Particle-level pattern, no conjugation.",
                "formal": "机の上に本やノートなどがあります。",
                "casual": "果物や野菜を買った。",
                "mistakes": "Using や as complete list marker like と.",
                "traps": "や implies omitted items.",
                "related": "と (complete listing)",
                "differences": "と is exhaustive; や/など are partial examples.",
                "examples": [
                    ("スーパーでりんごやバナナを買いました。", "スーパーでりんごやバナナをかいました。", "suupaa de ringo ya banana o kaimashita.", "I bought apples, bananas, and so on at the supermarket."),
                    ("休日は映画や音楽などを楽しみます。", "きゅうじつはえいがやおんがくなどをたのしみます。", "kyuujitsu wa eiga ya ongaku nado o tanoshimimasu.", "On holidays I enjoy things like movies and music."),
                    ("かばんにペンやノートがあります。", "かばんにペンやノートがあります。", "kaban ni pen ya nooto ga arimasu.", "There are pens and notebooks in my bag."),
                    ("日本には寿司や天ぷらなどがあります。", "にほんにはすしやてんぷらなどがあります。", "nihon ni wa sushi ya tenpura nado ga arimasu.", "Japan has sushi, tempura, and other dishes."),
                    ("会議では予算や予定などを話しました。", "かいぎではよさんやよていなどをはなしました。", "kaigi dewa yosan ya yotei nado o hanashimashita.", "At the meeting we discussed budget, schedule, etc.")
                ],
                "conversation": [
                    "A: 何を買いましたか。",
                    "B: 本やペンなどを買いました。"
                ]
            }
        ]
    },
    {
        "category": "Giving & Receiving",
        "jlpt_category": "Social Direction",
        "points": [
            {
                "pattern": "あげます / もらいます / くれます",
                "meaning": "give / receive",
                "english_concept": "direction of giving",
                "structure": "A は B に N を あげます / A は B に N を もらいます / A は (私に) N を くれます",
                "formation": "Track point-of-view carefully.",
                "conjugation": "Standard polite verb conjugation.",
                "formal": "先生は私に本をくれました。",
                "casual": "友達にペンをあげた。",
                "mistakes": "Using くれる when recipient is not speaker/in-group.",
                "traps": "Perspective flips are classic JLPT trap.",
                "related": "〜をください",
                "differences": "あげる = give outward, くれる = give to me, もらう = receive.",
                "examples": [
                    ("私は妹にケーキをあげます。", "わたしはいもうとにケーキをあげます。", "watashi wa imouto ni keeki o agemasu.", "I give cake to my younger sister."),
                    ("友達は私にノートをくれました。", "ともだちはわたしにノートをくれました。", "tomodachi wa watashi ni nooto o kuremashita.", "My friend gave me a notebook."),
                    ("私は先生に辞書をもらいました。", "わたしはせんせいにじしょをもらいました。", "watashi wa sensei ni jisho o moraimashita.", "I received a dictionary from my teacher."),
                    ("母は弟にお金をあげました。", "はははおとうとにおかねをあげました。", "haha wa otouto ni okane o agemashita.", "Mother gave money to my younger brother."),
                    ("私は父に時計をもらいました。", "わたしはちちにとけいをもらいました。", "watashi wa chichi ni tokei o moraimashita.", "I got a watch from my father.")
                ],
                "conversation": [
                    "A: その本、だれがくれましたか。",
                    "B: 先生がくれました。"
                ]
            }
        ]
    },
    {
        "category": "Advice",
        "jlpt_category": "Recommendation",
        "points": [
            {
                "pattern": "〜たほうがいいです",
                "meaning": "You should",
                "english_concept": "advice and recommendation",
                "structure": "Ta-form + ほうがいいです (or Nai-form + ほうがいいです)",
                "formation": "Past-like form used as recommendation frame.",
                "conjugation": "行ったほうがいいです / 行かないほうがいいです",
                "formal": "早く寝たほうがいいです。",
                "casual": "病院に行ったほうがいいよ。",
                "mistakes": "Using dictionary form before ほうがいいです.",
                "traps": "Negative advice uses nai-form + ほうがいい.",
                "related": "obligation family",
                "differences": "Advice is softer than strict obligation.",
                "examples": [
                    ("熱があるなら、病院へ行ったほうがいいです。", "ねつがあるなら、びょういんへいったほうがいいです。", "netsu ga aru nara, byouin e itta hou ga ii desu.", "If you have a fever, you should go to the hospital."),
                    ("毎日少しずつ勉強したほうがいいです。", "まいにちすこしずつべんきょうしたほうがいいです。", "mainichi sukoshi zutsu benkyou shita hou ga ii desu.", "You should study a little every day."),
                    ("夜遅くコーヒーを飲まないほうがいいです。", "よるおそくコーヒーをのまないほうがいいです。", "yoru osoku koohii o nomanai hou ga ii desu.", "You should not drink coffee late at night."),
                    ("この単語は覚えたほうがいいです。", "このたんごはおぼえたほうがいいです。", "kono tango wa oboeta hou ga ii desu.", "You should memorize this word."),
                    ("疲れているなら、休んだほうがいいです。", "つかれているなら、やすんだほうがいいです。", "tsukarete iru nara, yasunda hou ga ii desu.", "If you are tired, you should rest.")
                ],
                "conversation": [
                    "A: のどが痛いです。",
                    "B: あたたかいお茶を飲んだほうがいいですよ。"
                ]
            }
        ]
    },
    {
        "category": "Noun Modification",
        "jlpt_category": "Attributive",
        "points": [
            {
                "pattern": "〜の",
                "meaning": "noun modification and possession",
                "english_concept": "'s / of / noun-to-noun linking",
                "structure": "Noun A の Noun B",
                "formation": "Place modifier noun before の and target noun after.",
                "conjugation": "Particle-level pattern.",
                "formal": "日本の文化を勉強します。",
                "casual": "これは私の本。",
                "mistakes": "Dropping の between two nouns.",
                "traps": "In some set phrases の may be omitted, but not in standard N5 tests.",
                "related": "relative clauses and demonstratives",
                "differences": "の links nouns; adjectives directly modify nouns without の (for i-adj).",
                "examples": [
                    ("これは私のかばんです。", "これはわたしのかばんです。", "kore wa watashi no kaban desu.", "This is my bag."),
                    ("日本語の先生は親切です。", "にほんごのせんせいはしんせつです。", "nihongo no sensei wa shinsetsu desu.", "The Japanese teacher is kind."),
                    ("駅の前にカフェがあります。", "えきのまえにカフェがあります。", "eki no mae ni kafe ga arimasu.", "There is a cafe in front of the station."),
                    ("友達の誕生日は明日です。", "ともだちのたんじょうびはあしたです。", "tomodachi no tanjoubi wa ashita desu.", "My friend's birthday is tomorrow."),
                    ("東京の地図を見ています。", "とうきょうのちずをみています。", "toukyou no chizu o mite imasu.", "I am looking at a map of Tokyo.")
                ],
                "conversation": [
                    "A: それはだれのノートですか。",
                    "B: 山田さんのノートです。"
                ]
            }
        ]
    }
]

TE_FORM_MASTER = {
    "group_1_rules": [
        "く -> いて",
        "ぐ -> いで",
        "む -> んで",
        "ぶ -> んで",
        "ぬ -> んで",
        "す -> して",
        "つ -> って",
        "る -> って",
        "う -> って",
    ],
    "exception": "いく -> いって",
    "usages": [
        "Request (〜てください)",
        "Permission (〜てもいいです)",
        "Prohibition (〜てはいけません)",
        "Sequential Action (〜て)",
        "Ongoing Action (〜ています)",
        "State (〜ています)",
    ],
}

REVISION_MODE = {
    "top25": [
        "〜です", "〜ではありません", "〜でした", "〜ではありませんでした", "〜ですか", "〜があります", "〜います", "〜にあります", "〜にいます",
        "〜へいきます", "〜にいきます", "〜てください", "〜をください", "〜ませんか", "〜ましょう", "〜てもいいです", "〜てはいけません",
        "〜なければなりません", "〜たいです", "〜ほしいです", "〜ことができます", "〜ています", "〜から", "〜ので", "〜と思います"
    ],
    "top50": [
        "〜です", "〜ではありません", "〜でした", "〜ではありませんでした", "〜ですか", "なに", "なん", "だれ", "どこ", "いつ", "なぜ", "どうして", "どう", "どんな", "どれ", "どちら", "いくつ", "いくら",
        "〜があります", "〜います", "〜にあります", "〜にいます", "〜へいきます", "〜にいきます", "〜へきます", "〜からきます", "〜まえに", "〜あとで", "〜てから",
        "〜てください", "〜をください", "〜ませんか", "〜ましょう", "〜てもいいです", "〜てはいけません", "〜なければなりません", "〜なくてはいけません", "〜なきゃ", "〜なくちゃ",
        "〜たいです", "〜ほしいです", "〜ことができます", "〜より", "〜のほうが", "〜いちばん", "〜ています", "〜たり〜たりします", "〜でしょう", "〜かもしれません", "〜だけ", "〜しか〜ません"
    ],
    "exam": [
        "〜て-form conversion", "〜てもいいです vs 〜てはいけません", "〜だけ vs 〜しか〜ません", "〜から vs 〜ので", "あります vs います",
        "に (existence) vs で (action)", "〜なければなりません family", "〜と思います plain-form requirement", "〜たり〜たりします structure"
    ],
    "oneday": [
        "Morning: Copula set + Questions + Existence",
        "Noon: Te-form rules + Request/Permission/Prohibition",
        "Afternoon: Obligation + Desire + Ability + Comparison",
        "Evening: Reasons + Opinion + Intention + Conjecture",
        "Night: Limits + Listing + Giving/Receiving + Advice + Noun の"
    ],
}
