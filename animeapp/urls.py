from django.urls import path
from animeapp.views import hello_world, get_anime

urlpatterns = [
    path("hello_world/", hello_world),
    path("get_anime/", get_anime)
]
