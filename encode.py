from PIL import Image
import time 
import string 
im = Image.open(r'C:\Users\adush\Downloads\encoded.png')
pixelMap = im.load()

alphabet = string.ascii_uppercase
a = 0
word = input('What word do you want to hide? ').upper()
print(word)
time.sleep(3)
img = Image.new('RGBA', (1920, 1080))
pixelsNew = img.load()
pixelsNew[777, 777] = (len(word), 0, 0, 0)
for height in range(0, 1920//len(word), 50):
    for width, letter in zip(range(0, 1080, 50), word):

        try:
            if letter == ' ':
                pixelsNew[height, width] = (69, 100, 0, 255)
            else:
                pixelsNew[height, width] = (alphabet.index(letter), 100, 0, 255)
        except Exception as e:
            print(e)

        print('colored')        
        a +=1   

print('operation complete')
img.save(r'C:\Users\adush\Downloads\encoded.png')
