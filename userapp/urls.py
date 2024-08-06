from django.urls import path
from userapp.views import check_unique_id

urlpatterns = [
    path("check_id", check_unique_id),
]
