import re

with open('projets/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_words = ['metro', 'vehicule', 'moto', 'auto', 'train', 'véhicule', 'vélo', 'transport', 'bicyclette', 'automobile', 'velo', 'voiture', 'tramway']

def replacer(match):
    pre = match.group(1)
    data = match.group(2)
    post = match.group(3)
    
    # only remove if it's Mobilier (it contains 'mobilier')
    if 'mobilier' in data:
        for w in bad_words:
            data = re.sub(r'\b' + w + r'\b', '', data)
        # clean up extra spaces
        data = re.sub(r'\s+', ' ', data).strip()
        
    return pre + data + post

new_content = re.sub(r'(data-name=")([^"]*ufo[^"]*)(")', replacer, content, flags=re.IGNORECASE)

with open('projets/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

with open('studio/index.html', 'r', encoding='utf-8') as f:
    content2 = f.read()
new_content2 = re.sub(r'(data-name=")([^"]*ufo[^"]*)(")', replacer, content2, flags=re.IGNORECASE)
with open('studio/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content2)

print("UFO fixed.")
