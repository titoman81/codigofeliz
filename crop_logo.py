from PIL import Image
import os

# Open the logo image
img_path = 'public/img/logo_final.png'
img = Image.open(img_path)

print(f"Original size: {img.size}")
print(f"Mode: {img.mode}")

# Convert to RGBA if not already
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Get the bounding box of non-transparent/non-white pixels
# Get image data
pixels = img.load()
width, height = img.size

# Find the bounding box
min_x, min_y = width, height
max_x, max_y = 0, 0

for y in range(height):
    for x in range(width):
        pixel = pixels[x, y]
        # Check if pixel is not white or transparent
        # For RGBA: (R, G, B, A)
        if len(pixel) == 4:
            r, g, b, a = pixel
            # If pixel has some opacity and is not pure white
            if a > 10 and not (r > 240 and g > 240 and b > 240):
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
        else:
            r, g, b = pixel
            # If pixel is not pure white
            if not (r > 240 and g > 240 and b > 240):
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

# Add a small padding (5 pixels)
padding = 5
min_x = max(0, min_x - padding)
min_y = max(0, min_y - padding)
max_x = min(width, max_x + padding)
max_y = min(height, max_y + padding)

print(f"Bounding box: ({min_x}, {min_y}, {max_x}, {max_y})")

# Crop the image
if min_x < max_x and min_y < max_y:
    cropped = img.crop((min_x, min_y, max_x, max_y))
    print(f"Cropped size: {cropped.size}")
    
    # Save the cropped image
    output_path = 'public/img/logo_final_cropped.png'
    cropped.save(output_path, 'PNG')
    print(f"Saved cropped logo to: {output_path}")
    
    # Also create a backup of the original
    backup_path = 'public/img/logo_final_original.png'
    if not os.path.exists(backup_path):
        img.save(backup_path, 'PNG')
        print(f"Backup of original saved to: {backup_path}")
else:
    print("Could not find valid bounding box!")
