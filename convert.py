import os
import glob
from bs4 import BeautifulSoup
import json

def process_file(filepath, outdir, layout):
    with open(filepath, 'r') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract language
    html_tag = soup.find('html')
    locale = html_tag.get('lang', 'fr') if html_tag else 'fr'
    
    # Title
    h1 = soup.find('h1')
    title = h1.text.strip() if h1 else "Untitled"
    title = title.replace('"', '\\"')
    
    # Meta
    meta_dict = {}
    dmeta = soup.find('div', class_='dmeta')
    if dmeta:
        for div in dmeta.find_all('div'):
            k_span = div.find('span', class_='k')
            if k_span:
                k = k_span.text.strip()
                v = div.text.replace(k, '').strip()
                # Map keys to standard english ones for frontmatter
                if k in ['Catégorie', 'Category']: k = 'category'
                elif k in ['Marque', 'Brand']: k = 'brand'
                elif k in ['Collection']: k = 'collection'
                elif k in ['Année', 'Year']: k = 'year'
                elif k in ['Date']: k = 'date'
                elif k in ['Projet', 'Project']: k = 'project_tag'
                meta_dict[k] = v.replace('"', '\\"')

    # Body
    body_div = soup.find('div', class_='body')
    content = ""
    if body_div:
        content = body_div.decode_contents()

    # Gallery
    gallery = []
    gal_div = soup.find('div', class_='gal')
    if gal_div:
        for img in gal_div.find_all('img'):
            src = img.get('src')
            if src:
                gallery.append(src)
    
    # Create frontmatter
    fm = f"---\nlayout: {layout}\ntitle: \"{title}\"\nlocale: \"{locale}\"\n"
    for k, v in meta_dict.items():
        fm += f"{k}: \"{v}\"\n"
    
    if gallery:
        fm += "gallery:\n"
        for img in gallery:
            fm += f"  - \"{img}\"\n"
    fm += "---\n"
    
    # Create output
    basename = os.path.basename(filepath).replace('.html', '.md')
    outpath = os.path.join(outdir, basename)
    
    # Ensure dir exists
    os.makedirs(outdir, exist_ok=True)
    
    with open(outpath, 'w') as f:
        f.write(fm + content)

# Process studio
for f in glob.glob('studio/*.html'):
    if not f.endswith('index.html'): process_file(f, 'src/studio', 'project.njk')
for f in glob.glob('en/studio/*.html'):
    if not f.endswith('index.html'): process_file(f, 'src/en/studio', 'project.njk')

# Process products
for f in glob.glob('products/*.html'):
    if not f.endswith('index.html'): process_file(f, 'src/products', 'project.njk')
for f in glob.glob('en/products/*.html'):
    if not f.endswith('index.html'): process_file(f, 'src/en/products', 'project.njk')

# Process news
for f in glob.glob('news/*.html'):
    if not f.endswith('index.html'): process_file(f, 'src/news', 'article.njk')
for f in glob.glob('en/news/*.html'):
    if not f.endswith('index.html'): process_file(f, 'src/en/news', 'article.njk')

print("Done converting to Markdown!")
