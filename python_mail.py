import time
import random
import requests
import numpy as np
import matplotlib.pyplot as plt
import schedule


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
		receiver = 'PauulParker@gmail.com'  # 设置邮件接收人，可以是扣扣邮箱
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

	def job(self):
		print("hello world!")

	def sche_foes(self):

		# schedule.every(10).minutes.do(self.job)
		# schedule.every().hour.do(self.job)
		# schedule.every().day.at("10:30").do(self.job)
		# schedule.every(5).to(10).minutes.do(self.job)
		# schedule.every().monday.do(self.job)
		# schedule.every().wednesday.at("13:15").do(self.job)
		schedule.every().minute.at(":17").do(self.job)
		n = 0
		while True:
			schedule.run_pending()
			time.sleep(1)


class Dprossing:
	'''dp找出最长递减子序列'''
	def __init__(self):
		self.height = [300, 207, 155, 398, 299, 170, 158, 65]

	def dp_processing(self):
		num_hgt = len(self.height)
		dp = [1]*num_hgt
		dp2 = [1]*num_hgt
		trace = [[i] for i in self.height]
		trace2 = [[i] for i in self.height]
		for i in range(1, num_hgt):
			for j in range(i):
				if self.height[i] < self.height[j]:
					submax = max(dp[i], dp[j]+1)
					if submax > dp[i]:
						dp[i] = submax
						trace[i] = trace[j] + [self.height[i]]
				else:
					submax = max(dp2[i], dp2[j] + 1)
					if submax > dp2[i]:
						dp2[i] = submax
						trace2[i] = trace2[j] + [self.height[i]]
		print("done")
		for i in range(num_hgt):
			print(f"{dp[i]}: {trace[i]}")
		print("#"*100)
		for i in range(num_hgt):
			print(f"{dp2[i]}: {trace2[i]}")


solution = Dprossing()
solution.dp_processing()









