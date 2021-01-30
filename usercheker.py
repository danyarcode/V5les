import requests
import random
import os 
import sys
import time

# Gar to bo edit yan dzene hatwi awa Mn encrypte nakam qaynaka Beba Bas agadar ba ama zerake pe nalen balkw to kaseke mshaxoryt hichi tr mn barham henekm 


# asan karem krdwa Ka encryptm  nakrdwa dway bro posty kan poze pe le dan chand jar wam le hatwa!!!!


# Tool  drust kra lalayan ani_software
os.system("xdg-open https://instagram.com/vl5es?igshid=laa0q0c2lys0")
def password():
	os.system("clear")
	print("Tkaya passworde tool bnwsa")
	print("")
	print("-------------")
	print("password tool ( ani ) ")
	print("")
	username="bzhiala"
	ani=input("Password tool => ")
	if ani==username:
		print("rasta")
	elif ani=="ani":
		os.system("clear")
		print(" Ke wty ba qsam ka ?!")
		time.sleep(2)
		password()
		
	else:
		print("xalata")
		time.sleep(2)
		password()
password()
def fb():
	ani="""\033[1;36m
	
                               
o     o 8 oooooo               
8     8 8 8                    
8     8 8 8pPYo. .oPYo. .oPYo. 
`b   d' 8     `8 8oooo8 Yb..   
 `b d'  8     .P 8.       'Yb. 
  `8'   8 `YooP' `Yooo' `YooP' 
:::..:::..:.....::.....::.....:
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
 
 -----------
 snapchat >= shex_gaya
             
 instagram >= vl5es
                                    
 telgram >= uns1d
 
 ----------
	\033[0;37m
	"""
	os.system("clear")
	print(ani)
	filer=open("user.txt","r").readlines()
	for x in filer:
		u=x.strip()
		re = requests.get('https://www.facebook.com/{}'.format(u)).status_code
		if re==200:
			print("")
			print(u+" >= \033[1;31mHAYA \033[1;37m ")
		else:
			print("")
			print(u+" >= \033[1;32mNYA \033[1;37m")
		time.sleep(3)
	

##############


def insta():
	os.system("clear")
	
	ani="""\033[1;36m
	
                               
o     o 8 oooooo               
8     8 8 8                    
8     8 8 8pPYo. .oPYo. .oPYo. 
`b   d' 8     `8 8oooo8 Yb..   
 `b d'  8     .P 8.       'Yb. 
  `8'   8 `YooP' `Yooo' `YooP' 
:::..:::..:.....::.....::.....:
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
 
 -----------
 snapchat >= shex_gaya
             
 instagram >= vl5es
                                    
 telgram >= uns1d
 
 ----------
	\033[0;37m
	"""
	
	print(ani)
	namee=open("user.txt","r").readlines()
	for x in namee:
		time.sleep(1)
		u=x.strip()
		re =requests.get('https://www.instagram.com/{}/'.format(u)).status_code
		if re==200:
			print("")
			print(u+ " >= \033[1;31mHAYA\033[1;37m")
		else:
			print("")
			print(u+ " >= \033[1;32mNYA\033[1;37m")

	
def user_maker():
	os.system("clear")
	ani="""
	
	TEAM TEROR
	
	   -----
	
           -----
	
	"""
	print(ani)
	filer=open("user.txt","w")
	print("==================")
	print("")
	user=int(input("Chand Pet be :"))
	for x in range(300):
		text="qwertyuioplkjhgfdsazxcvbnm1234567i90-_."
		word=''.join(random.choice(text) for x in range(user))
		filer.write(word+"\n")
		
		print(word)
	time.sleep(3)
	print("")
	print("----------")
	print("")
	print("ALL USER SAVED IN FILE USER.TXT")
	time.sleep(3)




def minu():
	os.system("clear")
	print("------")
	print("    -----------")
	print(" vl5es     =========")
	
	print("------")
	print("    -----------")
	print("           =========")
	print("")
	print("")
	print("")
	print("============ani_software===============")
	print("")
	
	print(" < 1 > henane username ")
	print("")
	print("-------")
	print("< 2 > fa7s krdne username instagram")
	print("")
	print("-------")
	print(" < 3 > fa7d krdne username facbook")
	print("")
	print('`````````````')
	print("")
	print("")
	ani=int(input(" Choice : "))
	if ani==1:
		os.system("clear")
		user_maker()
		minu()
	if ani==2:
		os.system("clear")
		insta()
		minu()
	if ani==3:
		os.system("clear")
		fb()
		minu()
	
	
minu()