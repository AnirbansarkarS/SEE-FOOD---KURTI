from PIL import Image
import io

def load_image(image_bytes):
    """Load image from bytes for processing."""
    return Image.open(io.BytesIO(image_bytes))
