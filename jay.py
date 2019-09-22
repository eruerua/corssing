import requests
import csv
url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg"

querystring = {"biztype":"1","topid":"237773700","cmd":"8","pagenum":"1","pagesize":"25"}

response = requests.request("GET", url, params=querystring)
comment=response.json()
commentlist=comment['comment']['commentlist']
list=[[i['nick'],i['praisenum'],i['rootcommentcontent'],i['time']]for i in commentlist]
print(list)








list.insert(0,['昵称','点赞时','评论','时间'])
with open('jay.csv','w',encoding='utf_8_sig') as f:
    cw= csv.writer(f)
    cw.writerows(list)
