from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.mongo import MongoDB

db = MongoDB()

@api_view(['POST'])
def check_unique_id(request):
    try:
        id = request.data['id']
        result = db.get_one_data(db.db, 'users', {"id": id})
        status = False
        if result == None: 
            status = True
        return Response({"result": status})
    except Exception as e:
        raise e