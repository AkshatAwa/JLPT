# data_kanji.py
# Contains all the N5 Kanji data for the Kanji Learning Center

KANJI_DATA = [
    # ==========================================
    # NUMBERS
    # ==========================================
    {
        "kanji": "一", "meaning": "One", "jlpt": "N5", "strokes": 1, "radical": "一 (one)", "onyomi": ["イチ", "イツ"], "kunyomi": ["ひと", "ひと.つ"], "category": "Numbers",
        "mnemonic": "A single horizontal line representing the number one.",
        "visual_breakdown": "一 (one)",
        "related_kanji": ["二", "三"],
        "common_mistakes": "Do not confuse with the prolonged sound mark in katakana (ー).",
        "real_life_usage": ["Calendars (一日 - 1st of the month)", "Menus (一つ - one item)"],
        "vocab": [
            {"word": "一", "kana": "いち", "romaji": "ichi", "english": "One", "sentence_jp": "一から十まで数えます。", "sentence_kana": "いちからじゅうまでかぞえます。", "sentence_romaji": "Ichi kara juu made kazoemasu.", "sentence_eng": "I will count from one to ten."},
            {"word": "一つ", "kana": "ひとつ", "romaji": "hitotsu", "english": "One thing", "sentence_jp": "りんごを一つください。", "sentence_kana": "りんごをひとつください。", "sentence_romaji": "Ringo o hitotsu kudasai.", "sentence_eng": "Please give me one apple."},
            {"word": "一日", "kana": "ついたち", "romaji": "tsuitachi", "english": "First day of the month", "sentence_jp": "五月一日に生まれます。", "sentence_kana": "ごがつついたちにうまれます。", "sentence_romaji": "Gogatsu tsuitachi ni umaremasu.", "sentence_eng": "He will be born on May 1st."},
            {"word": "一日", "kana": "いちにち", "romaji": "ichinichi", "english": "One day", "sentence_jp": "一日かかります。", "sentence_kana": "いちにちかかります。", "sentence_romaji": "Ichinichi kakarimasu.", "sentence_eng": "It takes one day."},
            {"word": "一人", "kana": "ひとり", "romaji": "hitori", "english": "One person / Alone", "sentence_jp": "一人で行きます。", "sentence_kana": "ひとりでいきます。", "sentence_romaji": "Hitori de ikimasu.", "sentence_eng": "I will go alone."}
        ]
    },
    {
        "kanji": "二", "meaning": "Two", "jlpt": "N5", "strokes": 2, "radical": "二 (two)", "onyomi": ["ニ"], "kunyomi": ["ふた", "ふた.つ"], "category": "Numbers",
        "mnemonic": "Two horizontal lines.",
        "visual_breakdown": "二 (two)",
        "related_kanji": ["一", "三"],
        "common_mistakes": "The top line is slightly shorter than the bottom line.",
        "real_life_usage": ["Train platforms (2番線)", "Dates (二日)"],
        "vocab": [
            {"word": "二", "kana": "に", "romaji": "ni", "english": "Two", "sentence_jp": "一、二、三。", "sentence_kana": "いち、に、さん。", "sentence_romaji": "Ichi, ni, san.", "sentence_eng": "One, two, three."},
            {"word": "二つ", "kana": "ふたつ", "romaji": "futatsu", "english": "Two things", "sentence_jp": "かばんが二つあります。", "sentence_kana": "かばんがふたつあります。", "sentence_romaji": "Kaban ga futatsu arimasu.", "sentence_eng": "There are two bags."},
            {"word": "二人", "kana": "ふたり", "romaji": "futari", "english": "Two people", "sentence_jp": "二人で食べました。", "sentence_kana": "ふたりでたべました。", "sentence_romaji": "Futari de tabemashita.", "sentence_eng": "We ate as a pair (two people)."},
            {"word": "二日", "kana": "ふつか", "romaji": "futsuka", "english": "2nd day of the month / Two days", "sentence_jp": "二日かかります。", "sentence_kana": "ふつかかかります。", "sentence_romaji": "Futsuka kakarimasu.", "sentence_eng": "It takes two days."}
        ]
    },
    {
        "kanji": "三", "meaning": "Three", "jlpt": "N5", "strokes": 3, "radical": "一 (one)", "onyomi": ["サン"], "kunyomi": ["み", "みっ.つ"], "category": "Numbers",
        "mnemonic": "Three horizontal lines.",
        "visual_breakdown": "三 (three)",
        "related_kanji": ["二", "四"],
        "common_mistakes": "The middle line is the shortest. The bottom is the longest.",
        "real_life_usage": ["Floors in a building (3階)", "Time (3時)"],
        "vocab": [
            {"word": "三", "kana": "さん", "romaji": "san", "english": "Three", "sentence_jp": "三万円です。", "sentence_kana": "さんまんえんです。", "sentence_romaji": "Sanman en desu.", "sentence_eng": "It is 30,000 yen."},
            {"word": "三つ", "kana": "みっつ", "romaji": "mittsu", "english": "Three things", "sentence_jp": "みかんを三つ買いました。", "sentence_kana": "みかんをみっつかいました。", "sentence_romaji": "Mikan o mittsu kaimashita.", "sentence_eng": "I bought three tangerines."},
            {"word": "三人", "kana": "さんにん", "romaji": "sannin", "english": "Three people", "sentence_jp": "三人家族です。", "sentence_kana": "さんにんかぞくです。", "sentence_romaji": "Sannin kazoku desu.", "sentence_eng": "We are a family of three."},
            {"word": "三日", "kana": "みっか", "romaji": "mikka", "english": "3rd day / Three days", "sentence_jp": "三日休みます。", "sentence_kana": "みっかやすみます。", "sentence_romaji": "Mikka yasumimasu.", "sentence_eng": "I will rest for three days."}
        ]
    },
    {
        "kanji": "四", "meaning": "Four", "jlpt": "N5", "strokes": 5, "radical": "囗 (enclosure)", "onyomi": ["シ"], "kunyomi": ["よ", "よっ.つ", "よん"], "category": "Numbers",
        "mnemonic": "A box with curtains. Sometimes 4 is an unlucky number, so you close the curtains.",
        "visual_breakdown": "囗 (enclosure) + 八 (eight/divide)",
        "related_kanji": ["西"],
        "common_mistakes": "The number 4 in Japan is often pronounced 'yon' instead of 'shi' because 'shi' sounds like death.",
        "real_life_usage": ["Time (4時 - yo-ji)", "Dates (4月 - shi-gatsu)"],
        "vocab": [
            {"word": "四", "kana": "よん", "romaji": "yon", "english": "Four", "sentence_jp": "四人います。", "sentence_kana": "よにんいます。", "sentence_romaji": "Yonin imasu.", "sentence_eng": "There are four people."},
            {"word": "四つ", "kana": "よっつ", "romaji": "yottsu", "english": "Four things", "sentence_jp": "椅子が四つあります。", "sentence_kana": "いすがよっつあります。", "sentence_romaji": "Isu ga yottsu arimasu.", "sentence_eng": "There are four chairs."},
            {"word": "四月", "kana": "しがつ", "romaji": "shigatsu", "english": "April", "sentence_jp": "四月は桜が綺麗です。", "sentence_kana": "しがつはさくらがきれいです。", "sentence_romaji": "Shigatsu wa sakura ga kirei desu.", "sentence_eng": "In April, the cherry blossoms are beautiful."},
            {"word": "四時", "kana": "よじ", "romaji": "yoji", "english": "4 O'clock", "sentence_jp": "四時に終わります。", "sentence_kana": "よじにおわります。", "sentence_romaji": "Yoji ni owarimasu.", "sentence_eng": "It finishes at 4 o'clock."}
        ]
    },
    {
        "kanji": "五", "meaning": "Five", "jlpt": "N5", "strokes": 4, "radical": "二 (two)", "onyomi": ["ゴ"], "kunyomi": ["いつ", "いつ.つ"], "category": "Numbers",
        "mnemonic": "Looks like the number 5 if you draw it squarely.",
        "visual_breakdown": "二 (two) + | (vertical stroke) + ⼐ (box)",
        "related_kanji": ["吾"],
        "common_mistakes": "Don't write the middle vertical stroke straight down; it hooks.",
        "real_life_usage": ["Coins (500円玉)", "Days (五日)"],
        "vocab": [
            {"word": "五", "kana": "ご", "romaji": "go", "english": "Five", "sentence_jp": "五分待ちます。", "sentence_kana": "ごふんまちます。", "sentence_romaji": "Gofun machimasu.", "sentence_eng": "I will wait 5 minutes."},
            {"word": "五つ", "kana": "いつつ", "romaji": "itsutsu", "english": "Five things", "sentence_jp": "鍵が五つあります。", "sentence_kana": "かぎがいつつあります。", "sentence_romaji": "Kagi ga itsutsu arimasu.", "sentence_eng": "There are five keys."},
            {"word": "五日", "kana": "いつか", "romaji": "itsuka", "english": "5th day / Five days", "sentence_jp": "五日に帰ります。", "sentence_kana": "いつかにかえります。", "sentence_romaji": "Itsuka ni kaerimasu.", "sentence_eng": "I will return on the 5th."}
        ]
    },
    {
        "kanji": "六", "meaning": "Six", "jlpt": "N5", "strokes": 4, "radical": "八 (eight)", "onyomi": ["ロク", "ロッ"], "kunyomi": ["む", "むっ.つ"], "category": "Numbers",
        "mnemonic": "A person with a hat and two legs spread wide.",
        "visual_breakdown": "亠 (lid) + 八 (eight/legs)",
        "related_kanji": ["八", "穴"],
        "common_mistakes": "The bottom strokes curve outwards.",
        "real_life_usage": ["Dates (六日)", "Time (六時)"],
        "vocab": [
            {"word": "六", "kana": "ろく", "romaji": "roku", "english": "Six", "sentence_jp": "六時におきます。", "sentence_kana": "ろくじにおきます。", "sentence_romaji": "Rokuji ni okimasu.", "sentence_eng": "I wake up at 6 o'clock."},
            {"word": "六つ", "kana": "むっつ", "romaji": "muttsu", "english": "Six things", "sentence_jp": "卵を六つ買いました。", "sentence_kana": "たまごをむっつかいました。", "sentence_romaji": "Tamago o muttsu kaimashita.", "sentence_eng": "I bought six eggs."},
            {"word": "六日", "kana": "むいか", "romaji": "muika", "english": "6th day / Six days", "sentence_jp": "六日間旅行します。", "sentence_kana": "むいかかんりょこうします。", "sentence_romaji": "Muikakan ryokou shimasu.", "sentence_eng": "I will travel for six days."}
        ]
    },
    {
        "kanji": "七", "meaning": "Seven", "jlpt": "N5", "strokes": 2, "radical": "一 (one)", "onyomi": ["シチ"], "kunyomi": ["なな", "なな.つ"], "category": "Numbers",
        "mnemonic": "An upside-down '7' with a line through it.",
        "visual_breakdown": "一 (one) + 乚 (hook)",
        "related_kanji": ["十"],
        "common_mistakes": "Looks similar to the katakana 'ナ' (na), but the vertical stroke hooks upwards.",
        "real_life_usage": ["Dates (七日)", "Time (七時 - shichi-ji)"],
        "vocab": [
            {"word": "七", "kana": "なな", "romaji": "nana", "english": "Seven", "sentence_jp": "七番です。", "sentence_kana": "ななばんです。", "sentence_romaji": "Nanaban desu.", "sentence_eng": "It is number seven."},
            {"word": "七つ", "kana": "ななつ", "romaji": "nanatsu", "english": "Seven things", "sentence_jp": "七つのお星さま。", "sentence_kana": "ななつのおほしさま。", "sentence_romaji": "Nanatsu no ohoshisama.", "sentence_eng": "The seven stars."},
            {"word": "七月", "kana": "しちがつ", "romaji": "shichigatsu", "english": "July", "sentence_jp": "七月は暑いです。", "sentence_kana": "しちがつはあついです。", "sentence_romaji": "Shichigatsu wa atsui desu.", "sentence_eng": "July is hot."},
            {"word": "七日", "kana": "なのか", "romaji": "nanoka", "english": "7th day / Seven days", "sentence_jp": "七日かかります。", "sentence_kana": "なのかかかります。", "sentence_romaji": "Nanoka kakarimasu.", "sentence_eng": "It takes seven days."}
        ]
    },
    {
        "kanji": "八", "meaning": "Eight", "jlpt": "N5", "strokes": 2, "radical": "八 (eight)", "onyomi": ["ハチ", "ハッ"], "kunyomi": ["や", "やっ.つ"], "category": "Numbers",
        "mnemonic": "A mountain peaking out, or two drops sliding down. The number 8 is considered lucky in Japan because it widens at the bottom (growth).",
        "visual_breakdown": "丿 (bend) + 捺 (stroke)",
        "related_kanji": ["入", "人"],
        "common_mistakes": "Do not connect the top. If connected, it becomes 入 (enter) or 人 (person).",
        "real_life_usage": ["Dates (八日)", "Time (八時)"],
        "vocab": [
            {"word": "八", "kana": "はち", "romaji": "hachi", "english": "Eight", "sentence_jp": "八時半です。", "sentence_kana": "はちじはんです。", "sentence_romaji": "Hachijihan desu.", "sentence_eng": "It is 8:30."},
            {"word": "八つ", "kana": "やっつ", "romaji": "yattsu", "english": "Eight things", "sentence_jp": "八つ数えます。", "sentence_kana": "やっつかぞえます。", "sentence_romaji": "Yattsu kazoemasu.", "sentence_eng": "I will count eight things."},
            {"word": "八日", "kana": "ようか", "romaji": "youka", "english": "8th day / Eight days", "sentence_jp": "八日に出発します。", "sentence_kana": "ようかにしゅっぱつします。", "sentence_romaji": "Youka ni shuppatsu shimasu.", "sentence_eng": "I depart on the 8th."}
        ]
    },
    {
        "kanji": "九", "meaning": "Nine", "jlpt": "N5", "strokes": 2, "radical": "乙 (second)", "onyomi": ["キュウ", "ク"], "kunyomi": ["ここの", "ここの.つ"], "category": "Numbers",
        "mnemonic": "Looks like a person doing a pushup with bent knees (90 degrees).",
        "visual_breakdown": "丿 (slash) + 乙 (hook)",
        "related_kanji": ["丸"],
        "common_mistakes": "Can be confused with the katakana 'n' (ン) or 'so' (ソ) if written poorly.",
        "real_life_usage": ["Months (九月 - ku-gatsu)", "Time (九時 - ku-ji)"],
        "vocab": [
            {"word": "九", "kana": "きゅう", "romaji": "kyuu", "english": "Nine", "sentence_jp": "九階に行きます。", "sentence_kana": "きゅうかいにいきます。", "sentence_romaji": "Kyuukai ni ikimasu.", "sentence_eng": "I am going to the 9th floor."},
            {"word": "九つ", "kana": "ここのつ", "romaji": "kokonotsu", "english": "Nine things", "sentence_jp": "九つあります。", "sentence_kana": "ここのつあります。", "sentence_romaji": "Kokonotsu arimasu.", "sentence_eng": "There are nine."},
            {"word": "九月", "kana": "くがつ", "romaji": "kugatsu", "english": "September", "sentence_jp": "九月は涼しいです。", "sentence_kana": "くがつはすずしいです。", "sentence_romaji": "Kugatsu wa suzushii desu.", "sentence_eng": "September is cool."},
            {"word": "九日", "kana": "ここのか", "romaji": "kokonoka", "english": "9th day / Nine days", "sentence_jp": "九日は暇ですか。", "sentence_kana": "ここのかはひまですか。", "sentence_romaji": "Kokonoka wa hima desu ka.", "sentence_eng": "Are you free on the 9th?"}
        ]
    },
    {
        "kanji": "十", "meaning": "Ten", "jlpt": "N5", "strokes": 2, "radical": "十 (ten)", "onyomi": ["ジュウ", "ジッ"], "kunyomi": ["とお", "と"], "category": "Numbers",
        "mnemonic": "A cross. Think of the Roman numeral X turned slightly.",
        "visual_breakdown": "一 (one) + | (line)",
        "related_kanji": ["七", "千"],
        "common_mistakes": "Make sure the horizontal line crosses exactly in the middle.",
        "real_life_usage": ["Counting (十、百、千)", "Dates (十日)"],
        "vocab": [
            {"word": "十", "kana": "じゅう", "romaji": "juu", "english": "Ten", "sentence_jp": "十万円。", "sentence_kana": "じゅうまんえん。", "sentence_romaji": "Juuman en.", "sentence_eng": "100,000 yen."},
            {"word": "十", "kana": "とお", "romaji": "too", "english": "Ten things", "sentence_jp": "りんごが十あります。", "sentence_kana": "りんごがとおあります。", "sentence_romaji": "Ringo ga too arimasu.", "sentence_eng": "There are ten apples."},
            {"word": "十分", "kana": "じゅっぷん", "romaji": "juppun", "english": "10 Minutes", "sentence_jp": "十分待ちます。", "sentence_kana": "じゅっぷんまちます。", "sentence_romaji": "Juppun machimasu.", "sentence_eng": "I will wait 10 minutes."},
            {"word": "十日", "kana": "とおか", "romaji": "tooka", "english": "10th day / Ten days", "sentence_jp": "十日かかります。", "sentence_kana": "とおかかかります。", "sentence_romaji": "Tooka kakarimasu.", "sentence_eng": "It takes ten days."}
        ]
    },
    {
        "kanji": "百", "meaning": "Hundred", "jlpt": "N5", "strokes": 6, "radical": "白 (white)", "onyomi": ["ヒャク", "ビャク", "ピャク"], "kunyomi": [], "category": "Numbers",
        "mnemonic": "Number one (一) turned on its side (白) to make 100.",
        "visual_breakdown": "一 (one) + 白 (white)",
        "related_kanji": ["白", "千"],
        "common_mistakes": "Pronunciation changes depending on the number: 300 (san-byaku), 600 (rop-pyaku), 800 (hap-pyaku).",
        "real_life_usage": ["Shopping (百円)", "Stores (百円ショップ)"],
        "vocab": [
            {"word": "百", "kana": "ひゃく", "romaji": "hyaku", "english": "100", "sentence_jp": "百円です。", "sentence_kana": "ひゃくえんです。", "sentence_romaji": "Hyaku en desu.", "sentence_eng": "It is 100 yen."},
            {"word": "三百", "kana": "さんびゃく", "romaji": "sanbyaku", "english": "300", "sentence_jp": "三百円です。", "sentence_kana": "さんびゃくえんです。", "sentence_romaji": "Sanbyaku en desu.", "sentence_eng": "It is 300 yen."},
            {"word": "六百", "kana": "ろっぴゃく", "romaji": "roppyaku", "english": "600", "sentence_jp": "六百円です。", "sentence_kana": "ろっぴゃくえんです。", "sentence_romaji": "Roppyaku en desu.", "sentence_eng": "It is 600 yen."}
        ]
    },
    {
        "kanji": "千", "meaning": "Thousand", "jlpt": "N5", "strokes": 3, "radical": "十 (ten)", "onyomi": ["セン", "ゼン"], "kunyomi": ["ち"], "category": "Numbers",
        "mnemonic": "A drop (ten) on top of ten (十). Ten tens is almost a thousand.",
        "visual_breakdown": "丿 (drop) + 十 (ten)",
        "related_kanji": ["干", "十"],
        "common_mistakes": "Do not confuse with 干 (dry) which has a flat top horizontal line.",
        "real_life_usage": ["Money (千円札 - 1000 yen bill)"],
        "vocab": [
            {"word": "千", "kana": "せん", "romaji": "sen", "english": "1,000", "sentence_jp": "千円かします。", "sentence_kana": "せんえんかします。", "sentence_romaji": "Sen en kashimasu.", "sentence_eng": "I will lend you 1,000 yen."},
            {"word": "三千", "kana": "さんぜん", "romaji": "sanzen", "english": "3,000", "sentence_jp": "三千円です。", "sentence_kana": "さんぜんえんです。", "sentence_romaji": "Sanzen en desu.", "sentence_eng": "It is 3,000 yen."},
            {"word": "八千", "kana": "はっせん", "romaji": "hassen", "english": "8,000", "sentence_jp": "八千円です。", "sentence_kana": "はっせんえんです。", "sentence_romaji": "Hassen en desu.", "sentence_eng": "It is 8,000 yen."}
        ]
    },
    {
        "kanji": "万", "meaning": "Ten Thousand", "jlpt": "N5", "strokes": 3, "radical": "一 (one)", "onyomi": ["マン", "バン"], "kunyomi": [], "category": "Numbers",
        "mnemonic": "Looks like the number 5, but means 10,000. Japanese numbers are grouped by 10,000s, not 1,000s.",
        "visual_breakdown": "一 (one) + 勹 (wrap) + 丿 (drop)",
        "related_kanji": ["方"],
        "common_mistakes": "In English we say 'Ten thousand'. In Japanese you must say 'ONE ten-thousand' (一万 - ichiman).",
        "real_life_usage": ["Prices (一万円 - 10,000 yen)"],
        "vocab": [
            {"word": "一万", "kana": "いちまん", "romaji": "ichiman", "english": "10,000", "sentence_jp": "一万円を払います。", "sentence_kana": "いちまんえんをはらいます。", "sentence_romaji": "Ichiman en o haraimasu.", "sentence_eng": "I will pay 10,000 yen."},
            {"word": "二万", "kana": "にまん", "romaji": "niman", "english": "20,000", "sentence_jp": "二万円かかりました。", "sentence_kana": "にまんえんかかりました。", "sentence_romaji": "Niman en kakarimashita.", "sentence_eng": "It cost 20,000 yen."},
            {"word": "万年筆", "kana": "まんねんひつ", "romaji": "mannenhitsu", "english": "Fountain pen (Literally 10,000 year pen)", "sentence_jp": "万年筆を買いました。", "sentence_kana": "まんねんひつをかいました。", "sentence_romaji": "Mannenhitsu o kaimashita.", "sentence_eng": "I bought a fountain pen."}
        ]
    },
    {
        "kanji": "円", "meaning": "Yen / Circle", "jlpt": "N5", "strokes": 4, "radical": "冂 (box)", "onyomi": ["エン"], "kunyomi": ["まる.い"], "category": "Numbers",
        "mnemonic": "Looks like a ticket window where you hand over Yen.",
        "visual_breakdown": "冂 (enclosure) + | | (lines)",
        "related_kanji": ["国", "内"],
        "common_mistakes": "In Romaji it is 'Yen', but in Japanese it is pronounced 'En'.",
        "real_life_usage": ["Shopping tags", "Currency exchanges"],
        "vocab": [
            {"word": "円", "kana": "えん", "romaji": "en", "english": "Yen", "sentence_jp": "百円です。", "sentence_kana": "ひゃくえんです。", "sentence_romaji": "Hyaku en desu.", "sentence_eng": "It is 100 yen."},
            {"word": "円い", "kana": "まるい", "romaji": "marui", "english": "Round", "sentence_jp": "円いテーブルです。", "sentence_kana": "まるいテーブルです。", "sentence_romaji": "Marui teeburu desu.", "sentence_eng": "It is a round table."},
            {"word": "五千円", "kana": "ごせんえん", "romaji": "gosen'en", "english": "5,000 Yen", "sentence_jp": "五千円貸してください。", "sentence_kana": "ごせんえんかしてください。", "sentence_romaji": "Gosen'en kashite kudasai.", "sentence_eng": "Please lend me 5,000 yen."}
        ]
    },

    # ==========================================
    # DAYS & NATURE (The elements of the week)
    # ==========================================
    {
        "kanji": "日", "meaning": "Sun / Day", "jlpt": "N5", "strokes": 4, "radical": "日 (sun)", "onyomi": ["ニチ", "ジツ"], "kunyomi": ["ひ", "び", "か"], "category": "Time",
        "mnemonic": "A window looking out at the sun. Originates from a drawing of the sun.",
        "visual_breakdown": "日 (sun)",
        "related_kanji": ["白", "目", "月"],
        "common_mistakes": "Has many different readings depending on the word (nichi, hi, bi, ka).",
        "real_life_usage": ["Days of the week (日曜日)", "Japan (日本)", "Dates (〇日)"],
        "vocab": [
            {"word": "日曜日", "kana": "にちようび", "romaji": "nichiyoubi", "english": "Sunday", "sentence_jp": "日曜日は休みです。", "sentence_kana": "にちようびはやすみです。", "sentence_romaji": "Nichiyoubi wa yasumi desu.", "sentence_eng": "Sunday is my day off."},
            {"word": "日本", "kana": "にほん", "romaji": "nihon", "english": "Japan", "sentence_jp": "日本へ行きたいです。", "sentence_kana": "にほんへいきたいです。", "sentence_romaji": "Nihon e ikitai desu.", "sentence_eng": "I want to go to Japan."},
            {"word": "今日", "kana": "きょう", "romaji": "kyou", "english": "Today", "sentence_jp": "今日は暑いです。", "sentence_kana": "きょうはあついです。", "sentence_romaji": "Kyou wa atsui desu.", "sentence_eng": "Today is hot."},
            {"word": "毎日", "kana": "まいにち", "romaji": "mainichi", "english": "Every day", "sentence_jp": "毎日勉強します。", "sentence_kana": "まいにちべんきょうします。", "sentence_romaji": "Mainichi benkyou shimasu.", "sentence_eng": "I study every day."}
        ]
    },
    {
        "kanji": "月", "meaning": "Moon / Month", "jlpt": "N5", "strokes": 4, "radical": "月 (moon)", "onyomi": ["ゲツ", "ガツ"], "kunyomi": ["つき"], "category": "Time",
        "mnemonic": "A crescent moon behind some clouds.",
        "visual_breakdown": "月 (moon)",
        "related_kanji": ["日", "明"],
        "common_mistakes": "Gatsu is used for naming months (January = Ichi-gatsu). Getsu is used for Monday (Getsuyoubi) and counting months (Ikka-getsu).",
        "real_life_usage": ["Months (〇月)", "Monday (月曜日)"],
        "vocab": [
            {"word": "月曜日", "kana": "げつようび", "romaji": "getsuyoubi", "english": "Monday", "sentence_jp": "月曜日は忙しいです。", "sentence_kana": "げつようびはいそがしいです。", "sentence_romaji": "Getsuyoubi wa isogashii desu.", "sentence_eng": "Monday is busy."},
            {"word": "一月", "kana": "いちがつ", "romaji": "ichigatsu", "english": "January", "sentence_jp": "一月は寒いです。", "sentence_kana": "いちがつはさむいです。", "sentence_romaji": "Ichigatsu wa samui desu.", "sentence_eng": "January is cold."},
            {"word": "一ヶ月", "kana": "いっかげつ", "romaji": "ikkagetsu", "english": "One month (duration)", "sentence_jp": "一ヶ月かかります。", "sentence_kana": "いっかげつかかります。", "sentence_romaji": "Ikkagetsu kakarimasu.", "sentence_eng": "It takes one month."},
            {"word": "今月", "kana": "こんげつ", "romaji": "kongetsu", "english": "This month", "sentence_jp": "今月、国へ帰ります。", "sentence_kana": "こんげつ、くにへかえります。", "sentence_romaji": "Kongetsu, kuni e kaerimasu.", "sentence_eng": "I will return to my country this month."}
        ]
    },
    {
        "kanji": "火", "meaning": "Fire", "jlpt": "N5", "strokes": 4, "radical": "火 (fire)", "onyomi": ["カ"], "kunyomi": ["ひ", "び"], "category": "Nature",
        "mnemonic": "Sparks flying off a campfire.",
        "visual_breakdown": "火 (fire)",
        "related_kanji": ["水", "炎"],
        "common_mistakes": "Often appears as a radical at the bottom of other kanji as four dots (灬).",
        "real_life_usage": ["Tuesday (火曜日)", "Fire warnings (火事)"],
        "vocab": [
            {"word": "火曜日", "kana": "かようび", "romaji": "kayoubi", "english": "Tuesday", "sentence_jp": "火曜日に会いましょう。", "sentence_kana": "かようびにあいましょう。", "sentence_romaji": "Kayoubi ni aimashou.", "sentence_eng": "Let's meet on Tuesday."},
            {"word": "火", "kana": "ひ", "romaji": "hi", "english": "Fire", "sentence_jp": "火に気をつけてください。", "sentence_kana": "ひにきをつけてください。", "sentence_romaji": "Hi ni ki o tsukete kudasai.", "sentence_eng": "Please be careful of the fire."},
            {"word": "花火", "kana": "はなび", "romaji": "hanabi", "english": "Fireworks (Fire flowers)", "sentence_jp": "花火を見ました。", "sentence_kana": "はなびをみました。", "sentence_romaji": "Hanabi o mimashita.", "sentence_eng": "I saw fireworks."}
        ]
    },
    {
        "kanji": "水", "meaning": "Water", "jlpt": "N5", "strokes": 4, "radical": "水 (water)", "onyomi": ["スイ"], "kunyomi": ["みず"], "category": "Nature",
        "mnemonic": "Water splashing out from a central stream.",
        "visual_breakdown": "水 (water)",
        "related_kanji": ["氷", "永"],
        "common_mistakes": "Appears as a radical on the left side of many kanji as three drops (氵).",
        "real_life_usage": ["Wednesday (水曜日)", "Drinking water (水)", "Plumbing (水道)"],
        "vocab": [
            {"word": "水曜日", "kana": "すいようび", "romaji": "suiyoubi", "english": "Wednesday", "sentence_jp": "水曜日は休みです。", "sentence_kana": "すいようびはやすみです。", "sentence_romaji": "Suiyoubi wa yasumi desu.", "sentence_eng": "I am off on Wednesday."},
            {"word": "水", "kana": "みず", "romaji": "mizu", "english": "Water", "sentence_jp": "水を飲みます。", "sentence_kana": "みずをのみます。", "sentence_romaji": "Mizu o nomimasu.", "sentence_eng": "I drink water."},
            {"word": "水道", "kana": "すいどう", "romaji": "suidou", "english": "Water supply", "sentence_jp": "水道の水は飲めます。", "sentence_kana": "すいどうのみずはのめます。", "sentence_romaji": "Suidou no mizu wa nomemasu.", "sentence_eng": "You can drink the tap water."}
        ]
    },
    {
        "kanji": "木", "meaning": "Tree / Wood", "jlpt": "N5", "strokes": 4, "radical": "木 (tree)", "onyomi": ["モク", "ボク"], "kunyomi": ["き"], "category": "Nature",
        "mnemonic": "A tree with branches stretching out and roots going down.",
        "visual_breakdown": "木 (tree)",
        "related_kanji": ["本", "林", "森"],
        "common_mistakes": "If you add a line at the bottom, it becomes 本 (Book/Root).",
        "real_life_usage": ["Thursday (木曜日)", "Nature signs"],
        "vocab": [
            {"word": "木曜日", "kana": "もくようび", "romaji": "mokuyoubi", "english": "Thursday", "sentence_jp": "木曜日に映画を見ます。", "sentence_kana": "もくようびにえいがをみます。", "sentence_romaji": "Mokuyoubi ni eiga o mimasu.", "sentence_eng": "I will watch a movie on Thursday."},
            {"word": "木", "kana": "き", "romaji": "ki", "english": "Tree", "sentence_jp": "木が大きいです。", "sentence_kana": "きがおおきいです。", "sentence_romaji": "Ki ga ookii desu.", "sentence_eng": "The tree is big."}
        ]
    },
    {
        "kanji": "金", "meaning": "Gold / Money", "jlpt": "N5", "strokes": 8, "radical": "金 (gold)", "onyomi": ["キン", "コン"], "kunyomi": ["かね"], "category": "Nature",
        "mnemonic": "Gold nuggets hidden under a mountain roof.",
        "visual_breakdown": "人 (person/roof) + 王 (king) + ハ (drops/gold)",
        "related_kanji": ["全", "針"],
        "common_mistakes": "When meaning money, it almost always takes the honorific 'o': お金 (o-kane).",
        "real_life_usage": ["Friday (金曜日)", "Banks, ATMS (お金)"],
        "vocab": [
            {"word": "金曜日", "kana": "きんようび", "romaji": "kinyoubi", "english": "Friday", "sentence_jp": "金曜日の夜は暇です。", "sentence_kana": "きんようびのよるはひまです。", "sentence_romaji": "Kinyoubi no yoru wa hima desu.", "sentence_eng": "I am free on Friday night."},
            {"word": "お金", "kana": "おかね", "romaji": "okane", "english": "Money", "sentence_jp": "お金がありません。", "sentence_kana": "おかねがありません。", "sentence_romaji": "Okane ga arimasen.", "sentence_eng": "I have no money."},
            {"word": "お金持ち", "kana": "おかねもち", "romaji": "okanemochi", "english": "Rich person", "sentence_jp": "彼はお金持ちです。", "sentence_kana": "かれはおかねもちです。", "sentence_romaji": "Kare wa okanemochi desu.", "sentence_eng": "He is rich."}
        ]
    },
    {
        "kanji": "土", "meaning": "Soil / Earth", "jlpt": "N5", "strokes": 3, "radical": "土 (soil)", "onyomi": ["ド", "ト"], "kunyomi": ["つち"], "category": "Nature",
        "mnemonic": "A sprout coming out of the ground (soil).",
        "visual_breakdown": "十 (cross) + 一 (ground)",
        "related_kanji": ["士", "上"],
        "common_mistakes": "Do not confuse with 士 (samurai), where the top line is longer than the bottom line. For 土, the bottom line is longer.",
        "real_life_usage": ["Saturday (土曜日)"],
        "vocab": [
            {"word": "土曜日", "kana": "どようび", "romaji": "doyoubi", "english": "Saturday", "sentence_jp": "土曜日に買い物をします。", "sentence_kana": "どようびにかいものをします。", "sentence_romaji": "Doyoubi ni kaimono o shimasu.", "sentence_eng": "I go shopping on Saturday."},
            {"word": "土", "kana": "つち", "romaji": "tsuchi", "english": "Soil", "sentence_jp": "土を触ります。", "sentence_kana": "つちをさわります。", "sentence_romaji": "Tsuchi o sawarimasu.", "sentence_eng": "I touch the soil."}
        ]
    },
    # ==========================================
    # NATURE & THE WORLD
    # ==========================================
    {
        "kanji": "山", "meaning": "Mountain", "jlpt": "N5", "strokes": 3, "radical": "山 (mountain)", "onyomi": ["サン", "ザン"], "kunyomi": ["やま"], "category": "Nature",
        "mnemonic": "A picture of three mountain peaks.",
        "visual_breakdown": "山 (mountain)",
        "related_kanji": ["川", "出"],
        "common_mistakes": "The middle stroke is drawn first.",
        "real_life_usage": ["Names (山田 - Yamada)", "Places (富士山 - Fuji-san)"],
        "vocab": [
            {"word": "山", "kana": "やま", "romaji": "yama", "english": "Mountain", "sentence_jp": "山に登ります。", "sentence_kana": "やまにのぼります。", "sentence_romaji": "Yama ni noborimasu.", "sentence_eng": "I climb the mountain."},
            {"word": "富士山", "kana": "ふじさん", "romaji": "fujisan", "english": "Mt. Fuji", "sentence_jp": "富士山はきれいです。", "sentence_kana": "ふじさんはきれいです。", "sentence_romaji": "Fujisan wa kirei desu.", "sentence_eng": "Mt. Fuji is beautiful."},
            {"word": "火山", "kana": "かざん", "romaji": "kazan", "english": "Volcano", "sentence_jp": "火山があります。", "sentence_kana": "かざんがあります。", "sentence_romaji": "Kazan ga arimasu.", "sentence_eng": "There is a volcano."}
        ]
    },
    {
        "kanji": "川", "meaning": "River", "jlpt": "N5", "strokes": 3, "radical": "川 (river)", "onyomi": ["セン"], "kunyomi": ["かわ", "がわ"], "category": "Nature",
        "mnemonic": "Three lines representing flowing water.",
        "visual_breakdown": "川 (river)",
        "related_kanji": ["水", "山"],
        "common_mistakes": "Do not confuse with the three drops (氵) radical.",
        "real_life_usage": ["Names (小川 - Ogawa)"],
        "vocab": [
            {"word": "川", "kana": "かわ", "romaji": "kawa", "english": "River", "sentence_jp": "川で泳ぎます。", "sentence_kana": "かわでおよぎます。", "sentence_romaji": "Kawa de oyogimasu.", "sentence_eng": "I swim in the river."}
        ]
    },
    {
        "kanji": "花", "meaning": "Flower", "jlpt": "N5", "strokes": 7, "radical": "艹 (grass)", "onyomi": ["カ"], "kunyomi": ["はな"], "category": "Nature",
        "mnemonic": "A person transforming (化) under the grass (艹) to become a flower.",
        "visual_breakdown": "艹 (grass) + 化 (change)",
        "related_kanji": ["草", "茶"],
        "common_mistakes": "The top radical is specifically for plants/grass.",
        "real_life_usage": ["Hanami (花見 - Flower viewing)", "Florists (花屋)"],
        "vocab": [
            {"word": "花", "kana": "はな", "romaji": "hana", "english": "Flower", "sentence_jp": "花を買います。", "sentence_kana": "はなをかいます。", "sentence_romaji": "Hana o kaimasu.", "sentence_eng": "I buy flowers."},
            {"word": "花見", "kana": "はなみ", "romaji": "hanami", "english": "Flower viewing", "sentence_jp": "花見に行きます。", "sentence_kana": "はなみにいきます。", "sentence_romaji": "Hanami ni ikimasu.", "sentence_eng": "I go flower viewing."}
        ]
    },
    {
        "kanji": "魚", "meaning": "Fish", "jlpt": "N5", "strokes": 11, "radical": "魚 (fish)", "onyomi": ["ギョ"], "kunyomi": ["さかな", "うお"], "category": "Nature",
        "mnemonic": "The top is the head, the middle is the scaly body, the bottom is the tail.",
        "visual_breakdown": "𠂊 (bound) + 田 (field) + 灬 (fire/tail)",
        "related_kanji": ["鳥"],
        "common_mistakes": "Often acts as a radical on the left side of specific fish names (like sushi menu items).",
        "real_life_usage": ["Fish markets", "Sushi restaurants"],
        "vocab": [
            {"word": "魚", "kana": "さかな", "romaji": "sakana", "english": "Fish", "sentence_jp": "魚を食べます。", "sentence_kana": "さかなをたべます。", "sentence_romaji": "Sakana o tabemasu.", "sentence_eng": "I eat fish."},
            {"word": "金魚", "kana": "きんぎょ", "romaji": "kingyo", "english": "Goldfish", "sentence_jp": "金魚がいます。", "sentence_kana": "きんぎょがいます。", "sentence_romaji": "Kingyo ga imasu.", "sentence_eng": "There is a goldfish."}
        ]
    },
    {
        "kanji": "雨", "meaning": "Rain", "jlpt": "N5", "strokes": 8, "radical": "雨 (rain)", "onyomi": ["ウ"], "kunyomi": ["あめ", "あま"], "category": "Weather",
        "mnemonic": "Water drops falling from a cloud in the sky.",
        "visual_breakdown": "雨 (rain)",
        "related_kanji": ["雪", "雲", "電"],
        "common_mistakes": "Acts as the top radical for almost all weather-related kanji.",
        "real_life_usage": ["Weather forecasts (天気予報)"],
        "vocab": [
            {"word": "雨", "kana": "あめ", "romaji": "ame", "english": "Rain", "sentence_jp": "雨が降ります。", "sentence_kana": "あめがふります。", "sentence_romaji": "Ame ga furimasu.", "sentence_eng": "It rains."},
            {"word": "大雨", "kana": "おおあめ", "romaji": "ooame", "english": "Heavy rain", "sentence_jp": "大雨ですね。", "sentence_kana": "おおあめですね。", "sentence_romaji": "Ooame desu ne.", "sentence_eng": "It's heavy rain, isn't it?"}
        ]
    },
    {
        "kanji": "天", "meaning": "Heavens / Sky", "jlpt": "N5", "strokes": 4, "radical": "大 (big)", "onyomi": ["テン"], "kunyomi": ["あまつ", "あめ"], "category": "Nature",
        "mnemonic": "A person (大) pointing to the sky with an extra line above their head.",
        "visual_breakdown": "一 (one) + 大 (big/person)",
        "related_kanji": ["大", "夫"],
        "common_mistakes": "Do not confuse with 夫 (husband), where the vertical stroke pushes through the top.",
        "real_life_usage": ["Weather (天気)"],
        "vocab": [
            {"word": "天気", "kana": "てんき", "romaji": "tenki", "english": "Weather", "sentence_jp": "いい天気です。", "sentence_kana": "いいてんきです。", "sentence_romaji": "Ii tenki desu.", "sentence_eng": "It is good weather."},
            {"word": "天国", "kana": "てんごく", "romaji": "tengoku", "english": "Heaven", "sentence_jp": "天国に行きたい。", "sentence_kana": "てんごくにいきたい。", "sentence_romaji": "Tengoku ni ikitai.", "sentence_eng": "I want to go to heaven."}
        ]
    },
    {
        "kanji": "空", "meaning": "Sky / Empty", "jlpt": "N5", "strokes": 8, "radical": "穴 (hole)", "onyomi": ["クウ"], "kunyomi": ["そら", "あ.く", "から"], "category": "Nature",
        "mnemonic": "Looking through a hole (穴) at the sky (working/crafting 工).",
        "visual_breakdown": "穴 (hole) + 工 (work)",
        "related_kanji": ["穴", "突"],
        "common_mistakes": "Can mean both the literal sky, and 'empty' (like Karate - empty hand).",
        "real_life_usage": ["Airports (空港)", "Karate (空手)"],
        "vocab": [
            {"word": "空", "kana": "そら", "romaji": "sora", "english": "Sky", "sentence_jp": "空が青いです。", "sentence_kana": "そらがあおいです。", "sentence_romaji": "Sora ga aoi desu.", "sentence_eng": "The sky is blue."},
            {"word": "空気", "kana": "くうき", "romaji": "kuuki", "english": "Air", "sentence_jp": "空気がきれいです。", "sentence_kana": "くうきがきれいです。", "sentence_romaji": "Kuuki ga kirei desu.", "sentence_eng": "The air is clean."},
            {"word": "空港", "kana": "くうこう", "romaji": "kuukou", "english": "Airport", "sentence_jp": "空港に行きます。", "sentence_kana": "くうこうにいきます。", "sentence_romaji": "Kuukou ni ikimasu.", "sentence_eng": "I go to the airport."}
        ]
    },

    # ==========================================
    # PEOPLE & FAMILY
    # ==========================================
    {
        "kanji": "人", "meaning": "Person", "jlpt": "N5", "strokes": 2, "radical": "人 (person)", "onyomi": ["ジン", "ニン"], "kunyomi": ["ひと"], "category": "People",
        "mnemonic": "A person standing with two legs.",
        "visual_breakdown": "人 (person)",
        "related_kanji": ["入", "八"],
        "common_mistakes": "As a radical, it squishes to the left side (亻).",
        "real_life_usage": ["Nationality (アメリカ人)", "Counters (三人)"],
        "vocab": [
            {"word": "人", "kana": "ひと", "romaji": "hito", "english": "Person", "sentence_jp": "あの人は誰ですか。", "sentence_kana": "あのひとはだれですか。", "sentence_romaji": "Ano hito wa dare desu ka.", "sentence_eng": "Who is that person?"},
            {"word": "日本人", "kana": "にほんじん", "romaji": "nihonjin", "english": "Japanese person", "sentence_jp": "私は日本人です。", "sentence_kana": "わたしはにほんじんです。", "sentence_romaji": "Watashi wa nihonjin desu.", "sentence_eng": "I am Japanese."},
            {"word": "男の人", "kana": "おとこのひと", "romaji": "otoko no hito", "english": "Man", "sentence_jp": "男の人がいます。", "sentence_kana": "おとこのひとがいます。", "sentence_romaji": "Otoko no hito ga imasu.", "sentence_eng": "There is a man."}
        ]
    },
    {
        "kanji": "女", "meaning": "Woman", "jlpt": "N5", "strokes": 3, "radical": "女 (woman)", "onyomi": ["ジョ", "ニョ"], "kunyomi": ["おんな", "め"], "category": "People",
        "mnemonic": "A woman crossing her legs.",
        "visual_breakdown": "女 (woman)",
        "related_kanji": ["好", "妹", "姉"],
        "common_mistakes": "Used as a radical for many female-related words.",
        "real_life_usage": ["Restrooms (女)"],
        "vocab": [
            {"word": "女", "kana": "おんな", "romaji": "onna", "english": "Woman", "sentence_jp": "女の人が好きです。", "sentence_kana": "おんなのひとがすきです。", "sentence_romaji": "Onna no hito ga suki desu.", "sentence_eng": "I like women."},
            {"word": "女の子", "kana": "おんなのこ", "romaji": "onnanoko", "english": "Girl", "sentence_jp": "女の子が走ります。", "sentence_kana": "おんなのこがはしります。", "sentence_romaji": "Onnanoko ga hashirimasu.", "sentence_eng": "The girl runs."}
        ]
    },
    {
        "kanji": "男", "meaning": "Man", "jlpt": "N5", "strokes": 7, "radical": "田 (field)", "onyomi": ["ダン", "ナン"], "kunyomi": ["おとこ"], "category": "People",
        "mnemonic": "Using power/strength (力) in the rice field (田).",
        "visual_breakdown": "田 (field) + 力 (power)",
        "related_kanji": ["女", "力", "田"],
        "common_mistakes": "Do not confuse the bottom part with 刀 (sword). It is 力 (power).",
        "real_life_usage": ["Restrooms (男)"],
        "vocab": [
            {"word": "男", "kana": "おとこ", "romaji": "otoko", "english": "Man", "sentence_jp": "男の子です。", "sentence_kana": "おとこのこです。", "sentence_romaji": "Otokonoko desu.", "sentence_eng": "It is a boy."},
            {"word": "男の人", "kana": "おとこのひと", "romaji": "otoko no hito", "english": "Man", "sentence_jp": "あの男の人は先生です。", "sentence_kana": "あのおとこのひとはせんせいです。", "sentence_romaji": "Ano otoko no hito wa sensei desu.", "sentence_eng": "That man is a teacher."}
        ]
    },
    {
        "kanji": "子", "meaning": "Child", "jlpt": "N5", "strokes": 3, "radical": "子 (child)", "onyomi": ["シ", "ス"], "kunyomi": ["こ"], "category": "People",
        "mnemonic": "A child wrapped in a blanket with their arms sticking out.",
        "visual_breakdown": "子 (child)",
        "related_kanji": ["学", "字", "好"],
        "common_mistakes": "Very common radical or suffix for nouns.",
        "real_life_usage": ["Children (子供)"],
        "vocab": [
            {"word": "子供", "kana": "こども", "romaji": "kodomo", "english": "Child", "sentence_jp": "子供がいます。", "sentence_kana": "こどもがいます。", "sentence_romaji": "Kodomo ga imasu.", "sentence_eng": "I have a child."},
            {"word": "男の子", "kana": "おとこのこ", "romaji": "otokonoko", "english": "Boy", "sentence_jp": "男の子が遊びます。", "sentence_kana": "おとこのこがあそびます。", "sentence_romaji": "Otokonoko ga asobimasu.", "sentence_eng": "The boy plays."}
        ]
    },
    {
        "kanji": "母", "meaning": "Mother", "jlpt": "N5", "strokes": 5, "radical": "毋 (mother)", "onyomi": ["ボ"], "kunyomi": ["はは", "かあ"], "category": "Family",
        "mnemonic": "A woman with two drops representing breasts.",
        "visual_breakdown": "毋 (mother)",
        "related_kanji": ["毎", "父"],
        "common_mistakes": "Used to refer to your OWN mother. Use お母さん for someone else's.",
        "real_life_usage": ["Family introductions"],
        "vocab": [
            {"word": "母", "kana": "はは", "romaji": "haha", "english": "My mother", "sentence_jp": "母は元気です。", "sentence_kana": "はははげんきです。", "sentence_romaji": "Haha wa genki desu.", "sentence_eng": "My mother is well."},
            {"word": "お母さん", "kana": "おかあさん", "romaji": "okaasan", "english": "Mother (Polite)", "sentence_jp": "お母さんはどこですか。", "sentence_kana": "おかあさんはどこですか。", "sentence_romaji": "Okaasan wa doko desu ka.", "sentence_eng": "Where is your mother?"}
        ]
    },
    {
        "kanji": "父", "meaning": "Father", "jlpt": "N5", "strokes": 4, "radical": "父 (father)", "onyomi": ["フ"], "kunyomi": ["ちち", "とう"], "category": "Family",
        "mnemonic": "A father holding two axes/sticks crossing them.",
        "visual_breakdown": "ハ (divide) + 乂 (cross)",
        "related_kanji": ["交", "母"],
        "common_mistakes": "Used to refer to your OWN father. Use お父さん for someone else's.",
        "real_life_usage": ["Family introductions"],
        "vocab": [
            {"word": "父", "kana": "ちち", "romaji": "chichi", "english": "My father", "sentence_jp": "父は医者です。", "sentence_kana": "ちちはいしゃです。", "sentence_romaji": "Chichi wa isha desu.", "sentence_eng": "My father is a doctor."},
            {"word": "お父さん", "kana": "おとうさん", "romaji": "otousan", "english": "Father (Polite)", "sentence_jp": "お父さんは会社員です。", "sentence_kana": "おとうさんはかいしゃいんです。", "sentence_romaji": "Otousan wa kaishain desu.", "sentence_eng": "Your father is an office worker."}
        ]
    },
    {
        "kanji": "友", "meaning": "Friend", "jlpt": "N5", "strokes": 4, "radical": "又 (again/right hand)", "onyomi": ["ユウ"], "kunyomi": ["とも"], "category": "People",
        "mnemonic": "Two hands joining together.",
        "visual_breakdown": "𠂇 (left hand) + 又 (right hand)",
        "related_kanji": ["有", "右"],
        "common_mistakes": "Often confused with 抜 or 右 because of the left-hand radical.",
        "real_life_usage": ["Friends (友達)"],
        "vocab": [
            {"word": "友達", "kana": "ともだち", "romaji": "tomodachi", "english": "Friend", "sentence_jp": "友達に会います。", "sentence_kana": "ともだちにあいます。", "sentence_romaji": "Tomodachi ni aimasu.", "sentence_eng": "I will meet a friend."},
            {"word": "友人", "kana": "ゆうじん", "romaji": "yuujin", "english": "Friend (Formal)", "sentence_jp": "友人と食事します。", "sentence_kana": "ゆうじんとしょくじします。", "sentence_romaji": "Yuujin to shokuji shimasu.", "sentence_eng": "I eat with a friend."}
        ]
    },

    # ==========================================
    # BODY PARTS
    # ==========================================
    {
        "kanji": "手", "meaning": "Hand", "jlpt": "N5", "strokes": 4, "radical": "手 (hand)", "onyomi": ["シュ"], "kunyomi": ["て"], "category": "Body",
        "mnemonic": "Looks like a hand with fingers spread out.",
        "visual_breakdown": "手 (hand)",
        "related_kanji": ["毛", "看"],
        "common_mistakes": "When used as a radical, it squishes to the left (扌) and is used for hand actions (throw, push, pull).",
        "real_life_usage": ["Restrooms (お手洗い)", "Letters (手紙)"],
        "vocab": [
            {"word": "手", "kana": "て", "romaji": "te", "english": "Hand", "sentence_jp": "手を洗います。", "sentence_kana": "てをあらいます。", "sentence_romaji": "Te o araimasu.", "sentence_eng": "I wash my hands."},
            {"word": "上手", "kana": "じょうず", "romaji": "jouzu", "english": "Skilled", "sentence_jp": "歌が上手です。", "sentence_kana": "うたがじょうずです。", "sentence_romaji": "Uta ga jouzu desu.", "sentence_eng": "He is good at singing."},
            {"word": "手紙", "kana": "てがみ", "romaji": "tegami", "english": "Letter", "sentence_jp": "手紙を書きます。", "sentence_kana": "てがみをかきます。", "sentence_romaji": "Tegami o kakimasu.", "sentence_eng": "I write a letter."}
        ]
    },
    {
        "kanji": "目", "meaning": "Eye", "jlpt": "N5", "strokes": 5, "radical": "目 (eye)", "onyomi": ["モク", "ボク"], "kunyomi": ["め", "ま"], "category": "Body",
        "mnemonic": "An eye turned sideways.",
        "visual_breakdown": "目 (eye)",
        "related_kanji": ["見", "日", "自"],
        "common_mistakes": "Do not confuse with 日 (sun) or 白 (white).",
        "real_life_usage": ["Goals (目的)", "Eye drops (目薬)"],
        "vocab": [
            {"word": "目", "kana": "め", "romaji": "me", "english": "Eye", "sentence_jp": "目が痛いです。", "sentence_kana": "めがいたいです。", "sentence_romaji": "Me ga itai desu.", "sentence_eng": "My eye hurts."},
            {"word": "目薬", "kana": "めぐすり", "romaji": "megusuri", "english": "Eye drops", "sentence_jp": "目薬を買います。", "sentence_kana": "めぐすりをかいます。", "sentence_romaji": "Megusuri o kaimasu.", "sentence_eng": "I buy eye drops."}
        ]
    },
    {
        "kanji": "耳", "meaning": "Ear", "jlpt": "N5", "strokes": 6, "radical": "耳 (ear)", "onyomi": ["ジ"], "kunyomi": ["みみ"], "category": "Body",
        "mnemonic": "Looks like an ear with cartilage ridges inside.",
        "visual_breakdown": "耳 (ear)",
        "related_kanji": ["聞", "目"],
        "common_mistakes": "Used as the radical inside the 'Listen' kanji (聞).",
        "real_life_usage": ["Body descriptions"],
        "vocab": [
            {"word": "耳", "kana": "みみ", "romaji": "mimi", "english": "Ear", "sentence_jp": "耳が大きいです。", "sentence_kana": "みみがおおきいです。", "sentence_romaji": "Mimi ga ookii desu.", "sentence_eng": "His ears are big."}
        ]
    },
    {
        "kanji": "口", "meaning": "Mouth", "jlpt": "N5", "strokes": 3, "radical": "口 (mouth)", "onyomi": ["コウ", "ク"], "kunyomi": ["くち", "ぐち"], "category": "Body",
        "mnemonic": "An open mouth.",
        "visual_breakdown": "口 (mouth)",
        "related_kanji": ["言", "古", "右"],
        "common_mistakes": "Do not confuse with 囗 (enclosure radical). 口 is a standalone character.",
        "real_life_usage": ["Exits (出口)", "Entrances (入口)", "Population (人口)"],
        "vocab": [
            {"word": "口", "kana": "くち", "romaji": "kuchi", "english": "Mouth", "sentence_jp": "口を開けてください。", "sentence_kana": "くちをあけてください。", "sentence_romaji": "Kuchi o akete kudasai.", "sentence_eng": "Please open your mouth."},
            {"word": "出口", "kana": "でぐち", "romaji": "deguchi", "english": "Exit", "sentence_jp": "出口はどこですか。", "sentence_kana": "でぐちはどこですか。", "sentence_romaji": "Deguchi wa doko desu ka.", "sentence_eng": "Where is the exit?"},
            {"word": "入口", "kana": "いりぐち", "romaji": "iriguchi", "english": "Entrance", "sentence_jp": "入口で待ちます。", "sentence_kana": "いりぐちでまちます。", "sentence_romaji": "Iriguchi de machimasu.", "sentence_eng": "I will wait at the entrance."}
        ]
    },
    {
        "kanji": "足", "meaning": "Foot / Leg / Sufficient", "jlpt": "N5", "strokes": 7, "radical": "足 (foot)", "onyomi": ["ソク"], "kunyomi": ["あし", "た.りる", "た.す"], "category": "Body",
        "mnemonic": "A mouth (口) complaining while walking on legs (止 modified).",
        "visual_breakdown": "口 (mouth) + 止 (stop/walk)",
        "related_kanji": ["走", "歩"],
        "common_mistakes": "Can mean a physical foot, or the concept of 'enough/sufficient'.",
        "real_life_usage": ["Shoes", "Running", "Saying 'enough'"],
        "vocab": [
            {"word": "足", "kana": "あし", "romaji": "ashi", "english": "Foot / Leg", "sentence_jp": "足が痛いです。", "sentence_kana": "あしがいたいです。", "sentence_romaji": "Ashi ga itai desu.", "sentence_eng": "My leg hurts."},
            {"word": "足りる", "kana": "たりる", "romaji": "tariru", "english": "To be enough", "sentence_jp": "お金が足ります。", "sentence_kana": "おかねがたります。", "sentence_romaji": "Okane ga tarimasu.", "sentence_eng": "I have enough money."},
            {"word": "一足", "kana": "いっそく", "romaji": "issoku", "english": "One pair (of shoes)", "sentence_jp": "靴を一足買います。", "sentence_kana": "くつをいっそくかいます。", "sentence_romaji": "Kutsu o issoku kaimasu.", "sentence_eng": "I buy a pair of shoes."}
        ]
    },

    # ==========================================
    # DIRECTIONS & POSITIONS
    # ==========================================
    {
        "kanji": "北", "meaning": "North", "jlpt": "N5", "strokes": 5, "radical": "匕 (spoon)", "onyomi": ["ホク"], "kunyomi": ["きた"], "category": "Direction",
        "mnemonic": "Two people sitting back-to-back to stay warm in the cold North.",
        "visual_breakdown": "爿 (left side) + 匕 (spoon/person)",
        "related_kanji": ["比", "化"],
        "common_mistakes": "Do not confuse with 比 (compare).",
        "real_life_usage": ["Hokkaido (北海道)", "North Exit (北口)"],
        "vocab": [
            {"word": "北", "kana": "きた", "romaji": "kita", "english": "North", "sentence_jp": "北へ行きます。", "sentence_kana": "きたへいきます。", "sentence_romaji": "Kita e ikimasu.", "sentence_eng": "I go north."},
            {"word": "北口", "kana": "きたぐち", "romaji": "kitaguchi", "english": "North exit", "sentence_jp": "北口で会いましょう。", "sentence_kana": "きたぐちであいましょう。", "sentence_romaji": "Kitaguchi de aimashou.", "sentence_eng": "Let's meet at the north exit."}
        ]
    },
    {
        "kanji": "南", "meaning": "South", "jlpt": "N5", "strokes": 9, "radical": "十 (ten)", "onyomi": ["ナン", "ナ"], "kunyomi": ["みなみ"], "category": "Direction",
        "mnemonic": "A cross (十) marking a border with an enclosure containing a sheep (¥) enjoying the warm South.",
        "visual_breakdown": "十 (cross) + 冂 (border) + ¥ (yen/sheep)",
        "related_kanji": ["商", "幸"],
        "common_mistakes": "Contains the Yen symbol inside.",
        "real_life_usage": ["South Exit (南口)", "South America (南米)"],
        "vocab": [
            {"word": "南", "kana": "みなみ", "romaji": "minami", "english": "South", "sentence_jp": "南にあります。", "sentence_kana": "みなみにあります。", "sentence_romaji": "Minami ni arimasu.", "sentence_eng": "It is in the south."},
            {"word": "南口", "kana": "みなみぐち", "romaji": "minamiguchi", "english": "South exit", "sentence_jp": "南口から出ます。", "sentence_kana": "みなみぐちからでます。", "sentence_romaji": "Minamiguchi kara demasu.", "sentence_eng": "I exit from the south exit."}
        ]
    },
    {
        "kanji": "東", "meaning": "East", "jlpt": "N5", "strokes": 8, "radical": "木 (tree)", "onyomi": ["トウ"], "kunyomi": ["ひがし"], "category": "Direction",
        "mnemonic": "The sun (日) rising behind a tree (木) in the East.",
        "visual_breakdown": "木 (tree) + 日 (sun)",
        "related_kanji": ["車", "重"],
        "common_mistakes": "Do not confuse with 車 (car). 東 has lines going through it.",
        "real_life_usage": ["Tokyo (東京)", "East Exit (東口)"],
        "vocab": [
            {"word": "東", "kana": "ひがし", "romaji": "higashi", "english": "East", "sentence_jp": "東の空です。", "sentence_kana": "ひがしのそらです。", "sentence_romaji": "Higashi no sora desu.", "sentence_eng": "It is the eastern sky."},
            {"word": "東京", "kana": "とうきょう", "romaji": "toukyou", "english": "Tokyo", "sentence_jp": "東京に住んでいます。", "sentence_kana": "とうきょうにすんでいます。", "sentence_romaji": "Toukyou ni sunde imasu.", "sentence_eng": "I live in Tokyo."}
        ]
    },
    {
        "kanji": "西", "meaning": "West", "jlpt": "N5", "strokes": 6, "radical": "襾 (west)", "onyomi": ["セイ", "サイ"], "kunyomi": ["にし"], "category": "Direction",
        "mnemonic": "A bird returning to its nest (box) as the sun sets in the West.",
        "visual_breakdown": "一 (one) + 冂 (box) + ハ (legs)",
        "related_kanji": ["四", "酒"],
        "common_mistakes": "Looks like the number 4 (四) but the legs inside are different.",
        "real_life_usage": ["West Exit (西口)", "Kansai region (関西)"],
        "vocab": [
            {"word": "西", "kana": "にし", "romaji": "nishi", "english": "West", "sentence_jp": "西へ行きます。", "sentence_kana": "にしへいきます。", "sentence_romaji": "Nishi e ikimasu.", "sentence_eng": "I go west."},
            {"word": "西口", "kana": "にしぐち", "romaji": "nishiguchi", "english": "West exit", "sentence_jp": "西口で待ってください。", "sentence_kana": "にしぐちでまってください。", "sentence_romaji": "Nishiguchi de matte kudasai.", "sentence_eng": "Please wait at the west exit."}
        ]
    },
    {
        "kanji": "上", "meaning": "Above / Up", "jlpt": "N5", "strokes": 3, "radical": "一 (one)", "onyomi": ["ジョウ"], "kunyomi": ["うえ", "あ.がる", "のぼ.る"], "category": "Direction",
        "mnemonic": "A line sticking UP from a baseline.",
        "visual_breakdown": "一 (one) + 卜 (divination/stick)",
        "related_kanji": ["下", "止"],
        "common_mistakes": "Has many kunyomi readings depending on if you are 'going up', 'raising something', or just saying 'above'.",
        "real_life_usage": ["Elevators", "Skilled (上手)"],
        "vocab": [
            {"word": "上", "kana": "うえ", "romaji": "ue", "english": "Above / On top", "sentence_jp": "机の上にあります。", "sentence_kana": "つくえのうえにあります。", "sentence_romaji": "Tsukue no ue ni arimasu.", "sentence_eng": "It is on the desk."},
            {"word": "上手", "kana": "じょうず", "romaji": "jouzu", "english": "Skilled", "sentence_jp": "日本語が上手ですね。", "sentence_kana": "にほんごがじょうずですね。", "sentence_romaji": "Nihongo ga jouzu desu ne.", "sentence_eng": "Your Japanese is good!"},
            {"word": "上がる", "kana": "あがる", "romaji": "agaru", "english": "To go up", "sentence_jp": "二階へ上がります。", "sentence_kana": "にかいへあがります。", "sentence_romaji": "Nikai e agarimasu.", "sentence_eng": "I go up to the second floor."}
        ]
    },
    {
        "kanji": "下", "meaning": "Below / Down", "jlpt": "N5", "strokes": 3, "radical": "一 (one)", "onyomi": ["カ", "ゲ"], "kunyomi": ["した", "さ.がる", "くだ.る"], "category": "Direction",
        "mnemonic": "A line sticking DOWN from a baseline.",
        "visual_breakdown": "一 (one) + 卜 (stick/down)",
        "related_kanji": ["上", "不"],
        "common_mistakes": "Like 'Up', has many readings depending on the verb.",
        "real_life_usage": ["Subways (地下鉄)", "Unskilled (下手)"],
        "vocab": [
            {"word": "下", "kana": "した", "romaji": "shita", "english": "Below / Under", "sentence_jp": "机の下に猫がいます。", "sentence_kana": "つくえのしたにねこがいます。", "sentence_romaji": "Tsukue no shita ni neko ga imasu.", "sentence_eng": "There is a cat under the desk."},
            {"word": "下手", "kana": "へた", "romaji": "heta", "english": "Unskilled", "sentence_jp": "歌が下手です。", "sentence_kana": "うたがへたです。", "sentence_romaji": "Uta ga heta desu.", "sentence_eng": "I am bad at singing."},
            {"word": "地下鉄", "kana": "ちかてつ", "romaji": "chikatetsu", "english": "Subway", "sentence_jp": "地下鉄に乗ります。", "sentence_kana": "ちかてつにのります。", "sentence_romaji": "Chikatetsu ni norimasu.", "sentence_eng": "I ride the subway."}
        ]
    },
    {
        "kanji": "左", "meaning": "Left", "jlpt": "N5", "strokes": 5, "radical": "工 (work)", "onyomi": ["サ"], "kunyomi": ["ひだり"], "category": "Direction",
        "mnemonic": "The left hand holding a carpenter's square (工).",
        "visual_breakdown": "𠂇 (left hand) + 工 (work/tool)",
        "related_kanji": ["右", "友"],
        "common_mistakes": "Do not confuse with Right (右). Left has the 'work' I-beam tool. Right has a 'mouth'.",
        "real_life_usage": ["Directions"],
        "vocab": [
            {"word": "左", "kana": "ひだり", "romaji": "hidari", "english": "Left", "sentence_jp": "左へ曲がります。", "sentence_kana": "ひだりへまがります。", "sentence_romaji": "Hidari e magarimasu.", "sentence_eng": "Turn left."},
            {"word": "左手", "kana": "ひだりて", "romaji": "hidarite", "english": "Left hand", "sentence_jp": "左手を上げます。", "sentence_kana": "ひだりてをあげます。", "sentence_romaji": "Hidarite o agemasu.", "sentence_eng": "Raise your left hand."}
        ]
    },
    {
        "kanji": "右", "meaning": "Right", "jlpt": "N5", "strokes": 5, "radical": "口 (mouth)", "onyomi": ["ウ", "ユウ"], "kunyomi": ["みぎ"], "category": "Direction",
        "mnemonic": "The right hand holding a mouth (eating with your right hand).",
        "visual_breakdown": "𠂇 (hand) + 口 (mouth)",
        "related_kanji": ["左", "石", "友"],
        "common_mistakes": "Do not confuse with Left (左). Right has the mouth.",
        "real_life_usage": ["Directions"],
        "vocab": [
            {"word": "右", "kana": "みぎ", "romaji": "migi", "english": "Right", "sentence_jp": "右を見てください。", "sentence_kana": "みぎをみてください。", "sentence_romaji": "Migi o mite kudasai.", "sentence_eng": "Please look to the right."},
            {"word": "右手", "kana": "みぎて", "romaji": "migite", "english": "Right hand", "sentence_jp": "右手で書きます。", "sentence_kana": "みぎてでかきます。", "sentence_romaji": "Migite de kakimasu.", "sentence_eng": "I write with my right hand."}
        ]
    },
    {
        "kanji": "外", "meaning": "Outside", "jlpt": "N5", "strokes": 5, "radical": "夕 (evening)", "onyomi": ["ガイ", "ゲ"], "kunyomi": ["そと", "はず.す"], "category": "Direction",
        "mnemonic": "Smoking (ト) outside in the evening (夕).",
        "visual_breakdown": "夕 (evening) + 卜 (stick/divination)",
        "related_kanji": ["名", "多"],
        "common_mistakes": "Used heavily for 'foreign' words.",
        "real_life_usage": ["Foreigners (外国人)", "Foreign countries (外国)"],
        "vocab": [
            {"word": "外", "kana": "そと", "romaji": "soto", "english": "Outside", "sentence_jp": "外は寒いです。", "sentence_kana": "そとはさむいです。", "sentence_romaji": "Soto wa samui desu.", "sentence_eng": "It is cold outside."},
            {"word": "外国", "kana": "がいこく", "romaji": "gaikoku", "english": "Foreign country", "sentence_jp": "外国へ行きます。", "sentence_kana": "がいこくへいきます。", "sentence_romaji": "Gaikoku e ikimasu.", "sentence_eng": "I go to a foreign country."},
            {"word": "外国人", "kana": "がいこくじん", "romaji": "gaikokujin", "english": "Foreigner", "sentence_jp": "私は外国人です。", "sentence_kana": "わたしはがいこくじんです。", "sentence_romaji": "Watashi wa gaikokujin desu.", "sentence_eng": "I am a foreigner."}
        ]
    },
    {
        "kanji": "中", "meaning": "Inside / Middle", "jlpt": "N5", "strokes": 4, "radical": "丨 (line)", "onyomi": ["チュウ"], "kunyomi": ["なか"], "category": "Direction",
        "mnemonic": "A line going straight through the MIDDLE of a box.",
        "visual_breakdown": "口 (box) + 丨 (line)",
        "related_kanji": ["虫", "申"],
        "common_mistakes": "Can mean inside a box, or the middle of a country (China).",
        "real_life_usage": ["China (中国)", "Junior High (中学校)"],
        "vocab": [
            {"word": "中", "kana": "なか", "romaji": "naka", "english": "Inside", "sentence_jp": "箱の中を見ます。", "sentence_kana": "はこのなかをみます。", "sentence_romaji": "Hako no naka o mimasu.", "sentence_eng": "I look inside the box."},
            {"word": "中国", "kana": "ちゅうごく", "romaji": "chuugoku", "english": "China (Middle Country)", "sentence_jp": "中国から来ました。", "sentence_kana": "ちゅうごくからきました。", "sentence_romaji": "Chuugoku kara kimashita.", "sentence_eng": "I came from China."},
            {"word": "一日中", "kana": "いちにちじゅう", "romaji": "ichinichijuu", "english": "All day long", "sentence_jp": "一日中寝ました。", "sentence_kana": "いちにちじゅうねました。", "sentence_romaji": "Ichinichijuu nemashita.", "sentence_eng": "I slept all day long."}
        ]
    },
    {
        "kanji": "前", "meaning": "Front / Before", "jlpt": "N5", "strokes": 9, "radical": "刂 (knife)", "onyomi": ["ゼン"], "kunyomi": ["まえ"], "category": "Direction",
        "mnemonic": "Chopping (刂) flesh (月) before/in front of you.",
        "visual_breakdown": "䒑 (horns) + 月 (flesh/moon) + 刂 (knife)",
        "related_kanji": ["後", "剪"],
        "common_mistakes": "Has a very complex top/left structure.",
        "real_life_usage": ["AM (午前)", "Names (名前)"],
        "vocab": [
            {"word": "前", "kana": "まえ", "romaji": "mae", "english": "Front / Before", "sentence_jp": "駅の前にあります。", "sentence_kana": "えきのまえにあります。", "sentence_romaji": "Eki no mae ni arimasu.", "sentence_eng": "It is in front of the station."},
            {"word": "午前", "kana": "ごぜん", "romaji": "gozen", "english": "A.M. (Before noon)", "sentence_jp": "午前九時に行きます。", "sentence_kana": "ごぜんくじにいきます。", "sentence_romaji": "Gozen kuji ni ikimasu.", "sentence_eng": "I go at 9 A.M."},
            {"word": "名前", "kana": "なまえ", "romaji": "namae", "english": "Name", "sentence_jp": "名前を書いてください。", "sentence_kana": "なまえをかいてください。", "sentence_romaji": "Namae o kaite kudasai.", "sentence_eng": "Please write your name."}
        ]
    },
    {
        "kanji": "後", "meaning": "Behind / After", "jlpt": "N5", "strokes": 9, "radical": "彳 (step)", "onyomi": ["ゴ", "コウ"], "kunyomi": ["うし.ろ", "あと", "のち"], "category": "Direction",
        "mnemonic": "Walking (彳) trailing behind a thread (幺) and dragging feet (夂).",
        "visual_breakdown": "彳 (step) + 幺 (thread) + 夂 (winter/walk slowly)",
        "related_kanji": ["前", "待"],
        "common_mistakes": "Extremely complex. Ensure you write the three distinct radicals.",
        "real_life_usage": ["PM (午後)"],
        "vocab": [
            {"word": "後ろ", "kana": "うしろ", "romaji": "ushiro", "english": "Behind", "sentence_jp": "後ろを見てください。", "sentence_kana": "うしろをみてください。", "sentence_romaji": "Ushiro o mite kudasai.", "sentence_eng": "Please look behind you."},
            {"word": "午後", "kana": "ごご", "romaji": "gogo", "english": "P.M. (After noon)", "sentence_jp": "午後三時です。", "sentence_kana": "ごごさんじです。", "sentence_romaji": "Gogo sanji desu.", "sentence_eng": "It is 3 P.M."},
            {"word": "後で", "kana": "あとで", "romaji": "atode", "english": "Later", "sentence_jp": "後で行きます。", "sentence_kana": "あとでいきます。", "sentence_romaji": "Atode ikimasu.", "sentence_eng": "I will go later."}
        ]
    },
    # ==========================================
    # SCHOOL & STUDY
    # ==========================================
    {
        "kanji": "本", "meaning": "Book / Root / Origin", "jlpt": "N5", "strokes": 5, "radical": "木 (tree)", "onyomi": ["ホン"], "kunyomi": ["もと"], "category": "School",
        "mnemonic": "A tree (木) with a line at the base marking the root. Books come from tree roots.",
        "visual_breakdown": "木 (tree) + 一 (one)",
        "related_kanji": ["木", "休"],
        "common_mistakes": "Do not confuse with 木 (tree) or 休 (rest).",
        "real_life_usage": ["Japan (日本)", "Books (本)"],
        "vocab": [
            {"word": "本", "kana": "ほん", "romaji": "hon", "english": "Book", "sentence_jp": "本を読みます。", "sentence_kana": "ほんをよみます。", "sentence_romaji": "Hon o yomimasu.", "sentence_eng": "I read a book."},
            {"word": "日本", "kana": "にほん", "romaji": "nihon", "english": "Japan", "sentence_jp": "日本が好きです。", "sentence_kana": "にほんがすきです。", "sentence_romaji": "Nihon ga suki desu.", "sentence_eng": "I like Japan."}
        ]
    },
    {
        "kanji": "語", "meaning": "Language / Word", "jlpt": "N5", "strokes": 14, "radical": "言 (words)", "onyomi": ["ゴ"], "kunyomi": ["かた.る"], "category": "School",
        "mnemonic": "Words (言) spoken from five (五) mouths (口) form a language.",
        "visual_breakdown": "言 (words) + 五 (five) + 口 (mouth)",
        "related_kanji": ["言", "話"],
        "common_mistakes": "Used as a suffix for languages (-go).",
        "real_life_usage": ["Japanese language (日本語)", "English (英語)"],
        "vocab": [
            {"word": "日本語", "kana": "にほんご", "romaji": "nihongo", "english": "Japanese Language", "sentence_jp": "日本語を勉強します。", "sentence_kana": "にほんごをべんきょうします。", "sentence_romaji": "Nihongo o benkyou shimasu.", "sentence_eng": "I study Japanese."},
            {"word": "英語", "kana": "えいご", "romaji": "eigo", "english": "English Language", "sentence_jp": "英語がわかりますか。", "sentence_kana": "えいごがわかりますか。", "sentence_romaji": "Eigo ga wakarimasu ka.", "sentence_eng": "Do you understand English?"}
        ]
    },
    {
        "kanji": "国", "meaning": "Country", "jlpt": "N5", "strokes": 8, "radical": "囗 (enclosure)", "onyomi": ["コク"], "kunyomi": ["くに"], "category": "School",
        "mnemonic": "A king (王) with a jewel (丶) inside a border (囗) representing a country.",
        "visual_breakdown": "囗 (enclosure) + 玉 (jewel)",
        "related_kanji": ["口", "円"],
        "common_mistakes": "The jewel is inside the enclosure, not a regular king (王).",
        "real_life_usage": ["Foreign countries (外国)", "China (中国)"],
        "vocab": [
            {"word": "国", "kana": "くに", "romaji": "kuni", "english": "Country", "sentence_jp": "国へ帰ります。", "sentence_kana": "くにへかえります。", "sentence_romaji": "Kuni e kaerimasu.", "sentence_eng": "I return to my country."},
            {"word": "外国", "kana": "がいこく", "romaji": "gaikoku", "english": "Foreign country", "sentence_jp": "外国に行きたい。", "sentence_kana": "がいこくにいきたい。", "sentence_romaji": "Gaikoku ni ikitai.", "sentence_eng": "I want to go to a foreign country."}
        ]
    },
    {
        "kanji": "学", "meaning": "Study / Learning", "jlpt": "N5", "strokes": 8, "radical": "子 (child)", "onyomi": ["ガク", "ガッ"], "kunyomi": ["まな.ぶ"], "category": "School",
        "mnemonic": "A child (子) sitting under a school roof (⺍/冖) studying.",
        "visual_breakdown": "⺍ (crown) + 冖 (cover) + 子 (child)",
        "related_kanji": ["校", "子", "字"],
        "common_mistakes": "Used heavily in education terms.",
        "real_life_usage": ["Students (学生)", "School (学校)"],
        "vocab": [
            {"word": "学生", "kana": "がくせい", "romaji": "gakusei", "english": "Student", "sentence_jp": "私は学生です。", "sentence_kana": "わたしはがくせいです。", "sentence_romaji": "Watashi wa gakusei desu.", "sentence_eng": "I am a student."},
            {"word": "学校", "kana": "がっこう", "romaji": "gakkou", "english": "School", "sentence_jp": "学校へ行きます。", "sentence_kana": "がっこうへいきます。", "sentence_romaji": "Gakkou e ikimasu.", "sentence_eng": "I go to school."},
            {"word": "大学", "kana": "だいがく", "romaji": "daigaku", "english": "University (Big study)", "sentence_jp": "大学で勉強します。", "sentence_kana": "だいがくでべんきょうします。", "sentence_romaji": "Daigaku de benkyou shimasu.", "sentence_eng": "I study at university."}
        ]
    },
    {
        "kanji": "校", "meaning": "School / Exam", "jlpt": "N5", "strokes": 10, "radical": "木 (tree)", "onyomi": ["コウ"], "kunyomi": [], "category": "School",
        "mnemonic": "A tree (木) next to a building where the father (交 cross) rules the school.",
        "visual_breakdown": "木 (tree) + 交 (mix/cross)",
        "related_kanji": ["学", "休"],
        "common_mistakes": "Has a tree radical because old schools were made of wood.",
        "real_life_usage": ["High School (高校)"],
        "vocab": [
            {"word": "学校", "kana": "がっこう", "romaji": "gakkou", "english": "School", "sentence_jp": "学校はどこですか。", "sentence_kana": "がっこうはどこですか。", "sentence_romaji": "Gakkou wa doko desu ka.", "sentence_eng": "Where is the school?"},
            {"word": "高校", "kana": "こうこう", "romaji": "koukou", "english": "High School", "sentence_jp": "高校に行きます。", "sentence_kana": "こうこうにいきます。", "sentence_romaji": "Koukou ni ikimasu.", "sentence_eng": "I go to high school."}
        ]
    },
    {
        "kanji": "名", "meaning": "Name", "jlpt": "N5", "strokes": 6, "radical": "口 (mouth)", "onyomi": ["メイ", "ミョウ"], "kunyomi": ["な"], "category": "School",
        "mnemonic": "In the evening (夕), you must open your mouth (口) and state your name so people know who you are in the dark.",
        "visual_breakdown": "夕 (evening) + 口 (mouth)",
        "related_kanji": ["外", "多"],
        "common_mistakes": "Do not confuse with 外 (outside).",
        "real_life_usage": ["Names (名前)", "Famous (有名)"],
        "vocab": [
            {"word": "名前", "kana": "なまえ", "romaji": "namae", "english": "Name", "sentence_jp": "お名前は何ですか。", "sentence_kana": "おなまえはなんですか。", "sentence_romaji": "Onamae wa nan desu ka.", "sentence_eng": "What is your name?"},
            {"word": "有名", "kana": "ゆうめい", "romaji": "yuumei", "english": "Famous", "sentence_jp": "有名な店です。", "sentence_kana": "ゆうめいなみせです。", "sentence_romaji": "Yuumeina mise desu.", "sentence_eng": "It is a famous store."}
        ]
    },

    # ==========================================
    # TIME
    # ==========================================
    {
        "kanji": "時", "meaning": "Time / Hour", "jlpt": "N5", "strokes": 10, "radical": "日 (sun)", "onyomi": ["ジ"], "kunyomi": ["とき"], "category": "Time",
        "mnemonic": "Measuring time using the sun (日) moving over a temple (寺).",
        "visual_breakdown": "日 (sun) + 寺 (temple)",
        "related_kanji": ["待", "持", "分"],
        "common_mistakes": "Used as the suffix for O'Clock (-ji).",
        "real_life_usage": ["Time (時間)", "O'clock (１時)"],
        "vocab": [
            {"word": "一時", "kana": "いちじ", "romaji": "ichiji", "english": "1 O'clock", "sentence_jp": "今は一時です。", "sentence_kana": "いまはいちじです。", "sentence_romaji": "Ima wa ichiji desu.", "sentence_eng": "It is 1 o'clock now."},
            {"word": "時間", "kana": "じかん", "romaji": "jikan", "english": "Time", "sentence_jp": "時間がありません。", "sentence_kana": "じかんがありません。", "sentence_romaji": "Jikan ga arimasen.", "sentence_eng": "I have no time."},
            {"word": "時計", "kana": "とけい", "romaji": "tokei", "english": "Watch / Clock", "sentence_jp": "時計を買います。", "sentence_kana": "とけいをかいます。", "sentence_romaji": "Tokei o kaimasu.", "sentence_eng": "I buy a watch."}
        ]
    },
    {
        "kanji": "分", "meaning": "Minute / Divide / Understand", "jlpt": "N5", "strokes": 4, "radical": "刀 (knife)", "onyomi": ["フン", "ブン", "プン"], "kunyomi": ["わ.かる", "わ.ける"], "category": "Time",
        "mnemonic": "A knife (刀) dividing (八) something into minutes/parts.",
        "visual_breakdown": "八 (eight/divide) + 刀 (knife)",
        "related_kanji": ["半", "切"],
        "common_mistakes": "Pronunciation changes depending on the number (ippun, nifun, sanpun, yonfun, gofun).",
        "real_life_usage": ["Minutes (５分)", "Understanding (分かる)"],
        "vocab": [
            {"word": "五分", "kana": "ごふん", "romaji": "gofun", "english": "5 Minutes", "sentence_jp": "五分待ちます。", "sentence_kana": "ごふんまちます。", "sentence_romaji": "Gofun machimasu.", "sentence_eng": "I will wait 5 minutes."},
            {"word": "十分", "kana": "じゅっぷん", "romaji": "juppun", "english": "10 Minutes", "sentence_jp": "十分かかります。", "sentence_kana": "じゅっぷんかかります。", "sentence_romaji": "Juppun kakarimasu.", "sentence_eng": "It takes 10 minutes."},
            {"word": "分かる", "kana": "わかる", "romaji": "wakaru", "english": "To understand", "sentence_jp": "日本語が分かります。", "sentence_kana": "にほんごがわかります。", "sentence_romaji": "Nihongo ga wakarimasu.", "sentence_eng": "I understand Japanese."}
        ]
    },
    {
        "kanji": "年", "meaning": "Year", "jlpt": "N5", "strokes": 6, "radical": "干 (dry)", "onyomi": ["ネン"], "kunyomi": ["とし"], "category": "Time",
        "mnemonic": "A person riding an ox across a field over the course of a year.",
        "visual_breakdown": "丿 (drop) + 一 (one) + ヰ (resembles ox/hide) + 丨 (line)",
        "related_kanji": ["午", "手"],
        "common_mistakes": "Do not confuse with 午 (noon).",
        "real_life_usage": ["Next year (来年)", "This year (今年)"],
        "vocab": [
            {"word": "今年", "kana": "ことし", "romaji": "kotoshi", "english": "This year", "sentence_jp": "今年は日本へ行きます。", "sentence_kana": "ことしはにほんへいきます。", "sentence_romaji": "Kotoshi wa nihon e ikimasu.", "sentence_eng": "I am going to Japan this year."},
            {"word": "来年", "kana": "らいねん", "romaji": "rainen", "english": "Next year", "sentence_jp": "来年は忙しいです。", "sentence_kana": "らいねんはいそがしいです。", "sentence_romaji": "Rainen wa isogashii desu.", "sentence_eng": "I will be busy next year."},
            {"word": "去年", "kana": "きょねん", "romaji": "kyonen", "english": "Last year", "sentence_jp": "去年買いました。", "sentence_kana": "きょねんかいました。", "sentence_romaji": "Kyonen kaimashita.", "sentence_eng": "I bought it last year."}
        ]
    },
    {
        "kanji": "午", "meaning": "Noon", "jlpt": "N5", "strokes": 4, "radical": "十 (ten)", "onyomi": ["ゴ"], "kunyomi": [], "category": "Time",
        "mnemonic": "A person standing tall holding a cross at high noon.",
        "visual_breakdown": "𠂉 (person) + 十 (ten/cross)",
        "related_kanji": ["牛", "年"],
        "common_mistakes": "Do NOT push the vertical line up through the top. If you do, it becomes 牛 (cow).",
        "real_life_usage": ["AM (午前)", "PM (午後)"],
        "vocab": [
            {"word": "午前", "kana": "ごぜん", "romaji": "gozen", "english": "A.M.", "sentence_jp": "午前に行きます。", "sentence_kana": "ごぜんにいきます。", "sentence_romaji": "Gozen ni ikimasu.", "sentence_eng": "I will go in the morning."},
            {"word": "午後", "kana": "ごご", "romaji": "gogo", "english": "P.M.", "sentence_jp": "午後に雨が降ります。", "sentence_kana": "ごごにあめがふります。", "sentence_romaji": "Gogo ni ame ga furimasu.", "sentence_eng": "It will rain in the afternoon."}
        ]
    },
    {
        "kanji": "毎", "meaning": "Every", "jlpt": "N5", "strokes": 6, "radical": "毋 (mother)", "onyomi": ["マイ"], "kunyomi": [], "category": "Time",
        "mnemonic": "Every person (人) has a mother (母).",
        "visual_breakdown": "𠂉 (person) + 毋 (mother)",
        "related_kanji": ["母", "海"],
        "common_mistakes": "Used as a prefix for time words.",
        "real_life_usage": ["Every day (毎日)", "Every week (毎週)"],
        "vocab": [
            {"word": "毎日", "kana": "まいにち", "romaji": "mainichi", "english": "Every day", "sentence_jp": "毎日走ります。", "sentence_kana": "まいにちはしります。", "sentence_romaji": "Mainichi hashirimasu.", "sentence_eng": "I run every day."},
            {"word": "毎週", "kana": "まいしゅう", "romaji": "maishuu", "english": "Every week", "sentence_jp": "毎週映画を見ます。", "sentence_kana": "まいしゅうえいがをみます。", "sentence_romaji": "Maishuu eiga o mimasu.", "sentence_eng": "I watch a movie every week."},
            {"word": "毎年", "kana": "まいとし", "romaji": "maitoshi", "english": "Every year", "sentence_jp": "毎年旅行します。", "sentence_kana": "まいとしりょこうします。", "sentence_romaji": "Maitoshi ryokou shimasu.", "sentence_eng": "I travel every year."}
        ]
    },
    {
        "kanji": "週", "meaning": "Week", "jlpt": "N5", "strokes": 11, "radical": "辶 (road)", "onyomi": ["シュウ"], "kunyomi": [], "category": "Time",
        "mnemonic": "Traveling on a road (辶) for a whole week around a mountain (周).",
        "visual_breakdown": "辶 (road) + 周 (circumference/lap)",
        "related_kanji": ["道", "近", "間"],
        "common_mistakes": "The 'road' radical is drawn last.",
        "real_life_usage": ["Next week (来週)", "Last week (先週)"],
        "vocab": [
            {"word": "今週", "kana": "こんしゅう", "romaji": "konshuu", "english": "This week", "sentence_jp": "今週は忙しいです。", "sentence_kana": "こんしゅうはいそがしいです。", "sentence_romaji": "Konshuu wa isogashii desu.", "sentence_eng": "I am busy this week."},
            {"word": "来週", "kana": "らいしゅう", "romaji": "raishuu", "english": "Next week", "sentence_jp": "来週行きます。", "sentence_kana": "らいしゅういきます。", "sentence_romaji": "Raishuu ikimasu.", "sentence_eng": "I will go next week."},
            {"word": "先週", "kana": "せんしゅう", "romaji": "senshuu", "english": "Last week", "sentence_jp": "先週買いました。", "sentence_kana": "せんしゅうかいました。", "sentence_romaji": "Senshuu kaimashita.", "sentence_eng": "I bought it last week."}
        ]
    },
    {
        "kanji": "間", "meaning": "Interval / Between / Duration", "jlpt": "N5", "strokes": 12, "radical": "門 (gate)", "onyomi": ["カン", "ケン"], "kunyomi": ["あいだ", "ま"], "category": "Time",
        "mnemonic": "The sun (日) shining BETWEEN the gates (門).",
        "visual_breakdown": "門 (gate) + 日 (sun)",
        "related_kanji": ["門", "聞", "開"],
        "common_mistakes": "When used with time, it signifies 'duration' (e.g., 時間 = hours duration).",
        "real_life_usage": ["Time (時間)", "Between (間)"],
        "vocab": [
            {"word": "間", "kana": "あいだ", "romaji": "aida", "english": "Between", "sentence_jp": "AとBの間にあります。", "sentence_kana": "AとBのあいだにあります。", "sentence_romaji": "A to B no aida ni arimasu.", "sentence_eng": "It is between A and B."},
            {"word": "時間", "kana": "じかん", "romaji": "jikan", "english": "Time / Hours", "sentence_jp": "三時間かかります。", "sentence_kana": "さんじかんかかります。", "sentence_romaji": "Sanjikan kakarimasu.", "sentence_eng": "It takes 3 hours."},
            {"word": "一週間", "kana": "いっしゅうかん", "romaji": "isshuukan", "english": "One week (duration)", "sentence_jp": "一週間休みます。", "sentence_kana": "いっしゅうかんやすみます。", "sentence_romaji": "Isshuukan yasumimasu.", "sentence_eng": "I will rest for a week."}
        ]
    },
    {
        "kanji": "半", "meaning": "Half", "jlpt": "N5", "strokes": 5, "radical": "十 (ten)", "onyomi": ["ハン"], "kunyomi": ["なか.ば"], "category": "Time",
        "mnemonic": "A sword (十) cutting two lines (丷) and a horizontal line (一) in HALF.",
        "visual_breakdown": "丷 (horns) + 一 (one) + 十 (ten/cross)",
        "related_kanji": ["平", "分"],
        "common_mistakes": "Used to say 'half past' the hour.",
        "real_life_usage": ["Time (半 - half past)"],
        "vocab": [
            {"word": "半", "kana": "はん", "romaji": "han", "english": "Half", "sentence_jp": "半分ください。", "sentence_kana": "はんぶんください。", "sentence_romaji": "Hanbun kudasai.", "sentence_eng": "Please give me half."},
            {"word": "一時半", "kana": "いちじはん", "romaji": "ichijihan", "english": "1:30 (Half past one)", "sentence_jp": "一時半に会います。", "sentence_kana": "いちじはんにあいます。", "sentence_romaji": "Ichijihan ni aimasu.", "sentence_eng": "We will meet at 1:30."}
        ]
    },
    {
        "kanji": "今", "meaning": "Now", "jlpt": "N5", "strokes": 4, "radical": "人 (person)", "onyomi": ["コン", "キン"], "kunyomi": ["いま"], "category": "Time",
        "mnemonic": "A clock pendulum swinging right NOW.",
        "visual_breakdown": "人 (person/roof) + 一 (one) + フ (hook)",
        "related_kanji": ["会", "合"],
        "common_mistakes": "Pronounced 'Kyou' when combined with day (今日), 'Kotoshi' when combined with year (今年).",
        "real_life_usage": ["Now (今)", "Today (今日)"],
        "vocab": [
            {"word": "今", "kana": "いま", "romaji": "ima", "english": "Now", "sentence_jp": "今は何時ですか。", "sentence_kana": "いまはなんじですか。", "sentence_romaji": "Ima wa nanji desu ka.", "sentence_eng": "What time is it now?"},
            {"word": "今日", "kana": "きょう", "romaji": "kyou", "english": "Today", "sentence_jp": "今日は雨です。", "sentence_kana": "きょうはあめです。", "sentence_romaji": "Kyou wa ame desu.", "sentence_eng": "Today is rain."},
            {"word": "今月", "kana": "こんげつ", "romaji": "kongetsu", "english": "This month", "sentence_jp": "今月帰ります。", "sentence_kana": "こんげつかえります。", "sentence_romaji": "Kongetsu kaerimasu.", "sentence_eng": "I will return this month."}
        ]
    },

    # ==========================================
    # ADJECTIVES & CONCEPTS
    # ==========================================
    {
        "kanji": "小", "meaning": "Small", "jlpt": "N5", "strokes": 3, "radical": "小 (small)", "onyomi": ["ショウ"], "kunyomi": ["ちい.さい", "こ", "お"], "category": "Adjectives",
        "mnemonic": "A vertical line divided into two smaller pieces.",
        "visual_breakdown": "亅 (hook) + 八 (divide)",
        "related_kanji": ["少", "大", "水"],
        "common_mistakes": "Do not confuse with 少 (Few) which has an extra slash at the bottom.",
        "real_life_usage": ["Elementary School (小学校)", "Small (小さい)"],
        "vocab": [
            {"word": "小さい", "kana": "ちいさい", "romaji": "chiisai", "english": "Small", "sentence_jp": "小さい犬です。", "sentence_kana": "ちいさいいぬです。", "sentence_romaji": "Chiisai inu desu.", "sentence_eng": "It is a small dog."},
            {"word": "小学校", "kana": "しょうがっこう", "romaji": "shougakkou", "english": "Elementary school", "sentence_jp": "小学校へ行きます。", "sentence_kana": "しょうがっこうへいきます。", "sentence_romaji": "Shougakkou e ikimasu.", "sentence_eng": "I go to elementary school."}
        ]
    },
    {
        "kanji": "大", "meaning": "Big", "jlpt": "N5", "strokes": 3, "radical": "大 (big)", "onyomi": ["ダイ", "タイ"], "kunyomi": ["おお.きい", "おお"], "category": "Adjectives",
        "mnemonic": "A person stretching their arms and legs out to look BIG.",
        "visual_breakdown": "一 (one) + 人 (person)",
        "related_kanji": ["小", "天", "太"],
        "common_mistakes": "If you put a dot at the bottom, it becomes 太 (fat/thick).",
        "real_life_usage": ["University (大学)", "Big (大きい)", "Tough/Hard (大変)"],
        "vocab": [
            {"word": "大きい", "kana": "おおきい", "romaji": "ookii", "english": "Big", "sentence_jp": "大きい車です。", "sentence_kana": "おおきいくるまです。", "sentence_romaji": "Ookii kuruma desu.", "sentence_eng": "It is a big car."},
            {"word": "大学", "kana": "だいがく", "romaji": "daigaku", "english": "University", "sentence_jp": "大学で勉強します。", "sentence_kana": "だいがくでべんきょうします。", "sentence_romaji": "Daigaku de benkyou shimasu.", "sentence_eng": "I study at university."},
            {"word": "大変", "kana": "たいへん", "romaji": "taihen", "english": "Hard / Terrible", "sentence_jp": "仕事が大変です。", "sentence_kana": "しごとがたいへんです。", "sentence_romaji": "Shigoto ga taihen desu.", "sentence_eng": "The work is hard."}
        ]
    },
    {
        "kanji": "少", "meaning": "Few / A little", "jlpt": "N5", "strokes": 4, "radical": "小 (small)", "onyomi": ["ショウ"], "kunyomi": ["すく.ない", "すこ.し"], "category": "Adjectives",
        "mnemonic": "Take something small (小) and cut it even more (丿) to make it a FEW.",
        "visual_breakdown": "小 (small) + 丿 (slash)",
        "related_kanji": ["小", "多", "歩"],
        "common_mistakes": "Often confused with 小 (small). Little vs Few.",
        "real_life_usage": ["A little bit (少し)"],
        "vocab": [
            {"word": "少し", "kana": "すこし", "romaji": "sukoshi", "english": "A little", "sentence_jp": "少し疲れています。", "sentence_kana": "すこしつかれています。", "sentence_romaji": "Sukoshi tsukarete imasu.", "sentence_eng": "I am a little tired."},
            {"word": "少ない", "kana": "すくない", "romaji": "sukunai", "english": "Few / Scarce", "sentence_jp": "人が少ないです。", "sentence_kana": "ひとがすくないです。", "sentence_romaji": "Hito ga sukunai desu.", "sentence_eng": "There are few people."}
        ]
    },
    {
        "kanji": "多", "meaning": "Many / Much", "jlpt": "N5", "strokes": 6, "radical": "夕 (evening)", "onyomi": ["タ"], "kunyomi": ["おお.い"], "category": "Adjectives",
        "mnemonic": "Evening (夕) happens many times (夕) over the years.",
        "visual_breakdown": "夕 (evening) + 夕 (evening)",
        "related_kanji": ["少", "外", "名"],
        "common_mistakes": "Looks like two 'ta' (タ) katakanas stacked.",
        "real_life_usage": ["Many people (人が多い)"],
        "vocab": [
            {"word": "多い", "kana": "おおい", "romaji": "ooi", "english": "Many / Much", "sentence_jp": "車が多いです。", "sentence_kana": "くるまがおおいです。", "sentence_romaji": "Kuruma ga ooi desu.", "sentence_eng": "There are many cars."},
            {"word": "多分", "kana": "たぶん", "romaji": "tabun", "english": "Probably", "sentence_jp": "多分行きます。", "sentence_kana": "たぶんいきます。", "sentence_romaji": "Tabun ikimasu.", "sentence_eng": "I will probably go."}
        ]
    },
    {
        "kanji": "古", "meaning": "Old", "jlpt": "N5", "strokes": 5, "radical": "口 (mouth)", "onyomi": ["コ"], "kunyomi": ["ふる.い"], "category": "Adjectives",
        "mnemonic": "A tombstone (十) over a mouth/skull (口) - very OLD.",
        "visual_breakdown": "十 (cross/ten) + 口 (mouth)",
        "related_kanji": ["新", "居", "固"],
        "common_mistakes": "Used for old THINGS, not old people.",
        "real_life_usage": ["Old things (古い)"],
        "vocab": [
            {"word": "古い", "kana": "ふるい", "romaji": "furui", "english": "Old (thing)", "sentence_jp": "古い家です。", "sentence_kana": "ふるいいえです。", "sentence_romaji": "Furui ie desu.", "sentence_eng": "It is an old house."}
        ]
    },
    {
        "kanji": "新", "meaning": "New", "jlpt": "N5", "strokes": 13, "radical": "斤 (axe)", "onyomi": ["シン"], "kunyomi": ["あたら.しい", "あら.た", "にい"], "category": "Adjectives",
        "mnemonic": "Standing (立) on a tree (木) with an axe (斤) to cut NEW wood.",
        "visual_breakdown": "立 (stand) + 木 (tree) + 斤 (axe)",
        "related_kanji": ["古", "親"],
        "common_mistakes": "Extremely common in names of places and things.",
        "real_life_usage": ["Bullet train (新幹線)", "Newspaper (新聞)", "New (新しい)"],
        "vocab": [
            {"word": "新しい", "kana": "あたらしい", "romaji": "atarashii", "english": "New", "sentence_jp": "新しい車を買いました。", "sentence_kana": "あたらしいうるまをかいました。", "sentence_romaji": "Atarashii kuruma o kaimashita.", "sentence_eng": "I bought a new car."},
            {"word": "新聞", "kana": "しんぶん", "romaji": "shinbun", "english": "Newspaper (New hears)", "sentence_jp": "新聞を読みます。", "sentence_kana": "しんぶんをよみます。", "sentence_romaji": "Shinbun o yomimasu.", "sentence_eng": "I read the newspaper."},
            {"word": "新幹線", "kana": "しんかんせん", "romaji": "shinkansen", "english": "Bullet Train", "sentence_jp": "新幹線に乗ります。", "sentence_kana": "しんかんせんにのります。", "sentence_romaji": "Shinkansen ni norimasu.", "sentence_eng": "I ride the bullet train."}
        ]
    },
    {
        "kanji": "長", "meaning": "Long / Leader", "jlpt": "N5", "strokes": 8, "radical": "長 (long)", "onyomi": ["チョウ"], "kunyomi": ["なが.い"], "category": "Adjectives",
        "mnemonic": "An old man with long hair trailing down his back, acting as the leader.",
        "visual_breakdown": "長 (long)",
        "related_kanji": ["短", "張"],
        "common_mistakes": "Can mean physically long, or the 'head/boss' of a group (like Shachou - company president).",
        "real_life_usage": ["Long (長い)", "President (社長)"],
        "vocab": [
            {"word": "長い", "kana": "ながい", "romaji": "nagai", "english": "Long", "sentence_jp": "髪が長いです。", "sentence_kana": "かみがながいです。", "sentence_romaji": "Kami ga nagai desu.", "sentence_eng": "My hair is long."},
            {"word": "社長", "kana": "しゃちょう", "romaji": "shachou", "english": "Company President", "sentence_jp": "彼は社長です。", "sentence_kana": "かれはしゃちょうです。", "sentence_romaji": "Kare wa shachou desu.", "sentence_eng": "He is the president."}
        ]
    },
    {
        "kanji": "高", "meaning": "High / Expensive", "jlpt": "N5", "strokes": 10, "radical": "高 (high)", "onyomi": ["コウ"], "kunyomi": ["たか.い"], "category": "Adjectives",
        "mnemonic": "A tall multi-story pagoda building.",
        "visual_breakdown": "亠 (lid) + 口 (mouth) + 冂 (border) + 口 (mouth)",
        "related_kanji": ["安", "低"],
        "common_mistakes": "Used for both physical height and price.",
        "real_life_usage": ["Expensive (高い)", "High School (高校)"],
        "vocab": [
            {"word": "高い", "kana": "たかい", "romaji": "takai", "english": "High / Expensive", "sentence_jp": "この本は高いです。", "sentence_kana": "このほんはたかいです。", "sentence_romaji": "Kono hon wa takai desu.", "sentence_eng": "This book is expensive."},
            {"word": "高校", "kana": "こうこう", "romaji": "koukou", "english": "High School", "sentence_jp": "高校生です。", "sentence_kana": "こうこうせいです。", "sentence_romaji": "Koukousei desu.", "sentence_eng": "I am a high school student."}
        ]
    },
    {
        "kanji": "白", "meaning": "White", "jlpt": "N5", "strokes": 5, "radical": "白 (white)", "onyomi": ["ハク", "ビャク"], "kunyomi": ["しろ", "しろ.い"], "category": "Adjectives",
        "mnemonic": "A drop of light on the sun (日) making it blindingly WHITE.",
        "visual_breakdown": "丿 (drop) + 日 (sun)",
        "related_kanji": ["百", "自", "日"],
        "common_mistakes": "Do not confuse with 百 (hundred) which has a horizontal top line.",
        "real_life_usage": ["Colors (白い)", "Interesting (面白い)"],
        "vocab": [
            {"word": "白い", "kana": "しろい", "romaji": "shiroi", "english": "White", "sentence_jp": "白いシャツを着ます。", "sentence_kana": "しろいシャツをきます。", "sentence_romaji": "Shiroi shatsu o kimasu.", "sentence_eng": "I wear a white shirt."},
            {"word": "面白い", "kana": "おもしろい", "romaji": "omoshiroi", "english": "Interesting (Face white)", "sentence_jp": "この映画は面白いです。", "sentence_kana": "このえいがはおもしろいです。", "sentence_romaji": "Kono eiga wa omoshiroi desu.", "sentence_eng": "This movie is interesting."}
        ]
    },
    {
        "kanji": "気", "meaning": "Spirit / Feeling / Air", "jlpt": "N5", "strokes": 6, "radical": "气 (air)", "onyomi": ["キ", "ケ"], "kunyomi": [], "category": "Adjectives",
        "mnemonic": "Steam (气) rising from rice (メ) giving energy/spirit.",
        "visual_breakdown": "气 (air) + メ (sheaf/rice)",
        "related_kanji": ["空", "天", "風"],
        "common_mistakes": "Used in hundreds of compounds related to feelings, energy, and weather.",
        "real_life_usage": ["Weather (天気)", "Healthy (元気)", "Careful (気をつけて)"],
        "vocab": [
            {"word": "元気", "kana": "げんき", "romaji": "genki", "english": "Healthy / Energetic", "sentence_jp": "お元気ですか。", "sentence_kana": "おげんきですか。", "sentence_romaji": "Ogenki desu ka.", "sentence_eng": "Are you well?"},
            {"word": "天気", "kana": "てんき", "romaji": "tenki", "english": "Weather", "sentence_jp": "いい天気です。", "sentence_kana": "いいてんきです。", "sentence_romaji": "Ii tenki desu.", "sentence_eng": "The weather is good."},
            {"word": "気をつける", "kana": "きをつける", "romaji": "ki o tsukeru", "english": "To be careful", "sentence_jp": "気をつけてください。", "sentence_kana": "きをつけてください。", "sentence_romaji": "Ki o tsukete kudasai.", "sentence_eng": "Please be careful."}
        ]
    },
    {
        "kanji": "何", "meaning": "What", "jlpt": "N5", "strokes": 7, "radical": "人 (person)", "onyomi": ["カ"], "kunyomi": ["なに", "なん"], "category": "Adjectives",
        "mnemonic": "A person (亻) carrying a box (可) asking 'WHAT is inside?'",
        "visual_breakdown": "亻 (person) + 可 (can/possible)",
        "related_kanji": ["可", "河"],
        "common_mistakes": "Pronounced 'nan' before D, N, T sounds and counters. Pronounced 'nani' before particles like ga, o.",
        "real_life_usage": ["Questions (何ですか)"],
        "vocab": [
            {"word": "何", "kana": "なに", "romaji": "nani", "english": "What", "sentence_jp": "何をしますか。", "sentence_kana": "なにをしますか。", "sentence_romaji": "Nani o shimasu ka.", "sentence_eng": "What will you do?"},
            {"word": "何時", "kana": "なんじ", "romaji": "nanji", "english": "What time", "sentence_jp": "今、何時ですか。", "sentence_kana": "いま、なんじですか。", "sentence_romaji": "Ima, nanji desu ka.", "sentence_eng": "What time is it now?"},
            {"word": "何人", "kana": "なんにん", "romaji": "nannin", "english": "How many people", "sentence_jp": "何人いますか。", "sentence_kana": "なんにんいますか。", "sentence_romaji": "Nannin imasu ka.", "sentence_eng": "How many people are there?"}
        ]
    },
    # ==========================================
    # VERBS & PLACES
    # ==========================================
    {
        "kanji": "食", "meaning": "Eat / Food", "jlpt": "N5", "strokes": 9, "radical": "食 (eat)", "onyomi": ["ショク"], "kunyomi": ["た.べる"], "category": "Verbs",
        "mnemonic": "People (人) gathering under a roof to eat good (良) food.",
        "visual_breakdown": "人 (person) + 良 (good)",
        "related_kanji": ["飲", "館"],
        "common_mistakes": "The bottom is 良 (good), not exactly just straight lines.",
        "real_life_usage": ["Cafeteria (食堂)", "Food (食べ物)"],
        "vocab": [
            {"word": "食べる", "kana": "たべる", "romaji": "taberu", "english": "To eat", "sentence_jp": "ご飯を食べます。", "sentence_kana": "ごはんをたべます。", "sentence_romaji": "Gohan o tabemasu.", "sentence_eng": "I eat rice."},
            {"word": "食べ物", "kana": "たべもの", "romaji": "tabemono", "english": "Food", "sentence_jp": "好きな食べ物は何ですか。", "sentence_kana": "すきなたべものはなんですか。", "sentence_romaji": "Sukina tabemono wa nan desu ka.", "sentence_eng": "What is your favorite food?"},
            {"word": "食事", "kana": "しょくじ", "romaji": "shokuji", "english": "Meal", "sentence_jp": "家族と食事します。", "sentence_kana": "かぞくとしょくじします。", "sentence_romaji": "Kazoku to shokuji shimasu.", "sentence_eng": "I have a meal with my family."}
        ]
    },
    {
        "kanji": "飲", "meaning": "Drink", "jlpt": "N5", "strokes": 12, "radical": "食 (eat)", "onyomi": ["イン"], "kunyomi": ["の.む"], "category": "Verbs",
        "mnemonic": "Eating/food (食) going down the throat lacking air (欠). A liquid.",
        "visual_breakdown": "食 (eat) + 欠 (lack/yawn)",
        "related_kanji": ["食", "吹"],
        "common_mistakes": "The left side is the 'eat' radical slightly squished.",
        "real_life_usage": ["Drinks (飲み物)", "Restaurants (飲食店)"],
        "vocab": [
            {"word": "飲む", "kana": "のむ", "romaji": "nomu", "english": "To drink", "sentence_jp": "水を飲みます。", "sentence_kana": "みずをのみます。", "sentence_romaji": "Mizu o nomimasu.", "sentence_eng": "I drink water."},
            {"word": "飲み物", "kana": "のみもの", "romaji": "nomimono", "english": "Drink / Beverage", "sentence_jp": "冷たい飲み物が欲しいです。", "sentence_kana": "つめたいのみものがほしいです。", "sentence_romaji": "Tsumetai nomimono ga hoshii desu.", "sentence_eng": "I want a cold drink."}
        ]
    },
    {
        "kanji": "見", "meaning": "See / Look", "jlpt": "N5", "strokes": 7, "radical": "見 (see)", "onyomi": ["ケン"], "kunyomi": ["み.る", "み.える", "み.せる"], "category": "Verbs",
        "mnemonic": "An eye (目) on legs (儿) walking around to SEE things.",
        "visual_breakdown": "目 (eye) + 儿 (legs)",
        "related_kanji": ["目", "貝", "覚"],
        "common_mistakes": "Ensure you draw the 'eye' part completely, not the 'sun' (日).",
        "real_life_usage": ["Sightseeing (見物)", "Showing (見せる)"],
        "vocab": [
            {"word": "見る", "kana": "みる", "romaji": "miru", "english": "To see / watch", "sentence_jp": "テレビを見ます。", "sentence_kana": "テレビをみます。", "sentence_romaji": "Terebi o mimasu.", "sentence_eng": "I watch TV."},
            {"word": "見せる", "kana": "みせる", "romaji": "miseru", "english": "To show", "sentence_jp": "写真を見せてください。", "sentence_kana": "しゃしんをみせてください。", "sentence_romaji": "Shashin o misete kudasai.", "sentence_eng": "Please show me the photo."},
            {"word": "見える", "kana": "みえる", "romaji": "mieru", "english": "To be visible", "sentence_jp": "山が見えます。", "sentence_kana": "やまがみえます。", "sentence_romaji": "Yama ga miemasu.", "sentence_eng": "The mountain is visible."}
        ]
    },
    {
        "kanji": "聞", "meaning": "Listen / Hear / Ask", "jlpt": "N5", "strokes": 14, "radical": "耳 (ear)", "onyomi": ["ブン", "モン"], "kunyomi": ["き.く", "き.こえる"], "category": "Verbs",
        "mnemonic": "An ear (耳) listening through a gate/door (門).",
        "visual_breakdown": "門 (gate) + 耳 (ear)",
        "related_kanji": ["門", "耳", "間"],
        "common_mistakes": "Do not confuse with 間 (interval) which has a sun (日) inside the gate.",
        "real_life_usage": ["Newspaper (新聞)", "Listening (聞く)"],
        "vocab": [
            {"word": "聞く", "kana": "きく", "romaji": "kiku", "english": "To listen / hear / ask", "sentence_jp": "音楽を聞きます。", "sentence_kana": "おんがくをききます。", "sentence_romaji": "Ongaku o kikimasu.", "sentence_eng": "I listen to music."},
            {"word": "新聞", "kana": "しんぶん", "romaji": "shinbun", "english": "Newspaper", "sentence_jp": "毎朝新聞を読みます。", "sentence_kana": "まいあさしんぶんをよみます。", "sentence_romaji": "Maiasa shinbun o yomimasu.", "sentence_eng": "I read the newspaper every morning."},
            {"word": "聞こえる", "kana": "きこえる", "romaji": "kikoeru", "english": "To be audible", "sentence_jp": "鳥の声が聞こえます。", "sentence_kana": "とりのこえがきこえます。", "sentence_romaji": "Tori no koe ga kikoemasu.", "sentence_eng": "I can hear the birds' voices."}
        ]
    },
    {
        "kanji": "行", "meaning": "Go", "jlpt": "N5", "strokes": 6, "radical": "行 (go)", "onyomi": ["コウ", "ギョウ"], "kunyomi": ["い.く", "ゆ.く", "おこな.う"], "category": "Verbs",
        "mnemonic": "A picture of a crossroads, where you GO.",
        "visual_breakdown": "彳 (step) + 亍 (step)",
        "related_kanji": ["来", "帰"],
        "common_mistakes": "Do not confuse the right side with 丁.",
        "real_life_usage": ["Travel (旅行)", "Banks (銀行)"],
        "vocab": [
            {"word": "行く", "kana": "いく", "romaji": "iku", "english": "To go", "sentence_jp": "学校へ行きます。", "sentence_kana": "がっこうへいきます。", "sentence_romaji": "Gakkou e ikimasu.", "sentence_eng": "I go to school."},
            {"word": "旅行", "kana": "りょこう", "romaji": "ryokou", "english": "Travel", "sentence_jp": "日本へ旅行します。", "sentence_kana": "にほんへりょこうします。", "sentence_romaji": "Nihon e ryokou shimasu.", "sentence_eng": "I will travel to Japan."},
            {"word": "銀行", "kana": "ぎんこう", "romaji": "ginkou", "english": "Bank", "sentence_jp": "銀行でお金を下ろします。", "sentence_kana": "ぎんこうでおかねをおろします。", "sentence_romaji": "Ginkou de okane o oroshimasu.", "sentence_eng": "I withdraw money at the bank."}
        ]
    },
    {
        "kanji": "来", "meaning": "Come", "jlpt": "N5", "strokes": 7, "radical": "木 (tree)", "onyomi": ["ライ"], "kunyomi": ["く.る", "き.ます", "こ.ない"], "category": "Verbs",
        "mnemonic": "A tree (木) with two people coming to sit under it.",
        "visual_breakdown": "一 (one) + 丷 (horns) + 木 (tree)",
        "related_kanji": ["行", "未"],
        "common_mistakes": "The verb 'kuru' is irregular. (Kimasu, Konai, Kite).",
        "real_life_usage": ["Next year (来年)", "Next week (来週)"],
        "vocab": [
            {"word": "来る", "kana": "くる", "romaji": "kuru", "english": "To come", "sentence_jp": "友達が来ます。", "sentence_kana": "ともだちがきます。", "sentence_romaji": "Tomodachi ga kimasu.", "sentence_eng": "My friend will come."},
            {"word": "来年", "kana": "らいねん", "romaji": "rainen", "english": "Next year", "sentence_jp": "来年結婚します。", "sentence_kana": "らいねんけっこんします。", "sentence_romaji": "Rainen kekkon shimasu.", "sentence_eng": "I will get married next year."},
            {"word": "来週", "kana": "らいしゅう", "romaji": "raishuu", "english": "Next week", "sentence_jp": "来週テストがあります。", "sentence_kana": "らいしゅうテストがあります。", "sentence_romaji": "Raishuu tesuto ga arimasu.", "sentence_eng": "There is a test next week."}
        ]
    },
    {
        "kanji": "言", "meaning": "Say / Word", "jlpt": "N5", "strokes": 7, "radical": "言 (words)", "onyomi": ["ゲン", "ゴン"], "kunyomi": ["い.う", "こと"], "category": "Verbs",
        "mnemonic": "Sound waves coming out of a mouth (口).",
        "visual_breakdown": "亠 (lid) + 二 (two) + 口 (mouth)",
        "related_kanji": ["語", "話", "読"],
        "common_mistakes": "Used as a radical (訁) on the left side of MANY communication kanji.",
        "real_life_usage": ["Words (言葉)", "Say (言う)"],
        "vocab": [
            {"word": "言う", "kana": "いう", "romaji": "iu", "english": "To say", "sentence_jp": "「ありがとう」と言いました。", "sentence_kana": "「ありがとう」といいました。", "sentence_romaji": "「Arigatou」 to iimashita.", "sentence_eng": "I said 'Thank you'."},
            {"word": "言葉", "kana": "ことば", "romaji": "kotoba", "english": "Word / Language", "sentence_jp": "言葉が分かりません。", "sentence_kana": "ことばがわかりません。", "sentence_romaji": "Kotoba ga wakarimasen.", "sentence_eng": "I do not understand the words."}
        ]
    },
    {
        "kanji": "話", "meaning": "Talk / Speak / Tale", "jlpt": "N5", "strokes": 13, "radical": "言 (words)", "onyomi": ["ワ"], "kunyomi": ["はな.す", "はなし"], "category": "Verbs",
        "mnemonic": "Saying words (言) with your tongue (舌) allows you to SPEAK.",
        "visual_breakdown": "言 (words) + 舌 (tongue)",
        "related_kanji": ["語", "言"],
        "common_mistakes": "Do not confuse the right side with 古 (old). It is 舌 (tongue).",
        "real_life_usage": ["Phone (電話)", "Conversation (会話)"],
        "vocab": [
            {"word": "話す", "kana": "はなす", "romaji": "hanasu", "english": "To talk / speak", "sentence_jp": "日本語を話します。", "sentence_kana": "にほんごをはなします。", "sentence_romaji": "Nihongo o hanashimasu.", "sentence_eng": "I speak Japanese."},
            {"word": "話", "kana": "はなし", "romaji": "hanashi", "english": "Story / Talk", "sentence_jp": "面白い話を聞きました。", "sentence_kana": "おもしろいはなしをききました。", "sentence_romaji": "Omoshiroi hanashi o kikimashita.", "sentence_eng": "I heard an interesting story."},
            {"word": "電話", "kana": "でんわ", "romaji": "denwa", "english": "Telephone", "sentence_jp": "電話をかけます。", "sentence_kana": "でんわをかけます。", "sentence_romaji": "Denwa o kakemasu.", "sentence_eng": "I make a phone call."}
        ]
    },
    {
        "kanji": "読", "meaning": "Read", "jlpt": "N5", "strokes": 14, "radical": "言 (words)", "onyomi": ["ドク"], "kunyomi": ["よ.む"], "category": "Verbs",
        "mnemonic": "Words (言) that are sold (売) are in books that you READ.",
        "visual_breakdown": "言 (words) + 売 (sell)",
        "related_kanji": ["書", "語"],
        "common_mistakes": "The right side is slightly modified from standard 売 (sell).",
        "real_life_usage": ["Reading books (本を読む)", "Reading comprehension (読解)"],
        "vocab": [
            {"word": "読む", "kana": "よむ", "romaji": "yomu", "english": "To read", "sentence_jp": "本を読みます。", "sentence_kana": "ほんをよみます。", "sentence_romaji": "Hon o yomimasu.", "sentence_eng": "I read a book."},
            {"word": "読書", "kana": "どくしょ", "romaji": "dokusho", "english": "Reading (hobby)", "sentence_jp": "趣味は読書です。", "sentence_kana": "しゅみはどくしょです。", "sentence_romaji": "Shumi wa dokusho desu.", "sentence_eng": "My hobby is reading."}
        ]
    },
    {
        "kanji": "書", "meaning": "Write", "jlpt": "N5", "strokes": 10, "radical": "曰 (say)", "onyomi": ["ショ"], "kunyomi": ["か.く"], "category": "Verbs",
        "mnemonic": "A hand holding a brush/pen drawing lines over the sun (日) to WRITE.",
        "visual_breakdown": "聿 (brush) + 日 (sun)",
        "related_kanji": ["読", "筆"],
        "common_mistakes": "Has many horizontal lines. Be sure to count them correctly.",
        "real_life_usage": ["Library (図書館)", "Dictionary (辞書)"],
        "vocab": [
            {"word": "書く", "kana": "かく", "romaji": "kaku", "english": "To write", "sentence_jp": "手紙を書きます。", "sentence_kana": "てがみをかきます。", "sentence_romaji": "Tegami o kakimasu.", "sentence_eng": "I write a letter."},
            {"word": "図書館", "kana": "としょかん", "romaji": "toshokan", "english": "Library", "sentence_jp": "図書館で勉強します。", "sentence_kana": "としょかんでべんきょうします。", "sentence_romaji": "Toshokan de benkyou shimasu.", "sentence_eng": "I study at the library."},
            {"word": "辞書", "kana": "じしょ", "romaji": "jisho", "english": "Dictionary", "sentence_jp": "辞書を引きます。", "sentence_kana": "じしょをひきます。", "sentence_romaji": "Jisho o hikimasu.", "sentence_eng": "I look it up in the dictionary."}
        ]
    },
    {
        "kanji": "買", "meaning": "Buy", "jlpt": "N5", "strokes": 12, "radical": "貝 (shell)", "onyomi": ["バイ"], "kunyomi": ["か.う"], "category": "Verbs",
        "mnemonic": "A net (罒) catching shells (貝). Shells used to be used as money to BUY things.",
        "visual_breakdown": "罒 (net) + 貝 (shell/money)",
        "related_kanji": ["売", "貝"],
        "common_mistakes": "The top is an eye/net, not the number four (四).",
        "real_life_usage": ["Shopping (買い物)"],
        "vocab": [
            {"word": "買う", "kana": "かう", "romaji": "kau", "english": "To buy", "sentence_jp": "新しい車を買います。", "sentence_kana": "あたらしいくるまをかいます。", "sentence_romaji": "Atarashii kuruma o kaimasu.", "sentence_eng": "I will buy a new car."},
            {"word": "買い物", "kana": "かいもの", "romaji": "kaimono", "english": "Shopping", "sentence_jp": "デパートへ買い物に行きます。", "sentence_kana": "デパートへかいものにいきます。", "sentence_romaji": "Depaato e kaimono ni ikimasu.", "sentence_eng": "I go shopping at the department store."}
        ]
    },
    {
        "kanji": "立", "meaning": "Stand", "jlpt": "N5", "strokes": 5, "radical": "立 (stand)", "onyomi": ["リツ", "リュウ"], "kunyomi": ["た.つ"], "category": "Verbs",
        "mnemonic": "A person standing on the ground with their arms out.",
        "visual_breakdown": "立 (stand)",
        "related_kanji": ["音", "暗"],
        "common_mistakes": "Used as the top radical in many other kanji like 音 (sound) and 新 (new).",
        "real_life_usage": ["Stand up (立つ)", "National (国立)"],
        "vocab": [
            {"word": "立つ", "kana": "たつ", "romaji": "tatsu", "english": "To stand", "sentence_jp": "立ってください。", "sentence_kana": "たってください。", "sentence_romaji": "Tatte kudasai.", "sentence_eng": "Please stand up."},
            {"word": "国立", "kana": "こくりつ", "romaji": "kokuritsu", "english": "National", "sentence_jp": "国立大学です。", "sentence_kana": "こくりつだいがくです。", "sentence_romaji": "Kokuritsu daigaku desu.", "sentence_eng": "It is a national university."}
        ]
    },
    {
        "kanji": "休", "meaning": "Rest", "jlpt": "N5", "strokes": 6, "radical": "人 (person)", "onyomi": ["キュウ"], "kunyomi": ["やす.む", "やす.み"], "category": "Verbs",
        "mnemonic": "A person (亻) leaning against a tree (木) to REST.",
        "visual_breakdown": "亻 (person) + 木 (tree)",
        "related_kanji": ["体", "木"],
        "common_mistakes": "Do not confuse with 体 (body) which has 'root/book' (本) instead of 'tree'.",
        "real_life_usage": ["Holidays (休み)", "Absence (休む)"],
        "vocab": [
            {"word": "休む", "kana": "やすむ", "romaji": "yasumu", "english": "To rest / take a day off", "sentence_jp": "今日は仕事を休みます。", "sentence_kana": "きょうはしごとをやすみます。", "sentence_romaji": "Kyou wa shigoto o yasumimasu.", "sentence_eng": "I am taking the day off from work today."},
            {"word": "休み", "kana": "やすみ", "romaji": "yasumi", "english": "Holiday / Break", "sentence_jp": "明日は休みです。", "sentence_kana": "あしたはやすみです。", "sentence_romaji": "Ashita wa yasumi desu.", "sentence_eng": "Tomorrow is a holiday."},
            {"word": "夏休み", "kana": "なつやすみ", "romaji": "natsuyasumi", "english": "Summer vacation", "sentence_jp": "夏休みに海へ行きます。", "sentence_kana": "なつやすみにうみへいきます。", "sentence_romaji": "Natsuyasumi ni umi e ikimasu.", "sentence_eng": "I will go to the sea during summer vacation."}
        ]
    },
    {
        "kanji": "入", "meaning": "Enter", "jlpt": "N5", "strokes": 2, "radical": "入 (enter)", "onyomi": ["ニュウ"], "kunyomi": ["はい.る", "い.れる"], "category": "Verbs",
        "mnemonic": "A wedge entering a space.",
        "visual_breakdown": "入 (enter)",
        "related_kanji": ["人", "八"],
        "common_mistakes": "The RIGHT stroke is longer than the left stroke. (Opposite of 人 - person).",
        "real_life_usage": ["Entrance (入口)", "Insert (入れる)"],
        "vocab": [
            {"word": "入る", "kana": "はいる", "romaji": "hairu", "english": "To enter", "sentence_jp": "部屋に入ります。", "sentence_kana": "へやにはいります。", "sentence_romaji": "Heya ni hairimasu.", "sentence_eng": "I enter the room."},
            {"word": "入れる", "kana": "いれる", "romaji": "ireru", "english": "To put in", "sentence_jp": "かばんに本を入れます。", "sentence_kana": "かばんにほんをいれます。", "sentence_romaji": "Kaban ni hon o iremasu.", "sentence_eng": "I put the book in the bag."},
            {"word": "入口", "kana": "いりぐち", "romaji": "iriguchi", "english": "Entrance", "sentence_jp": "入口はあそこです。", "sentence_kana": "いりぐちはあそこです。", "sentence_romaji": "Iriguchi wa asoko desu.", "sentence_eng": "The entrance is over there."}
        ]
    },
    {
        "kanji": "出", "meaning": "Exit / Leave", "jlpt": "N5", "strokes": 5, "radical": "凵 (box)", "onyomi": ["シュツ", "スイ"], "kunyomi": ["で.る", "だ.す"], "category": "Verbs",
        "mnemonic": "Two mountains (山) stacked, showing something climbing OUT.",
        "visual_breakdown": "山 (mountain) + 山 (mountain)",
        "related_kanji": ["山"],
        "common_mistakes": "Make sure the middle vertical line passes through completely.",
        "real_life_usage": ["Exit (出口)", "Departure (出発)"],
        "vocab": [
            {"word": "出る", "kana": "でる", "romaji": "deru", "english": "To exit / leave", "sentence_jp": "家を出ます。", "sentence_kana": "いえをでます。", "sentence_romaji": "Ie o demasu.", "sentence_eng": "I leave the house."},
            {"word": "出す", "kana": "だす", "romaji": "dasu", "english": "To take out / submit", "sentence_jp": "宿題を出します。", "sentence_kana": "しゅくだいをだします。", "sentence_romaji": "Shukudai o dashimasu.", "sentence_eng": "I submit the homework."},
            {"word": "出口", "kana": "でぐち", "romaji": "deguchi", "english": "Exit", "sentence_jp": "出口から出てください。", "sentence_kana": "でぐちからでてください。", "sentence_romaji": "Deguchi kara dete kudasai.", "sentence_eng": "Please exit from the exit."}
        ]
    },
    {
        "kanji": "生", "meaning": "Life / Birth", "jlpt": "N5", "strokes": 5, "radical": "生 (life)", "onyomi": ["セイ", "ショウ"], "kunyomi": ["い.きる", "う.まれる", "なま"], "category": "Places & Concepts",
        "mnemonic": "A plant growing out of the earth (土) showing LIFE.",
        "visual_breakdown": "土 (soil) + 丿 (slash) + 一 (one)",
        "related_kanji": ["王", "土"],
        "common_mistakes": "Has over a dozen readings depending on the word.",
        "real_life_usage": ["Teacher (先生)", "Student (学生)", "Raw (生)"],
        "vocab": [
            {"word": "先生", "kana": "せんせい", "romaji": "sensei", "english": "Teacher", "sentence_jp": "先生に聞きます。", "sentence_kana": "せんせいきききます。", "sentence_romaji": "Sensei ni kikimasu.", "sentence_eng": "I will ask the teacher."},
            {"word": "学生", "kana": "がくせい", "romaji": "gakusei", "english": "Student", "sentence_jp": "私は学生です。", "sentence_kana": "わたしはがくせいです。", "sentence_romaji": "Watashi wa gakusei desu.", "sentence_eng": "I am a student."},
            {"word": "生まれる", "kana": "うまれる", "romaji": "umareru", "english": "To be born", "sentence_jp": "日本で生まれました。", "sentence_kana": "にほんでうまれました。", "sentence_romaji": "Nihon de umaremashita.", "sentence_eng": "I was born in Japan."}
        ]
    },
    {
        "kanji": "車", "meaning": "Car / Vehicle", "jlpt": "N5", "strokes": 7, "radical": "車 (car)", "onyomi": ["シャ"], "kunyomi": ["くるま"], "category": "Places & Concepts",
        "mnemonic": "A bird's eye view of a cart with two wheels and an axle going down the middle.",
        "visual_breakdown": "車 (car)",
        "related_kanji": ["東", "連"],
        "common_mistakes": "Used as a radical for almost all vehicles.",
        "real_life_usage": ["Trains (電車)", "Bicycles (自転車)", "Cars (車)"],
        "vocab": [
            {"word": "車", "kana": "くるま", "romaji": "kuruma", "english": "Car", "sentence_jp": "車を運転します。", "sentence_kana": "くるまをうんてんします。", "sentence_romaji": "Kuruma o unten shimasu.", "sentence_eng": "I drive a car."},
            {"word": "電車", "kana": "でんしゃ", "romaji": "densha", "english": "Train", "sentence_jp": "電車に乗ります。", "sentence_kana": "でんしゃにのります。", "sentence_romaji": "Densha ni norimasu.", "sentence_eng": "I ride the train."},
            {"word": "自転車", "kana": "じてんしゃ", "romaji": "jitensha", "english": "Bicycle", "sentence_jp": "自転車で行きます。", "sentence_kana": "じてんしゃでいきます。", "sentence_romaji": "Jitensha de ikimasu.", "sentence_eng": "I go by bicycle."}
        ]
    },
    {
        "kanji": "電", "meaning": "Electricity", "jlpt": "N5", "strokes": 13, "radical": "雨 (rain)", "onyomi": ["デン"], "kunyomi": [], "category": "Places & Concepts",
        "mnemonic": "Lightning (electricity) striking a rice field (田) during the rain (雨).",
        "visual_breakdown": "雨 (rain) + 田 (field) + 乚 (hook)",
        "related_kanji": ["雨", "雷"],
        "common_mistakes": "The bottom right hooks outwards like lightning.",
        "real_life_usage": ["Train (電車)", "Phone (電話)", "Electricity (電気)"],
        "vocab": [
            {"word": "電車", "kana": "でんしゃ", "romaji": "densha", "english": "Train", "sentence_jp": "電車が来ます。", "sentence_kana": "でんしゃがきます。", "sentence_romaji": "Densha ga kimasu.", "sentence_eng": "The train is coming."},
            {"word": "電話", "kana": "でんわ", "romaji": "denwa", "english": "Telephone", "sentence_jp": "電話番号は何ですか。", "sentence_kana": "でんわばんごうはなんですか。", "sentence_romaji": "Denwa bangou wa nan desu ka.", "sentence_eng": "What is your phone number?"},
            {"word": "電気", "kana": "でんき", "romaji": "denki", "english": "Electricity / Light", "sentence_jp": "電気を消してください。", "sentence_kana": "でんきをけしてください。", "sentence_romaji": "Denki o keshite kudasai.", "sentence_eng": "Please turn off the light."}
        ]
    },
    {
        "kanji": "道", "meaning": "Road / Way", "jlpt": "N5", "strokes": 12, "radical": "辶 (road)", "onyomi": ["ドウ", "トウ"], "kunyomi": ["みち"], "category": "Places & Concepts",
        "mnemonic": "A head/chief (首) walking along a road (辶).",
        "visual_breakdown": "辶 (road) + 首 (neck/head)",
        "related_kanji": ["週", "近"],
        "common_mistakes": "Used heavily in martial arts (Judo, Kendo, Karate-do) meaning 'The Way'.",
        "real_life_usage": ["Streets", "Water supply (水道)", "Calligraphy (書道)"],
        "vocab": [
            {"word": "道", "kana": "みち", "romaji": "michi", "english": "Road / Street", "sentence_jp": "道を歩きます。", "sentence_kana": "みちをあるきます。", "sentence_romaji": "Michi o arukimasu.", "sentence_eng": "I walk down the street."},
            {"word": "水道", "kana": "すいどう", "romaji": "suidou", "english": "Water supply", "sentence_jp": "水道が止まりました。", "sentence_kana": "すいどうがとまりました。", "sentence_romaji": "Suidou ga tomarimashita.", "sentence_eng": "The water supply stopped."},
            {"word": "柔道", "kana": "じゅうどう", "romaji": "juudou", "english": "Judo", "sentence_jp": "柔道を習います。", "sentence_kana": "じゅうどうをならいます。", "sentence_romaji": "Juudou o naraimasu.", "sentence_eng": "I learn Judo."}
        ]
    },
    {
        "kanji": "社", "meaning": "Company / Shrine", "jlpt": "N5", "strokes": 7, "radical": "示 (altar)", "onyomi": ["シャ"], "kunyomi": ["やしろ"], "category": "Places & Concepts",
        "mnemonic": "People gathering at a shrine/altar (示) on the dirt (土) to form a society or company.",
        "visual_breakdown": "示 (altar) + 土 (soil)",
        "related_kanji": ["神", "土"],
        "common_mistakes": "Do not confuse the left radical (示) with clothes (衤).",
        "real_life_usage": ["Company (会社)", "Society (社会)"],
        "vocab": [
            {"word": "会社", "kana": "かいしゃ", "romaji": "kaisha", "english": "Company", "sentence_jp": "会社で働きます。", "sentence_kana": "かいしゃではたらきます。", "sentence_romaji": "Kaisha de hatarakimasu.", "sentence_eng": "I work at a company."},
            {"word": "社長", "kana": "しゃちょう", "romaji": "shachou", "english": "Company President", "sentence_jp": "社長に会います。", "sentence_kana": "しゃちょうにあいます。", "sentence_romaji": "Shachou ni aimasu.", "sentence_eng": "I will meet the president."},
            {"word": "社会", "kana": "しゃかい", "romaji": "shakai", "english": "Society", "sentence_jp": "社会のルールを守ります。", "sentence_kana": "しゃかいのルールをまもります。", "sentence_romaji": "Shakai no ruuru o mamorimasu.", "sentence_eng": "I follow the rules of society."}
        ]
    },
    {
        "kanji": "店", "meaning": "Shop / Store", "jlpt": "N5", "strokes": 8, "radical": "广 (roof)", "onyomi": ["テン"], "kunyomi": ["みせ"], "category": "Places & Concepts",
        "mnemonic": "A fortune teller (占) under a canopy/roof (广) running a small shop.",
        "visual_breakdown": "广 (roof) + 占 (fortune)",
        "related_kanji": ["広", "座"],
        "common_mistakes": "Has a wide roof radical, not a full box.",
        "real_life_usage": ["Stores (お店)", "Cafes (喫茶店)"],
        "vocab": [
            {"word": "店", "kana": "みせ", "romaji": "mise", "english": "Shop / Store", "sentence_jp": "あの店は安いです。", "sentence_kana": "あのみせはやすいです。", "sentence_romaji": "Ano mise wa yasui desu.", "sentence_eng": "That store is cheap."},
            {"word": "喫茶店", "kana": "きっさてん", "romaji": "kissaten", "english": "Coffee shop", "sentence_jp": "喫茶店でコーヒーを飲みます。", "sentence_kana": "きっさてんでコーヒーをのみます。", "sentence_romaji": "Kissaten de koohii o nomimasu.", "sentence_eng": "I drink coffee at a coffee shop."}
        ]
    },
    {
        "kanji": "駅", "meaning": "Station", "jlpt": "N5", "strokes": 14, "radical": "馬 (horse)", "onyomi": ["エキ"], "kunyomi": [], "category": "Places & Concepts",
        "mnemonic": "In the old days, horses (馬) were stationed at a measuring post (尺) - like a train station today.",
        "visual_breakdown": "馬 (horse) + 尺 (measure/ruler)",
        "related_kanji": ["馬", "訳"],
        "common_mistakes": "The left side is a full horse.",
        "real_life_usage": ["Train stations (駅)", "Station attendant (駅員)"],
        "vocab": [
            {"word": "駅", "kana": "えき", "romaji": "eki", "english": "Station", "sentence_jp": "駅で友達に会います。", "sentence_kana": "えきでともだちにあいます。", "sentence_romaji": "Eki de tomodachi ni aimasu.", "sentence_eng": "I will meet my friend at the station."},
            {"word": "駅前", "kana": "えきまえ", "romaji": "ekimae", "english": "In front of the station", "sentence_jp": "駅前で買い物をします。", "sentence_kana": "えきまえでかいものをします。", "sentence_romaji": "Ekimae de kaimono o shimasu.", "sentence_eng": "I shop in front of the station."},
            {"word": "駅員", "kana": "えきいん", "romaji": "ekiin", "english": "Station attendant", "sentence_jp": "駅員に聞きます。", "sentence_kana": "えきいんにききます。", "sentence_romaji": "Ekiin ni kikimasu.", "sentence_eng": "I will ask the station attendant."}
        ]
    }
]
