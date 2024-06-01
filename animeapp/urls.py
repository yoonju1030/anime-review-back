from django.urls import path
from animeapp.views import hello_world, get_anime, get_info

urlpatterns = [
    path("hello_world/", hello_world),
    path("get_anime/", get_anime),
    path("get_info", get_info)
]
