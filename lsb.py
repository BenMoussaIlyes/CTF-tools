from PIL import Image
i = Image.open("lsbencrypted.png")

pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size

all_pixels = []
for y in range(height):
   for x in range(width):

        cpixel = pixels[x, y]
        all_pixels.append(cpixel)
one=0b0000001
text =""
#print str(all_pixels[1][2] & 1 )
for i in range (0,len(all_pixels)):
	
	text+= str(all_pixels[i][0] & 1) 
	text+= str(all_pixels[i][1] & 1)
	text+= str(all_pixels[i][2] & 1) 

print (hex(int(text, 2))[2:-1]).decode("hex")

