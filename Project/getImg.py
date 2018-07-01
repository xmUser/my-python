#coding = utf-8
import requests
import json
import urllib
import os

# 定义本地保存路径
path = 'D:/Projects/my-python/img/'

def getImages(category, tag, number):
    imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' + category+'&tag=' + tag + '&start=9&len='+str(number))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_info = {}
        imgs_info['url'] = j['pic_url']
        imgs_info['title'] = j['title']
        # 大图
        imgs_url.append(imgs_info)
    # 小图
    # imgs_url.append(j['bthumbUrl'])
    m = 0
    # print(imgs_url)
    for img_url in imgs_url:
        print(img_url)
        url = img_url['url']
        res = requests.get(url)
        img_name = path + str(m) + img_url['title'] + '.jpg'
        with open(img_name, 'wb') as f:
            f.write(res.content)
        m += 1
    print('Download complete!')

getImages('壁纸', '全部', 100)
