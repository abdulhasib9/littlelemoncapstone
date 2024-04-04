from django.urls import path 
from .import views 

app_name ='restaurant'

urlpatterns = [
    path('',views.index,name='index'),
    path('api/bookings/',views.BookingView.as_view())
]
