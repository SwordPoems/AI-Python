import requests
from bs4 import BeautifulSoup
import os
# https://read.qidian.com/chapter/cgdLbGBrMI46Q5WO_IQttQ2/JQgD55XMYMO2uJcMpdsVgA2/对这个网址使用python写一个网文爬虫，爬取小说标题和内容，并在代码运行完之后自动打开存储的文件
# 定义函数实现网页请求，获取小说页面内容
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        html = response.text
        return html
    except:
        print('网络请求错误！')

# 定义函数解析小说内容和保存小说
def parse_content(html, filepath):
    soup = BeautifulSoup(html, 'html.parser')
    # 获取小说标题
    title = soup.h1.text.strip()
    # 获取小说内容
    content_elem = soup.select('.read-content.j_readContent')[0]
    content = content_elem.get_text().strip()
    # 保存小说到文件中
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(title)
        f.write('\n\n')
        f.write(content)
    print('小说保存成功！')


if __name__ == '__main__':
    url = 'https://read.qidian.com/chapter/cgdLbGBrMI46Q5WO_IQttQ2/JQgD55XMYMO2uJcMpdsVgA2/'
    html = get_html(url)
    # 定义存储文件路径
    filepath = os.path.join(os.path.abspath('.'), 'novel.txt')
    parse_content(html, filepath)
    # 打开存储的小说文件
    os.startfile(filepath)
