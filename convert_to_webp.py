from PIL import Image
import os
import glob

# Get all PNG files in seq2 folder
png_files = sorted(glob.glob("seq2/*.png"))

print(f"Found {len(png_files)} PNG files to convert")

for png_path in png_files:
    # Create webp filename
    webp_path = png_path.replace(".png", ".webp")
    
    # Open and convert
    with Image.open(png_path) as img:
        # Convert to RGB if necessary (WebP doesn't support RGBA with transparency in same way)
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Save as WebP with good quality
        img.save(webp_path, 'WEBP', quality=85, method=6)
    
    # Delete original PNG
    os.remove(png_path)
    
    print(f"Converted: {os.path.basename(png_path)} -> {os.path.basename(webp_path)}")

print("\nConversion complete! All PNG files replaced with WebP.")
