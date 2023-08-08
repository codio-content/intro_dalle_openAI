import os
import openai
import secret
import requests
openai.api_key=secret.api_key

# CODIO SOLUTION BEGIN 
response = openai.Image.create(
  prompt="3d rendering  of a mage",
  n=1,
  size="256x256"
)

image_url = response['data'][0]['url']
print(image_url)
import requests

img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
# CODIO SOLUTION END 