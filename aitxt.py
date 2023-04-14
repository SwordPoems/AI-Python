import requests
from bs4 import BeautifulSoup
import os

# ���庯��ʵ����ҳ���󣬻�ȡС˵ҳ������
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        html = response.text
        return html
    except:
        print('�����������')

# ���庯������С˵���ݺͱ���С˵
def parse_content(html, filepath):
    soup = BeautifulSoup(html, 'html.parser')
    # ��ȡС˵����
    title = soup.h1.text.strip()
    # ��ȡС˵����
    content_elem = soup.select('.read-content.j_readContent')[0]
    content = content_elem.get_text().strip()
    # ����С˵���ļ���
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(title)
        f.write('\n\n')
        f.write(content)
    print('С˵����ɹ���')


if __name__ == '__main__':
    url = 'https://read.qidian.com/chapter/cgdLbGBrMI46Q5WO_IQttQ2/JQgD55XMYMO2uJcMpdsVgA2/'
    html = get_html(url)
    # ����洢�ļ�·��
    filepath = os.path.join(os.path.abspath('.'), 'novel.txt')
    parse_content(html, filepath)
    # �򿪴洢��С˵�ļ�
    os.startfile(filepath)
