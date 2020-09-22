from Crypto.PublicKey import RSA


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
def PrimeFactor(n):
    m = n
    while n%2==0:
        n = n//2
    if n == 1:         # check if only 2 is largest Prime Factor 
        return 2
    i = 3
    sqrt = int(m**(0.5))  # loop till square root of number
    last = 0              # to store last prime Factor i.e. Largest Prime Factor
    while i <= sqrt :
        while n%i == 0:   
            n = n//i       # reduce the number by dividing it by it's Prime Factor
            last = i
        i+=2
    if n> last:            # the remaining number(n) is also Factor of number 
        return n
    else:
        return last
exit(0)
f = open("/home/satan/Downloads/public.pem", "r")
key = RSA.importKey(f.read())
n= key.n #displays n
e= key.e #displays e

p = PrimeFactor(n)
q = n/p
c = 8226746732426060939102009545346192354

l = (p-1)*( q-1)


d = modinv(e, l)

try:
    print (str( hex(pow(c, d, n) ) )[2:-1].decode("hex"))
except:
    print ( hex(pow(c, d, n) ) )
