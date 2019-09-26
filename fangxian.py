# -*- coding = utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import csv
url='http://www.chinafx.gov.cn/Gov/list.asp?page=1&id=31&classid=6'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

r=requests.get(url,headers = headers)
soup=BeautifulSoup(r.text.encode('ISO-8859-1'),'html.parser')
link=soup.find_all('a')
list=[ [i['href'],i.get_text()] for i in link if 'Article' in i['href']]
print(len(list))

def get_list(url):
    url = url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text.encode('ISO-8859-1'), 'html.parser')
        link = soup.find_all('a')
        list = [[i['href'], i.get_text()] for i in link if 'Article' in i['href']]
        print('finished!')
        return list
    except Exception as e:
        print(e)
        return 'None'

a_list=[]
for i in range(1,52):
    url='http://www.chinafx.gov.cn/Gov/list.asp?page={}&id=31&classid=6'.format(i)
    a_list.extend(get_list(url))
    time.sleep(3)
print(a_list)
with open('fx.csv','w',encoding='utf_8_sig') as f:
    cw= csv.writer(f)
    cw.writerows(a_list)