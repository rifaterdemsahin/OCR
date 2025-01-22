from PIL import Image
import pytesseract
import sys
import os

# 📄 Path to the image file is now passed as a parameter
if len(sys.argv) != 2:
   print("Usage: python /workspaces/notepad/6.2_ocr.py <image_path>")
   sys.exit(1)

image_path = sys.argv[1]

# 🖼️ Open the image file
img = Image.open(image_path)

# 🔍 Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# # 📝 Print the extracted text

# 🎨 Create an ASCII art box around the captured text
def create_ascii_box(text):
   text = text.replace('\n', ' ')
   max_length = len(text)
   border_length = min(max_length + 2, 50)
   top_border = '📷 ' * border_length
   bottom_border = '📷 ' * border_length
   
   print(top_border)
   print(f'  {text}')
   print(bottom_border)


# 🧹 Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

print("----------- CAPTURED TEXT ---------- \n")

# 📦 Print the text in an ASCII art box
create_ascii_box(text)

# 🏃‍♂️ Run the script with: python ./ocr.py image.png