from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from utils.mongo import MongoDB

db = MongoDB()

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request):
    try:
        anime_id = request.data.get('animeId')
        user_id = request.data.get("userId")
        content = request.data.get('content')
        Comment.objects.create(
            user_id=user_id,
            content=content,
            anime=anime_id
        )
        response = Response({"result": status.HTTP_200_OK})
        return response
    except Exception as e:
        return Response({'message': "create comment fail", 'result': False})
    
@api_view(["POST"])
def get_all_comment_by_anime(request):
    try:
        anime_id = request.data.get('animeId')
        result = db.get_many_data(db.db, "commentapp_comment", {"anime": anime_id})
        comments = [{"comment": a['content'], "user_id": a['user_id'], "created_at": a['created_at']} for a in result]
        return Response({'message': "Success to get comments", 'result':comments})
    except Exception as e:
        return Response({'message': "Fail to get comment", 'result': False})