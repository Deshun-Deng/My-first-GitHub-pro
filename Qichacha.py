import time
import random
import requests
from bs4 import BeautifulSoup
from lxml import etree


class Spider:
    def __init__(self):
        self.url = "https://www.qcc.com/web/search?key="
        sess = requests.session()
        headers = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4455.2 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                   "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"]
        # 添加headers（header为自己登录的企查查网址，输入账号密码登录之后所显示的header，此代码的上方介绍了获取方法）
        self.afterLogin_headers = {'User-Agent': random.choice(headers)}

        # post请求(代表着登录行为，登录一次即可保存，方便后面执行查询指令)
        login = {'user': '13660624376', 'password': '101010dds'}
        sess.post('https://www.qcc.com', data=login, headers=self.afterLogin_headers)
        self.sess = sess

    def read_write(self):
        with open("company.csv", 'r') as fp:
            line = fp.readline()
            while line:
                line = fp.readline().strip()
                message = ''
                if line:
                    message = self.get_company_message(line)
                    if message == "失败":
                        message = self.get_company_message(line)
                        print('尝试第2次--'+line)
                    message = message.replace('\t', '')
                    message = message.replace('\n', '')
                with open("company_info.csv", 'a+') as f:
                    f.writelines([line+'\t', message+'\n'])

    def get_company_message(self, company):

        # 获取查询到的网页内容（全部）
        try:
            search = self.sess.get('https://www.qcc.com/search?key={}'.format(company), headers=self.afterLogin_headers, timeout=10)
            search.raise_for_status()
            search.encoding = 'utf-8'  # linux utf-8
            # soup = BeautifulSoup(search.text, features="html.parser")
            # href = soup.find_all('a', {'class': 'title'})[0].get('href')
            search_page = etree.HTML(search.text)
            href = search_page.xpath('//div[@class="maininfo"]/a/@href')[0]
            # print(href)
            # return
            time.sleep(random.randrange(1,4))
            # 获取查询到的网页内容（全部）
            details = self.sess.get(href, headers=self.afterLogin_headers, timeout=10)
            details.raise_for_status()
            details.encoding = 'utf-8'  # linux utf-8
            # details_soup = BeautifulSoup(details.text, features="html.parser")
            # message = details_soup.text
            details_page = etree.HTML(details.text)
            message = details_page.xpath('//*[@id="desc_content"]/text()')[0]
            # print(message)
            # return
            time.sleep(random.randrange(1,4))
            print(f"{company}--done!")
            return message
        except Exception as e:
            print(f"{company}--not done!")
            return "失败"

spider = Spider()
spider.read_write()