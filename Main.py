import os
from Module.ImgCrawler import *

URL = "https://www.dcard.tw/f/sex"
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
exclude = ['https://imgur.dcard.tw/JVwAaY4.jpg',
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
index_file = "index.txt"
id_file = "id.txt"
img_folder = "./img/"

def main():
    index = get_key(index_file)
    id_lst = get_id(URL, header, index)
    urls = get_img_urls(header, id_lst, id_file)
    download_img(urls, header, exclude, img_folder, index, index_file)

if __name__ == '__main__':
    # Create Folder
    if os.path.exists(r'.\img') == False:
        os.makedirs(r'.\img')
    for i in range(20):
        print("第 {} 次迴圈".format(i))
        main()
        id = get_key(id_file)
        URL = "https://www.dcard.tw/_api/forums/sex/posts?popular=true&limit=100&before={}".format(id)
