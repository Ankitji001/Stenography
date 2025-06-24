# Stenography
Steganography - Hiding Information in Images This project demonstrates how to hide secret information inside digital images using a simple and effective Least Significant Bit (LSB) steganography technique. It was developed as part of the Cyber Security Internship by Edunet Foundation in collaboration with IBM SkillsBuild.

📦 steganography-project/
 ┣ 📜 steganography.py         ← Core script to encode and decode messages
 ┣ 🖼️ input_image.png          ← Original image to hide message
 ┣ 🖼️ output_encoded.png       ← Image with embedded secret message
 ┗ 📄 README.md                ← Project documentation

 📌 Features
🔐 Hide text messages inside images (PNG)

🔍 Retrieve and decode hidden messages from images

🧠 Uses Least Significant Bit (LSB) technique

🛠️ Implemented using Python and Pillow

🔍 How It Works
This project uses the Least Significant Bit (LSB) of each pixel in an image to embed binary bits of the secret message. Here’s how:

Every character is converted to 8-bit binary.

These bits replace the least significant bits of RGB values in the image.

A special delimiter (1111111111111110) signals the end of the message.

On decoding, bits are extracted and converted back to characters.

🎯 Learning Outcomes
Understand image steganography and its applications in cybersecurity.

Perform basic image processing and manipulation.

Gain practical knowledge in data security and encryption concepts.

Implement a working Python project to hide/reveal secret information in images.

💡 Future Improvements
Add support for file/data hiding (not just text).

Encrypt the message before embedding for extra security.

Create a GUI for ease of use.

Expand support to audio or video steganography.

