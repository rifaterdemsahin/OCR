from PIL import Image
import pytesseract

# Path to the image file
image_path = '/workspaces/notepad/4_imaginary_Source_image_test.png'

# Open the image file
img = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)

#  python /workspaces/notepad/6.2_ocr.py