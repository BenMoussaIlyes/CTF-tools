enc = open("/home/ilyes/Desktop/flag.png","r")
dec = open("/home/ilyes/Desktop/flag.solved.png","w")

for line in enc:
	for c in line :
		dec.write(chr(ord(c)^ord("s")))
enc.close()
dec.close()