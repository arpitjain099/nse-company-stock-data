import codecs
fi=codecs.open("dump.json","w",encoding='utf-8')
fi.write('{"datasets":[')
import urllib2
da=range(1,20)
la=""
import time
for i in da:
	url='https://www.quandl.com/api/v3/datasets?database_code=NSE&page='+str(i)+'&per_page=200&query=&auth_token=JVbNrP-_zsnbC7i6yCUM'
	response = urllib2.urlopen(url)
	html = response.read()
	html=html.split('"datasets": [')[1].split('"meta":')[0]
	html=html.split("\n")
	for j in range(len(html)-2):
		fi.write(html[j]+"\n")
	if i!=19:
		fi.write(",")
	#print html
	print "yay"
	time.sleep(3)
fi.write("]}")