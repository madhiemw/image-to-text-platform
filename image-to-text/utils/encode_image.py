import base64
from PIL import Image
import io

def encode_image_to_base64(image):
    """Convert image to base64 string"""
    if isinstance(image, str):
        with open(image, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    else:
        buffered = io.BytesIO()
        Image.fromarray(image).save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')