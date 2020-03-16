import requests
import lxml.html as lh
url='http://149.56.110.180:1234/'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
td_elements = doc.xpath('//td')
res= ""
for i in range (0, len(td_elements)) :
	res+= td_elements[i].get('bgcolor') [1:]
print res
