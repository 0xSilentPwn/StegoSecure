from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import cv2
import os
import base64
import shutil
import secrets
import getpass

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_message_aes(message, key1):
    salt = secrets.token_bytes(16)  # Generate random salt
    key = derive_key(key1, salt)
    iv = secrets.token_bytes(16)  # Generate random IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padded_message = message + ' ' * (16 - len(message) % 16)  # Pad message to 16 bytes
    encrypted_data = encryptor.update(padded_message.encode()) + encryptor.finalize()
    
    return salt + iv + encrypted_data  # Store salt and IV with encrypted data

def encrypt_ciphertext_in_image(image_path, encrypted_message, key2, output_path="encryptedImage.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    original_backup_path = "decryptedImage.png"  # Save the original image for later retrieval
    shutil.copy(image_path, original_backup_path)  # Make a copy before modification

    data = base64.b64encode(encrypted_message).decode()
    
    d = {chr(i): i for i in range(255)}
    key2_shift = sum(ord(c) for c in key2)

    n, m, z = 0, 0, 0
    img[n, m, z] = len(data)
    m += 1 

    for char in data:
        img[n, m, z] = (d.get(char, 32) + key2_shift) % 255  # Apply key2-based shift
        n += 1
        m += 1
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    print(f"Ciphertext embedded and saved as {output_path}")
    os.system(f"start {output_path}")

if __name__ == "__main__":    
 image_path = input("Enter image path: ")  # Use PNG format to avoid compression issues
 message = input("Enter secret message: ")
 key1 = getpass.getpass("Enter encryption key (Key 1): ")
 key2 = getpass.getpass("Enter embedding key (Key 2): ")

 encrypted_message = encrypt_message_aes(message, key1)
 print("Ciphertext before embedding:", base64.b64encode(encrypted_message).decode())
 encrypt_ciphertext_in_image(image_path, encrypted_message, key2)