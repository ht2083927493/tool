den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= trang + "~" + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + "~" + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
import os
import requests
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")

checkip = requests.get(url=f"https://ipinfo.io/json")
ip = checkip.json()['ip']
region = checkip.json()['region']
city = checkip.json()['city']
country = checkip.json()['country']
org = checkip.json()['org']
postal = checkip.json()['postal']
timezone = checkip.json()['timezone']

time=datetime.now().strftime("%H:%M:%S")
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
os.system("cls" if os.name == "nt" else "clear")
print(f"{luc}Ngày{trang}:{vang}{ngay_hom_nay}{red} |{luc} Tháng{trang}:{vang}{thang_nay} {red}| {luc}Năm{trang}:{vang}{nam_}")
print(f'{lam}CẢM MƠN BẠN ĐÃ SỬ DỤNG TOO; CỦA KÊNH HIẾU-TOOL')
print(f'{thanh_xau}{luc}IP HIỆN TẠI CỦA BẠN LÀ{trang}:{vang} {ip}')
print(f'{thanh_xau}{luc}HUYỆN HOẶC THÀNH PHỐ{trang}:{vang} {city}')
print(f'{thanh_xau}{luc}TỈNH{trang}:{vang} {region}')
print(f'{thanh_xau}{luc}QUỐC GIA{trang}:{vang} {country}')
print(f'{thanh_xau}{luc}NHÀ MẠNG{trang}:{vang} {org}')
print(f'{thanh_xau}{luc}MÃ BƯU ĐIỆN{trang}:{vang} {postal}')
print(f'{thanh_xau}{luc}MÚI GIỜ{trang}:{vang} {timezone}\n')

exit=input(f'{lamd}ENTER ĐỂ{red} - {lamd}THOÁT TOOL{trang}')