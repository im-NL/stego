from PIL import Image
import string 
im = Image.open('encoded.png') # enter path to encoded file 
pixelMap = im.load()
a = 0 
alphabet = string.ascii_uppercase

word = ''

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
number_of_chars = pixelMap[777, 777]
for height in range(0, 1920, 10):
    for width in range(0, 1080, 10):

        letter, g, b, a = pixelMap[height, width] 
        try:
            if letter == 69:
                word += ' '
            else:
                try:
                    word += alphabet[letter]   
                except:
                    word += str(int(letter) - len(alphabet))
        except:
            print(word)

print(f'DECODED MESSAGE: {word[:number_of_chars[0]].lower()}')
