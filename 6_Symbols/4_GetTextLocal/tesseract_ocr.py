import os
import sys
from PIL import Image
import pytesseract
import textwrap

def process_image(image_path):
    """Process image using Tesseract OCR"""
    try:
        # Set Tesseract path (modify this path according to your installation)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Open and process image
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

def create_ascii_box(text, width=50):
    """Create ASCII box around text"""
    wrapped_text = textwrap.fill(text, width=width)
    border = '📷 ' * (width // 2)
    print(border)
    print(wrapped_text)
    print(border)

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python ocr_easy.py ./image.png")
        return

    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    # Process image
    print("Processing image...")
    text = process_image(image_path)
    
    if text:
        # Display results
        print("\n----------- CAPTURED TEXT ----------")
        create_ascii_box(text)
        
        # Save option
        if input("\nSave to file? (y/n): ").lower().strip() == 'y':
            with open('extracted_text.txt', 'w', encoding='utf-8') as f:
                f.write(text)
            print("Saved to extracted_text.txt")

if __name__ == "__main__":
    main()