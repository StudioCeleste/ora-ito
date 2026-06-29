import re
import os

def fix_data_name(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    def replacer(match):
        # We assume the current data-name is just "{title} {cat_year}" as set by previous script
        current_data_name = match.group(2)
        
        # We extract category from cat_year
        # e.g. "transport 2024" -> "transport"
        # Since we lowercased it and removed '·', it's space separated
        cat_str = match.group(6).strip().lower().replace('·', '')
        
        macro = ""
        if "architecture" in cat_str:
            macro = "architecture"
        elif "transport" in cat_str:
            macro = "transport transportation"
        elif "prototype" in cat_str or "virtual" in cat_str:
            macro = "virtual"
        else:
            # All others (Mobilier, Technologie, Accessoires, Cuisine, Bijouterie, etc.) are "Product"
            macro = "produit product"

        new_data_name = f"{current_data_name} {macro}"
        
        return f'<a class="{match.group(1)}" data-name="{new_data_name}" href="{match.group(3)}">{match.group(4)}<h3>{match.group(5)}</h3><span class="m">{match.group(6)}</span>{match.group(7)}'

    pattern = re.compile(r'<a class="([^"]*card[^"]*)" data-name="([^"]*)" href="([^"]+)">([^<]*<div class="thumb">.*?<span class="idx">.*?<span class="tx">)<h3>(.*?)</h3><span class="m">(.*?)</span>(.*?)</a>', re.DOTALL)
    
    new_content = pattern.sub(replacer, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Fixed macro categories in {filepath}")

files = ["index.html", "en/index.html", "projets/index.html", "en/projets/index.html"]
for f in files:
    if os.path.exists(f):
        fix_data_name(f)
