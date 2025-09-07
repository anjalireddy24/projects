from PIL import Image
import stepic

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded_img = stepic.encode(img, message.encode())
    encoded_img.save(output_path)

def decode_message(image_path):
    img = Image.open(image_path)
    message = stepic.decode(img)
    return message.decode()