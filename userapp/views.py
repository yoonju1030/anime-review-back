from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.mongo import MongoDB
from datetime import datetime
from .serialize import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status

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

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            
            return res
        else:
            raise e
    except Exception as e:
        return Response({'message': "sign up fail", 'result': False})
    
@api_view(['POST'])
def log_in_user(request):
    try:
        pass
    except Exception as e:
        raise e
    
@api_view(["POST"])
def log_out_user(request):
    try:
        pass
    except Exception as e:
        raise e
    
