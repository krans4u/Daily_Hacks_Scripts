import urllib
import urllib2
from cookielib import CookieJar
cj = CookieJar()
a=raw_input();
a=a.split(' ')
myId = a[0]
myPin = a[1]
data = {
	'StUdent':myId,
	'password':myPin,
	'searchin':'200',
	'submit': 'Submit',	
	
}
thing = urllib2.HTTPRedirectHandler()
opener = urllib2.build_opener(thing,urllib2.HTTPCookieProcessor(cj))
data = urllib.urlencode(data)
url = 'https://isas.iiit.ac.in/validate.php'
response = opener.open(url,data)
url = 'https://isas.iiit.ac.in/academicProfile.php'

response=opener.open(url)
flag=0;
#print response.read()
stri=response.read();		 
var=0;
for i in stri:
	if i=='<':
		var=0;
	if var==1:
		print i, 
	if i=='>':
		var=1;
response.close();
#print response.read()
