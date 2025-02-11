import os
import sys
from PIL import Image
import easyocr
import textwrap

# Check if the image path is provided
if len(sys.argv) != 2:
    print("Usage: python ocr_easy.py ./image.png")
    sys.exit(1)

# 📄 Path to the image file is passed as a parameter
image_path = sys.argv[1]

# 🧹 Ensure the file exists
if not os.path.isfile(image_path):
    print(f"Error: File '{image_path}' not found.")
    sys.exit(1)

# 🖼️ Open the image file
img = Image.open(image_path)

# 🔍 Initialize the EasyOCR reader (force CPU-only mode)
reader = easyocr.Reader(['en'], gpu=False)

# 🔍 Use EasyOCR to read text from the image
result = reader.readtext(image_path, detail=0)

# Join the result into a single string
text = ' '.join(result)

# Function to create an ASCII box with text wrapping
def create_ascii_box(text, width=50):
    wrapped_text = textwrap.fill(text, width=width)
    border = '📷 ' * (width // 2)
    
    print(border)
    print(wrapped_text)
    print(border)

# Clear the terminal (platform-independent)
def clear_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

# 🧹 Clear the terminal before starting the process
clear_terminal()

# 📄 Display extracted text with ASCII box
print("----------- CAPTURED TEXT ---------- \n")
create_ascii_box(text)

# Optionally, save the extracted text to a file
save_to_file = input("Do you want to save the extracted text to a file? (y/n): ").strip().lower()
if save_to_file == 'y':
    output_path = 'extracted_text.txt'
    with open(output_path, 'w') as f:
        f.write(text)
    print(f"Text saved to {output_path}")

# 🏃‍♂️ Run the script with: python ocr_easy.py image.png
