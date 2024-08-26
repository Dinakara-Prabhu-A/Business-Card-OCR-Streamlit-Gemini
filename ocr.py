import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

def get_gemini_response(image):
    condition = """
    Please analyze the image and extract the following information into a dictionary format:

    • Company Name
    • Name
    • Designation
    • Mobile Number
    • Email Address
    • Website URL
    • Area
    • City
    • State
    • Pin Code

    If any field contains multiple values (such as multiple phone numbers or emails), store these values as a list. If certain data is missing or not present in the image, store it as `null` for that key.
    """
    
    
    # Pass the image to the model and generate the content
    model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})
    response = model.generate_content([condition, image])
    return response.text