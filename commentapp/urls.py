from django.urls import path
from commentapp.views import create_comment

urlpatterns = [
    path('create', create_comment)
]