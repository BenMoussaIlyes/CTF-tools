cipher="sp4rk{0TP_i5_b4sica11y_ju5t_f4ncy_x0r}c7f"


import base64
def strxor (s0, s1):
	  l = [ chr ( ord (a) ^ ord (b) ) for a,b in zip (s0, s1) ]
	  return ''.join (l)

msg_enc=cipher

msg_key= "n}q_K"

msg_key_final=""

for i in range( len(msg_enc)/len(msg_key) +1 ) :
	msg_key_final+=msg_key

msg_key_final=msg_key_final[0:len(msg_enc)]

output = strxor(msg_key_final,"".join(msg_enc))

print base64.b64encode(output)
