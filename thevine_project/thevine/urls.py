from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('wines', views.WineList.as_view(), name='wine_list'),
    path('ratings', views.RatingList.as_view(), name='rating_list'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('wines/<int:pk>', views.WineDetail.as_view(), name='wine_detail'),
    path('ratings/<int:pk>', views.RatingDetail.as_view(), name='rating_detail'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail')
]