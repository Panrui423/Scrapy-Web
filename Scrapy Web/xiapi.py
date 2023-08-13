import requests
import re
import json
import pandas as pd
from bs4 import BeautifulSoup

cookies = {
    '__LOCALE__null': 'ID',
    '_gcl_au': '1.1.1386949128.1658914035',
    '_med': 'refer',
    'csrftoken': 'XICwdDRLTpspTdsp0I1g82xVJi0iGrHg',
    '_QPWSDCXHZQA': '2dfdf29c-5b29-454a-ddec-3ab9f1eb2275',
    'SPC_F': 'MSTXrxTmgv4w8LCf6X0NfUTMarfvtKiY',
    'REC_T_ID': '4e3eac55-0d8e-11ed-9dcd-b6ef78d63509',
    'SPC_R_T_ID': 'xkA/pG6Q4DKiWhUfR+QNOdcX0y2KG27Ox4IgV35UbQx5OuCNeZVEPbhAkjIwm3G6PyiF1z0UNYrhUTJ44n+Vf+TcBNjw/kF2BP1nDRt409pW+32DXGdDK/F0Qe0C2kSQwMGuRFwYOle2f3pZ1oKg4P0RE1wbXjLXfP7b1jmZBd8=',
    'SPC_R_T_IV': 'RVVCdjlkVXA1d3NscHJGVg==',
    'SPC_T_ID': 'xkA/pG6Q4DKiWhUfR+QNOdcX0y2KG27Ox4IgV35UbQx5OuCNeZVEPbhAkjIwm3G6PyiF1z0UNYrhUTJ44n+Vf+TcBNjw/kF2BP1nDRt409pW+32DXGdDK/F0Qe0C2kSQwMGuRFwYOle2f3pZ1oKg4P0RE1wbXjLXfP7b1jmZBd8=',
    'SPC_T_IV': 'RVVCdjlkVXA1d3NscHJGVg==',
    'SPC_SI': 'rRm8YgAAAABUZzlKTFFOTqeqeQAAAAAATHo0UlpCVm8=',
    'kk_leadtag': 'true',
    '_gid': 'GA1.3.515696914.1659259542',
    'HAS_BEEN_REDIRECTED': 'true',
    '_ga': 'GA1.3.290695403.1658914036',
    'shopee_webUnique_ccd': '0y0%2BAnsOltdJXnKqAAO6eQ%3D%3D%7C102nYWItEydB%2F7RRP3UPiq0HOUfOcfVcbnCLZgL2OU%2F8Rrm48Ap7yEgjVWFmUwju0p3N0Nd%2FQ5PrUcwAZxsH7LTeHS0%3D%7CskkKC0uUIzrll826%7C05%7C3',
    'cto_bundle': '5iKTkF9MQ0c1OFMlMkJVczJOJTJCRTJkQ1NFUG5QQThPaEZwV2tpbGdYOHI2NFpYdVhqbXF4QVNCMEkzeFpaeGZZSHVnOFo1N0JrOW5VWDJpa3dFMkE0SjhkZUNBQ0taakpkOW9GUk41d2Jrc3p0aXQxaVRKdzVhU29FelNKQlNEZWNhRHE4V0QlMkJzM3E4WldKOGZZT1VKalRNSyUyQk5HZyUzRCUzRA',
    '_dc_gtm_UA-61904553-8': '1',
    '_ga_SW6D8G0HXK': 'GS1.1.1659333576.7.1.1659333846.38',
}

headers = {
    'authority': 'shopee.co.id',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'af-ac-enc-dat': 'AAYyLjIuMTAAAAGCU+FtvwAAAAABPwAAAAAAAAABsDysRQt3WVmXwkFope8+0E3mGoOD4p6KDrViEnSFTAhjvNaaUFOrhxMfLZQXRo5JkbPEsmjzSIsQNAEa0jNTuZFjs4yw8pGWNnYQjtmnppaRY7OMsPKRljZ2EI7Zp6aWnRl9auO81kkFgPHH0g/c0J+Aiy5p+ABM+rxSjhyqrtl5FAo2vHRg66IN9TA+KYDRwaGG/jz5gr1Qgw1Ck21ETR0HSwUPBZGNLSslMRbs1QWfgIsuafgATPq8Uo4cqq7ZCRWGt8l2DVoo6rc0Tv2q8/CFmy10o0Bep1IX/Q54aEx1uhZ/ataY3Z+uH4DlUpHRMww5AjWtUEsQgVvq6pXTjk/TRVMn/R+rNrBH2x1cEXyRY7OMsPKRljZ2EI7Zp6aWIhk4cctnmLdwqo576VIPtEZIXXN5kQwi9jgPjpSdKSE=',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__LOCALE__null=ID; _gcl_au=1.1.1386949128.1658914035; _med=refer; csrftoken=XICwdDRLTpspTdsp0I1g82xVJi0iGrHg; _QPWSDCXHZQA=2dfdf29c-5b29-454a-ddec-3ab9f1eb2275; SPC_F=MSTXrxTmgv4w8LCf6X0NfUTMarfvtKiY; REC_T_ID=4e3eac55-0d8e-11ed-9dcd-b6ef78d63509; SPC_R_T_ID=xkA/pG6Q4DKiWhUfR+QNOdcX0y2KG27Ox4IgV35UbQx5OuCNeZVEPbhAkjIwm3G6PyiF1z0UNYrhUTJ44n+Vf+TcBNjw/kF2BP1nDRt409pW+32DXGdDK/F0Qe0C2kSQwMGuRFwYOle2f3pZ1oKg4P0RE1wbXjLXfP7b1jmZBd8=; SPC_R_T_IV=RVVCdjlkVXA1d3NscHJGVg==; SPC_T_ID=xkA/pG6Q4DKiWhUfR+QNOdcX0y2KG27Ox4IgV35UbQx5OuCNeZVEPbhAkjIwm3G6PyiF1z0UNYrhUTJ44n+Vf+TcBNjw/kF2BP1nDRt409pW+32DXGdDK/F0Qe0C2kSQwMGuRFwYOle2f3pZ1oKg4P0RE1wbXjLXfP7b1jmZBd8=; SPC_T_IV=RVVCdjlkVXA1d3NscHJGVg==; SPC_SI=rRm8YgAAAABUZzlKTFFOTqeqeQAAAAAATHo0UlpCVm8=; kk_leadtag=true; _gid=GA1.3.515696914.1659259542; HAS_BEEN_REDIRECTED=true; _ga=GA1.3.290695403.1658914036; shopee_webUnique_ccd=0y0%2BAnsOltdJXnKqAAO6eQ%3D%3D%7C102nYWItEydB%2F7RRP3UPiq0HOUfOcfVcbnCLZgL2OU%2F8Rrm48Ap7yEgjVWFmUwju0p3N0Nd%2FQ5PrUcwAZxsH7LTeHS0%3D%7CskkKC0uUIzrll826%7C05%7C3; cto_bundle=5iKTkF9MQ0c1OFMlMkJVczJOJTJCRTJkQ1NFUG5QQThPaEZwV2tpbGdYOHI2NFpYdVhqbXF4QVNCMEkzeFpaeGZZSHVnOFo1N0JrOW5VWDJpa3dFMkE0SjhkZUNBQ0taakpkOW9GUk41d2Jrc3p0aXQxaVRKdzVhU29FelNKQlNEZWNhRHE4V0QlMkJzM3E4WldKOGZZT1VKalRNSyUyQk5HZyUzRCUzRA; _dc_gtm_UA-61904553-8=1; _ga_SW6D8G0HXK=GS1.1.1659333576.7.1.1659333846.38',
    'referer': 'https://shopee.co.id/Komputer-Aksesoris-cat.11044364',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sz-token': '0y0+AnsOltdJXnKqAAO6eQ==|102nYWItEydB/7RRP3UPiq0HOUfOcfVcbnCLZgL2OU/8Rrm48Ap7yEgjVWFmUwju0p3N0Nd/Q5PrUcwAZxsH7LTeHS0=|skkKC0uUIzrll826|05|3',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36',
    'x-api-source': 'pc',
    'x-csrftoken': 'XICwdDRLTpspTdsp0I1g82xVJi0iGrHg',
    'x-requested-with': 'XMLHttpRequest',
    'x-sap-access-f': '3.0.0.3.0|13|2.2.10_5.2.8_0_109|dd3d580934bc4951a501c4957b3306193398054915bd4c|10900|100',
    'x-sap-access-s': 'zhRANcDOrlnLra57JvBH1DKAtoVKECyQBzCuFAhOL78=',
    'x-sap-access-t': '1658914036',
    'x-shopee-language': 'id',
}

params = {
    'by': 'relevancy',
    'limit': '60',
    'match_id': '11044364',
    'newest': '0',
    'order': 'desc',
    'page_type': 'search',
    'scenario': 'PAGE_CATEGORY',
    'version': '2',
}

next_params = params
# 创建一个空的 DataFrame
df_all = pd.DataFrame(columns=['Goods_name', 'brand', 'price'])
j=0
while next_params:
    response = requests.get('https://shopee.co.id/api/v4/search/search_items', params=next_params, cookies=cookies, headers=headers)
    bs = BeautifulSoup(response.text, 'html.parser')
    data = json.loads(bs.text)
    if 'items' in data:
        length_data = len(data['items'])
    else:
        break
    name = {}
    brand = {}
    price = {}
    for i in range(length_data):
        name[i] = data['items'][i]['item_basic']['name']
        brand[i] = data['items'][i]['item_basic']['brand']
        price[i] = data['items'][i]['item_basic']['price']/100000
    name = pd.DataFrame.from_dict(name,orient='index')
    brand = pd.DataFrame.from_dict(brand,orient='index')
    price = pd.DataFrame.from_dict(price,orient='index')
    frames = [name, brand, price]
    df = pd.concat(frames,axis = 1)
    df.columns = ['Goods_name', 'brand', 'price']
    df.index = list(range(0 + j*60, 60+j*60, 1))
    df_f = [df_all,df]
    df_all = pd.concat(df_f)
    next_params['newest'] = str(60*(j+1))
    j = j+1

print(df_all)
df_all.to_csv('goods.csv')  # 如果有缺失值,可以通过na_rep的方式把缺失值替换成自定义的名字













