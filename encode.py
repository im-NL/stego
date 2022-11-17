from PIL import Image
import time 
import string

alphabet = string.ascii_uppercase
a = 0
word = input('What word do you want to hide? ').upper()
print(word)
# time.sleep(3)
img = Image.open(r'C:\Users\adush\Downloads\decoder.png')
pixelsNew = img.load()
pixelsNew[777, 777] = (len(word), 0, 0, 0)
for height in range(0, 1920, 10):
    for width, letter in zip(range(0, 1080, 10), word):

        try:
            if letter == ' ':
                pixelsNew[height, width] = (69, 0, 0, 0)
            else:
                pixelsNew[height, width] = (alphabet.index(letter), 0, 0, 0)
        except Exception as e:
            print(e)

        print('colored')

print('operation complete')
img.save(r'C:\Users\adush\Downloads\encoded.png')
