import requests
import time
import random
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

# 从快代理API获取代理（因为没交钱所以已经废了）
def getp():
	return requests.get("http://dps.kdlapi.com/api/getdps/?orderid=976635491365392&num=1&pt=1&sep=1").text
# 获取用户订阅列表
def get_tags(user):
	api = "https://space.bilibili.com/ajax/tags/getSubList?mid="
	url = api + str(user)
	json = requests.get(url,headers=headers,proxies=proxies,timeout=3).json()
	# print(json)

# 获取用户个人信息
def get_info(user):
	api = "https://api.bilibili.com/x/space/acc/info?mid="
	url = api + str(user)
	# 有代理再开这行
	# json = requests.get(url,headers=headers,proxies=proxies,timeout=1.5).json()
	json = requests.get(url,headers=headers,timeout=5).json()
	# print(json)
	return json

# 首先获取代理ip
pro = getp()

http_proxy =  'http://'+pro
https_proxy = 'https://'+pro
proxies = {
	'http': http_proxy,
	'https': https_proxy,
}

# json = requests.get("https://api.bilibili.com/x/space/acc/info?mid=1",headers=headers,proxies=proxies,timeout=5).json()

# 第一个mid
n = 203616

while True:
	con = 0 # 错误计数
	while True:
		# 异常处理
		try:
			userinfo = get_info(n)
		except:
			if con == 2:
				print("连续2次都失败了。正在更换代理。。。。")
				pro = getp()

				http_proxy =  'http://'+pro
				https_proxy = 'https://'+pro
				
				proxies = {
					'http': http_proxy,
					'https': https_proxy,
				}
				
				con = 0 # 归零
			else:
				print("出现了问题，可能是因为ip被限制。")
				con = con + 1
				# time.sleep(1)
		else:
			break
	print(n)
	if(userinfo['code'] == 0):
		file = open("user-info.csv",'a')
		data = userinfo['data']
		file.write(str(data['mid']) +',')
		try:
			file.write(str(data['name'])+',')
		except:
			file.write(',')

		file.write(str(data['sex'])+',')
		# file.write(str(data['sign'])+',')
		file.write(',')

		file.write(str(data['level'])+',')
		file.write(str(data['birthday'])+',')
		file.write(str(data['fans_badge']) +',')

		vip = data['vip']
		file.write(str(vip['type'])+'\n')
		file.close()

	# 加了代理这行可以去掉，为的是防止被封ip
	time.sleep(1)
	n = n + 1