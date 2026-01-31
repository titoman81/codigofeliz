
import base64
import os

png_path = r"c:\Users\USUARIO\Desktop\codigo feliz\dgcom-1.0.0\img\logo.png"
svg_path = r"c:\Users\USUARIO\Desktop\codigo feliz\dgcom-1.0.0\img\logo.svg"

if os.path.exists(png_path):
    with open(png_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="500" height="500" viewBox="0 0 500 500">
  <image width="100%" height="100%" xlink:href="data:image/png;base64,{encoded_string}"/>
</svg>'''
    
    with open(svg_path, "w") as svg_file:
        svg_file.write(svg_content)
    print("Converted logo.png to logo.svg successfully.")
else:
    print("logo.png not found.")
