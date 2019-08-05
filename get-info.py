import requests
import time
import random
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
proxies = {
	'https': '101.6.69.5:1081'
}
url = "https://api.bilibili.com/x/web-interface/archive/stat?aid="
file = open("list.csv",'a')

def get(urls): #,proxies=proxies
	# 异常处理，如果被封IP会自动休息
	while True:
		con = 0 # 连续5次
		try:
			json = requests.get(urls,headers=headers,timeout=10).json()
		except:
			if con == 5:
				print("连续5次都失败了。建议更换代理。")
			else:
				print("出现了问题，可能是因为IP被限制。5秒后会重新尝试。")
				con = con+1
				time.sleep(5)
		else:
			break
	# print(json)
	if(json['code'] == 0):
		data = json['data']
		file.write(str(data['aid']) +',')
		file.write(str(data['view'])+',')
		file.write(str(data['danmaku'])+',')
		file.write(str(data['reply'])+',')
		file.write(str(data['favorite'])+',')
		file.write(str(data['coin'])+',')
		file.write(str(data['share'])+',')
		file.write(str(data['like']) + '\n')
		# 从上到下分别为：AV号,播放量,弹幕数,评论数,收藏数,硬币,分享,点赞

	
n = 931386 # 从AV n 开始爬
while True:
	get(url + str(n))
	n = n+1
	print(n)
	time.sleep(random.uniform(0,0.3))
	