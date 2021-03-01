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

	# spider = crawer()
	# spider.url = url
	# spider.tiebaSpider(bpage, epage)
	# spider.heart_plot()

from HTMLTEXT import *
class pymail:
	def python_mail(self):
		# coding:utf-8

		import smtplib
		from email.mime.text import MIMEText  # 引入smtplib和MIMEText

		host = 'smtp.163.com'  # 设置发件服务器地址
		port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
		sender = 'yagmail_mypymail@163.com'  # 设置发件邮箱，一定要自己注册的邮箱
		pwd = 'DUKVWBTAZLXGPVZH'  # 设置发件邮箱的密码，等会登陆会用到
		receiver = 'ahahaemiliod@163.com'  # 设置邮件接收人，可以是扣扣邮箱
		body = '<h1>Hi</h1><p>test</p>'  # 设置邮件正文，这里是支持HTML的

		msg = MIMEText(html, 'html')  # 设置正文为符合邮件格式的HTML内容
		msg['subject'] = 'Hello world'  # 设置邮件标题
		msg['from'] = sender  # 设置发送人
		msg['to'] = receiver  # 设置接收人

		try:
			s = smtplib.SMTP(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
			s.login(sender, pwd)  # 登陆邮箱
			s.sendmail(sender, receiver, msg.as_string())  # 发送邮件！
			print('Done')
		except smtplib.SMTPException:
			print('Error')
if __name__ == '__main__':
    mail = pymail().python_mail()









