with open('study_bible.html', 'r', encoding='utf-8') as f:
    c = f.read()

checks = [
    ("Sidebar nav", "sidebar" in c),
    ("Dark mode toggle", "darkModeBtn" in c),
    ("Print mode btn", "printModeBtn" in c),
    ("Export PDF btn", "exportPdfBtn" in c),
    ("Topbar", "topbar" in c),
    ("Lesson 1 section", 'id="lesson-1"' in c),
    ("Lesson 25 section", 'id="lesson-25"' in c),
    ("Grammar index", 'id="grammar-index"' in c),
    ("Particles guide", 'id="particles-guide"' in c),
    ("Verb conjugation", 'id="verb-conjugation"' in c),
    ("Vocab mock test", 'id="vocab-test"' in c),
    ("Grammar mock test", 'id="grammar-test"' in c),
    ("Revision pack", 'id="revision-pack"' in c),
    ("Grammar cards", "grammar-card" in c),
    ("Quiz items", "quiz-item" in c),
    ("Google Fonts", "fonts.googleapis.com" in c),
    ("Noto Sans JP", "Noto+Sans+JP" in c),
    ("BIZ UDPGothic", "BIZ+UDPGothic" in c),
    ("Inter font", "Inter" in c),
    ("Dark CSS vars", "0F172A" in c),
    ("Light CSS vars", "FAFAFA" in c),
    ("Sidebar search", "sidebarSearch" in c),
    ("IntersectionObserver", "IntersectionObserver" in c),
    ("Lesson nav prev/next", "lesson-nav-btn" in c),
    ("Max-width 960px", "960px" in c),
    ("No emoji in HTML", "\U0001f4d6" not in c and "\U0001f393" not in c and "\U0001f4dd" not in c),
]

all_pass = True
for name, ok in checks:
    s = "PASS" if ok else "FAIL"
    if not ok:
        all_pass = False
    print(f"{s}  {name}")

print(f"\nFile size: {len(c.encode('utf-8'))//1024} KB")
print("ALL CHECKS PASSED" if all_pass else "SOME CHECKS FAILED")
