from time import sleep
from random import randint
import json
from requests import  get as request_get
from bs4 import BeautifulSoup
import requests 
import base64


def headers():
    headers = dict()
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    return headers

def get_detail(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    items = soup.find(class_='emotion-yj4j4j').find(class_='emotion-13pa6yw').find_all(class_='emotion-7yevpr')
    ingredients = []
    for item in items:
        name = item.find(class_='emotion-1g8buaa').text
        count = item.find(class_='emotion-15im4d2').text
        ingredients.append(dict(name=name, count=count))
    
    items = []
    items_soup = soup.find_all(attrs={"itemprop" : "recipeInstructions"})
    for item in items_soup:
        step_tag = item.find(class_='emotion-bzb65q')
        if (step_tag is None):
            continue
        step = step_tag.text
        text = item.find(class_='emotion-6kiu05').text
        img = item.find('img')
        img_data = base64.encodebytes(requests.get(img.attrs['src']).content).decode('utf-8') if not img is None else None
        items.append(dict(step=step, text=text, img=img_data))
    return dict(ingredients=ingredients, items=items)


def parse(url, page=1):
    items = list()
    page_url = f"{url}/recepty?page={page}"
    
    resp = request_get(page_url, headers=headers())
    soup = BeautifulSoup(resp.text, 'lxml')
    
    recepty = soup.find_all(class_='emotion-etyz2y')
    urls = []
    for recept in recepty:
        categories = [i.text for i in recept.find(class_='emotion-1pet44l').find_all('a')]
        a = recept.find(class_='emotion-1eugp2w').find('a')
        page_url = f"{url}{a.attrs['href']}"
        datail = get_detail(request_get(page_url, headers=headers()))
        print(a.text)
        items.append(dict(name=a.text, datail=datail, cat=categories))
    
    return items
    
if __name__=="__main__":
    url = "https://eda.ru"
    
    result = []
    for i in range(1,30):
        result += parse(url, i)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    print(len(result))