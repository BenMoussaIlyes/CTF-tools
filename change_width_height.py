from PIL import Image

img = Image.open("out.jpg")
img2 = Image.new("RGB", (304,92))
for i in range(304):
	for j in range(92):
		img2.paste( img.crop( (92*i+j,0,92*i+j+1,1) ) , (i,j,(i+1),(j+1) ) )

img2.save("out2.jpg")