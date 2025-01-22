from PIL import Image
import pytesseract
import sys

# 📄 Path to the image file is now passed as a parameter
if len(sys.argv) != 2:
   print("Usage: python /workspaces/notepad/6.2_ocr.py <image_path>")
   sys.exit(1)

image_path = sys.argv[1]

# 🖼️ Open the image file
img = Image.open(image_path)

# 🔍 Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# 📝 Print the extracted text
print(text)
# 🎨 Create an ASCII art box around the captured text
def create_ascii_box(text):
   lines = text.split('\n')
   max_length = max(len(line) for line in lines)
   border = '🟦' * (max_length + 4)
   
   print(border)
   for line in lines:
      print(f'🟦 {line.ljust(max_length)} 🟦')
   print(border)

# 📦 Print the text in an ASCII art box
create_ascii_box(text)

# 🏃‍♂️ Run the script with: python /workspaces/notepad/6.2_ocr.py <image_path>