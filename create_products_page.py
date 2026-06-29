import re
import os
import shutil

def create_filtered_page(src_path, dest_path, title, macro_keyword):
    with open(src_path, 'r') as f:
        content = f.read()

    # Change title
    content = re.sub(r'<title>.*?</title>', f'<title>{title} — Ora-ïto</title>', content)
    # Change h2
    content = re.sub(r'<div class="sec-head"><h2>.*?</h2>', f'<div class="sec-head"><h2>{title.lower()}</h2>', content)
    
    # Remove filter tags
    content = re.sub(r'<div class="filter-tags">.*?</div>', '', content, flags=re.DOTALL)

    # Filter grid cards
    def filter_grid(match):
        cards_content = match.group(1)
        # Find all cards
        cards = re.findall(r'<a class="[^"]*card[^"]*"[^>]*>.*?</a>', cards_content, re.DOTALL)
        filtered_cards = [c for c in cards if macro_keyword in c.lower()]
        
        return f'<div class="grid">{ "".join(filtered_cards) }</div>'

    content = re.sub(r'<div class="grid">(.*?)</div>\s*</div>\s*<footer', lambda m: filter_grid(m) + '\n</div><footer', content, flags=re.DOTALL)

    # Fix relative links
    if 'en/products' in dest_path:
        pass # same level as en/projets, no link changes needed
    elif 'produits' in dest_path:
        pass # same level as projets, no link changes needed
    elif 'products' in dest_path and not 'en/products' in dest_path:
        pass

    # Ensure dest dir exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(content)
    print(f"Created {dest_path}")

create_filtered_page('projets/index.html', 'produits/index.html', 'Produits', 'produit product')
create_filtered_page('en/projets/index.html', 'en/products/index.html', 'Products', 'produit product')
# Also overwrite the root 'products/index.html' redirect with the french one just in case
create_filtered_page('projets/index.html', 'products/index.html', 'Produits', 'produit product')

