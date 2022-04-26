import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smarttourist.settings")

import django
django.setup()

from map.models import Place,Genre
from django.contrib.gis.geos import Point
import uuid
from django.core.files.base import ContentFile
import base64
import csv

def csv_to_image(data):
    print(data)
    if data == "":
        f = open("default_base64.txt")
        data = f.read()
        f.close()
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr),name=str(uuid.uuid4())+'.'+ext)
    return data

with open('../Datasets/final_dest_nepal_with_duplicates_removed.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        txt = row['genre'][1:-1]
        genres = txt.split(",")
        place, created = Place.objects.get_or_create(id=row['dest_id'],name=row['title'],description=row['genre'],photo=csv_to_image(row['img_url']),location=Point(float(row['longitude']),float(row['latitude'])))
        if row['genre']:
                for genre in row['genre'].split(sep=":"):
                    g = Genre.objects.get_or_create(name=genre)[0]
                    place.genres.add(g)
        place.save()
