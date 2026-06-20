"""
Minna no Nihongo I — Complete Japanese Learning Ecosystem
Generates a comprehensive digital learning platform covering N5 from first principles.
"""

import os
import json
import html as html_lib
from data_centers import VERB_CENTER, PARTICLES, ADJECTIVES, EXPRESSIONS
from data_lessons_1_5 import LESSONS_1_5
from data_lessons_6_10 import LESSONS_6_10
from data_lessons_11_15 import LESSONS_11_15
from data_lessons_16_20 import LESSONS_16_20
from data_lessons_21_25 import LESSONS_21_25
from data_kanji import KANJI_DATA
from data_n5_grammar_encyclopedia import N5_GRAMMAR_ENCYCLOPEDIA, REVISION_MODE_LISTS
from data_test import N5_TESTS

# The full list of lessons will be assembled here as we expand the database
ALL_LESSONS = LESSONS_1_5[:5] + LESSONS_6_10[:5] + LESSONS_11_15[:5] + LESSONS_16_20[:5] + LESSONS_21_25[:5]

COUNTER_SECTIONS = [
    {
        "title": "People Counter Center",
        "counter": "人",
        "used_for": "People",
        "core_note": "人 counts people. The first two forms are old native Japanese readings and must be memorized separately.",
        "forms": [
            ("1", "ひとり", "1 person", "Major exception"),
            ("2", "ふたり", "2 people", "Major exception"),
            ("3", "さんにん", "3 people", ""),
            ("4", "よにん", "4 people", "よ, not よん here"),
            ("5", "ごにん", "5 people", ""),
            ("6", "ろくにん", "6 people", ""),
            ("7", "しちにん / ななにん", "7 people", "Both appear; ななにん is common in speech"),
            ("8", "はちにん", "8 people", ""),
            ("9", "きゅうにん", "9 people", ""),
            ("10", "じゅうにん", "10 people", ""),
        ],
        "examples": ["教室に学生が三人います。", "家族は四人です。", "友達が二人来ました。"],
        "memory": "One and two people are special: ひとり and ふたり behave like set words, not simple number + にん.",
    },
    {
        "title": "Day Counter Center",
        "counter": "日",
        "used_for": "Calendar days and duration days",
        "core_note": "日 has many old Japanese readings. These are among the most tested N5 counter exceptions.",
        "forms": [
            ("1", "ついたち", "1st day of the month", "Calendar date only"),
            ("2", "ふつか", "2nd day / 2 days", "Irregular"),
            ("3", "みっか", "3rd day / 3 days", "Irregular"),
            ("4", "よっか", "4th day / 4 days", "Irregular"),
            ("5", "いつか", "5th day / 5 days", "Irregular"),
            ("6", "むいか", "6th day / 6 days", "Irregular"),
            ("7", "なのか", "7th day / 7 days", "Irregular"),
            ("8", "ようか", "8th day / 8 days", "Irregular"),
            ("9", "ここのか", "9th day / 9 days", "Irregular"),
            ("10", "とおか", "10th day / 10 days", "Irregular"),
            ("14", "じゅうよっか", "14th day / 14 days", "4-day exception repeats"),
            ("20", "はつか", "20th day / 20 days", "Major exception"),
            ("24", "にじゅうよっか", "24th day / 24 days", "4-day exception repeats"),
        ],
        "examples": ["今日は四月一日です。", "日本に三日いました。", "二十日に試験があります。"],
        "memory": "Days 1-10 are their own family. 14 and 24 reuse よっか. 20 is the special giant: はつか.",
    },
    {
        "title": "Minutes Counter Center",
        "counter": "分",
        "used_for": "Minutes",
        "core_note": "分 alternates between ふん and ぷん. Small っ before ぷん appears after 1, 6, 8, and 10.",
        "forms": [("1", "いっぷん", "1 minute", "Sound change"), ("2", "にふん", "2 minutes", ""), ("3", "さんぷん", "3 minutes", "ぷん"), ("4", "よんぷん", "4 minutes", "ぷん"), ("5", "ごふん", "5 minutes", ""), ("6", "ろっぷん", "6 minutes", "Sound change"), ("7", "ななふん", "7 minutes", ""), ("8", "はっぷん", "8 minutes", "Sound change"), ("9", "きゅうふん", "9 minutes", ""), ("10", "じゅっぷん", "10 minutes", "Sound change")],
        "examples": ["五分待ってください。", "駅まで十分かかります。", "三分でできます。"],
        "memory": "For 分, the punchy forms are 1, 6, 8, 10: いっぷん, ろっぷん, はっぷん, じゅっぷん.",
    },
    {
        "title": "Long Objects Counter",
        "counter": "本",
        "used_for": "Long cylindrical objects: pencils, bottles, umbrellas, roads, phone calls",
        "core_note": "本 changes between ほん, ぼん, and ぽん depending on the number.",
        "forms": [("1", "いっぽん", "1 long object", "ぽん"), ("2", "にほん", "2 long objects", ""), ("3", "さんぼん", "3 long objects", "ぼん"), ("4", "よんほん", "4 long objects", ""), ("5", "ごほん", "5 long objects", ""), ("6", "ろっぽん", "6 long objects", "ぽん"), ("7", "ななほん", "7 long objects", ""), ("8", "はっぽん", "8 long objects", "ぽん"), ("9", "きゅうほん", "9 long objects", ""), ("10", "じゅっぽん", "10 long objects", "ぽん")],
        "examples": ["鉛筆が一本あります。", "水を三本買いました。", "傘を二本持っています。"],
        "memory": "本 is the classic sound-change counter: ぽん after 1, 6, 8, 10; ぼん after 3.",
    },
    {
        "title": "Small Animals Counter",
        "counter": "匹",
        "used_for": "Small animals: cats, dogs, fish, insects",
        "core_note": "匹 changes between ひき, びき, and ぴき.",
        "forms": [("1", "いっぴき", "1 small animal", "ぴき"), ("2", "にひき", "2 small animals", ""), ("3", "さんびき", "3 small animals", "びき"), ("4", "よんひき", "4 small animals", ""), ("5", "ごひき", "5 small animals", ""), ("6", "ろっぴき", "6 small animals", "ぴき"), ("7", "ななひき", "7 small animals", ""), ("8", "はっぴき", "8 small animals", "ぴき"), ("9", "きゅうひき", "9 small animals", ""), ("10", "じゅっぴき", "10 small animals", "ぴき")],
        "examples": ["猫が一匹います。", "犬を二匹飼っています。", "魚を三匹見ました。"],
        "memory": "匹 mirrors 本: ぴき after 1, 6, 8, 10; びき after 3.",
    },
    {
        "title": "Books Counter",
        "counter": "冊",
        "used_for": "Bound volumes: books, notebooks, magazines",
        "core_note": "冊 is comparatively regular, but 1, 8, and 10 use small っ.",
        "forms": [("1", "いっさつ", "1 book", "Sound change"), ("2", "にさつ", "2 books", ""), ("3", "さんさつ", "3 books", ""), ("4", "よんさつ", "4 books", ""), ("5", "ごさつ", "5 books", ""), ("6", "ろくさつ", "6 books", ""), ("7", "ななさつ", "7 books", ""), ("8", "はっさつ", "8 books", "Sound change"), ("9", "きゅうさつ", "9 books", ""), ("10", "じゅっさつ", "10 books", "Sound change")],
        "examples": ["本を一冊読みました。", "ノートを三冊買いました。"],
        "memory": "冊 keeps さつ, but clipped numbers become いっさつ, はっさつ, じゅっさつ.",
    },
    {
        "title": "Flat Objects Counter",
        "counter": "枚",
        "used_for": "Flat thin objects: paper, tickets, photos, shirts, plates",
        "core_note": "枚 is regular and friendly. Use it for flat things you can stack.",
        "forms": [("1", "いちまい", "1 flat object", ""), ("2", "にまい", "2 flat objects", ""), ("3", "さんまい", "3 flat objects", ""), ("4", "よんまい", "4 flat objects", ""), ("5", "ごまい", "5 flat objects", ""), ("6", "ろくまい", "6 flat objects", ""), ("7", "ななまい", "7 flat objects", ""), ("8", "はちまい", "8 flat objects", ""), ("9", "きゅうまい", "9 flat objects", ""), ("10", "じゅうまい", "10 flat objects", "")],
        "examples": ["紙を一枚ください。", "切符を二枚買いました。", "写真を三枚撮りました。"],
        "memory": "Flat and thin usually means 枚.",
    },
    {
        "title": "Machines & Vehicles",
        "counter": "台",
        "used_for": "Machines and vehicles: cars, computers, TVs, bicycles",
        "core_note": "台 is regular and counts machines or large equipment.",
        "forms": [("1", "いちだい", "1 machine/vehicle", ""), ("2", "にだい", "2 machines/vehicles", ""), ("3", "さんだい", "3 machines/vehicles", ""), ("4", "よんだい", "4 machines/vehicles", ""), ("5", "ごだい", "5 machines/vehicles", ""), ("6", "ろくだい", "6 machines/vehicles", ""), ("7", "ななだい", "7 machines/vehicles", ""), ("8", "はちだい", "8 machines/vehicles", ""), ("9", "きゅうだい", "9 machines/vehicles", ""), ("10", "じゅうだい", "10 machines/vehicles", "")],
        "examples": ["車が一台あります。", "コンピューターを二台使います。", "テレビが三台あります。"],
        "memory": "If it is a machine, vehicle, or device, think 台.",
    },
    {
        "title": "Floors",
        "counter": "階",
        "used_for": "Building floors",
        "core_note": "階 is usually かい, but 3 can be さんがい. Watch 1, 6, 8, 10.",
        "forms": [("1", "いっかい", "1st floor", "Sound change"), ("2", "にかい", "2nd floor", ""), ("3", "さんがい / さんかい", "3rd floor", "がい is common"), ("4", "よんかい", "4th floor", ""), ("5", "ごかい", "5th floor", ""), ("6", "ろっかい", "6th floor", "Sound change"), ("7", "ななかい", "7th floor", ""), ("8", "はっかい", "8th floor", "Sound change"), ("9", "きゅうかい", "9th floor", ""), ("10", "じゅっかい", "10th floor", "Sound change")],
        "examples": ["教室は三階です。", "トイレは一階にあります。"],
        "memory": "階 behaves like many k-sound counters: いっかい, ろっかい, はっかい, じゅっかい.",
    },
    {
        "title": "Age Counter",
        "counter": "歳",
        "used_for": "Age",
        "core_note": "歳 counts years old. Twenty years old is the major exception はたち.",
        "forms": [("1", "いっさい", "1 year old", "Sound change"), ("2", "にさい", "2 years old", ""), ("3", "さんさい", "3 years old", ""), ("4", "よんさい", "4 years old", ""), ("5", "ごさい", "5 years old", ""), ("6", "ろくさい", "6 years old", ""), ("7", "ななさい", "7 years old", ""), ("8", "はっさい", "8 years old", "Sound change"), ("9", "きゅうさい", "9 years old", ""), ("10", "じゅっさい", "10 years old", "Sound change"), ("20", "はたち", "20 years old", "Major exception")],
        "examples": ["妹は八歳です。", "私は二十歳です。", "お子さんは何歳ですか。"],
        "memory": "For JLPT N5, never miss はたち.",
    },
    {
        "title": "Months Counter",
        "counter": "か月",
        "used_for": "Duration in months",
        "core_note": "か月 counts how many months. 1, 6, 8, and 10 use っかげつ.",
        "forms": [("1", "いっかげつ", "1 month", "Sound change"), ("2", "にかげつ", "2 months", ""), ("3", "さんかげつ", "3 months", ""), ("4", "よんかげつ", "4 months", ""), ("5", "ごかげつ", "5 months", ""), ("6", "ろっかげつ", "6 months", "Sound change"), ("7", "ななかげつ", "7 months", ""), ("8", "はっかげつ", "8 months", "Sound change"), ("9", "きゅうかげつ", "9 months", ""), ("10", "じゅっかげつ", "10 months", "Sound change")],
        "examples": ["三か月日本語を勉強しました。", "一か月休みます。"],
        "memory": "か月 follows the k-sound pattern: いっか, ろっか, はっか, じゅっか.",
    },
]

TIME_COUNTERS = [
    ("時間", "Hours / duration in hours", "一時間, 二時間, 三時間", "Mostly regular. Use for duration, not clock time."),
    ("週間", "Weeks", "一週間, 二週間, 三週間", "Often used with に for frequency: 一週間に二回."),
    ("年", "Years", "一年, 二年, 三年", "For duration or school year. Calendar years use different reading patterns."),
    ("回", "Times / occurrences", "一回, 二回, 三回", "Counts number of times an action happens."),
]

# ============================================================
#  HTML GENERATION ENGINE
# ============================================================

def generate_css():
    return """
    :root {
      --bg: #0F172A;
      --surface: #1E293B;
      --surface-raised: #334155;
      --text-1: #F8FAFC;
      --text-2: #E2E8F0;
      --text-3: #94A3B8;
      --text-4: #64748B;
      --accent: #3B82F6;
      --accent-light: #1E3A8A;
      --accent-text: #93C5FD;
      --border: #334155;
      --sidebar-w: 280px;
      --font-sans: 'Inter', -apple-system, sans-serif;
      --font-jp: 'Noto Sans JP', sans-serif;
    }
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: var(--font-sans); background: var(--bg); color: var(--text-2); line-height: 1.7; font-size: 15px; }
    a { color: var(--accent-text); text-decoration: none; }
    
    .layout { display: flex; min-height: 100vh; }
    
    .sidebar { width: var(--sidebar-w); background: var(--surface); border-right: 1px solid var(--border); position: fixed; height: 100vh; overflow-y: auto; padding: 20px 0 60px 0; }
    .sidebar-title { font-weight: 800; font-size: 16px; color: var(--text-1); padding: 0 20px 20px; border-bottom: 1px solid var(--border); margin-bottom: 10px; }
    .sidebar-footer { position: fixed; bottom: 0; left: 0; width: var(--sidebar-w); padding: 16px 20px; font-size: 12px; color: var(--text-4); border-top: 1px solid var(--border); background: var(--surface); z-index: 10; text-align: center; }
    .nav-group-toggle { width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 8px; background: transparent; border: 0; cursor: pointer; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-4); padding: 10px 20px 6px; font-weight: 700; text-align: left; }
    .nav-group-toggle:hover { background: var(--surface-raised); color: var(--text-1); }
    .nav-group-chevron { font-size: 12px; transition: transform 0.2s; }
    .nav-group-toggle[aria-expanded="false"] .nav-group-chevron { transform: rotate(-90deg); }
    .nav-group-links.collapsed { display: none; }
    .nav-link { display: block; padding: 6px 20px; font-size: 14px; color: var(--text-2); border-left: 3px solid transparent; transition: background 0.2s, color 0.2s, border-color 0.2s; }
    #nav-learning-centers .nav-link { color: var(--accent-text); font-weight: 700; }
    .nav-link:hover { background: var(--surface-raised); color: var(--text-1); }
    .nav-link.active { background: linear-gradient(90deg, rgba(59, 130, 246, 0.35), rgba(59, 130, 246, 0.12)); color: var(--text-1) !important; border-left-color: var(--accent); font-weight: 800; box-shadow: inset 0 0 0 1px rgba(147, 197, 253, 0.18); }
    
    .main-content { margin-left: var(--sidebar-w); flex: 1; padding: 40px 60px; max-width: 1000px; }
    .main-content > section {
      content-visibility: auto;
      contain-intrinsic-size: 1200px;
    }
    .card,
    .grammar-block,
    .kc-card,
    .kanji-card,
    .quiz-box,
    .encyclopedia-category {
      content-visibility: auto;
      contain-intrinsic-size: 320px;
    }
    
    h1 { font-size: 36px; color: var(--text-1); margin-bottom: 10px; letter-spacing: -0.02em; }
    h2 { font-size: 24px; color: var(--text-1); margin: 40px 0 20px; border-bottom: 1px solid var(--border); padding-bottom: 10px; }
    h3 { font-size: 18px; color: var(--text-1); margin: 24px 0 12px; }
    p { margin-bottom: 16px; }
    
    .card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 24px; margin-bottom: 24px; }
    .card-title { font-family: var(--font-jp); font-size: 20px; font-weight: 700; color: var(--text-1); margin-bottom: 8px; }
    
    .grammar-block { background: var(--surface-raised); border-left: 4px solid var(--accent); padding: 20px; border-radius: 0 8px 8px 0; margin-bottom: 20px; }
    .g-row { display: flex; margin-bottom: 8px; }
    .g-label { width: 120px; font-weight: 700; color: var(--accent-text); font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; flex-shrink: 0; }
    .g-content { flex: 1; color: var(--text-2); }
    
    .table-wrapper { overflow-x: auto; margin-bottom: 24px; border: 1px solid var(--border); border-radius: 8px; }
    table { width: 100%; border-collapse: collapse; text-align: left; background: var(--surface); }
    th { background: var(--surface-raised); padding: 12px 16px; font-size: 12px; text-transform: uppercase; color: var(--text-4); border-bottom: 1px solid var(--border); }
    td { padding: 12px 16px; border-bottom: 1px solid var(--border); font-size: 14px; }
    tr:last-child td { border-bottom: none; }
    .jp { font-family: var(--font-jp); font-size: 16px; color: var(--text-1); }
    
    .kanji-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; margin-bottom: 32px; }
    .kanji-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 20px; text-align: center; }
    .k-char { font-family: var(--font-jp); font-size: 48px; font-weight: 700; color: var(--text-1); margin-bottom: 10px; }
    .k-meta { font-size: 12px; color: var(--text-4); margin-bottom: 10px; }
    .k-tip { font-size: 13px; color: var(--accent-text); background: var(--accent-light); padding: 8px; border-radius: 4px; margin-bottom: 10px; }
    
    .alert { padding: 16px; border-radius: 8px; margin-bottom: 16px; font-size: 14px; }
    .alert-danger { background: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; color: #fca5a5; }
    .alert-warning { background: rgba(245, 158, 11, 0.1); border-left: 4px solid #f59e0b; color: #fcd34d; }
    .alert-info { background: rgba(59, 130, 246, 0.1); border-left: 4px solid #3b82f6; color: #93c5fd; }
    
    .quiz-box { border: 1px solid var(--border); border-radius: 8px; padding: 20px; margin-bottom: 16px; }
    .quiz-q { font-weight: 600; color: var(--text-1); margin-bottom: 12px; font-family: var(--font-jp); font-size: 16px; }
    .quiz-opts button { display: block; width: 100%; text-align: left; padding: 10px 16px; background: var(--surface-raised); border: 1px solid var(--border); border-radius: 4px; margin-bottom: 8px; color: var(--text-2); cursor: pointer; transition: 0.2s; font-family: var(--font-jp); font-size: 14px; }
    .quiz-opts button:hover { background: var(--border); }
    .quiz-exp { display: none; margin-top: 12px; padding: 12px; background: var(--surface); border-radius: 4px; font-size: 14px; border-left: 3px solid var(--accent); }
    .quiz-box.answered .quiz-exp { display: block; }
    .quiz-opts button.correct { background: rgba(16, 185, 129, 0.2); border-color: #10b981; color: #34d399; }
    .quiz-opts button.wrong { background: rgba(239, 68, 68, 0.2); border-color: #ef4444; color: #fca5a5; }
    
    .search-bar { width: 100%; padding: 12px 16px; font-size: 16px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface); color: var(--text-1); margin-bottom: 24px; }
    .search-bar:focus { outline: none; border-color: var(--accent); }
    
    .kc-card { display: flex; flex-direction: column; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; margin-bottom: 32px; overflow: hidden; }
    .kc-header { display: flex; background: var(--surface-raised); padding: 24px; border-bottom: 1px solid var(--border); }
    .kc-char-box { width: 120px; height: 120px; display: flex; align-items: center; justify-content: center; background: var(--bg); border: 1px solid var(--border); border-radius: 8px; margin-right: 24px; font-family: var(--font-jp); font-size: 80px; color: var(--text-1); line-height: 1; }
    .kc-info { flex: 1; }
    .kc-meaning { font-size: 28px; font-weight: 700; color: var(--text-1); margin-bottom: 8px; }
    .kc-meta-badges { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
    .kc-badge { padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; background: var(--bg); border: 1px solid var(--border); }
    .kc-badge.jlpt { background: var(--accent-light); color: var(--accent-text); border: none; }
    .kc-readings { display: grid; grid-template-columns: 80px 1fr; gap: 8px; font-size: 14px; margin-bottom: 12px; }
    .kc-r-label { color: var(--text-4); font-weight: 700; text-transform: uppercase; font-size: 11px; }
    .kc-r-val { color: var(--text-1); font-family: var(--font-jp); }
    
    .kc-body { padding: 24px; }
    .kc-memory { background: rgba(59, 130, 246, 0.1); border-left: 4px solid var(--accent); padding: 16px; border-radius: 4px; margin-bottom: 24px; font-size: 14px; }
    .kc-vocab-table { width: 100%; border-collapse: collapse; }
    .kc-vocab-table th, .kc-vocab-table td { padding: 12px; border-bottom: 1px solid var(--border); text-align: left; vertical-align: top; }
    .kc-vocab-table th { font-size: 11px; color: var(--text-4); text-transform: uppercase; border-bottom: 2px solid var(--border); }
    .kc-vocab-table td { font-size: 14px; }
    .kc-v-word { font-family: var(--font-jp); font-size: 18px; font-weight: 700; color: var(--text-1); }
    .kc-v-kana { font-size: 12px; color: var(--text-3); }
    .kc-v-romaji { font-size: 11px; color: var(--text-4); font-family: monospace; }
    .kc-s-jp { font-family: var(--font-jp); font-size: 15px; color: var(--text-2); margin-bottom: 4px; }
    .kc-s-eng { font-size: 13px; color: var(--text-4); }

        .hidden { display: none !important; }

        .grammar-search-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 12px;
            margin-bottom: 16px;
        }
        .grammar-search-grid input,
        .grammar-search-grid select {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid var(--border);
            border-radius: 8px;
            background: var(--surface);
            color: var(--text-1);
            font-size: 14px;
        }
        .grammar-search-grid label {
            display: block;
            margin-bottom: 6px;
            font-size: 12px;
            color: var(--text-3);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 700;
        }
        .grammar-filter-actions {
            display: flex;
            flex-direction: column;
            gap: 10px;
            align-items: stretch;
            flex-wrap: wrap;
        }
        .grammar-filter-btn {
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 10px 14px;
            background: var(--accent);
            color: var(--text-1);
            font-weight: 700;
            cursor: pointer;
        }
        .grammar-filter-btn.secondary {
            background: var(--surface-raised);
            color: var(--text-2);
        }
        .grammar-filter-btn:hover {
            filter: brightness(1.08);
        }
        .grammar-summary {
            background: var(--surface-raised);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 10px 12px;
            color: var(--accent-text);
            font-size: 13px;
            align-self: end;
        }

        .relationship-map {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
            margin-bottom: 12px;
        }
        .map-node {
            background: var(--surface-raised);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 13px;
            color: var(--text-2);
            white-space: nowrap;
        }
        .map-arrow { color: var(--accent-text); font-weight: 700; }

        .te-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }
        .te-box {
            background: var(--surface-raised);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 14px;
        }
        .te-box ul { margin-left: 18px; }
        .te-box li { margin-bottom: 6px; }

        .revision-tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 12px;
        }
        .revision-tab {
            border: 1px solid var(--border);
            background: var(--surface-raised);
            color: var(--text-2);
            padding: 8px 12px;
            border-radius: 999px;
            font-size: 13px;
            cursor: pointer;
        }
        .revision-tab.active {
            border-color: var(--accent);
            background: var(--accent-light);
            color: var(--accent-text);
        }
        .revision-list {
            margin-left: 20px;
        }
        .revision-list li {
            margin-bottom: 6px;
        }

        .encyclopedia-category {
            margin-top: 26px;
            border-top: 1px dashed var(--border);
            padding-top: 18px;
        }
        .encyclopedia-meta {
            font-size: 13px;
            color: var(--text-3);
            margin-bottom: 12px;
        }
        .grammar-encyclopedia-card {
            background: var(--surface-raised);
            border: 1px solid var(--border);
            border-left: 4px solid var(--accent);
            border-radius: 8px;
            padding: 14px;
            margin-bottom: 14px;
        }
        .g-pattern {
            font-family: var(--font-jp);
            font-size: 20px;
            color: var(--text-1);
            margin-bottom: 6px;
            font-weight: 700;
        }
        .g-sub {
            color: var(--accent-text);
            font-size: 14px;
            margin-bottom: 10px;
            font-weight: 600;
        }
        .g-row-rich {
            display: grid;
            grid-template-columns: 160px 1fr;
            gap: 8px;
            margin-bottom: 8px;
        }
        .g-row-rich .label {
            color: var(--text-3);
            font-size: 12px;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        .g-row-rich .val {
            color: var(--text-2);
            font-size: 14px;
        }
        .example-table { margin-top: 8px; }
        .conversation-block {
            margin-top: 10px;
            padding: 10px;
            border: 1px dashed var(--border);
            border-radius: 8px;
            background: var(--surface);
        }
        #n5-grammar-encyclopedia {
            display: flex;
            flex-direction: column;
        }
        #grammar-search-card { order: 1; }
        #n5-grammar-encyclopedia .encyclopedia-category { order: 2; }
        .grammar-support-card { order: 3; }

        @media (max-width: 900px) {
            .te-grid { grid-template-columns: 1fr; }
            .g-row-rich { grid-template-columns: 1fr; }
            .main-content { padding: 28px 18px; }
            .sidebar { width: 230px; }
            .main-content { margin-left: 230px; }
        }
    
    @media print {
        .sidebar { display: none; }
        .main-content { margin: 0; padding: 20px; max-width: 100%; }
        .quiz-exp { display: block; }
        body { background: white; color: black; }
        .card, .grammar-block, table { border: 1px solid #ccc; background: white; }
        * { color: black !important; }
    }
    """

def generate_js():
    script = """
    document.addEventListener('DOMContentLoaded', () => {
        // Quiz Logic
        // Store scores for test sections
        const testScores = {};
        
        document.querySelectorAll('.quiz-box').forEach(box => {
            const btns = box.querySelectorAll('button');
            const scoreDisplayId = box.dataset.scoreDisplay;
            const testId = box.dataset.testId;
            const total = box.dataset.total;
            
            if (testId && !(testId in testScores)) {
                testScores[testId] = 0;
            }

            btns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    if (box.classList.contains('answered')) return;
                    
                    const isCorrect = btn.dataset.correct === 'true';
                    btn.classList.add(isCorrect ? 'correct' : 'wrong');
                    
                    if (isCorrect && testId) {
                        testScores[testId]++;
                        const display = document.getElementById(scoreDisplayId);
                        if (display) {
                            display.textContent = `${testScores[testId]} / ${total}`;
                        }
                    }
                    
                    if (!isCorrect) {
                        const correctBtn = box.querySelector('[data-correct="true"]');
                        if (correctBtn) correctBtn.classList.add('correct');
                    }
                    box.classList.add('answered');
                });
            });
        });

        // Kanji Search Logic
        const searchInput = document.getElementById('kanji-search');
        if(searchInput) {
            searchInput.addEventListener('input', (e) => {
                const term = e.target.value.toLowerCase().trim();
                document.querySelectorAll('.kc-card').forEach(card => {
                    const directText = (card.dataset.search || '').toLowerCase();
                    card.style.display = !term || directText.includes(term) ? 'flex' : 'none';
                });

                document.querySelectorAll('.kanji-category-group').forEach(group => {
                    const hasVisibleCard = Array.from(group.querySelectorAll('.kc-card'))
                        .some(card => card.style.display !== 'none');
                    group.classList.toggle('hidden', !hasVisibleCard);
                });
            });
        }

        // Grammar Encyclopedia Category Filter
        const categorySelect = document.getElementById('grammar-category-search');
        const grammarFilterBtn = document.getElementById('grammar-filter-btn');
        const grammarClearFilterBtn = document.getElementById('grammar-clear-filter-btn');
        const grammarSummary = document.getElementById('grammar-search-summary');
        const grammarCards = Array.from(document.querySelectorAll('.grammar-encyclopedia-card'));

        function runGrammarFilter() {
            if (!grammarCards.length) return;
            const categoryTerm = categorySelect ? categorySelect.value.toLowerCase().trim() : '';

            let visible = 0;
            grammarCards.forEach(card => {
                const category = (card.dataset.category || '').toLowerCase();
                const show = !categoryTerm || category === categoryTerm;
                const wrapper = card.closest('.encyclopedia-category') || card;
                wrapper.classList.toggle('hidden', !show);
                if (show) visible += 1;
            });

            if (grammarSummary) {
                grammarSummary.textContent = categoryTerm
                    ? `Showing ${visible} grammar point(s) in ${categorySelect.options[categorySelect.selectedIndex].text}.`
                    : `Showing all ${visible} grammar point(s).`;
            }
        }

        if (grammarFilterBtn) grammarFilterBtn.addEventListener('click', runGrammarFilter);
        if (grammarClearFilterBtn) {
            grammarClearFilterBtn.addEventListener('click', () => {
                if (categorySelect) categorySelect.value = '';
                runGrammarFilter();
            });
        }
        runGrammarFilter();

        // Revision Mode Tabs
        const revisionTabs = Array.from(document.querySelectorAll('.revision-tab'));
        const revisionList = document.getElementById('grammar-revision-list');
        const revisionLists = __REVISION_LISTS__;

        function renderRevisionList(mode) {
            if (!revisionList || !revisionLists[mode]) return;
            revisionList.innerHTML = revisionLists[mode]
                .map(item => `<li>${item}</li>`)
                .join('');
        }

        revisionTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                revisionTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                renderRevisionList(tab.dataset.mode);
            });
        });

        renderRevisionList('top25');

        // Collapsible Sidebar Groups
        document.querySelectorAll('.nav-group-toggle').forEach(toggle => {
            const group = document.getElementById(toggle.getAttribute('aria-controls'));
            if (!group) return;
            toggle.addEventListener('click', () => {
                const expanded = toggle.getAttribute('aria-expanded') === 'true';
                toggle.setAttribute('aria-expanded', String(!expanded));
                group.classList.toggle('collapsed', expanded);
            });
        });

        // Sidebar Scroll Spy
        const navLinks = Array.from(document.querySelectorAll('.sidebar .nav-link[href^="#"]'));
        const sectionLinks = navLinks
            .map(link => {
                const id = decodeURIComponent(link.getAttribute('href').slice(1));
                return { link, section: document.getElementById(id) };
            })
            .filter(item => item.section);

        let ticking = false;
        let activeNavHref = '';
        function setActiveNavLink() {
            const anchorY = window.scrollY + Math.max(140, window.innerHeight * 0.28);
            let activeItem = sectionLinks[0];

            for (const item of sectionLinks) {
                if (item.section.offsetTop <= anchorY) {
                    activeItem = item;
                } else {
                    break;
                }
            }

            const nextHref = activeItem ? activeItem.link.getAttribute('href') : '';
            if (nextHref === activeNavHref) {
                ticking = false;
                return;
            }
            activeNavHref = nextHref;
            navLinks.forEach(link => link.classList.remove('active'));
            if (activeItem) {
                const group = activeItem.link.closest('.nav-group-links');
                const toggle = group ? document.querySelector(`.nav-group-toggle[aria-controls="${group.id}"]`) : null;
                if (group && toggle && group.classList.contains('collapsed')) {
                    group.classList.remove('collapsed');
                    toggle.setAttribute('aria-expanded', 'true');
                }
                activeItem.link.classList.add('active');
            }
            ticking = false;
        }

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(setActiveNavLink);
                ticking = true;
            }
        }, { passive: true });
        window.addEventListener('resize', setActiveNavLink);
        setActiveNavLink();
    });
    """
    return script.replace('__REVISION_LISTS__', json.dumps(REVISION_MODE_LISTS, ensure_ascii=False))

def build_sidebar():
    html = '<aside class="sidebar"><div class="sidebar-title">JLPT N5 Platform<br><span style="font-size:11px;font-weight:400;color:var(--text-4)">From First Principles</span></div>'
    
    html += '<button type="button" class="nav-group-toggle" aria-expanded="true" aria-controls="nav-learning-centers"><span>Learning Centers</span><span class="nav-group-chevron">▾</span></button>'
    html += '<div class="nav-group-links" id="nav-learning-centers">'
    html += '<a href="#n5-grammar-encyclopedia" class="nav-link">Complete N5 Grammar Encyclopedia</a>'
    html += '<a href="#kanji-center" class="nav-link">Kanji Learning Center</a>'
    html += '<a href="#particles" class="nav-link">Particle Encyclopedia</a>'
    html += '<a href="#counter-center" class="nav-link">Counter Encyclopedia</a>'
    html += '<a href="#expressions" class="nav-link">Expression Library</a>'
    html += '<a href="#verbs" class="nav-link">Verb Conjugation Center</a>'
    html += '</div>'
    html += '<button type="button" class="nav-group-toggle" aria-expanded="true" aria-controls="nav-curriculum-lessons"><span>Curriculum Lessons</span><span class="nav-group-chevron">▾</span></button>'
    html += '<div class="nav-group-links" id="nav-curriculum-lessons">'
    for l in ALL_LESSONS:
        html += f'<a href="#lesson-{l["num"]}" class="nav-link">Lesson {l["num"]}: {l["title"]}</a>'
    html += '</div>'
    
    html += '<button type="button" class="nav-group-toggle" aria-expanded="true" aria-controls="nav-test-center"><span>Take Test</span><span class="nav-group-chevron">▾</span></button>'
    html += '<div class="nav-group-links" id="nav-test-center">'
    for t in N5_TESTS:
        html += f'<a href="#test-{t["id"]}" class="nav-link">{t["title"]}</a>'
    html += '</div>'
    
    html += '<div class="sidebar-footer">Made with ❤️ by Akshat Awasthi</div>'
        
    html += '</aside>'
    return html

def build_verb_center():
    html = '<section id="verbs"><h1>Verb Conjugation Center</h1>'
    html += f'<p>{VERB_CENTER["intro"]}</p>'
    for g in VERB_CENTER["groups"]:
        html += f'<div class="card"><h2 style="margin-top:0">{g["name"]}</h2><p>{g["rules"]}</p>'
        html += f'<div class="alert alert-info"><strong>Formula:</strong> {g["example"]}</div>'
        html += '<div class="table-wrapper"><table><thead><tr><th>Dictionary</th><th>Masu (+)</th><th>Masu (-)</th><th>Past (+)</th><th>Past (-)</th></tr></thead><tbody>'
        for v in g["verbs"]:
            html += f'<tr><td class="jp">{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td><td>{v[3]}</td><td>{v[4]}</td></tr>'
        html += '</tbody></table></div></div>'
    
    html += f'<div class="card"><h2>{VERB_CENTER["te_form"]["title"]}</h2><p>{VERB_CENTER["te_form"]["explanation"]}</p>'
    html += '<div class="table-wrapper"><table><thead><tr><th>Verb Type</th><th>Rule</th><th>Example</th></tr></thead><tbody>'
    for r in VERB_CENTER["te_form"]["rules"]:
        html += f'<tr><td>{r[0]}</td><td>{r[1]}</td><td class="jp">{r[2]}</td></tr>'
    html += '</tbody></table></div></div>'
    html += '</section>'
    return html

def build_particle_center():
    html = '<section id="particles"><h1>Particle Encyclopedia</h1>'
    html += '<p>Particles are the glue of Japanese. They attach to the ends of nouns to indicate their grammatical role.</p>'
    for p in PARTICLES:
        html += f'<div class="card"><div class="card-title" style="font-size:32px">{p["particle"]} <span style="font-size:16px;color:var(--text-4)">({p["romaji"]})</span> - {p["core"]}</div>'
        if p.get("origin"):
            html += f'<p><strong>Origin & Logic:</strong> {p["origin"]}</p>'
        else:
            html += f'<p><strong>Core Logic:</strong> {p["core"]}</p>'
        html += '<div class="table-wrapper"><table><thead><tr><th>Usage</th><th>Example Sentence</th></tr></thead><tbody>'
        for u in p["meanings"]:
            html += f'<tr><td><strong>{u[0]}</strong></td><td class="jp">{u[1]}</td></tr>'
        html += '</tbody></table></div>'
        trap_items = p.get("jlpt_traps") or p.get("common_mistakes") or []
        if trap_items:
            html += '<div class="alert alert-danger"><strong>EXAM TRAP:</strong><ul style="margin:8px 0 0 18px">'
            for trap in trap_items:
                html += f'<li>{trap}</li>'
            html += '</ul></div>'
        if p.get("compare_with"):
            html += f'<div class="alert alert-info"><strong>Compare with:</strong> {", ".join(p["compare_with"])}</div>'
        html += '</div>'
    html += '</section>'
    return html

def build_expression_center():
    html = '<section id="expressions"><h1>Expression Library</h1>'
    html += '<p>Essential daily expressions and set phrases for various situations.</p>'
    for category, phrases in EXPRESSIONS:
        html += f'<div class="card"><h2>{category}</h2>'
        html += '<div class="table-wrapper"><table><thead><tr><th>Japanese</th><th>Romaji</th><th>Meaning & Nuance</th></tr></thead><tbody>'
        for jp, romaji, meaning in phrases:
            html += f'<tr><td class="jp" style="font-weight:700">{jp}</td><td style="color:var(--text-3)">{romaji}</td><td>{meaning}</td></tr>'
        html += '</tbody></table></div></div>'
    html += '</section>'
    return html

def build_kanji_center():
    html = '<section id="kanji-center"><h1>Kanji Learning Center</h1>'
    html += '<p>The complete, exhaustive JLPT N5 Kanji textbook. Master the characters, readings, and vocabulary.</p>'
    html += '<input type="text" id="kanji-search" class="search-bar" placeholder="Search by kanji, meaning, reading, or vocabulary...">'
    
    # Group by category
    categories = {}
    for k in KANJI_DATA:
        cat = k.get("category", "Other")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(k)
        
    for cat, kanjis in categories.items():
        html += '<div class="kanji-category-group">'
        html += f'<h2 style="color:var(--accent-text); border-bottom-color:var(--accent)">{cat} Kanji</h2>'
        for k in kanjis:
            search_terms = [
                k["kanji"],
                k["meaning"],
                " ".join(k.get("onyomi", [])),
                " ".join(k.get("kunyomi", [])),
            ]
            for v in k.get("vocab", []):
                search_terms.extend([
                    v.get("word", ""),
                    v.get("kana", ""),
                    v.get("romaji", ""),
                    v.get("english", ""),
                ])
            search_index = " ".join(str(term) for term in search_terms if term)
            html += f'<div class="kc-card" data-search="{html_lib.escape(search_index)}"><div class="kc-header">'
            html += f'<div class="kc-char-box">{k["kanji"]}</div>'
            html += f'<div class="kc-info"><div class="kc-meaning">{k["meaning"]}</div>'
            html += f'<div class="kc-meta-badges"><span class="kc-badge jlpt">{k["jlpt"]}</span><span class="kc-badge">{k["strokes"]} Strokes</span><span class="kc-badge">Radical: {k["radical"]}</span></div>'
            
            onyomi = "、".join(k["onyomi"]) if k["onyomi"] else "-"
            kunyomi = "、".join(k["kunyomi"]) if k["kunyomi"] else "-"
            
            html += f'<div class="kc-readings"><div class="kc-r-label">On:</div><div class="kc-r-val">{onyomi}</div>'
            html += f'<div class="kc-r-label">Kun:</div><div class="kc-r-val">{kunyomi}</div></div>'
            html += '</div></div>' # End header
            
            html += '<div class="kc-body">'
            html += f'<div class="kc-memory">🧠 <strong>Memory Trick:</strong> {k["mnemonic"]}<br><span style="font-size:12px;color:var(--text-3);margin-top:4px;display:block"><strong>Breakdown:</strong> {k["visual_breakdown"]}</span></div>'
            
            if "common_mistakes" in k:
                html += f'<div class="alert alert-warning" style="padding:12px">⚠️ <strong>Note:</strong> {k["common_mistakes"]}</div>'
                
            if "real_life_usage" in k:
                html += f'<div style="font-size:13px;color:var(--text-4);margin-bottom:16px"><strong>Real Life Usage:</strong> {", ".join(k["real_life_usage"])}</div>'
            
            html += '<table class="kc-vocab-table"><thead><tr><th style="width:200px">Vocabulary</th><th>Example Sentence</th></tr></thead><tbody>'
            for v in k["vocab"]:
                html += f'<tr><td><div class="kc-v-word">{v["word"]}</div><div class="kc-v-kana">{v["kana"]}</div><div class="kc-v-romaji">{v["romaji"]}</div><div style="font-size:13px;margin-top:4px;font-weight:600">{v["english"]}</div></td>'
                html += f'<td><div class="kc-s-jp">{v["sentence_jp"]}</div><div class="kc-s-jp" style="font-size:13px;color:var(--text-3)">{v["sentence_kana"]}</div><div class="kc-s-eng">{v["sentence_romaji"]}</div><div class="kc-s-eng" style="color:var(--text-2)">{v["sentence_eng"]}</div></td></tr>'
            html += '</tbody></table>'
            html += '</div></div>' # End body & card
        html += '</div>'
            
    html += '</section>'
    return html

def build_counter_center():
    html = '<section id="counter-center"><h1>Japanese Counter Encyclopedia (JLPT N5)</h1>'
    html += '<p>This independent counter center collects the core JLPT N5 counters in one place, separate from lesson order.</p>'

    html += '<div class="card"><h2 style="margin-top:0">Counter Overview</h2>'
    html += '<p><strong>Counters</strong> are words attached to numbers when counting things in Japanese. English says "three cats" or "two books"; Japanese says the number plus a counter that matches the object type.</p>'
    html += '<div class="table-wrapper"><table><thead><tr><th>English Idea</th><th>Japanese</th><th>Why This Counter?</th></tr></thead><tbody>'
    overview_rows = [
        ("1 person", "一人（ひとり）", "人 counts people, with ひとり as an exception."),
        ("2 books", "本二冊（ほん にさつ）", "冊 counts bound volumes."),
        ("3 cats", "猫三匹（ねこ さんびき）", "匹 counts small animals."),
    ]
    for eng, jp, why in overview_rows:
        html += f'<tr><td>{html_lib.escape(eng)}</td><td class="jp">{html_lib.escape(jp)}</td><td>{html_lib.escape(why)}</td></tr>'
    html += '</tbody></table></div>'
    html += '<p>Different objects require different counters because Japanese classifies objects by shape, type, animacy, and cultural category: people use 人, flat objects use 枚, long objects use 本, machines use 台, and so on.</p></div>'

    for section in COUNTER_SECTIONS:
        html += f'<div class="card"><h2 style="margin-top:0">{html_lib.escape(section["title"])}: {html_lib.escape(section["counter"])}</h2>'
        html += f'<p><strong>Used for:</strong> {html_lib.escape(section["used_for"])}</p>'
        html += f'<p>{html_lib.escape(section["core_note"])}</p>'
        exceptions = [row for row in section["forms"] if row[3]]
        if exceptions:
            html += '<div class="alert alert-warning"><strong>Dedicated Exception Notes:</strong><ul style="margin:8px 0 0 18px">'
            for number, reading, meaning, note in exceptions:
                html += f'<li><span class="jp">{html_lib.escape(reading)}</span> = {html_lib.escape(meaning)}. {html_lib.escape(note)}</li>'
            html += '</ul></div>'
        html += '<div class="table-wrapper"><table><thead><tr><th>Number</th><th>Reading</th><th>Meaning</th><th>Exception / Pronunciation Note</th></tr></thead><tbody>'
        for number, reading, meaning, note in section["forms"]:
            html += f'<tr><td>{html_lib.escape(number)}</td><td class="jp">{html_lib.escape(reading)}</td><td>{html_lib.escape(meaning)}</td><td>{html_lib.escape(note or "-")}</td></tr>'
        html += '</tbody></table></div>'
        html += f'<div class="alert alert-info"><strong>Memory Trick:</strong> {html_lib.escape(section["memory"])}</div>'
        html += '<h3>Example Sentences</h3><ul>'
        for ex in section["examples"]:
            html += f'<li class="jp">{html_lib.escape(ex)}</li>'
        html += '</ul>'
        html += '<div class="quiz-box"><div class="quiz-q">Which reading matches this counter pattern?</div><div class="quiz-opts">'
        correct = exceptions[0] if exceptions else section["forms"][0]
        html += f'<button data-correct="true">{html_lib.escape(correct[1])}</button>'
        html += f'<button data-correct="false">{html_lib.escape(section["forms"][1][1])}</button>'
        html += f'<button data-correct="false">{html_lib.escape(section["forms"][-1][1])}</button>'
        html += f'</div><div class="quiz-exp"><strong>Correct Answer:</strong> {html_lib.escape(correct[1])}. {html_lib.escape(correct[3] or section["core_note"])}</div></div>'
        html += '</div>'

    html += '<div class="card"><h2 style="margin-top:0">Time Counters</h2>'
    html += '<div class="table-wrapper"><table><thead><tr><th>Counter</th><th>Meaning</th><th>Examples</th><th>JLPT Note</th></tr></thead><tbody>'
    for counter, meaning, examples, note in TIME_COUNTERS:
        html += f'<tr><td class="jp">{html_lib.escape(counter)}</td><td>{html_lib.escape(meaning)}</td><td class="jp">{html_lib.escape(examples)}</td><td>{html_lib.escape(note)}</td></tr>'
    html += '</tbody></table></div></div>'

    html += '<div class="card"><h2 style="margin-top:0">Counter Comparison Table</h2>'
    html += '<div class="table-wrapper"><table><thead><tr><th>Counter</th><th>Used For</th><th>Examples</th><th>Exceptions</th><th>Pronunciation Notes</th></tr></thead><tbody>'
    for section in COUNTER_SECTIONS:
        exceptions = ", ".join(row[1] for row in section["forms"] if row[3]) or "-"
        examples = " / ".join(section["examples"][:2])
        notes = section["core_note"]
        html += f'<tr><td class="jp">{html_lib.escape(section["counter"])}</td><td>{html_lib.escape(section["used_for"])}</td><td class="jp">{html_lib.escape(examples)}</td><td class="jp">{html_lib.escape(exceptions)}</td><td>{html_lib.escape(notes)}</td></tr>'
    for counter, meaning, examples, note in TIME_COUNTERS:
        html += f'<tr><td class="jp">{html_lib.escape(counter)}</td><td>{html_lib.escape(meaning)}</td><td class="jp">{html_lib.escape(examples)}</td><td>-</td><td>{html_lib.escape(note)}</td></tr>'
    html += '</tbody></table></div></div>'

    html += '<div class="card"><h2 style="margin-top:0">Important Counter Exceptions</h2>'
    html += '<p>Use this as the fast irregular-form review before a quiz or JLPT mock test.</p>'
    html += '<div class="table-wrapper"><table><thead><tr><th>Counter</th><th>Irregular Forms</th></tr></thead><tbody>'
    for section in COUNTER_SECTIONS:
        exceptions = [row for row in section["forms"] if row[3]]
        if exceptions:
            html += f'<tr><td class="jp">{html_lib.escape(section["counter"])}</td><td class="jp">{html_lib.escape(", ".join(row[1] for row in exceptions))}</td></tr>'
    html += '</tbody></table></div></div>'

    html += '<div class="card"><h2 style="margin-top:0">Counter Quizzes</h2>'
    quiz_items = [
        ("Meaning Recognition", "Which counter counts small animals like cats?", [("匹", True), ("枚", False), ("台", False)], "匹 counts small animals."),
        ("Pronunciation Recognition", "How do you read 1 minute?", [("いっぷん", True), ("いちふん", False), ("ひとふん", False)], "1 minute is いっぷん."),
        ("Sentence Completion", "猫が三___います。", [("匹", True), ("冊", False), ("台", False)], "Cats are small animals, so use 匹."),
        ("JLPT Style", "Which reading is correct for 二十歳?", [("はたち", True), ("にじゅうさい", False), ("ふつか", False)], "Twenty years old is the special age form はたち."),
    ]
    for title, question, options, explanation in quiz_items:
        html += f'<div class="quiz-box"><div class="quiz-q">{html_lib.escape(title)}: {html_lib.escape(question)}</div><div class="quiz-opts">'
        for label, correct in options:
            html += f'<button data-correct="{str(correct).lower()}">{html_lib.escape(label)}</button>'
        html += f'</div><div class="quiz-exp"><strong>Explanation:</strong> {html_lib.escape(explanation)}</div></div>'
    html += '</div>'

    html += '<div class="card"><h2 style="margin-top:0">Final Revision Sheet</h2>'
    html += '<h3>Top N5 Counters</h3><p class="jp">人・日・分・本・匹・冊・枚・台・階・歳・か月・時間・週間・年・回</p>'
    html += '<h3>Most Important Exceptions</h3><p class="jp">ひとり、ふたり、ついたち、ふつか、みっか、よっか、はつか、いっぷん、ろっぷん、いっぽん、さんぼん、いっぴき、さんびき、はたち</p>'
    html += '<h3>Most Common JLPT Counter Questions</h3><ul><li>Choose the correct counter for an object.</li><li>Choose the correct pronunciation after sound change.</li><li>Recognize irregular dates and ages.</li><li>Complete sentences like 猫が三___います。</li></ul>'
    html += '<h3>One Page Counter Cheat Sheet</h3><p>People = 人. Days = 日. Minutes = 分. Long objects = 本. Small animals = 匹. Books = 冊. Flat objects = 枚. Machines/vehicles = 台. Floors = 階. Age = 歳. Months = か月. Hours/weeks/years/times = 時間・週間・年・回.</p>'
    html += '</div></section>'
    return html

def build_grammar_encyclopedia():
    flat_entries = []
    for entry in N5_GRAMMAR_ENCYCLOPEDIA:
        if "points" in entry:
            for point in entry["points"]:
                merged = {
                    "category": entry.get("category", "General"),
                    "jlpt_category": entry.get("jlpt_category", "N5"),
                }
                merged.update(point)
                flat_entries.append(merged)
        else:
            flat_entries.append(entry)

    categories = sorted({entry["category"] for entry in flat_entries})

    html = '<section id="n5-grammar-encyclopedia"><h1>Complete N5 Grammar Encyclopedia</h1>'
    html += '<p>This section is fully independent from lesson flow and is organized by grammar category so you can revise the entire JLPT N5 grammar syllabus from one place.</p>'

    html += '<div class="card" id="grammar-search-card">'
    html += '<h2 style="margin-top:0">Grammar Search</h2>'
    html += '<div class="grammar-search-grid">'
    html += '<div><label for="grammar-category-search">Category</label><select id="grammar-category-search"><option value="">All categories</option>'
    for cat in categories:
        html += f'<option value="{html_lib.escape(cat)}">{html_lib.escape(cat)}</option>'
    html += '</select></div>'
    html += '<div class="grammar-filter-actions"><button type="button" class="grammar-filter-btn" id="grammar-filter-btn">Filter</button><button type="button" class="grammar-filter-btn secondary" id="grammar-clear-filter-btn">Clear Filter</button></div>'
    html += '</div></div>'

    html += '<div class="card grammar-support-card"><h2 style="margin-top:0">Grammar Relationship Map</h2>'
    html += '<div class="relationship-map">'
    html += '<span class="map-node">Dictionary Form</span><span class="map-arrow">→</span>'
    html += '<span class="map-node">Masu Form</span><span class="map-arrow">→</span>'
    html += '<span class="map-node">Te Form</span><span class="map-arrow">→</span>'
    html += '<span class="map-node">Permission 〜てもいいです</span><span class="map-arrow">→</span>'
    html += '<span class="map-node">Prohibition 〜てはいけません</span><span class="map-arrow">→</span>'
    html += '<span class="map-node">Requests 〜てください</span><span class="map-arrow">→</span>'
    html += '<span class="map-node">Progressive 〜ています</span>'
    html += '</div></div>'

    html += '<div class="card grammar-support-card"><h2 style="margin-top:0">Te Form Master Section</h2>'
    html += '<div class="te-grid">'
    html += '<div class="te-box"><h3 style="margin-top:0">Group 1 Conversion Rules</h3><ul>'
    html += '<li>く → いて</li><li>ぐ → いで</li><li>む → んで</li><li>ぶ → んで</li><li>ぬ → んで</li><li>す → して</li><li>つ → って</li><li>る → って</li><li>う → って</li>'
    html += '</ul><p><strong>Exception:</strong> いく → いって</p></div>'
    html += '<div class="te-box"><h3 style="margin-top:0">All Core Te-form Usages</h3><ul>'
    html += '<li>Request: 〜てください</li><li>Permission: 〜てもいいです</li><li>Prohibition: 〜てはいけません</li><li>Sequential Action: 〜て</li><li>Ongoing Action: 〜ています</li><li>State: 〜ています</li>'
    html += '</ul></div>'
    html += '</div></div>'

    html += '<div class="card grammar-support-card"><h2 style="margin-top:0">Grammar Revision Mode</h2>'
    html += '<div class="revision-tabs">'
    html += '<button class="revision-tab active" data-mode="top25">Top 25 N5 Grammar</button>'
    html += '<button class="revision-tab" data-mode="top50">Top 50 N5 Grammar</button>'
    html += '<button class="revision-tab" data-mode="exam">Most Important Exam Grammar</button>'
    html += '<button class="revision-tab" data-mode="oneday">One-Day Revision Sheet</button>'
    html += '</div><ul class="revision-list" id="grammar-revision-list"></ul></div>'

    for entry in flat_entries:
        html += f'<div class="encyclopedia-category"><h2>{html_lib.escape(entry["category"])}</h2>'
        html += f'<div class="encyclopedia-meta">JLPT Category: {html_lib.escape(entry["jlpt_category"])}</div>'
        html += (
            f'<article class="grammar-encyclopedia-card" '
            f'data-pattern="{html_lib.escape(entry["pattern"])}" '
            f'data-meaning="{html_lib.escape(entry["meaning"])}" '
            f'data-concept="{html_lib.escape(entry["english_concept"])}" '
            f'data-structure="{html_lib.escape(entry["structure"])}" '
            f'data-category="{html_lib.escape(entry["category"])}">'
        )

        html += f'<div class="g-pattern">{html_lib.escape(entry["pattern"])}</div>'
        html += f'<div class="g-sub">{html_lib.escape(entry["meaning"])}</div>'

        rows = [
            ("Meaning", entry["meaning"]),
            ("Structure", entry["structure"]),
            ("Formation Rules", entry["formation"]),
            ("Conjugation Rules", entry["conjugation"]),
            ("Formal Usage", entry["formal"]),
            ("Casual Usage", entry["casual"]),
            ("Common Mistakes", entry["mistakes"]),
            ("JLPT Traps", entry["traps"]),
            ("Related Grammar", entry["related"]),
            ("Differences from Similar Grammar", entry["differences"]),
        ]
        for label, value in rows:
            html += f'<div class="g-row-rich"><div class="label">{html_lib.escape(label)}</div><div class="val">{html_lib.escape(value)}</div></div>'

        html += '<div class="table-wrapper example-table"><table><thead><tr><th>Japanese</th><th>Kana</th><th>Romaji</th><th>English Translation</th></tr></thead><tbody>'
        for jp, kana, romaji, eng in entry["examples"]:
            html += (
                f'<tr><td class="jp">{html_lib.escape(jp)}</td>'
                f'<td class="jp">{html_lib.escape(kana)}</td>'
                f'<td>{html_lib.escape(romaji)}</td>'
                f'<td>{html_lib.escape(eng)}</td></tr>'
            )
        html += '</tbody></table></div>'

        html += '<div class="conversation-block"><strong>Conversation Examples</strong><br>'
        for conv in entry["conversation"]:
            if isinstance(conv, (list, tuple)) and len(conv) >= 4:
                cjp, ckana, cromaji, ceng = conv[0], conv[1], conv[2], conv[3]
                html += f'<div class="jp" style="font-size:14px">{html_lib.escape(cjp)}</div>'
                html += f'<div style="font-size:13px;color:var(--text-3)">{html_lib.escape(ckana)}</div>'
                html += f'<div style="font-size:12px;color:var(--text-4)">{html_lib.escape(cromaji)}</div>'
                html += f'<div style="font-size:13px;margin-bottom:8px">{html_lib.escape(ceng)}</div>'
            else:
                html += f'<div style="font-size:13px;margin-bottom:8px">{html_lib.escape(str(conv))}</div>'
        html += '</div>'
        html += '</article></div>'

    html += '</section>'
    return html

def build_lesson(l):
    html = f'<section id="lesson-{l["num"]}"><h1>Lesson {l["num"]}: {l["title"]}</h1>'
    html += f'<p class="jp" style="font-size:20px; color:var(--text-3)">{l["jp_title"]}</p>'
    html += f'<div class="card"><p><strong>Overview:</strong> {l["overview"]}</p><h3>Objectives</h3><ul>'
    for obj in l["objectives"]:
        html += f'<li>{obj}</li>'
    html += '</ul></div>'
    
    # Vocab
    html += '<h2>Vocabulary (First Principles)</h2><div class="table-wrapper"><table>'
    html += '<thead><tr><th>Kanji</th><th>Kana</th><th>English</th><th>Type</th><th>Example in Context</th></tr></thead><tbody>'
    for v in l["vocab"]:
        html += f'<tr><td class="jp" style="font-weight:700">{v[0]}</td><td class="jp">{v[1]}</td><td>{v[2]}</td><td><span style="font-size:11px;background:var(--surface-raised);padding:2px 6px;border-radius:4px">{v[3]}</span></td><td class="jp" style="font-size:13px">{v[5]}<br><span style="color:var(--text-4)">{v[7]}</span></td></tr>'
    html += '</tbody></table></div>'
    
    # Grammar
    html += '<h2>Grammar Deep Dive</h2>'
    for g in l["grammar"]:
        html += f'<div class="grammar-block"><div class="card-title">{g["pattern"]}</div>'
        html += f'<p><em>Meaning: {g["meaning"]}</em></p>'
        html += f'<div class="g-row"><div class="g-label">Structure</div><div class="g-content"><code style="font-family:monospace;background:var(--bg);padding:2px 6px;border-radius:4px">{g["structure"]}</code></div></div>'
        html += f'<div class="g-row"><div class="g-label">Formation Logic</div><div class="g-content">{g["formation"]}</div></div>'
        html += f'<div class="g-row"><div class="g-label">Why? (Origin)</div><div class="g-content">{g["why"]}</div></div>'
        html += f'<div class="g-row"><div class="g-label">Formal Usage</div><div class="g-content">{g["formal"]}</div></div>'
        html += f'<div class="g-row"><div class="g-label">Casual Usage</div><div class="g-content">{g["casual"]}</div></div>'
        html += f'<div class="g-row"><div class="g-label">Native Nuance</div><div class="g-content">{g["native"]}</div></div>'
        html += '<div class="g-row" style="margin-top:12px"><div class="g-label">Examples</div><div class="g-content">'
        for ex in g["examples"]:
            html += f'<div style="margin-bottom:8px"><div class="jp">{ex[0]}</div><div style="font-size:13px;color:var(--text-4)">{ex[1]}</div></div>'
        html += '</div></div>'
        html += f'<div class="alert alert-warning" style="margin-top:16px"><strong>Common Mistake:</strong> {g["mistakes"]}</div>'
        html += f'<div class="alert alert-info"><strong>JLPT Strategy:</strong> {g["jlpt"]}</div>'
        html += '</div>'


    # Kanji
    if "kanji" in l:
        html += '<h2>Kanji Mastery</h2><div class="kanji-grid">'
        for k in l["kanji"]:
            html += f'<div class="kanji-card"><div class="k-char">{k[0]}</div>'
            html += f'<div class="k-meta">Kun: {k[1]} | On: {k[2]} | Strokes: {k[3]}</div>'
            html += f'<div style="font-weight:700;margin-bottom:8px">{k[4]}</div>'
            html += f'<div class="k-tip">🧠 <strong>Memory Tip:</strong> {k[5]}</div>'
            html += '<div style="text-align:left;font-size:13px;border-top:1px solid var(--border);padding-top:8px;margin-top:8px"><strong>JLPT Vocab:</strong><br>'
            for kv in k[6]:
                html += f'<span class="jp">{kv[0]}</span> ({kv[1]}) - {kv[2]}<br>'
            html += '</div></div>'
        html += '</div>'
        
    # Quiz
    if "quiz" in l:
        html += '<h2>Interactive Mock Test</h2>'
        for q in l["quiz"]:
            html += f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div><div class="quiz-opts">'
            for opt in q["opts"]:
                is_correct = 'true' if opt.startswith(q["ans"]) else 'false'
                html += f'<button data-correct="{is_correct}">{opt}</button>'
            html += f'</div><div class="quiz-exp"><strong>Correct Answer: {q["ans"]}</strong>. {q["exp"]}</div></div>'
            
    html += '</section><hr style="border-color:var(--border);margin:60px 0">'
    return html

def build_test_center():
    html = '<section id="test-center">'
    html += '<h1>Take Test \u2014 JLPT N5 Practice</h1>'
    html += '<p style="font-size:16px;color:var(--text-3);margin-bottom:36px">Genuine JLPT N5-level questions across grammar, vocabulary, kanji reading, sentence comprehension, and real-life situations. Click any answer to check it instantly.</p>'
    for test in N5_TESTS:
        color = test['color']
        html += f'<section id="test-{test["id"]}" style="margin-bottom:60px">'
        html += f'<h2 style="color:{color};border-bottom-color:{color}">{test["title"]}</h2>'
        html += f'<p style="color:var(--text-3);margin-bottom:24px">{test["description"]}</p>'
        html += f'<div style="background:var(--surface);border:2px solid {color};border-radius:10px;padding:14px 20px;margin-bottom:24px;display:flex;align-items:center;justify-content:space-between">'
        html += f'<span style="font-size:15px;font-weight:700;color:var(--text-1)">Score</span>'
        html += f'<span style="font-size:24px;font-weight:800;color:{color}" id="score-display-{test["id"]}">0 / {len(test["questions"])}</span>'
        html += '</div>'
        for i, q in enumerate(test['questions']):
            q_id = f"{test['id']}-q{i}"
            html += f'<div class="quiz-box" id="{q_id}" data-test-id="{test["id"]}" data-score-display="score-display-{test["id"]}" data-total="{len(test["questions"])}">'
            html += f'<div class="quiz-q" style="white-space:pre-line;font-size:15px">{q["q"]}</div>'
            html += '<div class="quiz-opts">'
            for opt in q['opts']:
                is_correct = 'true' if opt.startswith(q['ans'] + '.') else 'false'
                html += f'<button data-correct="{is_correct}">{opt}</button>'
            html += f'</div><div class="quiz-exp"><strong style="color:{color}">\u2713 Correct Answer: {q["ans"]}</strong><br><br>{q["exp"]}</div>'
            html += '</div>'
        html += '</section>'
    html += '</section>'
    return html


def build_all():
    html = f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Ultimate Japanese Learning Ecosystem</title><style>{generate_css()}</style></head><body>'
    html += '<div class="layout">'
    html += build_sidebar()
    html += '<main class="main-content">'
    html += '<h1>Minna no Nihongo JLPT N5 Revision Guide</h1>'
    html += '<p style="font-size:18px;color:var(--text-3);margin-bottom:12px">Revise easily, clear your doubts, and review grammar, kanji, particles, counters, vocabulary, and lessons directly from Minna no Nihongo.</p>'
    

    html += build_grammar_encyclopedia()
    html += '<hr style="border-color:var(--border);margin:60px 0">'
    html += build_kanji_center()
    html += '<hr style="border-color:var(--border);margin:60px 0">'
    html += build_particle_center()
    html += '<hr style="border-color:var(--border);margin:60px 0">'
    html += build_counter_center()
    html += '<hr style="border-color:var(--border);margin:60px 0">'
    html += build_expression_center()
    html += '<hr style="border-color:var(--border);margin:60px 0">'
    html += build_verb_center()
    html += '<hr style="border-color:var(--border);margin:60px 0">'
    
    for l in ALL_LESSONS:
        html += build_lesson(l)
        
    html += build_test_center()
    
    html += f'</main></div><script>{generate_js()}</script></body></html>'
    return html

if __name__ == "__main__":
    with open("study_bible.html", "w", encoding="utf-8") as f:
        f.write(build_all())
    print("SUCCESS: Generated massive First Principles ecosystem (Modular Build!)")
