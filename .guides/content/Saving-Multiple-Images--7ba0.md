Now that we can get the URL for the 3 images we are going to save them in different files. The button below after the Try It! button are setups to open the following file names:
* image_name1.jpg
* image_name2.jpg
* image_name3.jpg

Now remember the technique we previously used to save our image. We are going to use that to save the 3 images.
```python
img_data = requests.get(image_url1).content
with open('image_name1.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(image_url2).content
with open('image_name2.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(image_url3).content
with open('image_name3.jpg', 'wb') as handler:
    handler.write(img_data)
```


{Try it!}(python3 imageGen.py 190)
[Click here to get image 1](close_file image_name1.jpg panel=1; open_file image_name1.jpg panel=1) 
[Click here to get  image 2](close_file image_name1.jpg panel=1; open_file image_name2.jpg panel=1) 
[Click here to get image 3](close_file image_name2.jpg panel=1; open_file image_name3.jpg panel=1) 

If you click on every single link and you get a different image then you are on the right track. Since we are using Python let's start by cleaning up our code a bit. 

For starters in order to better see the change that our code worked we are going to switch the prompt from  ninja cat to ninja birds. 
```python
prompt="digital art of ninja bird "
```
Then remove everything after from when we mention `img_data = requests.get(image_url1).content`. 

Now that we have standard style to name our images it makes it easy for us to use Python function like `enumerate` to loop through and create our files. All we have to do is simply change the values from 1 to 2 to 3. 
```python
for i, image_url in enumerate([image_url1, image_url2, image_url3], start=1):
    img_data = requests.get(image_url).content
    with open(f'image_name{i}.jpg', 'wb') as handler:
        handler.write(img_data)
```

{Try it!}(python3 imageGen.py 2)
[Click here to get image 1](close_file image_name1.jpg panel=1; open_file image_name1.jpg panel=1) 
[Click here to get  image 2](close_file image_name1.jpg panel=1; open_file image_name2.jpg panel=1) 
[Click here to get image 3](close_file image_name2.jpg panel=1; open_file image_name3.jpg panel=1)

Just like that you cut more than half the lines of code you needed to store the different files. Using this code it should be pretty easy to replicate and save more than 3 pictures. Remember that `n` has a max value of 10. *Please Note:*  For free accounts the maximum rate is 5 pictures per minute.
|||guidance 
The following is the sample code that should work for the last page 
```python
import os
import openai
import secret
import requests
openai.api_key=secret.api_key

response = openai.Image.create(
  prompt="digital art of ninja bird ",
  n=3,
  size="256x256"
)

image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3  = response['data'][2]['url']

for i, image_url in enumerate([image_url1, image_url2, image_url3], start=1):
    img_data = requests.get(image_url).content
    with open(f'image_name{i}.jpg', 'wb') as handler:
        handler.write(img_data)
```
|||

{Check It!|assessment}(multiple-choice-2467313690)
