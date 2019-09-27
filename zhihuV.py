import requests

url_1 = 'https://www.zhihu.com/api/v4/members/'
url_2 = '/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&limit=20&offset=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/people/hou-hao-82/following',
    'Cookie': '_zap=d5d4f958-165b-4b92-ac25-b4368dd0f636; d_c0="AHAhNJROtg6PTgsLf9VX1XotGnMFk0JBVM0=|1545532580"; _xsrf=279f4dc4-a6b2-4828-929e-2d99e9a48b60; tst=r; q_c1=300abcd6bdff4be381c0cd88834b5018|1568039933000|1545532583000; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569339688,1569372187,1569380913,1569591439; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569591439'
}

to_crawl = ['hou-hao-82']
crawled = []

def get_following(user):
    print('crawling', user)
    global to_crawl, crawled
    url = url_1 + user + url_2
    for i in range(10):
        req = requests.get(url=url, headers=headers)
        data = req.json()

        for user in data['data']:
            if user['follower_count'] > 600000:
                token = user['url_token']
                if token not in to_crawl and token not in crawled:
                    print(user['name'])
                    to_crawl.append(token)

        paging = data['paging']
        if paging['is_end']:
            break
        url = paging['next'].replace('https://www.zhihu.com', 'https://www.zhihu.com/api/v4')
        print(url)
    print(to_crawl)
    print(crawled)

while len(to_crawl) > 0:
    user = to_crawl.pop()
    crawled.append(user)
    get_following(user)

