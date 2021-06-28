from PIL import Image
import string 
im = Image.open(r'C:\Users\adush\Downloads\encoded.png')
pixelMap = im.load()

alphabet = string.ascii_uppercase
a = 0
word = 'YOURMOTHER'
img = Image.new(im.mode, im.size)
pixelsNew = img.load()

for height in range(0, img.size[0], 10):
#    for width, letter in zip(range(0, img.size[1], 10), word):
    for width, letter in zip(range(0, img.size[1], 10), word):

        pixelsNew[height, width] = (alphabet.index(letter), 100, 0, 255)
        print('colored')        
        a +=1   
        
print('operation complete')
img.save(r'C:\Users\adush\Downloads\encoded.png')
