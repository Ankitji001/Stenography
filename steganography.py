from PIL import Image
import numpy as np

# Convert text to binary
def text_to_bin(message):
    return ''.join([format(ord(char), '08b') for char in message])

# Embed data in image using LSB
def encode(image_path, secret_text, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    np_img = np.array(img)

    bin_msg = text_to_bin(secret_text) + '1111111111111110'  # Delimiter
    data_index = 0
    msg_len = len(bin_msg)

    for row in np_img:
        for pixel in row:
            for i in range(3):  # R, G, B
                if data_index < msg_len:
                    pixel[i] = (pixel[i] & ~1) | int(bin_msg[data_index])
                    data_index += 1

    encoded_img = Image.fromarray(np_img)
    encoded_img.save(output_path)
    print("✅ Message embedded successfully!")

# Extract data from image
def decode(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    np_img = np.array(img)

    bin_data = ''
    for row in np_img:
        for pixel in row:
            for i in range(3):  # R, G, B
                bin_data += str(pixel[i] & 1)

    # Split at delimiter
    all_bytes = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
    decoded_text = ''
    for byte in all_bytes:
        if byte == '11111110':  # Stop at delimiter
            break
        decoded_text += chr(int(byte, 2))
    print("🔓 Hidden message:", decoded_text)

# Example usage
if __name__ == "__main__":
    # Encode message
    encode("input_image.png", "Secret Message: AI & Cybersecurity 🔒", "output_encoded.png")

    # Decode message
    decode("output_encoded.png")
