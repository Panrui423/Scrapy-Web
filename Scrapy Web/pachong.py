import requests  # urllib,urllib3

# pip install requests


# GET请求

# response=requests.get(url="http://www.baidu.com/")

# print(response.text)# 返回文本信息

# print(response.content.decode("utf-8"))# 对字节流数据进行解码

# with open("baidu.html",'wb')as f:

#     f.write(response.content)


# GET请求图片

# pic_url='https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2549177902.jpg'

# response=requests.get(pic_url)

# with open('绿皮书.jpg','wb')as f:

#     f.write(response.content)


# GET提交表单

# movie_url='https://maoyan.com/query?kw=%E6%88%91%E4%B8%8D%E6%98%AF%E8%8D%AF%E7%A5%9E'

# names=input("输入电影名称:")

# bd_url='https://maoyan.com/query'

# payout={'kw':names}

# response=requests.get(bd_url,params=payout)

# print(response.content.decode('utf-8'))


# POST请求

# payload={'username':'cs2433','password':'xxxxx'}

# response=requests.post("http://httpbin.org/post",data=payload)

# with open("post.html",'wb')as f:

#     f.write(response.content)

# response=requests.post("http://httpbin.org/post")

# with open("nopost.html",'wb')as f:

#     f.write(response.content)


# 响应和编码

# response=requests.get(url="http://www.baidu.com/")


# 字节流编码(从网页进行分析)

# print(response.content.decode("utf-8"))# 对字节流数据进行解码


# 调用text自动编码

# response.encoding='utf-8'

# print(response.text)# 返回文本信息


# response自动解析编码

# response.encoding=response.apparent_encoding

# print(response.text)


# chardet解码

# import chardet

# code=chardet.detect(response.content)['encoding']

# print(response.content.decode(code))


# 状态码

# 200表示成功 300开头表示跳转 404网址不存在 403拒绝访问 500服务器错误

# print(response.status_code)


# # 请求头

# dzdp='http://www.dianping.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

# response=requests.get(dzdp,headers=header)

# html=response.content.decode('UTF-8')

# print(len(html))

#

# response=requests.get(dzdp)

# html=response.content.decode('UTF-8')

# print(len(html))


# 设置cookies

# cookies_str="BAIDUID=1742D859EE234195BF39DBCE85653DE7:SL=0:NR=10:FG=1; BIDUPSID=1742D859EE234195BF39DBCE85653DE7; PSTM=1555496210; BD_UPN=13314752; sug=3; ORIGIN=0; bdime=0; H_WISE_SIDS=125703_128699_130408_128069_131368_130164_120161_131601_122157_118897_118875_131402_118854_118835_118798_130762_131649_131575_131536_131533_131530_130222_131391_129565_107314_131394_130128_131518_131239_131195_117332_130349_117431_129648_131022_127026_130690_131436_131687_131036_114819_129377_130990_124802_131474_131424_130803_110085_127969_131506_123289_130820_131033_131299_127317_128195_131550_131265_131263_130986_131457_128808; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1441_21127_29135_29237_29099_29368_28836_29220_20718; BDRCVFR[Fc9oatPmwxn]=aeXf-1x8UdYcs; delPer=0; BD_HOME=1; BD_CK_SAM=1; PSINO=5; H_PS_645EC=90cd8A%2BZCIDcIXM9shsY%2BLw2u8OhCVHSFME1yeqsu7IKcLyR2kWFrZlJ7HPXGz3psxGI; BDUSS=A0eEdHUFZOZWd6eW9sdC1BVW5BaGRZYVlOR01aVWMydWZBNUVnaVJsQ21rekpkSVFBQUFBJCQAAAAAAAAAAAEAAAD1Vsk2Y3MyNDMzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKYGC12mBgtdQj; sugstore=1"

# cookies_dict={}

# # cookies_dict['a']=1

# for i in cookies_str.split(";"):

#     item=i.split("=",1)

#     cookies_dict[item[0]]=item[1]

# print(cookies_dict)


# response=requests.get("https://www.baidu.com/",headers=header)

# html=response.content.decode('utf-8')

# print(len(html))

# response=requests.get("https://www.baidu.com/",headers=header,cookies=cookies_dict)

# html=response.content.decode('utf-8')

# print(len(html))


# # 超时处理

# for i in range(10):

#     try:

#         url='https://www.bilibili.com/'

#         response=requests.get(url,timeout=0.1)

#         print(response.status_code)

#     except:

#         print("网络连接超时!")

#         continue


# 代理

# proxies={

#     # 'http':'http://ip地址:端口号'

#     'http':'http://101.200.43.49:9999'

# }

# response=requests.get("http://httpbin.org/ip")

# print(response.text)


import json

seesion = requests.session()
payload = {'username': 'wangbw0918', 'password': '123654'}
url = 'http://account.chinaunix.net/login/login'
res = seesion.post(url, data=payload, headers=header)
print(res.cookies)
print(res.json())

# print(response.content.decode('utf-8'))
response = seesion.get('http://bbs.chinaunix.net/', headers=header)
text1 = response.content.decode('gbk')
print(len(text1))
response = requests.get('http://bbs.chinaunix.net/', headers=header)
text2 = response.content.decode('gbk')
print(len(text2))

# with open('post登录.html','wb')as f:

#     f.write(response.content)

# new=json.loads(response.content.decode('utf-8'))['data']['url']

# text=requests.get(new).content.decode('utf-8')

# print(text)

# print(requests.post(url).content.decode('utf-8'))







