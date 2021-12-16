import requests
import os
import sys
import dotenv
import shutil
import youtube_dl

dotenv.load_dotenv()

def get_vlist(user_id, num_per_page, page=1):
    r=requests.get('https://api.bilibili.com/x/space/arc/search?mid=%s&ps=%s&tid=0&pn=%s&keyword=&order=%s&jsonp=jsonp' % (user_id, num_per_page, page, os.getenv("order")))
    content = r.json()

    return content['data']['list']['vlist']

def download(vlist):
    print(vlist['title'])

    if os.getenv("download_pic") == "yes":
        print(vlist['pic'])

        image_file = "download/images/" + vlist['title'] + "." + vlist['pic'].split(".")[-1]
        r = requests.get(vlist['pic'], stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(image_file, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            print("ERROR download pic")
    
    if os.getenv("download_video") == "yes":
        video_url = "https://www.bilibili.com/video/%s" % vlist['bvid']
        video_file = "download/videos/" + vlist['title'] + ".flv"
        print(video_url)

        ydl_opts = {
            'outtmpl': video_file,
            'ignoreerrors': True,
            'continue_dl': True,
            'retries': 10,
        }

        if os.getenv("aria2c_enabled") == 'yes':
            ydl_opts["external_downloader"] = "aria2c"
            ydl_opts["external_downloader_args"] = ["-x", "16", "-k", "1M"]

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])



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
