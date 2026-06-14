from modules.ocr_engine import OCREngine
import glob
import os

ocr = OCREngine()

files = glob.glob(
    "saved_drawings/*_canvas.png"
)

latest_file = max(
    files,
    key=os.path.getctime
)

print("Reading:", latest_file)

result = ocr.read_equation(
    latest_file
)

print("Detected Text:")
print(repr(result))