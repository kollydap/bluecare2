from rest_framework import generics
from .models import Tested
from .serializers import TestedSerializer
from rest_framework.permissions import BasePermission,IsAdminUser,IsAuthenticated, AllowAny

class TestedList(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Tested.objects.all()
    serializer_class = TestedSerializer

class TestedDetail(generics.RetrieveAPIView):
    queryset = Tested.objects.all()
    serializer_class = TestedSerializer


