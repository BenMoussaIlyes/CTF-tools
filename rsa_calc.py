def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m




n =11371476076141273124695927906515459259
	
e=7
p = 8476985936429195377
q = 1341452747641497067
c = 8226746732426060939102009545346192354

l = (p-1)*( q-1)


d = modinv(e, l)

try:
	print str( hex(pow(c, d, n) ) )[2:-1].decode("hex")
except:
	print  hex(pow(c, d, n) ) 