from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from account.views import (
    user_list_create,
    user_delete,
    profile_list,
    profile_detail_update_delete
)

from edu.views import (
    climateEducation_list,
    climateFact_list,
    climateEducation_detail_update_delete,
    climateFact_detail_update_delete,
)

urlpatterns = [
    path('user/', user_list_create, name='user-list-create'),
    path('user/delete/account/', user_delete, name='user-delete'),
    path('author/', profile_list, name='profile-lsit'),
    path('author/<str:pk>/', profile_detail_update_delete,
         name='profile_detail_update_delete'),

    #  edu
    path('climate/', climateEducation_list, name='climate-list'),
    path('climate/<int:pk>/', climateEducation_detail_update_delete,
         name='climate-detail-update-delete'),
    path('climate/fact/', climateFact_list, name='climate-fact-list'),
    path('climate/fact/<int:pk>/', climateFact_detail_update_delete,
         name='climate-fact-detail-update-delete'),

    path('login/', obtain_auth_token)

]
