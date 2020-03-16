s = "sp4rk{caesar_cipher_isnt_so_hard_after_all}c7f"
arr = "abcdefghijklmnopqrstuvwxyz"
cyper = "";
i=0
for c in s :
	if c.isalpha() :
	 cyper += arr[(arr.index(c)+3+i)%26]
	 i+=1
	else: cyper += c

print cyper
