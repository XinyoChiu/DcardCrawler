import os
import re
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

class Crawler:
    def __init__(self, URL):
        self.URL = URL
        self.imgs_url = []
        # 版規圖
        self.exclude = ['https://imgur.dcard.tw/JVwAaY4.jpg',
                        'https://imgur.dcard.tw/kHP8nkk.jpg',
                        'https://imgur.dcard.tw/z0drHeZ.jpg',
                        'https://imgur.dcard.tw/jPSyH0t.jpg',
                        'https://imgur.dcard.tw/ytnjMUQ.jpg',
                        'https://imgur.dcard.tw/jPSyH0t.jpg',
                        'https://imgur.dcard.tw/ytnjMUQ.jpg',
                        'https://imgur.dcard.tw/ABJ0tVW.jpg',
                        'https://imgur.dcard.tw/Z6bPPGI.jpg',
                        'https://imgur.dcard.tw/eJBwBnZ.jpg',
                        'https://imgur.dcard.tw/WRI4X3w.jpg',
                        'https://imgur.dcard.tw/hoolY37.jpg',
                        'https://imgur.dcard.tw/Re3pRYi.jpg',
                        'https://imgur.dcard.tw/G5oLLN0.jpg']
    def get_id(self):
        rs = requests.get(self.URL, headers=headers, verify=False)
        with open('index.txt') as file:
            index = file.readline()
        if index == '0':
            pattern = re.compile(r'/f/sex/p/(\d+)-')
        else:
            pattern = re.compile(r'{"id":(\d+),')
        all_id = pattern.findall(rs.text)
        return all_id
    def download_imgs(self):
        # Create Folder
        if os.path.exists(r'.\img') == False:
            os.makedirs(r'.\img')

        ids = self.get_id()
        for id in ids:
            with open('id.txt', 'w+') as file:
                file.write(str(id))
            link = "https://www.dcard.tw/f/sex/p/{}-".format(id)
            rs = requests.get(link, headers=headers, verify=False)
            pattern = re.compile(r'https://imgur.dcard.tw/\w+.jpg')
            imgs = pattern.findall(rs.text)
            self.imgs_url.append(imgs)

        with open('index.txt') as tmp:
            index = tmp.readline()

        for imgs in self.imgs_url:
            for item in imgs:
                index = int(index) + 1
                img = "./img/" + str(index) + ".jpg"
                if item in self.exclude:
                    continue
                html = requests.get(item, verify=False)
                with open(img, 'wb') as file:
                    file.write(html.content)
                    file.flush()
                with open('index.txt', 'w+') as file:
                    file.write(str(index))

def main():
    URL = "https://www.dcard.tw/f/sex"
    sex = Crawler(URL)
    sex.download_imgs()
    with open('id.txt') as file:
        id = file.readline()
    URL = "https://www.dcard.tw/_api/forums/sex/posts?popular=true&limit=100&before={}".format(id)

if __name__ == '__main__':
    for i in range(10):
        main()