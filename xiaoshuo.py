#coding: gb18030

import requests
from bs4 import BeautifulSoup
def link_one():
    link = "https://www.biqudao.com/bqge19126"
    res =requests.get(link)
    res.encoding='gb18030'
    soup =BeautifulSoup(res.text,"lxml")
    list=[]
    ls = soup.find("div",id="list")
    for i in ls.find_all('a'):
          adr = i.get('href')
          list.append(adr)
    list.sort()
    return list
def huoqu(link):
    res = requests.get(link)
    res.encoding = 'gb18030'
    #print(res.text)
    soup=BeautifulSoup(res.text,"lxml")
    print(soup)
    title = soup.find("div",class_="bookname").get_text()
    print(title)
    t = title.find('h1').get_text()
    print(t)
    txt = soup.find("div",id="content").get_text("\n","<br>")
    print(title)
    print(txt)
def link():
    link = "https://www.biqudao.com"
    ls=link_one()
    for i in ls:
        adr = link+str(i)
        huoqu(adr)
link()




