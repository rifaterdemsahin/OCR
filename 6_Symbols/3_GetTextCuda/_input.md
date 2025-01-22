# Run Commands to get the text
- cd /workspaces/notepad/6_Symbols/3_GetTextCuda
- python3 -m venv myenv
- source myenv/bin/activate
- pip3 install Pillow torch torchvision easyocr
- python3 /workspaces/notepad/6_Symbols/2_GetText/ocr_easy.py ./image.png
