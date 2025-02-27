import cv2
import os

def decrypt_image(image_path, correct_password, original_image_path="decryptedImage.png"):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found!")
        return

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    message_length = img[n, m, z]  # Retrieve message length from first pixel
    m += 1  # Move to actual message location

    extracted_message = ""
    entered_password = input("Enter the key for decryption: ")

    if entered_password == correct_password:
        for _ in range(message_length):
            extracted_message += c.get(img[n, m, z], '?')  # Extract character (default to '?' if missing)
            n += 1
            m += 1
            z = (z + 1) % 3  # Rotate through RGB channels
        
        print("Decrypted message:", extracted_message)

        # Open the original image after decryption
        if os.path.exists(original_image_path):
            os.system(f"start {original_image_path}")  # Windows command to open image
            print(f"Original image opened: {original_image_path}")
        else:
            print("Error: Original image not found!")

    else:
        print("Authentication failed!")

# Example Usage
image_path = "encryptedImage.png"  # Use PNG format
password = input("Enter the key used for encryption: ")
decrypt_image(image_path, password)