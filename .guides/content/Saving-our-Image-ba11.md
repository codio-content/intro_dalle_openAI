### Image Generation
---
In order to not have to keep copying and pasting our result, we are going to save the image inside the URL as a file in our Codio box. 

The first thing we are going to do is import the `requests` library.The import requests statement is already included in the `imageGen.py` file. You do not need to add it yourself.

Using the request library we can get the image contents. We will use a handler to write in our new image file `image_name.jpg`. This code should go below all the code, we have already. At this point, we no longer need the print statement for the URL, delete it. 

```python

img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
```
{Try it!}(python3 imageGen.py 72)
[Click here to refresh your image](close_file image_name.jpg panel=1; open_file image_name.jpg panel=1) 

We will be rewriting our file. When regenerating an image we will need to click on our refresh button to see the changes. Try using the buttons below with a few different prompts.

If feeling uninspired, try the following prompts:
* digital art of a white cat ninja.
* acrylic painting of a mountain.
* a chef shark making shrimp. 
* digital art of white ninja cat with headband.

{Try it!}(python3 imageGen.py 19)
[Click here to refresh your image](close_file image_name.jpg panel=1; open_file image_name.jpg panel=1) 

The more descriptive you can be, the closer the image will get to what you are expecting. For example, Here is what it generated for me for that last input. 

![an Image with a cat with a black headband](image_name-copy.jpg)


Writing descriptive OpenAI DALL·E prompts helps the model to better understand the context of the task, allowing it to create more accurate and creative responses. In other words, the more precise the explanation, the greater the probability of achieving the desired outcome for you or your end user.


{Check It!|assessment}(multiple-choice-1434765826)
