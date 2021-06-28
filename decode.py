from PIL import Image
import string 
im = Image.open(r'C:\Users\adush\Downloads\encoded.png')
pixelMap = im.load()
a = 0 
alphabet = string.ascii_uppercase

word = ''

img = Image.new(im.mode, im.size)
pixelsNew = img.load()

for height in range(0, img.size[0], 10):
    for width in range(0, img.size[1], 10):

        letter, g, b, a = pixelMap[height, width] 
        try:
            word += alphabet[letter]   
        except:
            print(word)

print(word)

print(f'{pixelMap[5, 5]} pixelz')

img.show()
#img.save(r'C:\Users\adush\Downloads\encoded.png')
