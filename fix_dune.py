import re

img1 = "Dune-poltrona-girevole.jpg"
img3 = "342.jpg"

def swap_images(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple trick: replace img1 with TEMP, img3 with img1, TEMP with img3
    content = content.replace(img1, "TEMP_IMG")
    content = content.replace(img3, img1)
    content = content.replace("TEMP_IMG", img3)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

swap_images('studio/fauteuil-dune.html')
swap_images('projets/index.html')
swap_images('studio/index.html')

print("Dune images swapped.")
