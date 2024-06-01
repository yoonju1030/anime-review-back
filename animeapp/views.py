from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.mongo import MongoDB

db = MongoDB()

# Create your views here.
@api_view()
def hello_world(request):
    return Response({"message": "hello world"})

@api_view()
def get_anime(request): 
    try:
        result = db.get_many_data(db.db, "anime", {"genres": ["스포츠", '드라마']})
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
        return Response({"message": anime})
    except Exception as e:
        raise e