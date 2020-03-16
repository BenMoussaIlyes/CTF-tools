from PIL import Image
import bitarray
import base64

message = "sp4rk{LSB_i5_Gre4T_t0_5ne4k_D4t4}c7f"
encoded_message = base64.b64encode(message)
ba = bitarray.bitarray()
ba.frombytes(encoded_message.encode('utf-8'))
bit_array = [int(i) for i in ba]
im1 = Image.open("../hacking.png")
im1.save("lsbencrypted.png")

im = Image.open("lsbencrypted.png")
width, height = im1.size
pixels = im1.load()
other_pixels = im.load()

i=0
for y in range(height):
   for x in range(width):

        r,g,b,a = pixels[x, y]
        new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel = r,g,b
        if i<len(bit_array):
	        #Red pixel
	        r_bit = bin(r)
	        r_last_bit = int(r_bit[-1])
	        r_new_last_bit = r_last_bit & bit_array[i]
	        new_bit_red_pixel = int(r_bit[:-1]+str(r_new_last_bit),2)
	        i += 1
        if i<len(bit_array):
	        #Green pixel
	        g_bit = bin(g)
	        g_last_bit = int(g_bit[-1])
	        g_new_last_bit = g_last_bit & bit_array[i]
	        new_bit_green_pixel = int(g_bit[:-1]+str(g_new_last_bit),2)
	        i += 1
        if i<len(bit_array):
	        b_bit = bin(b)
	        b_last_bit = int(b_bit[-1])
	        b_new_last_bit = b_last_bit & bit_array[i]
	        new_bit_blue_pixel = int(b_bit[:-1]+str(b_new_last_bit),2)
	        i += 1
        other_pixels[x,y] = (new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel)



