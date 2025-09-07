from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def embed_text(image_path, output_path, message):
    # Ensure image is in RGBA mode for consistent pixel structure
    img = Image.open(image_path).convert("RGBA")
    binary = text_to_binary(message) + '1111111111111110'  # EOF marker
    pixels = img.load()
    idx = 0

    for y in range(img.height):
        for x in range(img.width):
            if idx < len(binary):
                r, g, b, a = pixels[x, y]
                r = (r & ~1) | int(binary[idx])  # Embed bit in red channel
                pixels[x, y] = (r, g, b, a)
                idx += 1
            else:
                img.save(output_path)
                return True
    return False  # Message too long for image

def extract_text(image_path):
    # Ensure image is in RGBA mode for consistent pixel structure
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()
    binary = ''

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            binary += str(r & 1)
            if binary.endswith('1111111111111110'):
                return binary_to_text(binary[:-16])
    return ''  # EOF marker not found