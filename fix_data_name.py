import re
import glob

def clean_data_name(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    def replacer(match):
        # match.group(0) is the whole match
        # match.group(1) is the class
        # match.group(2) is the current data-name
        # match.group(3) is the href
        # match.group(4) is the inner HTML before h3
        # match.group(5) is the h3 text
        # match.group(6) is the text inside <span class="m">
        # match.group(7) is the rest
        
        title = match.group(5).strip().lower()
        cat_year = match.group(6).strip().lower().replace('·', '')
        
        new_data_name = f"{title} {cat_year}"
        
        return f'<a class="{match.group(1)}" data-name="{new_data_name}" href="{match.group(3)}">{match.group(4)}<h3>{match.group(5)}</h3><span class="m">{match.group(6)}</span>{match.group(7)}'

    # Regex to match the entire anchor tag and extract the title and category
    # <a class="card reveal" data-name="2024 auto..." href="../studio/r17-electric-restomod.html"><div class="thumb">...<span class="idx">001</span><span class="tx"><h3>R17 electric restomod</h3><span class="m">Transport· 2024</span></span></span></a>
    pattern = re.compile(r'<a class="([^"]*card[^"]*)" data-name="([^"]*)" href="([^"]+)">([^<]*<div class="thumb">.*?<span class="idx">.*?<span class="tx">)<h3>(.*?)</h3><span class="m">(.*?)</span>(.*?)</a>', re.DOTALL)
    
    new_content = pattern.sub(replacer, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Cleaned {filepath}")

files = ["index.html", "en/index.html", "projets/index.html", "en/projets/index.html"]
for f in files:
    clean_data_name(f)
