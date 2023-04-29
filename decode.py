from PIL import Image
import string 
im = Image.open(r'PATH TO ENCODED IMAGE')
pixelMap = im.load()
a = 0 
alphabet = string.ascii_uppercase

word = ''

img = Image.open(r'PATH TO ENCODED IMAGE')   # enter path to image here
pixelsNew = img.load()
number_of_chars = pixelMap[777, 777]
for height in range(0, 1920, 10):
    for width in range(0, 1080, 10):

        letter, g, b, a = pixelMap[height, width] 
        try:
            if letter == 69:
                word += ' '
            else:
                word += alphabet[letter]   
        except:
            print(word[:number_of_chars[0]])

print(f'DECODED MESSAGE: {word[:number_of_chars[0]]}')
