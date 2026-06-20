import os
from data_centers import PARTICLES

# --- CONTENT DEFINITIONS ---

# 1. Grammar Master Guide
grammar_sections = [
    {
        "title": "State & Being (状態・存在)",
        "patterns": [
            {
                "pattern": "〜です / 〜ではありません",
                "meaning": "To be / Not to be (Present)",
                "structure": "[Noun/Na-Adj] です<br>[Noun/Na-Adj] ではありません",
                "ex": [("私は学生です。", "I am a student."), ("彼は先生ではありません。", "He is not a teacher.")],
                "notes": "ではありません is formal. じゃありません is used in daily speaking."
            },
            {
                "pattern": "〜でした / 〜ではありませんでした",
                "meaning": "Was / Was not (Past)",
                "structure": "[Noun/Na-Adj] でした<br>[Noun/Na-Adj] ではありませんでした",
                "ex": [("きのうは雨でした。", "It was raining yesterday."), ("テストは簡単ではありませんでした。", "The test was not easy.")],
                "notes": "Past tense of the copula. Watch out for I-adjectives which conjugate differently (〜かったです)."
            },
            {
                "pattern": "〜があります / 〜います",
                "meaning": "There is / To have (Existence)",
                "structure": "[Place] に [Thing] があります<br>[Place] に [Person/Animal] がいます",
                "ex": [("机の上に本があります。", "There is a book on the desk."), ("あそこに犬がいます。", "There is a dog over there.")],
                "notes": "あります is for inanimate objects. います is for living, moving things."
            }
        ]
    },
    {
        "title": "Movement & Requests (移動・依頼)",
        "patterns": [
            {
                "pattern": "〜へ行きます / 〜に行きます",
                "meaning": "Go to ~",
                "structure": "[Place] へ/に 行きます / 来ます / 帰ります",
                "ex": [("明日、東京へ行きます。", "I will go to Tokyo tomorrow."), ("うちへ帰ります。", "I will return home.")],
                "notes": "へ emphasizes direction, に emphasizes destination. Both are mostly interchangeable for N5."
            },
            {
                "pattern": "〜をください",
                "meaning": "Please give me ~",
                "structure": "[Noun] をください",
                "ex": [("水をください。", "Please give me water."), ("りんごを３つください。", "Please give me three apples.")],
                "notes": "Used when ordering at restaurants or asking for items in a store."
            },
            {
                "pattern": "〜てください",
                "meaning": "Please do ~",
                "structure": "[Verb て-form] ください",
                "ex": [("ちょっと待ってください。", "Please wait a moment."), ("ここに名前を書いてください。", "Please write your name here.")],
                "notes": "Standard polite request. Requires mastering the Verb て-form."
            }
        ]
    },
    {
        "title": "Suggestions & Permissions (提案・許可)",
        "patterns": [
            {
                "pattern": "〜ましょう / 〜ませんか",
                "meaning": "Let's ~ / Won't we ~?",
                "structure": "[Verb stem] ましょう<br>[Verb stem] ませんか",
                "ex": [("一緒に昼ご飯を食べましょう。", "Let's eat lunch together."), ("コーヒーを飲みませんか。", "Won't you drink some coffee?")],
                "notes": "ませんか is softer and more polite as it gives the listener room to refuse."
            },
            {
                "pattern": "〜てもいいです",
                "meaning": "May I ~ / It is okay to ~",
                "structure": "[Verb て-form] もいいです",
                "ex": [("ここで写真を撮ってもいいですか。", "May I take a picture here?"), ("このペンを使ってもいいです。", "You may use this pen.")],
                "notes": "Often used as a question to ask for permission."
            },
            {
                "pattern": "〜てはいけません",
                "meaning": "You must not ~",
                "structure": "[Verb て-form] はいけません",
                "ex": [("ここでタバコを吸ってはいけません。", "You must not smoke here."), ("病院で電話をしてはいけません。", "You must not talk on the phone in the hospital.")],
                "notes": "Strong prohibition. Often seen on signs or rules."
            }
        ]
    },
    {
        "title": "Obligation & State (義務・状態)",
        "patterns": [
            {
                "pattern": "〜なければなりません",
                "meaning": "Must do ~ / Have to ~",
                "structure": "[Verb ない-form, drop い] ければなりません",
                "ex": [("明日、早く起きなければなりません。", "I must wake up early tomorrow."), ("薬を飲まなければなりません。", "I must take medicine.")],
                "notes": "Double negative construction literally meaning 'if you don't do, it's not okay'."
            },
            {
                "pattern": "〜なくてもいいです",
                "meaning": "Don't have to ~",
                "structure": "[Verb ない-form, drop い] くてもいいです",
                "ex": [("明日は学校へ行かなくてもいいです。", "I don't have to go to school tomorrow.")],
                "notes": "The exact opposite of なければなりません."
            },
            {
                "pattern": "〜ています",
                "meaning": "Currently doing ~ / State of being",
                "structure": "[Verb て-form] います",
                "ex": [("今、本を読んでいます。", "I am reading a book right now."), ("私は結婚しています。", "I am married. (State)")],
                "notes": "Can mean an action in progress (I am eating) OR a continuous state (I live in Tokyo)."
            }
        ]
    },
    {
        "title": "Desire & Ability (願望・可能)",
        "patterns": [
            {
                "pattern": "〜たいです / 〜ほしいです",
                "meaning": "Want to do / Want a thing",
                "structure": "[Verb stem] たいです<br>[Noun] がほしいです",
                "ex": [("日本へ行きたいです。", "I want to go to Japan."), ("新しい車がほしいです。", "I want a new car.")],
                "notes": "たい attaches to verbs. ほしい acts like an adjective taking the object with が."
            },
            {
                "pattern": "〜ことができます",
                "meaning": "Can do ~ / Ability",
                "structure": "[Verb Dictionary Form] ことができます",
                "ex": [("私はピアノを弾くことができます。", "I can play the piano."), ("ここで切符を買うことができます。", "You can buy a ticket here.")],
                "notes": "Formal way to express potential/ability in N5."
            }
        ]
    },
    {
        "title": "Thoughts & Explanations (思考・説明)",
        "patterns": [
            {
                "pattern": "〜から / 〜ので",
                "meaning": "Because ~",
                "structure": "[Reason Phrase] から/ので、[Result]",
                "ex": [("雨が降っているから、行きません。", "Because it's raining, I won't go."), ("時間がないので、急いでください。", "Because there's no time, please hurry.")],
                "notes": "ので is slightly more formal and objective than から."
            },
            {
                "pattern": "〜と思います",
                "meaning": "I think that ~",
                "structure": "[Plain Form Verb/Adj] と思います",
                "ex": [("明日は晴れると思います。", "I think it will be sunny tomorrow."), ("この映画は面白いと思います。", "I think this movie is interesting.")],
                "notes": "Before と, you must use the plain/casual form (e.g., だ for nouns/na-adjectives)."
            },
            {
                "pattern": "〜んです",
                "meaning": "Explanatory tone / Seeking explanation",
                "structure": "[Plain Form] んです / のです",
                "ex": [("どうしたんですか。", "What happened? / What's wrong?"), ("頭が痛いんです。", "It's that my head hurts.")],
                "notes": "Used heavily in speech to explain a situation, reason, or ask for a reason."
            }
        ]
    },
    {
        "title": "Time Relations (時間関係)",
        "patterns": [
            {
                "pattern": "〜前に / 〜後で",
                "meaning": "Before ~ / After ~",
                "structure": "[Dict Verb/Nounの] 前に<br>[た-Form Verb/Nounの] 後で",
                "ex": [("寝る前に、本を読みます。", "Before sleeping, I read a book."), ("授業の後で、映画を見ます。", "After class, I will watch a movie.")],
                "notes": "前に takes dictionary form. 後で takes た(past) form."
            },
            {
                "pattern": "〜てから",
                "meaning": "After doing ~ (Sequential)",
                "structure": "[Verb て-form] から",
                "ex": [("手を洗ってから、ご飯を食べます。", "After washing hands, I eat dinner.")],
                "notes": "Indicates action B happens immediately or sequentially after action A."
            },
            {
                "pattern": "〜ながら",
                "meaning": "While doing ~",
                "structure": "[Verb stem] ながら",
                "ex": [("音楽を聞きながら、勉強します。", "I study while listening to music.")],
                "notes": "The main action is the second verb."
            }
        ]
    }
]

# 2. Daily Conversation Expressions
conversations = [
    {"jp": "ありがとうございます", "ro": "Arigatou gozaimasu", "en": "Thank you very much", "context": "Polite • Anytime"},
    {"jp": "どういたしまして", "ro": "Dou itashimashite", "en": "You're welcome", "context": "Polite • Reply to Thanks"},
    {"jp": "すみません", "ro": "Sumimasen", "en": "Excuse me / I'm sorry", "context": "Standard • Apology/Calling attention"},
    {"jp": "ごめんなさい", "ro": "Gomen nasai", "en": "I'm sorry", "context": "Casual/Standard • Apology"},
    {"jp": "失礼します", "ro": "Shitsurei shimasu", "en": "Excuse me (entering/leaving)", "context": "Formal • Office/Entering room"},
    {"jp": "よろしくお願いします", "ro": "Yoroshiku onegaishimasu", "en": "Please treat me well / Thanks in advance", "context": "Standard • Introductions/Requests"},
    {"jp": "いただきます", "ro": "Itadakimasu", "en": "Let's eat (I humbly receive)", "context": "Standard • Before meal"},
    {"jp": "ごちそうさまでした", "ro": "Gochisousama deshita", "en": "Thank you for the meal", "context": "Standard • After meal"},
    {"jp": "お疲れさまです", "ro": "Otsukaresama desu", "en": "Good work / Thanks for your hard work", "context": "Workplace • Greeting coworkers"},
    {"jp": "お先に失礼します", "ro": "Osakini shitsurei shimasu", "en": "Excuse me for leaving before you", "context": "Workplace • Leaving work early"},
    {"jp": "行ってきます", "ro": "Ittekimasu", "en": "I'm leaving (and coming back)", "context": "Home • Leaving house"},
    {"jp": "行ってらっしゃい", "ro": "Itterasshai", "en": "Please go and come back safely", "context": "Home • Reply to Ittekimasu"},
    {"jp": "ただいま", "ro": "Tadaima", "en": "I'm home", "context": "Home • Returning home"},
    {"jp": "おかえりなさい", "ro": "Okaerinasai", "en": "Welcome back", "context": "Home • Reply to Tadaima"},
    {"jp": "もしもし", "ro": "Moshi moshi", "en": "Hello? (on phone)", "context": "Phone • Answering"},
    {"jp": "いらっしゃいませ", "ro": "Irasshaimase", "en": "Welcome (to a store)", "context": "Retail • Staff greeting customer"},
    {"jp": "おめでとうございます", "ro": "Omedetou gozaimasu", "en": "Congratulations", "context": "Polite • Celebration"},
    {"jp": "お元気ですか", "ro": "Ogenki desu ka", "en": "How are you?", "context": "Standard • Greeting"},
    {"jp": "はい / いいえ", "ro": "Hai / Iie", "en": "Yes / No", "context": "Standard"},
    {"jp": "そうです / ちがいます", "ro": "Sou desu / Chigaimasu", "en": "That's right / That's wrong", "context": "Standard • Confirmation"},
    {"jp": "わかりました", "ro": "Wakarimashita", "en": "I understand", "context": "Standard • Acknowledgment"},
    {"jp": "大丈夫です", "ro": "Daijoubu desu", "en": "It's okay / I'm fine", "context": "Standard • Reassurance"}
]

# 3. Particles
particles = [
    {"p": "は", "ro": "wa", "meaning": "Topic Marker", "usage": "Marks the subject/topic. (Watashi wa...)", "ex": "私は学生です。"},
    {"p": "が", "ro": "ga", "meaning": "Subject Marker", "usage": "Marks new info, or object of desire/skill.", "ex": "犬が好きです。"},
    {"p": "を", "ro": "o", "meaning": "Object Marker", "usage": "Marks direct object of action verb.", "ex": "りんごを食べます。"},
    {"p": "に", "ro": "ni", "meaning": "Time / Destination", "usage": "Specific time, destination, or existence location.", "ex": "３時に行きます。 / 東京にいます。"},
    {"p": "へ", "ro": "e", "meaning": "Direction", "usage": "Direction of motion.", "ex": "学校へ行きます。"},
    {"p": "で", "ro": "de", "meaning": "Context / Means", "usage": "Location of action, or tool/method used.", "ex": "バスで行きます。 / レストランで食べます。"},
    {"p": "と", "ro": "to", "meaning": "And / With", "usage": "Exhaustive list of nouns, or accompanying person.", "ex": "肉と魚。 / 友達と行きます。"},
    {"p": "や", "ro": "ya", "meaning": "And (Partial)", "usage": "Incomplete list of nouns (A and B, among others).", "ex": "本やペンがあります。"},
    {"p": "も", "ro": "mo", "meaning": "Also / Too", "usage": "Replaces wa/ga/o to show similarity.", "ex": "私も学生です。"},
    {"p": "から", "ro": "kara", "meaning": "From", "usage": "Starting point in time/space.", "ex": "９時からです。"},
    {"p": "まで", "ro": "made", "meaning": "Until", "usage": "Ending point in time/space.", "ex": "５時までです。"},
    {"p": "ね", "ro": "ne", "meaning": "Agreement Tag", "usage": "Sentence ender seeking agreement (Right?).", "ex": "いい天気ですね。"},
    {"p": "よ", "ro": "yo", "meaning": "Assertion Tag", "usage": "Sentence ender providing new info.", "ex": "美味しいですよ！"}
]

# Use the full particle encyclopedia from data_centers.py for the slide table.
def build_particle_rows():
    rows = []
    for particle in PARTICLES:
        meanings = particle.get("meanings", [])
        usage_names = [meaning[0] for meaning in meanings]
        traps = particle.get("jlpt_traps") or particle.get("common_mistakes") or []
        usage = "Uses: " + ", ".join(usage_names[:4]) if usage_names else particle["core"]
        if traps:
            usage += f" | Trap: {traps[0]}"

        rows.append({
            "p": particle["particle"],
            "ro": particle["romaji"],
            "meaning": particle["core"],
            "usage": usage,
            "ex": meanings[0][1] if meanings else "",
        })
    return rows

particles = build_particle_rows()

# Generate New HTML Blocks
html = ""

# Helper to generate practice block
def generate_practice(title, questions):
    res = f'<div class="practice-section"><h3 class="practice-title"><i data-lucide="check-circle"></i> {title}</h3>'
    for q in questions:
        res += f'<div class="practice-question"><div class="pq-text">{q["text"]}</div><div class="practice-options">'
        for opt in q["options"]:
            correct_attr = ' data-correct' if opt["correct"] else ''
            res += f'<button class="practice-option"{correct_attr}>{opt["label"]}</button>'
        res += f'</div><div class="practice-explanation"><strong>Answer: {q["ans_text"]}</strong><br>{q["exp"]}</div></div>'
    res += '</div>'
    return res

# Start appending from slide 14
slide_index = 14

html += f"""
    <!-- SLIDE 14: GRAMMAR START -->
"""
# Add Grammar Sections dynamically
for idx, section in enumerate(grammar_sections):
    html += f"""
    <section class="slide" id="slide-{slide_index}" data-slide-index="{slide_index}">
      <div class="slide-header">
        <div class="slide-badge">Grammar Guide {idx+1}</div>
        <h2>{section['title']}</h2>
      </div>
      <div class="slide-body">
        <div class="grammar-grid">
"""
    for g in section['patterns']:
        html += f"""
          <div class="grammar-card">
            <div class="grammar-header">
              <div class="grammar-pattern">{g['pattern']}</div>
              <div class="grammar-meaning">{g['meaning']}</div>
            </div>
            <div class="grammar-structure">{g['structure']}</div>
            <div class="grammar-examples">
"""
        for ex_jp, ex_en in g['ex']:
            html += f'<div class="grammar-example"><div class="grammar-ex-jp">{ex_jp}</div><div class="grammar-ex-en">{ex_en}</div></div>'
        html += f"""
            </div>
            <div class="grammar-notes">💡 {g['notes']}</div>
          </div>
"""
    html += """
        </div>
      </div>
    </section>
"""
    slide_index += 1

# Grammar Practice Slide
html += f"""
    <section class="slide" id="slide-{slide_index}" data-slide-index="{slide_index}">
      <div class="slide-header">
        <div class="slide-badge">Practice</div>
        <h2>Grammar Practice Questions</h2>
      </div>
      <div class="slide-body">
"""
grammar_qs = [
    {"text": "１．あした、えいがを＿＿＿＿か。", "options": [{"label": "A. みます", "correct": True}, {"label": "B. みました", "correct": False}, {"label": "C. みて", "correct": False}], "ans_text": "A. みます", "exp": "Tomorrow (あした) indicates future tense."},
    {"text": "２．ここは びょういんです。タバコを ＿＿＿＿はいけません。", "options": [{"label": "A. すいます", "correct": False}, {"label": "B. すう", "correct": False}, {"label": "C. すって", "correct": True}], "ans_text": "C. すって", "exp": "〜てはいけません (must not) requires the Te-form."},
    {"text": "３．にく＿＿＿さかな＿＿＿どちらが好きですか。", "options": [{"label": "A. と / と", "correct": True}, {"label": "B. や / や", "correct": False}, {"label": "C. に / に", "correct": False}], "ans_text": "A. と / と", "exp": "The pattern is Aと Bと どちらが〜 (Which is more... A or B?)."}
]
html += generate_practice("JLPT N5 Style Grammar Quiz", grammar_qs)
html += """
      </div>
    </section>
"""
slide_index += 1

# Conversations Slide
html += f"""
    <section class="slide" id="slide-{slide_index}" data-slide-index="{slide_index}">
      <div class="slide-header">
        <div class="slide-badge">Expressions</div>
        <h2>Daily Conversation Expressions</h2>
      </div>
      <div class="slide-body">
        <div class="conv-grid">
"""
for c in conversations:
    html += f"""
          <div class="conv-card">
            <div class="conv-jp">{c['jp']}</div>
            <div class="conv-ro">{c['ro']}</div>
            <div class="conv-en">{c['en']}</div>
            <div class="conv-context">{c['context']}</div>
          </div>
"""
html += """
        </div>
      </div>
    </section>
"""
slide_index += 1

# Particles Slide
html += f"""
    <section class="slide" id="slide-{slide_index}" data-slide-index="{slide_index}">
      <div class="slide-header">
        <div class="slide-badge">Particles</div>
        <h2>Particles Master Table (助詞)</h2>
      </div>
      <div class="slide-body">
        <div class="table-container particle-table-container">
          <table class="vocab-table" id="table-particles">
            <thead>
              <tr>
                <th style="width: 10%">Particle</th>
                <th style="width: 25%">Core Meaning</th>
                <th style="width: 35%">Usage Note</th>
                <th style="width: 30%">Example</th>
              </tr>
            </thead>
            <tbody>
"""
for p in particles:
    html += f"""
              <tr class="vocab-row">
                <td class="jp-col" style="font-size: 1.5rem;">{p['p']}</td>
                <td class="meaning-col">{p['meaning']}</td>
                <td class="mnemonic-col">{p['usage']}</td>
                <td class="example-col">{p['ex']}</td>
              </tr>
"""
html += """
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
slide_index += 1

# Exam Traps Expanded
html += f"""
    <section class="slide" id="slide-{slide_index}" data-slide-index="{slide_index}">
      <div class="slide-header">
        <div class="slide-badge">Warning</div>
        <h2>Major Exam Traps (試験の罠)</h2>
      </div>
      <div class="slide-body">
        <div class="traps-grid">
          <div class="trap-card">
            <div class="trap-card-header"><h4>は (wa) vs が (ga)</h4></div>
            <div class="trap-comparison">
              <div class="comp-col"><span class="word-highlight">は</span><p class="desc">Topic marker. Used for known information.</p><p class="ex">私が学生です。(As for me, I am a student)</p></div>
              <div class="comp-col border-left"><span class="word-highlight">が</span><p class="desc">Subject marker. Used for new info, or with desires/skills (好き, ほしい).</p><p class="ex">犬が好きです。(I like dogs)</p></div>
            </div>
          </div>
          <div class="trap-card">
            <div class="trap-card-header"><h4>に (ni) vs で (de)</h4></div>
            <div class="trap-comparison">
              <div class="comp-col"><span class="word-highlight">に</span><p class="desc">Location of EXISTENCE (います/あります).</p><p class="ex">部屋に犬がいます。(Dog is in the room)</p></div>
              <div class="comp-col border-left"><span class="word-highlight">で</span><p class="desc">Location of ACTION (食べる/飲む).</p><p class="ex">部屋で食べます。(Eat in the room)</p></div>
            </div>
          </div>
          <div class="trap-card">
            <div class="trap-card-header"><h4>だけ (dake) vs しか (shika)</h4></div>
            <div class="trap-comparison">
              <div class="comp-col"><span class="word-highlight">だけ</span><p class="desc">Only. Takes positive verbs.</p><p class="ex">百円だけあります。</p></div>
              <div class="comp-col border-left"><span class="word-highlight">しか</span><p class="desc">Only. MUST take negative verbs.</p><p class="ex">百円しかありません。</p></div>
            </div>
          </div>
          <div class="trap-card">
            <div class="trap-card-header"><h4>あります (arimasu) vs います (imasu)</h4></div>
            <div class="trap-comparison">
              <div class="comp-col"><span class="word-highlight">あります</span><p class="desc">For non-living / immovable things (trees, books).</p></div>
              <div class="comp-col border-left"><span class="word-highlight">います</span><p class="desc">For living / moving things (people, animals).</p></div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
slide_index += 1

# Last Day Revision Sheet
html += f"""
    <section class="slide" id="slide-{slide_index}" data-slide-index="{slide_index}">
      <div class="slide-header">
        <div class="slide-badge">Final Review</div>
        <h2>Last Day Before Exam Revision</h2>
      </div>
      <div class="slide-body" style="font-size: 0.9rem;">
        <p class="slide-desc">Memorize this sheet in the 30 minutes before entering the exam room!</p>
        <div style="column-count: 2; column-gap: 2rem; background: var(--bg-table-header); padding: 1.5rem; border-radius: 8px;">
          <h4 style="color: var(--primary); margin-bottom: 0.5rem; border-bottom: 1px solid var(--border-color);">CRITICAL GRAMMAR</h4>
          <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; color: var(--text-main);">
            <li style="margin-bottom: 0.3rem;"><strong>〜てください</strong> : Please do</li>
            <li style="margin-bottom: 0.3rem;"><strong>〜てもいいです</strong> : May I do?</li>
            <li style="margin-bottom: 0.3rem;"><strong>〜てはいけません</strong> : Must not do</li>
            <li style="margin-bottom: 0.3rem;"><strong>〜なければなりません</strong> : Must do</li>
            <li style="margin-bottom: 0.3rem;"><strong>〜たことがあります</strong> : Have experienced</li>
            <li style="margin-bottom: 0.3rem;"><strong>〜たり〜たりします</strong> : Do things like A and B</li>
          </ul>

          <h4 style="color: var(--primary); margin-bottom: 0.5rem; border-bottom: 1px solid var(--border-color);">TRAP PARTICLES</h4>
          <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; color: var(--text-main);">
            <li style="margin-bottom: 0.3rem;"><strong>[Action Place] で</strong> : (公園で走る)</li>
            <li style="margin-bottom: 0.3rem;"><strong>[Existence Place] に</strong> : (公園にいる)</li>
            <li style="margin-bottom: 0.3rem;"><strong>しか ＋ Negative</strong> : Only</li>
          </ul>

          <h4 style="color: var(--primary); margin-bottom: 0.5rem; border-bottom: 1px solid var(--border-color);">ADVERBS</h4>
          <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem; color: var(--text-main);">
            <li style="margin-bottom: 0.3rem;"><strong>まだ ＋ Negative</strong> : Not yet</li>
            <li style="margin-bottom: 0.3rem;"><strong>もう ＋ Past</strong> : Already</li>
            <li style="margin-bottom: 0.3rem;"><strong>あまり ＋ Negative</strong> : Not very</li>
            <li style="margin-bottom: 0.3rem;"><strong>ぜんぜん ＋ Negative</strong> : Not at all</li>
          </ul>
        </div>
      </div>
    </section>
"""

# Read existing index.html
with open("index.html", "r", encoding="utf-8") as f:
    original_content = f.read()

# Find the closing </main> tag and insert new slides right before it
if "</main>" in original_content:
    new_content = original_content.replace("</main>", html + "\n  </main>")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Successfully appended {slide_index - 14 + 1} new slides to index.html")
else:
    print("Error: Could not find </main> in index.html")
