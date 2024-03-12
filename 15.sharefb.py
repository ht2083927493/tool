
import requests, time,os,sys,threading
from datetime import datetime
os.system('clear')
#color
lucnhat = "\033[1;96m"
do = "\033[1;91m"
xanh = "\033[1;92m"
vang = "\033[1;93m"
xanhd = "\033[1;94m"
hong = "\033[1;95m"
trang = "\033[1;97m"
class Shareao:
  def __init__(self):
    pass
  def file(self):
    print(xanhd+'Tool share bởi kênh: Hiếu tool')
    print(trang+'Mọi người dùng cho 1 like, 1 đăng kí để admin có động lực!')
    print(xanhd+'Link kênh: https://www.youtube.com/@hieutool248')
    print('════════════════════════════════════════════════════════════')
    file=open('ckk.txt','a+')
    file=open('ckk.txt','r')
    self.cookie=file.readline()
  #  print(cookie)
    if 'datr=' in self.cookie:
      choose=input(xanh+'Bạn đã nhập cookie,bạn muốn nhập lại hay chạy tiếp(y/n): '+vang)
      if choose=="y":
        new=input(xanh+'Nhập cookie mới: '+vang)
        filenew=open('ckk.txt','w')
        filenew.write(new)
      else:
        print(lucnhat+'Chạy với cookie cũ')
        time.sleep(2)
    else:
      nhap=input(xanh+'Nhập cookie: '+vang)
      doick=open('ckk.txt','w')
      doick.write(nhap)
  def get_token(self):
    os.system('clear')
    print(xanhd+'Tool share bởi kênh: Hiếu tool')
    print(trang+'Mọi người dùng cho 1 like, 1 đăng kí để admin có động lực!')
    print(xanhd+'Link kênh: https://www.youtube.com/@hieutool248')
    print('════════════════════════════════════════════════════════════')
    headers = {
              'Host': 'business.facebook.com',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'accept-language': 'vi',
              'cache-control': 'max-age=0',
              'cookie': self.cookie,
              'referer': 'https://www.facebook.com/',
             'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Linux"',
              'sec-fetch-dest': 'document',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-user': '?1',
              'upgrade-insecure-requests': '1',
              }
    try:
        business=requests.get('https://business.facebook.com/content_management',headers=headers).text
        tk=business.split('EAAG')[1].split('","')[0]
        self.token=f'EAAG{tk}'
    except:
        exit(do+'Cookie die!!')
  def decor(self):
    self.idpost=input('Nhập id bài viết cần share: ')
    self.delay=int(input('Nhập delay: '))
    self.total=int(input('Nhập số lần share: '))
    self.time=datetime.now().strftime('%H:%M:%S')
  def share(self):
    headershare={
      'Host': 'graph.facebook.com',
      'cache-control': 'max-age=0',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'cross-site',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'accept-language': 'vi',
      'cookie':self.cookie
    }
    url=f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{self.idpost}&published=0&access_token={self.token}'
    buff=requests.post(url,headers=headershare).json()
    if 'id' in buff:
      idshare=buff['id']
      print(xanhd+f"{self.time} {idshare}")
    else:
      print(do+f'{self.time}: SHARE POST FAILED !!')
  def runshare(self):
    stt=0
    while True:
      stt = stt+1
      run=threading.Thread(target=self.share).start()
      time.sleep(self.delay)
      if self.total == stt:
        break
main=Shareao()
main.file()
main.get_token()
main.decor()
main.runshare()
main.share()
