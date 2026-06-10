import os
import glob

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig = content
    # Replace the metadata span in grid cards
    content = content.replace('<span class="m">Commercial·', '<span class="m">Architecture·')
    content = content.replace('<span class="m">Commercial ·', '<span class="m">Architecture ·')
    
    # Replace in the detail pages
    content = content.replace('<span class="k">Catégorie</span> Commercial', '<span class="k">Catégorie</span> Architecture')
    
    # Replace in data-name attributes
    # We can just replace 'commercial' with 'architecture' in data-name since it's localized
    # A simple way without regex is just replacing the string if we know where it is, but data-name might have commercial anywhere.
    import re
    def replacer(match):
        pre = match.group(1)
        data = match.group(2)
        post = match.group(3)
        return pre + data.replace('commercial', 'architecture').replace('Commercial', 'Architecture') + post
        
    content = re.sub(r'(data-name=")([^"]*)(")', replacer, content)
    
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for f in glob.glob('*.html') + glob.glob('projets/*.html') + glob.glob('studio/*.html'):
    replace_in_file(f)

print("Done.")
