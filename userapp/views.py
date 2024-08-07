from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.mongo import MongoDB
from datetime import datetime

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
    
@api_view(['POST'])
def sign_up_user(request):
    try:
        id = request.data['id']
        if id == None:
            raise e
        pwd = request.data['password']
        now_date = datetime.now()
        insert_data = {
            "id": id, 
            'account': 'member', 
            'status':False, 
            'password': pwd,
            'create_date': now_date,
            'update_date': now_date
        }
        inserted_id = db.insert_one_data(db.db, 'users', insert_data)
        return Response({'message': "sign up finish", 'result': inserted_id})
    except Exception as e:
        return Response({'message': "sign up fail", 'result': False})
