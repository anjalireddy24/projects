def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def embed_binary_in_image(image_path, message, output_path):
    from PIL import Image
    binary = text_to_binary(message) + '1111111111111110'  # EOF marker
    img = Image.open(image_path)
    pixels = img.load()
    idx = 0

    for y in range(img.height):
        for x in range(img.width):
            if idx < len(binary):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary[idx])  # Replace LSB
                pixels[x, y] = (r, g, b)
                idx += 1
    img.save(output_path)