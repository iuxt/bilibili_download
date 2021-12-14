# 哔哩哔哩下载

## 项目说明

这个项目可以获取到一个up主的所有视频链接，（下载视频调用的是[youtube-dl](https://github.com/ytdl-org/youtube-dl)）  
防止b站封ip，采用分页加载的方式， 支持获取视频标题， 可以同时下载视频封面

## 快速开始

1. 下载youtube-dl
    下载[youtube-dl](https://github.com/ytdl-org/youtube-dl)到当前脚本所在目录，linux需要修改为可执行权限

2. 修改配置文件
    复制`.env.example` 到 `.env`，修改userid为对应up主的id  

3. 安装Python
4. 安装Python包

    ```bash
    pip install -r requirements.txt
    ```

5. 开始下载

    ```bash
    python3 main.py
    ```
