from django.urls import path
from userapp.views import check_unique_id, sign_up_user

urlpatterns = [
    path("check_id", check_unique_id),
    path("signup", sign_up_user)
]
