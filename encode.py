from PIL import Image
import time 
import string

alphabet = string.ascii_uppercase
a = 0
word = input('What word do you want to hide? ').upper()
print(word)

img = Image.new('RGBA', (1920, 1080))
pixelsNew = img.load()
pixelsNew[777, 777] = (len(word), 0, 0, 0)
for height in range(0, 1920, 10):
    for width, letter in zip(range(0, 1080, 10), word):

        try:
            if letter == ' ':
                pixelsNew[height, width] = (69, 0, 0, 0)
            else:
                try:
                    pixelsNew[height, width] = (alphabet.index(letter), 0, 0, 0)
                except:
                    pixelsNew[height, width] = (len(alphabet)+int(letter), 0, 0, 0)
        except Exception as e:
            print(e)

        print('colored')

print('operation complete')
img.save(r'encoded.png') # enter path to where you want to save the image
