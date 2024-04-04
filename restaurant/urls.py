from django.urls import path 
from .import views 
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


app_name ='restaurant'

urlpatterns = [
    path('',views.index,name='index'),
    path('api/bookings/',views.BookingView.as_view()),
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.MenuRetrieveDestroyAPIView.as_view()),
    path('api/message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]
