from django.urls import path
from commentapp.views import create_comment, get_all_comment_by_anime

urlpatterns = [
    path('create', create_comment),
    path('get_comments/', get_all_comment_by_anime)
]