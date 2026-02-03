#!/usr/bin/env python3
"""
Script to crop the center colored portion of an image, removing black borders.
"""
try:
    from PIL import Image
    import sys
    import os
    
    if len(sys.argv) < 3:
        print("Usage: python3 crop_image.py <input_image> <output_image>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Open image
    img = Image.open(input_path)
    width, height = img.size
    
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Find the bounding box of non-black content
    # Sample pixels to find where the colored content starts and ends
    pixels = img.load()
    
    # Find top border (first row with non-black content)
    top = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Check if pixel is not black (threshold: if any channel > 30)
            if r > 30 or g > 30 or b > 30:
                top = y
                break
        if top > 0:
            break
    
    # Find bottom border (last row with non-black content)
    bottom = height
    for y in range(height - 1, -1, -1):
        for x in range(width):
            r, g, b = pixels[x, y]
            if r > 30 or g > 30 or b > 30:
                bottom = y + 1
                break
        if bottom < height:
            break
    
    # Find left border
    left = 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if r > 30 or g > 30 or b > 30:
                left = x
                break
        if left > 0:
            break
    
    # Find right border
    right = width
    for x in range(width - 1, -1, -1):
        for y in range(height):
            r, g, b = pixels[x, y]
            if r > 30 or g > 30 or b > 30:
                right = x + 1
                break
        if right < width:
            break
    
    # Add small padding (5% of dimensions)
    padding_w = int((right - left) * 0.05)
    padding_h = int((bottom - top) * 0.05)
    
    left = max(0, left - padding_w)
    top = max(0, top - padding_h)
    right = min(width, right + padding_w)
    bottom = min(height, bottom + padding_h)
    
    # Crop the image
    cropped = img.crop((left, top, right, bottom))
    
    # Save the cropped image
    cropped.save(output_path, 'PNG')
    print(f"Cropped image saved to {output_path}")
    print(f"Original size: {width}x{height}")
    print(f"Cropped size: {right-left}x{bottom-top}")
    print(f"Crop box: ({left}, {top}, {right}, {bottom})")
    
except ImportError:
    print("PIL/Pillow not available. Trying alternative method...")
    # Fallback: use sips (macOS built-in)
    import subprocess
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python3 crop_image.py <input_image> <output_image>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Get image dimensions using sips
    result = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', input_path], 
                          capture_output=True, text=True)
    
    width = None
    height = None
    for line in result.stdout.split('\n'):
        if 'pixelWidth' in line:
            width = int(line.split(':')[1].strip())
        elif 'pixelHeight' in line:
            height = int(line.split(':')[1].strip())
    
    if width and height:
        # Estimate crop (remove 10% from each side as approximation)
        crop_x = int(width * 0.1)
        crop_y = int(height * 0.1)
        crop_w = int(width * 0.8)
        crop_h = int(height * 0.8)
        
        # Use sips to crop
        subprocess.run(['sips', '-c', str(crop_h), str(crop_w), '-x', str(crop_x), '-y', str(crop_y), 
                       input_path, '--out', output_path])
        print(f"Cropped image saved to {output_path} (approximate crop)")
    else:
        print("Could not determine image dimensions")
