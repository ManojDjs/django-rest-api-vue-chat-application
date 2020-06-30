from .serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
class CustomUserview(APIView):
    def get(self,request):
        serialize=CustomUserSerializer(request.user)
        return Response(serialize.data)
