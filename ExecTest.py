import os
import importlib
from PIL import Image

# load the student's script
student_script = importlib.import_module('exerc')

def test_imageGen():
    # Run the student's function
    prompt = "a cool car on water"
    try:
        student_script.imageGen(prompt)

        # Check if the image file was created
        assert os.path.isfile('my_image.jpg'), "Image file 'my_image.jpg' was not created"

        # Check if the file is a valid image file
        try:
            img = Image.open('my_image.jpg')
            img.verify()
        except (IOError, SyntaxError) as e:
            print(f"File 'my_image.jpg' is not a valid image file: {e}")

        # Check if the image dimensions are as expected
        img = Image.open('my_image.jpg')
        assert img.size == (256, 256), f"Image size is {img.size}, but expected (256, 256)"

        print("Test passed!")
    except Exception as e:
        print(f"Test failed: {e}")

# Run the test function
test_imageGen()
