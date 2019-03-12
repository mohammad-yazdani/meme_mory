import tempfile

from PIL import Image


class IO:

    @staticmethod
    def open_image(binary: bytes, ext: str):
        with tempfile.TemporaryFile(mode="wb", suffix=ext) as temp_img:
            temp_img.write(binary)
            temp_img.close()

            img: Image.Image = Image.open("temp" + ext)
            img.show()
