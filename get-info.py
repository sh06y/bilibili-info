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
# AV号,播放量,弹幕数,评论数,收藏数,硬币,分享,点赞"
def get(urls): #,proxies=proxies
	json = requests.get(urls,headers=headers,timeout=100).json()
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
n = 202997
while True:
	get(url + str(n))
	n = n+1
	print(n)
	time.sleep(random.uniform(0,0.5))
	