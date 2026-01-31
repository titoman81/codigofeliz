
from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=3):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        # Resize for speed
        image = image.resize((150, 150))
        pixels = list(image.getdata())
        counts = Counter(pixels)
        # Sort by count
        common = counts.most_common(num_colors + 5) # Get a few more to skip white/black
        
        dominant = []
        for color, count in common:
            # Filter out near-white and near-black (backgrounds/text)
            if sum(color) > 700: # Too white
                continue
            if sum(color) < 50: # Too black
                continue
            dominant.append(color)
            if len(dominant) >= num_colors:
                break
        
        return dominant
    except Exception as e:
        print(f"Error: {e}")
        return []

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Path to the LOGO (not the screenshot, or the screenshot if that's all we have)
# Using the screenshot path since the cropped logo might not exist yet or I want source colors
img_path = r"C:\Users\USUARIO\.gemini\antigravity\brain\49ede825-e4a1-4798-becc-0c12b05460aa\uploaded_media_1769794055525.jpg"
colors = get_dominant_colors(img_path)

print("Dominant Colors Found:")
for c in colors:
    print(rgb_to_hex(c))
