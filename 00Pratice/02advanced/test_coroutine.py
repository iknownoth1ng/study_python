import asyncio
import requests


async def download_image(ur1):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动化切换到其他任务）
    print("开始下载：", ur1)

    loop = asyncio.get_running_loop()
    # requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
    future = loop.run_in_executor(None, requests.get, ur1)

    response = await future
    print("下载完成")
    # 图片保存到本地文件
    file_name = ur1.rsplit("_")[-1]
    with open(file_name, mode="wb") as file_object:
        file_object.write(response.content)


if __name__ == "__main__":
    url_list = [
        "https://car2.autoimg.cn/cardfs/product/g30/M0B/07/4E/1400x0_1_q95_autohomecar__ChxknGNsfhSALeWKAAbD352xoh0016.jpg",
        "https://car3.autoimg.cn/cardfs/product/g30/M01/5A/C8/1400x0_1_q95_autohomecar__ChsFJ2NsfhWAYM11AAbaasHf4YU139.jpg",
        "https://car3.autoimg.cn/cardfs/product/g30/M01/07/4E/1400x0_1_q95_autohomecar__ChxknGNsfhSAQIchAAaXwNPGCb4158.jpg",
    ]

    tasks = [download_image(ur1) for ur1 in url_list]
    
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(asyncio.wait(tasks))
