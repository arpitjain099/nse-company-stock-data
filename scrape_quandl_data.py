
#import urllib2
#response = urllib2.urlopen('https://www.quandl.com/api/v1/datasets/NSE/20MICRONS.csv?auth_token=JVbNrP-_zsnbC7i6yCUM')
#html3 = response.read()
#print html3
#import wget
#url = 'https://www.quandl.com/api/v1/datasets/NSE/20MICRONS.csv?auth_token=JVbNrP-_zsnbC7i6yCUM'
#fi=wget.download(url)

#import requests
#r=requests.get('https://www.quandl.com/api/v1/datasets/NSE/20MICRONS.csv?auth_token=JVbNrP-_zsnbC7i6yCUM')
#print r.content

	#fi.write(html+",\n")
import json
import Quandl
import os
with open('dump.json') as data_file:    
    data = json.load(data_file)
    print len(data['datasets'])
    for i in data['datasets']:
    	temp=i['database_code']+'/'+i['dataset_code']
    	print i['name']
    	#mydata = Quandl.get(temp, authtoken="JVbNrP-_zsnbC7i6yCUM")
    	if not os.path.isfile('dump/'+i['dataset_code']+'_'+i['name']+".csv"):
		print i['database_code']+"/"+i['dataset_code']
	    	mydata = Quandl.get(i['database_code']+"/"+i['dataset_code'], authtoken="JVbNrP-_zsnbC7i6yCUM")
    		mydata.to_csv('dump/'+i['dataset_code']+'_'+i['name']+".csv")