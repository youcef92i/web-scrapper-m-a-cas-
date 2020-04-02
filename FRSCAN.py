import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

os.chdir(r"C://Users//Lenovo//Nsi")

trunk="https:"

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Img = soup.findAll('img')
    ListeLiens = []
    for item in Img:
        if 'class' in item.attrs and item['class'] == ['img-responsive']:
            a= item['data-src']
            d = a.strip(" ")
            b= trunk+d
            ListeLiens.append(b)
    return ListeLiens


def Next(soup,url):
    a=reste(url)
    b=num(url)
    NextUrl=a+str(b+1)
    f=str(NextUrl)
    if RecupListeLiens(soup) == []:
        NextUrl = "fin du manga"
        print (NextUrl)
    else:
        print(NextUrl)
    return NextUrl


def num(url):
    var = url.split('/')[-1]
    return int(var)

def reste(url):
    var=url.split(str(num(url)))[0]
    return var







