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
print(PrimeFactor(int(input()))) 
