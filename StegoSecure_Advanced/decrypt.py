from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import cv2
import os
import base64
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

def decrypt_message_aes(encrypted_data, key1):
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    cipher_text = encrypted_data[32:]
    
    key = derive_key(key1, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded_message = decryptor.update(cipher_text) + decryptor.finalize()
    return decrypted_padded_message.rstrip().decode()

def extract_ciphertext_from_image(image_path, key2):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return None
    
    c = {i: chr(i) for i in range(255)}
    key2_shift = sum(ord(c) for c in key2) % 255  # Use key2 for shifting ASCII values
    
    n, m, z = 0, 0, 0
    message_length = img[n, m, z]
    m += 1
    
    extracted_data = ""
    for _ in range(message_length):
        extracted_data += c.get((img[n, m, z] - key2_shift) % 255, '?')  # Reverse key2-based shift
        n += 1
        m += 1
        z = (z + 1) % 3
    
    try:
        return base64.b64decode(extracted_data.encode())
    except Exception as e:
        print("Error decoding extracted data:", str(e))
        return None

# Example Usage
if __name__ == "__main__":
    image_path = input("Enter encrypted image path: ")
    key2 = getpass.getpass("Enter embedding key (Key 2) to extract ciphertext: ")
    
    encrypted_message = extract_ciphertext_from_image(image_path, key2)
    if encrypted_message:
        key1 = getpass.getpass("Enter decryption key (Key 1) to decrypt message: ")
        try:
            decrypted_message = decrypt_message_aes(encrypted_message, key1)
            print("Decrypted message:", decrypted_message)
        except Exception as e:
            print("Decryption failed! Incorrect Key 1 or corrupted data.", str(e))
