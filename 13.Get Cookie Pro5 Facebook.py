
import os,sys,requests
from time import sleep
list_id_name_page=[]
# =========================== [ MÀU ] ===========================
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;20m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;20m"
lam="\033[1;20m"
tim="\033[1;20m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;20m"
lam = "\033[1;36m"
tim = "\033[35m"
hong = "\033[1;95m"

def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.01)
   print()
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def thanh():
    echo(f'{hong}─────────────────────────────────────────────────────────────')
clear()
cookie=input(f'{luc}NHẬP COOKIE CHỨA PAGE{trang}: ')
headers_check_live={
    'authority':'mbasic.facebook.com',
    'cache-control':'max-age=0',
    'sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'upgrade-insecure-requests':'1',
    'origin':'https://mbasic.facebook.com',
    'content-type':'application/x-www-form-urlencoded',
    'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site':'same-origin',
    'sec-fetch-mode':'navigate',
    'sec-fetch-user':'?1',
    'sec-fetch-dest':'document',
    'referer':'https://mbasic.facebook.com/',
    'accept-language':'en-US,en;q=0.9',
    'cookie':cookie
}
try:
    find_data=requests.get('https://mbasic.facebook.com/',headers=headers_check_live).text
    fb_dtsg=find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest=find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    thanh()
    exit(f'{red}COOKIE DIE OR OUT!!!')
headers_getid={
    'cookie':cookie,
}
data={
    'fb_dtsg':fb_dtsg,
    'jazoest':jazoest,
    'variables':'{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id':'5300338636681652'
}
get_id_page=requests.post(f'https://www.facebook.com/api/graphql/',headers=headers_getid,data=data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
for i in get_id_page:
    uid_page=i['profile']['id']
    name_page=i['profile']['name']
    gomlist=f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
clear()
print(f'{xnhac}ĐÃ TÌM THẤY '+vang+str(len(list_id_name_page))+xnhac+' PAGE PRO5 & PAGE THƯỜNG')
thanh()
lua_chon=input(f'{luc}LƯU COOKIE KÈM TÊN & UID PAGE(y/n){trang}: ')
thanh()
if lua_chon=='y':
    file=input(f'{xanhduong}VUI LÒNG NHẬP FILE LƯU COOKIE: ')
    for a in get_id_page:
        uid_page=a['profile']['id']
        name_page=a['profile']['name']
        with open(file,'a',encoding='utf-8')as f:
            f.write(f"{cookie};i_user={uid_page}|{name_page}|{uid_page}\n")
else:
    file=input(f'{xanhduong}VUI LÒNG NHẬP FILE LƯU COOKIE: ')
    for a in get_id_page:
        uid_page=a['profile']['id']
    with open(file,'a',encoding='utf-8')as f:
        f.write(f"{cookie};i_user={uid_page}\n")
thanh()
echo(f'{xanhbien}ĐÃ LƯU COOKIE VUI LÒNG KIỂM TRA LẠI FILE')
sleep(1.5)