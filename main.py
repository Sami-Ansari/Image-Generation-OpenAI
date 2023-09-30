import openai 

# openai.api_key = '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'

import io
import openai
import requests
import PIL
from PIL import Image

def generate_image(text):
    # Generate the image using OpenAI's DALLE-Model 

    response = openai.Image.create(
        prompt = text,
        n=1,
        size = '512x512'
    )
       
       #Get the image URL from the response
    image_url = response.data[0]['url']
    
    #Download the image and convert it to a PIL image
    image_content = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_content))
    image.show()
    
prompt = input("Enter your prompt to generate the image: ")
generate_image(prompt)
