import re
import requests

def get_key(path):
    with open(path) as file:
        key = file.readline()
    return key

def write_file(path, key):
    with open(path, 'w+') as file:
        file.write(str(key))

def get_id(url, header, index):
    rs = requests.get(url, headers=header, verify=False)
    if index == '0':
        pattern = re.compile(r'/f/sex/p/(\d+)-')
    else:
        pattern = re.compile(r'{"id":(\d+),')
    id_lst = pattern.findall(rs.text)
    return id_lst

def get_img_urls(header, id_lst, id_path):
    img_urls = []
    for id in id_lst:
        write_file(id_path, id)
        link = "https://www.dcard.tw/f/sex/p/{}-".format(id)
        rs = requests.get(link, headers=header, verify=False)
        pattern = re.compile(r'https://imgur.dcard.tw/\w+.jpg')
        imgs = pattern.findall(rs.text)
        img_urls.append(imgs)
    return img_urls

def download_img(urls, header, exclude, img_folder, index, index_path):
    for imgs in urls:
        for item in imgs:
            index = int(index) + 1
            img = img_folder + str(index) + ".jpg"
            if item in exclude:
                continue
            html = requests.get(item, headers=header, verify=False)
            with open(img, 'wb') as file:
                file.write(html.content)
                file.flush()
            write_file(index_path, index)
