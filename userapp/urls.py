from django.urls import path
from userapp.views import check_unique_id, sign_up_user, log_in_user, log_out_user, test

urlpatterns = [
    path("check_id", check_unique_id),
    path("signup", sign_up_user),
    path("login", log_in_user),
    path("logout", log_out_user),
    path("test", test)
]
