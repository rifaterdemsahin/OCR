# Run on desktop
## Run Commands to get the text
- cd /workspaces/notepad/6_Symbols/4_GetTextLocal
- python3 -m venv myenv
- C:\projects\OCR\6_Symbols\4_GetTextLocal\myenv\Scripts\Activate.ps1
- pip3 install Pillow torch torchvision tesseractocr
- install exe https://github.com/UB-Mannheim/tesseract/wiki
- python3 /workspaces/notepad/6_Symbols/2_GetText/tesseract-ocr.py ./image.png


---
## Run in VSCode
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