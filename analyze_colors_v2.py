
from PIL import Image
from collections import Counter
import os

def get_dominant_colors(image_path, num_colors=3):
    try:
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            return []
            
        image = Image.open(image_path)
        image = image.convert('RGB')
        # Focus on the center where the logo usually is to avoid screenshots borders
        width, height = image.size
        # crop center 50%
        left = width * 0.25
        top = height * 0.25
        right = width * 0.75
        bottom = height * 0.75
        image = image.crop((left, top, right, bottom))
        
        image = image.resize((100, 100))
        pixels = list(image.getdata())
        counts = Counter(pixels)
        common = counts.most_common(10)
        
        dominant = []
        for color, count in common:
            # Filter out whites/blacks/greys
            r, g, b = color
            if r > 240 and g > 240 and b > 240: continue # White
            if r < 20 and g < 20 and b < 20: continue # Black
            if abs(r-g) < 20 and abs(g-b) < 20: continue # Grey
            
            dominant.append(color)
            if len(dominant) >= num_colors:
                break
        
        return dominant
    except Exception as e:
        print(f"Error: {e}")
        return []

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

img_path = r"C:\Users\USUARIO\.gemini\antigravity\brain\49ede825-e4a1-4798-becc-0c12b05460aa\uploaded_media_1769794055525.jpg"
print(f"Analyzing {img_path}...")
colors = get_dominant_colors(img_path)

print("Dominant Colors Found:")
for c in colors:
    print(rgb_to_hex(c))
