from PIL import Image
import time 
import string 
im = Image.open(r'PATH TO ANY IMAGE')
pixelMap = im.load()

alphabet = string.ascii_uppercase
a = 0
word = input('What word do you want to hide? ').replace(' ', '').upper()
print(word)
time.sleep(3)
img = Image.new(im.mode, im.size)
pixelsNew = img.load()

for height in range(0, img.size[0], 10):
    for width, letter in zip(range(0, img.size[1], 10), word):

        try:
            pixelsNew[height, width] = (alphabet.index(letter), 100, 0, 255)
        except Exception as e:
            print(e)

        print('colored')        
        a +=1   
        
print('operation complete')
img.save(r'PATH TO THE SAME IMAGE AT "IM" VARIABLE')
