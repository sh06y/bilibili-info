import requests
import time
import random
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

url = "https://api.bilibili.com/x/web-interface/archive/stat?aid="

def getp():
	return requests.get("http://dps.kdlapi.com/api/getdps/?orderid=976635491365392&num=1&pt=1&sep=1").text

def get(urls): #,proxies=proxies
	con = 0 # 错误计数
	while True:
		# 异常处理，如果被封IP会自动休息
		try:
			json = requests.get(urls,headers=headers,timeout=3).json()
		except:
			if con == 5:
				print("连续5次都失败了。建议更换代理。")
				con = 0 # 归零
				# pro = getp()

				# http_proxy =  'http://'+pro
				# https_proxy = 'https://'+pro
				
				# proxies = {
				# 	'http': http_proxy,
				# 	'https': https_proxy,
				# }
				# time.sleep(2)
			else:
				print("出现了问题，可能是因为IP被限制。5秒后会重新尝试。")
				con = con + 1
				# time.sleep(2)
		else:
			break
	# print(json)

	# 如果视频存在，写入
	if(json['code'] == 0):
		print("yes")
		file = open("video-info.csv",'a')
		data = json['data']
		# 从上到下分别为：AV号,播放量,弹幕数,评论数,收藏数,硬币,分享,点赞
		file.write(str(data['aid']) +',')
		file.write(str(data['view'])+',')
		file.write(str(data['danmaku'])+',')
		file.write(str(data['reply'])+',')
		file.write(str(data['favorite'])+',')
		file.write(str(data['coin'])+',')
		file.write(str(data['share'])+',')
		file.write(str(data['like']) + '\n')
		# 需要关闭文件以保存
		file.close()

# 首先获取代理ip
# pro = getp()

# http_proxy =  'http://'+pro
# https_proxy = 'https://'+pro

# proxies = {
# 	'http': http_proxy,
# 	'https': https_proxy,
# }

n = 2433907 # 从AV n 开始爬
while True:
	print(n)
	get(url + str(n))
	n = n+1
	time.sleep(1)
