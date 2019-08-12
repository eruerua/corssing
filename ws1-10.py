import requests
import re
from lxml import etree
n=int(input('请输入要爬取的页数：'))
def gender(s):
    if s =='womenIcon':
        return '女'
    else:
        return '男'

url='https://www.qiushibaike.com/hot/page/'
def get_content(url):
    r=requests.get(url)
    html=r.text
    html=html.replace('<br>',"")
    html=html.replace('<br/>',"")
    html=html.replace('<br />',"")
    tree=etree.HTML(html)
    author=tree.xpath('//div[@class="author clearfix"]//h2//text()')
    content=tree.xpath('//div[@class="content"]//span//text()')
    laugh=tree.xpath('//span[@class="stats-vote"]//i//text()')
    comm=tree.xpath('//span[@class="stats-comments"]//i//text()')
    author=[x.strip('\n') for x in author]
    content=[x.strip('\n') for x in content]
    string=re.compile(r'<div class="articleGender (.+?)">(.+?)</div>')
    gender_age=re.findall(string,html)
    genders=[ gender(x) for x in gender_age ]
    age=[x[1] for x in gender_age]
    result=''
    for i in range(len(author)):
        result+='作者：{} 性别: {} 年龄：{}'.format(author[i],genders[i],age[i])
        result+='\n'
        result+=content[i]
        result+='\n'
        result+='好评数：{} 评论: {} '.format(laugh[i],comm[i])
        result+='\n'
        result+='\n'
    return result
result=''
for i in range(1,n+1):
    url+='{}/'.format(i)
    result+=get_content(url)
with open('corssing/result.txt','w') as f:
    f.write(result)
