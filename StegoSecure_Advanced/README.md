# StegoSecure Advanced - Cryptography Edition

## 🔐 About This Version
This is an **enhanced version** of StegoSecure that integrates **AES encryption** before embedding messages into images. Unlike the previous version, this edition ensures **double-layer security** by using:

1. **Key 1 (AES Encryption)** - Encrypts the message using AES before hiding it.
2. **Key 2 (Steganography)** - Embeds the AES-encrypted message inside an image.

During decryption, both keys are required:
- **Key 2** extracts the hidden encrypted text from the image.
- **Key 1** decrypts the extracted ciphertext back into plaintext.

## 📂 Project Structure
```
StegoSecure/
│── (Previous version files)
│
│── StegoSecure_Advanced/
│   ├── stego_encrypt.py  # Encrypts and hides data
│   ├── stego_decrypt.py  # Extracts and decrypts data
```

## 🚀 How to Use
### **Encryption**
```bash
python stego_encrypt.py
```
- Enter an **image path**.
- Provide a **message** to hide.
- Set **Key 1** (for AES encryption).
- Set **Key 2** (for embedding into the image).

### **Decryption**
```bash
python stego_decrypt.py
```
- Enter the **image path** of the encrypted image.
- Enter **Key 2** to extract the ciphertext.
- Enter **Key 1** to decrypt the message.

## 🔑 Security Features
✅ **AES Encryption (CBC Mode)** for strong encryption.

✅ **Dual Key System** for extra security.

✅ **Steganography** to hide the encrypted message in images.

## License
This project is licensed under the [MIT License](LICENSE).

## 🛠 Future Enhancements
- Add **file encryption support** (e.g., PDFs, EXEs).
- Implement **GUI-based encryption & decryption**.

### 🎯 Developed By: *SlientPwn*