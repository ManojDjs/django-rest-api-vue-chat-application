from .serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
class CustomUserview(APIView):
    def get(self,request):
        serialize=CustomUserSerializer(request.user)
        return Response(serialize.data)
class Usersview(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer