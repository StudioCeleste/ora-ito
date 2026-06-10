import os
import glob
import re

replacements = {
    "Optiques 7887L": "Accessoires",
    "Optiques 7888L": "Accessoires",
    "Optiques 7889L": "Accessoires",
    "Optiques 7890L": "Accessoires",
    "Solaires 7927L": "Accessoires",
    "Solaires 7928L": "Accessoires",
    "Casque intra-auriculaire": "Technologie",
    "Casque supra-auriculaire": "Technologie",
    "Chargeur allume-cigare": "Technologie",
    "Chargeur secteur": "Technologie",
    "Câble USB": "Technologie",
    "Câble double USB": "Technologie",
    "Enceinte sans fil": "Technologie",
    "Coque rigide pour Smartphones": "Technologie",
    "Coque semi-rigide": "Technologie",
    "Etui Folio pour Smartphones": "Technologie",
    "Etui Folio pour Tablettes": "Technologie",
    "Urbanisation": "Architecture",
    "Résidentiel": "Architecture",
    "Showroom": "Architecture"
}

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig = content
    for old, new in replacements.items():
        content = content.replace(f'<span class="m">{old}·', f'<span class="m">{new}·')
        content = content.replace(f'<span class="m">{old} ·', f'<span class="m">{new} ·')
        content = content.replace(f'<span class="k">Catégorie</span> {old}', f'<span class="k">Catégorie</span> {new}')
        
        def replacer(match):
            pre = match.group(1)
            data = match.group(2)
            post = match.group(3)
            d = data.replace(old.lower(), new.lower())
            return pre + d + post
            
        content = re.sub(r'(data-name=")([^"]*)(")', replacer, content)
        
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for f in glob.glob('*.html') + glob.glob('projets/*.html') + glob.glob('studio/*.html') + glob.glob('products/*.html'):
    replace_in_file(f)

print("Done.")
