from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Booking,Menu
from .serializers import BookingSerializer,MenuSerializer
from rest_framework.decorators import api_view
from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})



def index(request):
    return render(request,'index.html',{})

class BookingView(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items,many=True)
        return Response(serializer.data)
    
    
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieveDestroyAPIView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView ):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


