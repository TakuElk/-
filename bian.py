import requests
from bs4 import BeautifulSoup


def download(url_, file_path="../img/"):
    res = requests.get(url_, stream=True)  # 获取响应体
    soup = BeautifulSoup(res.text, 'lxml')  # 解析响应体
    img_tags = soup.find_all('img')  # 查找响应中所有的img标签
    for img in img_tags:  # 遍历img标签
        src = img.get('src')  # 获取src属性
        url_ = "https://pic.netbian.com" + src  # 拼接图片地址
        img = requests.get(url_).content  # 拿第二次的响应体
        if "qq" not in src:  # 过滤掉qq图片
            with open(file_path + url_.split("/")[-1], "wb") as f:
                f.write(img)
            print(f"{url_}下载成功")


for i in range(2, 10):
    url = f"https://pic.netbian.com/4k/index_{i}.html"
    download(url)




