import re
import requests
import _thread
m=0
page=input('请输入页数：')
url='https://www.qiushibaike.com/imgrank/page/%d/'%int(page)
r= requests.get(url)
string=re.compile(r'pic.qiushibaike.com/system/pictures/.*?.jpg')
result=re.findall(string,r.text)
print('There are %d images in page %s'%(len(result),page))
#下载函数
def downloadImage(url,i):
    try:
        r=requests.get('http://'+url)
        with open('corssing/%d.jpg'%i,'wb') as f:
            f.write(r.content)
    except Exception as e:
        print(e)
    else:
        print('image %d is finished\n'%i)
        global m #记录下载照片的数量，如果下载完毕，提示按下enter键
        m+=1
        if m==len(result):
            print('All image are finished,you can press ENTER to exit')
#爬虫线程
for i in range(len(result)):
    _thread.start_new_thread(downloadImage, (result[i],i,))
#防止图片未下完就退出程序
input('press ENTER to exit...\n')
