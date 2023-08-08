When generating our prompt our code looks something like this:
``` python-hide-clipboard
response = openai.Image.create(
  prompt="a dog smoking a cigar in a poker room.",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
```
We have talked about the prompt and the size. The main thing we are calling and have not talked about yet is the `n`. You can request 1-10 images at a time using the n parameter. Try replacing `n` with 3.

{Try it!}(python3 imageGen.py 1)
[Click here to refresh your image](close_file image_name.jpg panel=1; open_file image_name.jpg panel=1) 

As you can see from the image file we saved in our response, we got only one image. Let's try adding a print statement to visualize what we are getting for the URL. 
```python 
image_url = response['data'][0]['url']
print(image_url)
```
{Try it!}(python3 imageGen.py 20)

Here we realize that we are going to only get one URL. We are going to change our code to view more of the response data.

```python
image_url = response['data']
print(image_url)
```

{Try it!}(python3 imageGen.py 21)

Here we can see we got 3 URLs generated. What we are going to do is pull the different URL into separate variables and generate files to save the URL. To make our life easier we should have the following:
```python
image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3  = response['data'][2]['url']
```
Please note you have have had `image_url = response['data'][0]['url']` from the following page,comment it out for now. If you want to check if the URLs look like what you have in mind, you can run the following code:
```python
print(image_url1[0:15])
print(image_url2[0:15])
print(image_url3[0:15])
```
{Try it!}(python3 imageGen.py 23)

We are slicing the content of our print statements here because we are generating URLs. The URLs tend to be in a longer format, because of that slicing might make the result more pleasing to the eye since we are just checking. 


{Check It!|assessment}(fill-in-the-blanks-712111423)
