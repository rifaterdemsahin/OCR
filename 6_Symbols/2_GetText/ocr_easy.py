from PIL import Image
import easyocr
import sys
import os

# 📄 Path to the image file is now passed as a parameter
if len(sys.argv) != 2:
   print("Usage: python /workspaces/notepad/6.2_ocr.py <image_path>")
   sys.exit(1)

image_path = sys.argv[1]

# 🖼️ Open the image file
img = Image.open(image_path)

# 🔍 Initialize the EasyOCR reader with the desired languages
reader = easyocr.Reader(['en'])

# 🔍 Use EasyOCR to read text from the image
result = reader.readtext(image_path, detail=0)

# Join the result into a single string
text = ' '.join(result)

# 🎨 Create an ASCII art box around the captured text
# Version 1: No line breaks
def create_ascii_box_no_line_breaks(text):
   text = text.replace('\n', ' ')
   max_length = len(text)
   border_length = min(max_length + 2, 50)
   bottom_border = '📷 ' * border_length
   
   print(f'  {text}')
   print(bottom_border)

# Version 2: With line breaks
def create_ascii_box_with_line_breaks(text):
   lines = text.split('\n')
   max_length = max(len(line) for line in lines)
   border_length = min(max_length + 2, 50)
   bottom_border = '📷 ' * border_length
   
   for line in lines:
      print(f'  {line}')
   print(bottom_border)

# 🧹 Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

print("----------- CAPTURED TEXT ---------- \n")
create_ascii_box_with_line_breaks(text)
print("-----------NOLINE BREAKS ---------- \n")
create_ascii_box_no_line_breaks(text)

# 🏃‍♂️ Run the script with: python ./ocr.py image.png
