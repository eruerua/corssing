import requests
import re
from lxml import etree
url='http://www.waduanzi.com/'
r=requests.get(url)
html=r.text
html=html.replace('<br>',"")
html=html.replace('<br/>',"")
tree=etree.HTML(html)
result=tree.xpath('//div[@class="item-content"]//text()')
for div in result:
    print(div)
    print('========')
