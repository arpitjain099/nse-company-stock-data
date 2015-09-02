
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
import sys
import codecs
fi=codecs.open("error.log","a+",encoding="utf-8")
with open('dump.json') as data_file:    
    data = json.load(data_file)
    print len(data['datasets'])
    for i in data['datasets']:
    	temp=i['database_code']+'/'+i['dataset_code']
    	print i['name']

    	#mydata = Quandl.get(temp, authtoken="JVbNrP-_zsnbC7i6yCUM")
    	if not os.path.isfile('dump/'+i['dataset_code']+'_'+i['name']+".csv"):
            #dada=Quandl.get(i['database_code']+"/"+"20MICRONS", authtoken="JVbNrP-_zsnbC7i6yCUM")
            #print dada
            #print i['database_code']+"/"+i['dataset_code']
            try:
                mydata = Quandl.get(i['database_code']+"/"+i['dataset_code'], authtoken="gNHGL_H-4X9BPuLvnrBC")
                mydata.to_csv('dump/'+i['dataset_code']+'_'+i['name']+".csv")
            except:
                print "error in "+i['database_code']+"/"+i['dataset_code']
                fi.write(i['database_code']+"/"+i['dataset_code']+"\n")
fi.close()