from PIL import Image, ImageFile
import os

# Allows Pillow to load truncated images if necessary
ImageFile.LOAD_TRUNCATED_IMAGES = True

def optimize_image_for_web(input_path, output_path, max_size=(1200, 1200), quality=80):
    """
    Optimizes an image for web delivery using native Pillow support for formats 
    like JPEG, WebP, and AVIF.
    """
    try:
        with Image.open(input_path) as img:
            
            # Convert to RGB if saving a transparency image (RGBA or P mode)
            # to a format that doesn't support transparency (JPEG, AVIF without alpha)
            if img.mode in ('RGBA', 'P') and output_path.lower().endswith(('.jpg', '.jpeg', '.avif')):
                 # Create a white background if needed, otherwise convert directly
                 if output_path.lower().endswith(('.jpg', '.jpeg')):
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
                    img = background
                 else:
                    # For AVIF, just convert to RGB if not supporting alpha
                    img = img.convert('RGB')
            elif img.mode == 'CMYK':
                 img = img.convert('RGB')
                 
            # Resize operation (maintains aspect ratio)
            if max_size:
                # LANCZOS is a high-quality resampling filter
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Determine format from output file extension and save
            output_format = output_path.split('.')[-1].upper()
            
            # Save the image with format-specific parameters
            # Use 'quality' for lossy formats (JPEG, WebP, AVIF)
            img.save(output_path, format=output_format, quality=quality, optimize=True)
            
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)

        print(f"Saved to {output_format} format.")
        print(f"Original size: {original_size / 1024:.2f} KB")
        print(f"Compressed size: {compressed_size / 1024:.2f} KB")
        print(f"Total size reduction: {(1 - compressed_size / original_size) * 100:.2f}%")

    except IOError as e:
        print(f"Error processing image: {e}")

# --- Example Usage (Assuming you have Pillow >= 11.3.0 installed) ---

# Convert a JPG to a high-quality WebP 
# optimize_image_for_web(
#     input_path='original_image.jpg',
#     output_path='optimized_image.webp', 
#     quality=80 
# )

# Convert to AVIF using built-in support
# optimize_image_for_web(
#     input_path='original_image.jpg',
#     output_path='optimized_image.avif', 
#     quality=75
# )

# Convert to a standard compressed JPEG
# optimize_image_for_web(
#     input_path='original_image.jpg',
#     output_path='optimized_image.jpg', 
#     quality=75
# )

# Convert a JPG to a high-quality WebP (recommended for web photos)
optimize_image_for_web(
    input_path="C:/Users/USUARIO/Desktop/Bon Appetit/FOTOS_LILIANA/ESCOGIDAS/IMG_4764.jpg",
    output_path="C:/Users/USUARIO/Desktop/Bon Appetit/Bon Appetit/Assets/img/postre_arequipe_mora.webp", 
    quality=85 
)