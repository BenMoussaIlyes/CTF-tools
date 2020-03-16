f = open("data.dat" , "r" )
lines=0
for line in f :
	 if  line.count("0") % 3 == 0 or line.count("1") % 2 == 0 :
		print line
		lines+=1
print "number of lines : " + str(lines)
