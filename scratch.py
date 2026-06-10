import re
from collections import defaultdict

with open('projets/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<span class="tx"><h3>(.*?)</h3><span class="m">(.*?)· \d{4}</span>', re.IGNORECASE)
matches = pattern.findall(content)

categories = defaultdict(list)
for title, cat in matches:
    categories[cat.strip()].append(title.strip())

with open('scratch.txt', 'w', encoding='utf-8') as f:
    for cat, titles in sorted(categories.items()):
        f.write(f"=== {cat} ===\n")
        for t in titles:
            f.write(f" - {t}\n")
        f.write("\n")
