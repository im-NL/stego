from PIL import Image
import string 
im = Image.open(r'C:\Users\adush\Downloads\encoded.png')
pixelMap = im.load()
a = 0 
alphabet = string.ascii_uppercase

word = ''

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
number_of_chars = pixelMap[777, 777]
for height in range(0, 1920, 50):
    for width in range(0, 1080, 50):

        letter, g, b, a = pixelMap[height, width] 
        try:
            if letter == 69:
                word += ' '
            else:
                word += alphabet[letter]   
        except:
            print(word)

print(word[:number_of_chars[0]])