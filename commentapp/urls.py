from django.urls import path
from commentapp.views import create_comment, get_all_comment_by_anime, get_comment_by_users

urlpatterns = [
    path('create', create_comment),
    path('get_comments/', get_all_comment_by_anime),
    path('get_comment_by_users/', get_comment_by_users)
]