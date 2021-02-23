# import urllib.request as ure
# import re

# url = r'http://www.baidu.com'

# rp = ure.urlopen(url).read().decode()
# pattern = r'<title>(.*?)</title>'
# data = re.findall(pattern, rp)
# print(''.join(data))

# from urllib import request
# import random

# proxylist = [
# 	{"36.22.77.166":"3128"},
# 	{"223.242.224.159":"9999"},
# 	{"60.168.207.108":"8888"},
# 	{"27.220.164.186":"9000"},
# 	{"218.66.253.145":"80"}
# ]

# proxyHandler = random.choice(proxylist)
# print(proxyHandler)
import urllib
from urllib import request
import time
import random
import requests
import numpy as np
import matplotlib.pyplot as plt
class crawer:
	def __init__(self):
		self.url = url

	def tiebaSpider(self, begin, end):
		for page in range(begin, end+1):
			pn = (page - 1) * 50
			fullurl = self.url + "&pn=" + str(pn)
			filename = "/Users/dengdeshun/Desktop/Spider_testing/第{}页.html".format(page)
			html = self.loadpage(fullurl, filename)
			self.writepage(html, filename)

	def loadpage(self, fullurl, filename):
		header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4408.0 Safari/537.36"}
		print("Now is downloading:", filename)
		# req = request.Request(fullurl, headers = header)
		resp = requests.get(fullurl, headers = header).content
		return resp

	def writepage(self, html, filename):
		print("Now is saving:", filename)
		with open(filename, "wb") as f:
			f.write(html)

		print('-'*30)

	def heart_plot(self):
		x =  np.linspace(-2, 2, 1000)
		pr = np.sqrt(np.pi - x**2)
		pr[pr<0] = 1

		y = x ** 2/3 + np.e/3 * pr * np.sin(50*np.pi*x)
		plt.plot(x, y, color= 'r')



if __name__ == '__main__':
	# kw = imput("tieba name:")
	# bpage = int(input("begin page:"))
	# epage = int(input("end page:"))
	kw = "java"
	bpage = 1
	epage = 5

	url = "http://tieba.baidu.com/f?"
	# key = urllib.parse.urlencode({"kw": kw})
	key = "kw=java"

	url = url + key

	spider = crawer()
	spider.url = url
	# spider.tiebaSpider(bpage, epage)
	# spider.heart_plot()









