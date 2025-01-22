# Run Commands to get the text
- cd /workspaces/notepad/6_Symbols/2_GetText
- Capture image into the clipboard and delete the existing one
- pip install -r requirements.txt
- python ./ocr.py image.png



- python3 -m venv myenv
- source myenv/bin/activate
- pip3 install Pillow torch torchvision easyocr
- python3 /workspaces/notepad/6_Symbols/2_GetText/ocr_easy.py ./image.png



Extension VSCODE on Local
🌐 [Windmillcode Paste Text From Image](https://marketplace.visualstudio.com/items?itemName=windmillcode-publisher-0.windmillcode-paste-text-from-image)

💖 Sponsor | 💸 Donate

# 🖼️ Windmillcode Paste Text From Image

## 🎥 Demo GIF

## 📄 Overview
Do you often find yourself needing to extract text from images, screenshots, or other visual content while working on your projects? The "Windmillcode Paste Text From Image" extension is designed to make this process seamless and efficient by allowing you to extract and paste text from images directly into your VSCode editor.

## 🛠️ Usage
1. **Copy an image to your clipboard:**
    - Take a screenshot or copy an image from any source.
2. **Paste the image as text in VSCode:**
    - Right-click in your editor where you want to paste the text.
    - Select `Windmillcode: Paste Image as Text` from the context menu.
    - The extension will extract the text from the image using Tesseract.js and insert it into your active editor at the current cursor position.