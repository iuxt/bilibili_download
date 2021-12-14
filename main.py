import requests
import os
import sys

def get_vlist(user_id, num_per_page, page=1):
    r=requests.get('https://api.bilibili.com/x/space/arc/search?mid=%s&ps=%s&tid=0&pn=%s&keyword=&order=pubdate&jsonp=jsonp' % (user_id, num_per_page, page))
    content = r.json()

    return content['data']['list']['vlist']

def download(vlist):
    video_url = "https://www.bilibili.com/video/%s" % vlist['bvid']
    print(vlist['title'])
    print(video_url)
    print(vlist['pic'])

if __name__ == "__main__":
    ### 配置
    num_per_page = 30
    user_id = 408287624
    page = 1

    while True:
        vlist = get_vlist(user_id, num_per_page, page)

        if not vlist:
            sys.exit(0)

        print("===============================================当前是第" + str(page) + "页=====================================================")

        for i in vlist:
            download(i)
        page += 1
