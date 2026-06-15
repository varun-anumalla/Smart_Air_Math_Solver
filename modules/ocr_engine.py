import easyocr


class OCREngine:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

    def read_equation(self, image_path):

        results = self.reader.readtext(
            image_path,
            detail=0,
            allowlist="0123456789+-*/="
        )

        text = "".join(results)

        return text.strip()