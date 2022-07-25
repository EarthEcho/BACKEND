from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from account.views import (
    user_list_create,
    user_delete,
    profile_list,
    profile_detail_update_delete
)

urlpatterns = [
    path('user/', user_list_create, name='user-list-create'),
    path('user/delete/account/', user_delete, name='user-delete'),
    path('author/', profile_list, name='profile-lsit'),
    path('author/<str:pk>/', profile_detail_update_delete,
         name='profile_detail_update_delete'),

    path('login/', obtain_auth_token)

]
