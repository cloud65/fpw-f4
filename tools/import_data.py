import json
import base64
#exec(open('tools\import_data.py').read())
from eda.models import *

file_name = r'C:\Users\sedaiko\Documents\tmp-py\data.json'
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f)

cache_cat = dict()
cache_ing = dict()

for d in data:
    eda = Eda.objects.create(name=d['name'])

    for cat in d['cat']:
        if cache_cat.get(cat) is None:
            cache_cat[cat] = Categories(name=cat)
            cache_cat[cat].save()
        cache_cat[cat].eda.add(eda)

    for ing in d['datail']['ingredients']:
        if cache_ing.get(ing['name']) is None:
            cache_ing[ing['name']] = Ingredients.objects.create(name=ing['name'])
        EdaIngredients.objects.create(eda=eda, ingredient=cache_ing[ing['name']], count=ing['count'])

    for item in d['datail']['items']:
        step=int(item['step'])
        image = base64.b64decode(item['img'].encode('ascii')) if not item['img'] is None else None
        EdaItems.objects.create(eda=eda, step=step, text=item['text'], image=image)

for cat in cache_cat.values():
    cat.save()



