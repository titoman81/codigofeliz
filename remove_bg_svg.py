
from PIL import Image
import base64
import os

img_path = r"c:\Users\USUARIO\Desktop\codigo feliz\dgcom-1.0.0\img\logo.png"
svg_path = r"c:\Users\USUARIO\Desktop\codigo feliz\dgcom-1.0.0\img\logo.svg"

def remove_background(path):
    try:
        img = Image.open(path)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Change all white (also shades of whites)
            # Find all pixels that are very bright (white background)
            if item[0] > 220 and item[1] > 220 and item[2] > 220:  
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        
        img.putdata(newData)
        return img
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

if os.path.exists(img_path):
    print("Processing image...")
    img = remove_background(img_path)
    if img:
        # Save processed png temporarily to bytes
        from io import BytesIO
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="500" height="500" viewBox="0 0 500 500">
  <image width="100%" height="100%" xlink:href="data:image/png;base64,{img_str}"/>
</svg>'''
        
        with open(svg_path, "w") as svg_file:
            svg_file.write(svg_content)
        print("Background removed and saved to logo.svg")
    else:
        print("Failed to process image")
else:
    print("logo.png not found")
