# CODIO SOLUTION BEGIN 
import requests
import os
import openai
import secret
import requests
openai.api_key=secret.api_key

def imageGen(prompts):
  response = openai.Image.create(
    prompt=prompts,
    n=1,
    size="256x256"
  )

  image_url = response['data'][0]['url']
  img_data = requests.get(image_url).content
  with open('my_image.jpg', 'wb') as handler:
    handler.write(img_data)
imageGen("a cool car on water")
# CODIO SOLUTION END