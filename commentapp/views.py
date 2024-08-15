from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment

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