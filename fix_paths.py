import os
import re

def update_html_paths():
    root_dir = r'c:\Users\USUARIO\Desktop\codigo feliz\dgcom-1.0.0'
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    
    # Patterns to catch img/, lib/, js/, css/ in src and href
    # We want to catch things like src="img/..." or href="css/..."
    # and turn them into src="/img/..." or href="/css/..."
    patterns = [
        (r'(src|href)="((?!http|https|/|#)[^"]*?(?:img|lib|js|css)/)', r'\1="/\2'),
        # Simplified version if the above is too strict:
        (r'src="(?!(http|https|/))', 'src="/'),
        (r'href="(?!(http|https|/|#|mailto:|tel:))', 'href="/')
    ]

    for filename in html_files:
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update paths
        # Let's be precise: only prefix img, lib, js, css
        for folder in ['img', 'lib', 'js', 'css']:
            content = content.replace(f'src="{folder}/', f'src="/{folder}/')
            content = content.replace(f'href="{folder}/', f'href="/{folder}/')

        # Fix lang in Spanish files (those not containing -en)
        if '-en.html' not in filename:
            content = content.replace('<html lang="en">', '<html lang="es">')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    update_html_paths()
