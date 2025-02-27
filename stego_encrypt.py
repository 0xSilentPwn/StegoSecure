import cv2
import os
import shutil  # To create a backup of the original image

def encrypt_image(image_path, message, password, output_path="encryptedImage.png"):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found!")
        return

    # Backup the original image before modifying it
    original_backup_path = "decryptedImage.png"  # Save the original image for later retrieval
    shutil.copy(image_path, original_backup_path)  # Make a copy before modification

    d = {chr(i): i for i in range(255)}

    # Store message length in the first pixel
    n, m, z = 0, 0, 0
    img[n, m, z] = len(message)
    m += 1  # Move to the next pixel for message storage

    # Store the message in pixels
    for char in message:
        img[n, m, z] = d.get(char, 32)  # Store ASCII values (default to space if not found)
        n += 1
        m += 1
        z = (z + 1) % 3  # Rotate through RGB channels

    cv2.imwrite(output_path, img)  # Save encrypted image
    print(f"Message encrypted and saved as {output_path}")
    os.system(f"start {output_path}")  # Opens encrypted image (Windows)

# Example Usage
image_path = "PIC.png"  # Use PNG format to avoid compression issues
message = input("Enter secret message: ")
password = input("Enter secret key: ")
encrypt_image(image_path, message, password)