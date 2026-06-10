import re
import os

keyword_map = {
    "vêtement": ["vetement", "vêtements", "vetements", "pull", "veste", "chemise", "mode", "habit", "habillement", "t-shirt"],
    "montre": ["montres", "horlogerie", "bracelet", "watch", "bijoux", "montre"],
    "lunette": ["lunettes", "lunetterie", "lunettes de soleil", "verres", "lunette", "monture", "montures"],
    "chaussure": ["chaussures", "basket", "baskets", "sneakers", "soulier", "chaussure"],
    "véhicule": ["vehicule", "voiture", "auto", "automobile", "moto", "train", "tramway", "metro", "vélo", "velo", "bicyclette", "transport", "véhicule"],
    "sac": ["sacs", "bagage", "bagagerie", "sacoche", "valise", "sac"],
    "meuble": ["meubles", "mobilier", "ameublement", "chaise", "fauteuil", "canapé", "table", "tabouret", "lit", "bureau", "rangement", "étagère", "meuble"],
    "cuisine": ["cuisiner", "ustensile", "ustensiles", "poêle", "poele", "casserole", "faitout", "électroménager", "four", "frigo", "réfrigérateur", "cuisine", "sauteuse"],
    "parfum": ["parfumerie", "cosmétique", "cosmetique", "beauté", "beaute", "flacon", "fragrance", "parfum"],
    "bouteille": ["boisson", "eau", "bouteilles", "packaging", "emballage", "heineken", "ogo", "cristaline", "vittel", "bière", "bouteille"],
    "téléphone": ["telephone", "smartphone", "mobile", "coque", "housse", "téléphone"],
    "ordinateur": ["pc", "mac", "informatique", "ordinateur", "laptop", "clavier", "souris"],
    "briquet": ["briquets", "briquet"],
    "stylo": ["stylos", "stylo", "plume", "bic"],
}

triggers = {
    "vêtement": ["bompard", "modulor", "vêtement", "vetement", "t-shirt"],
    "montre": ["patrimony", "swatch", "bijouterie", "montre"],
    "lunette": ["lightec", "optique", "solaire", "vision", "lunette", "morel"],
    "chaussure": ["nike", "nikeames", "chaussure", "sneaker"],
    "véhicule": ["r17", "renault", "transport", "vélo", "bike", "angell", "metro", "tramway", "voiture", "auto", "citroen", "toyota", "evo mobil", "ufo"],
    "sac": ["bag", "back up", "sac", "lancaster", "bagage"],
    "meuble": ["mobilier", "chaise", "fauteuil", "canapé", "table", "tabouret", "meuble", "roche bobois", "cassina", "vondom", "steiner", "dunlopillo"],
    "cuisine": ["cuisine", "poêle", "casserole", "faitout", "gorenje", "scavolini", "aubecq", "guzzini", "sauteuse"],
    "parfum": ["cosmétique", "parfum", "pucci", "guerlain", "flacon", "okaïdi", "adidas", "idylle", "beauté"],
    "bouteille": ["heineken", "ogo", "packaging", "bouteille", "cristaline", "vittel", "bière", "eau", "boisson"],
    "téléphone": ["smartphone", "sagem", "téléphone", "mobile", "ïta"],
    "ordinateur": ["hack-mac", "ordinateur", "pc", "clavier", "souris"],
    "briquet": ["briquet", "atomique"],
    "stylo": ["stylo", "plume", "bic"],
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if 'data-name="' in line:
            text_to_check = line.lower()
            added_keywords = set()
            for cat, trigs in triggers.items():
                if any(trig in text_to_check for trig in trigs):
                    added_keywords.add(cat)
                    for kw in keyword_map[cat]:
                        added_keywords.add(kw)
                        
            if added_keywords:
                match = re.search(r'data-name="([^"]*)"', line)
                if match:
                    existing_data = match.group(1)
                    words = existing_data.split()
                    existing_set = set(words)
                    
                    new_words = []
                    for kw in added_keywords:
                        if kw not in existing_set:
                            new_words.append(kw)
                            existing_set.add(kw)
                    
                    if new_words:
                        new_data = existing_data + " " + " ".join(new_words)
                        lines[i] = line.replace(f'data-name="{existing_data}"', f'data-name="{new_data}"')
                        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

print("Processing files...")
process_file('projets/index.html')
process_file('studio/index.html')
print("Done.")
