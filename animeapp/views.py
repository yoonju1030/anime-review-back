from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.mongo import MongoDB
from bson.objectid import ObjectId
from random import shuffle

db = MongoDB()

# Create your views here.
@api_view()
def hello_world(request):
    return Response({"message": "hello world"})

@api_view()
def get_anime(request): 
    try:
        result = db.get_many_data(db.db, "anime",{"genres": {"$in":["스포츠", '드라마']}})
        anime = []
        for a in result:
            obj = {
                "id":str(a['_id']), 
                "Name": a['name'], 
                'Image': a['image'], 
            }
            anime.append(obj)
        
        for a in range(len(anime)):
            anime[a]["idx"] = a
        shuffle(anime)
        res = Response({"message": anime})
        res["Access-Control-Allow-Origin"]="*"
        return res
    except Exception as e:
        raise e
    
@api_view(["POST"])
def get_info(request):
    try:
        id = request.data['id']
        result = db.get_one_data(db.db, 'anime', {"_id": ObjectId(id)})
        anime = {
            "name": result['name'],
            "airYearQuarter": result['air_year_quarter'],
            "content": result['content'],
            "contentRating": result['content_rating'],
            "ended": result['ended'],
            'genres': result['genres'],
            "tags": result['tags'],
            "image": result['image']
        }
        return Response({"message": anime})
    except Exception as e:
        raise e