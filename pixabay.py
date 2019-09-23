import requests
from bs4 import BeautifulSoup
import time
url='https://pixabay.com'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

r=requests.get(url,headers = headers)
soup=BeautifulSoup(r.text,'html.parser')
list=soup.find_all('div',class_='item')
img_url=[]
for index,i in enumerate(list):
    img=i.find('img').get('src')
    print(img)
    try:
        pic = requests.get(img,headers = headers)
    except Exception as e:
        print(e)
    else:
        print('download')
        with open(str(index) + '.jpg', 'wb') as file:
            file.write(pic.content)
        time.sleep(3)


