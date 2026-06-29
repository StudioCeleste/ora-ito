import re
import os

def fix_data_name(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    def replacer(match):
        title = match.group(5).strip().lower()
        cat_year = match.group(6).strip().lower().replace('·', '')
        macro = ""
        if "architecture" in cat_year:
            macro = "architecture"
        elif "transport" in cat_year:
            macro = "transport transportation"
        elif "prototype" in cat_year or "virtual" in cat_year:
            macro = "virtual"
        else:
            macro = "produit product"
        new_data_name = f"{title} {cat_year} {macro}"
        return f'<a class="{match.group(1)}" data-name="{new_data_name}" href="{match.group(3)}">{match.group(4)}<h3>{match.group(5)}</h3><span class="m">{match.group(6)}</span>{match.group(7)}'

    pattern = re.compile(r'<a class="([^"]*card[^"]*)" data-name="([^"]*)" href="([^"]+)">([^<]*<div class="thumb">.*?<span class="idx">.*?<span class="tx">)<h3>(.*?)</h3><span class="m">(.*?)</span>(.*?)</a>', re.DOTALL)
    new_content = pattern.sub(replacer, content)
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Cleaned {filepath}")

files = ["src/index.html", "src/en/index.html", "src/projets/index.html", "src/en/projets/index.html", "src/produits/index.html", "src/en/products/index.html"]
for f in files:
    if os.path.exists(f):
        fix_data_name(f)
