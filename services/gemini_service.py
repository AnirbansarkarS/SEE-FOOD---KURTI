import google.generativeai as genai
from PIL import Image
import io
from config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)

def identify_food(image_bytes):
    """Identify main food item from image using Gemini."""
    model = genai.GenerativeModel(GEMINI_MODEL)
    image = Image.open(io.BytesIO(image_bytes))

    prompt = (
        "Identify the exact food in this image. "
        "Return only the main food name in singular form, e.g., 'Cheese Margherita Pizza'."
        "Do not add extra description."
    )

    response = model.generate_content([prompt, image])
    return response.text.strip()
