import base64
from io import BytesIO
from PIL import Image

def image_to_base64(image: Image.Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def base64_to_image(base64_str: str) -> Image.Image:
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data))
    return img
