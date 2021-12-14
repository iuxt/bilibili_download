import requests
import os
import sys
import dotenv

dotenv.load_dotenv()

def get_vlist(user_id, num_per_page, page=1):
    r=requests.get('https://api.bilibili.com/x/space/arc/search?mid=%s&ps=%s&tid=0&pn=%s&keyword=&order=%s&jsonp=jsonp' % (user_id, num_per_page, page, os.getenv("order")))
    content = r.json()

    return content['data']['list']['vlist']

def download(vlist):
    video_url = "https://www.bilibili.com/video/%s" % vlist['bvid']
    print(vlist['title'])
    print(video_url)
    if os.getenv("download_pic") == "yes":
        print(vlist['pic'])


if __name__ == "__main__":

    num_per_page = os.getenv("num_per_page")
    user_id = os.getenv("user_id")
    page = 1

    while True:
        vlist = get_vlist(user_id, num_per_page, page)

        if not vlist:
            sys.exit(0)

        print("===============================================当前是第" + str(page) + "页=====================================================")

        for i in vlist:
            download(i)
        page += 1
