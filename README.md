# 哔哩哔哩下载

## 项目说明

这个项目可以下载到一个up主的所有视频  
防止b站封ip，采用分页加载的方式， 支持获取视频标题， 可以同时下载视频封面  
目前没有添加多进程下载的功能，多个视频同时下载不知道会不会被b站封ip  

## 快速开始

1. 修改配置文件
    复制`.env.example` 到 `.env`，修改userid为对应up主的id  

2. 安装Python
3. 安装Python依赖包

    ```bash
    pip install -r requirements.txt
    ```

4. 开始下载

    ```bash
    python3 main.py
    ```
