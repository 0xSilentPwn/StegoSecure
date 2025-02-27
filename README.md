# Secure Data Hiding in Images Using Steganography (CLI-Based)

## 🔐 Introduction
This project provides a CLI-based steganography tool that allows users to hide secret messages inside images securely. 
The tool includes both encryption (hiding messages) and decryption (extracting messages) functionalities. 
It ensures message security by storing data within pixel values and requiring a password for decryption.

## Features
- 🔹 Hide a secret message inside an image using pixel modifications.
- 🔹 Retrieve the hidden message with password-based authentication.
- 🔹 Supports lossless PNG images to prevent data loss.
- 🔹 Keeps a backup of the original image for later retrieval.
- 🔹 Command-line interface (CLI) for easy execution.

## 📂 Project Structure

- ├── stego_encrypt.py      # Encrypting messages into images
- ├── stego_decrypt.py      # Decrypting hidden messages from images
- ├── PIC.png               # Sample input image
- ├── encryptedImage.png    # Output image after encryption
- ├── decryptedImage.png    # Backup of the original image
- ├── README.md             # Documentation file

## 📌 Installation
1️⃣ Clone the Repository
#### git clone https://github.com/0xSilentPwn/StegoSecure.git
#### cd StegoSecure

2️⃣ Install Required Dependencies
#### pip install -r requirements.txt

## Usage
🔒 Encrypting a Message into an Image  

To hide a secret message inside an image, run:  

`python stego_encrypt.py`  

Input Prompts:  
Enter the secret message to hide.  
Provide a password for encryption.

A new image (encryptedImage.png) containing the hidden message.
A backup of the original image (decryptedImage.png) is saved.

🔓Decrypting a Message from an Image

To extract a hidden message from an encrypted image, run:

`python stego_decrypt.py`

Input Prompts:  
Enter the encryption password.  
Output:

The decrypted message will be displayed in the terminal.
The original image (decryptedImage.png) will be opened if available.

## 📜 Notes
Use PNG images to prevent data loss due to compression.
Ensure the correct password is provided during decryption.
If the message extraction fails, verify that the correct encrypted image and password are used.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributors
- [0xSilentPwn](https://github.com/0xSilentPwn)
