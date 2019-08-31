import requests
city=input("请输入城市名称：")

url='https://api.seniverse.com/v3/weather/now.json?key='+key+'&location='+city+'&language=zh-Hans&unit=c'
r = requests.get(url)
message=r.json()
print(message)
print('%s今天天气为%s,温度为%s摄氏度'%(message['results'][0]['location']['name'],message['results'][0]['now']['text'],message['results'][0]['now']['temperature']))