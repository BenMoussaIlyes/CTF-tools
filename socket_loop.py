
import socket
from  Crypto.Util.number import *
from binascii import hexlify,unhexlify
import hashlib

HOST = '34.245.90.212' 
PORT = 12347  
BUFFER_SIZE = 4096


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
count=0

data = s.recv(BUFFER_SIZE)
print count ,
print data
print data.split(" ")
f=open("../10mpwd.txt","r")

v = data.split(" ")[11]
for line in f:
	m = hashlib.sha256()
	m.update(line.strip("\n") )
	sol = m.hexdigest()
	#print ">" + sol 
	print sol[-6:] + " looking for "+ v
	if sol[-6:].strip("\n")== v.strip("\n"):
		print "found ittt"+sol
		s.send( sol.encode()+'\n')
		data = s.recv(BUFFER_SIZE)
		print data
		break

s.close()	    



