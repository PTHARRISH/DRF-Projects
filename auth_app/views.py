from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class BaseView(APIView):
    permission_classes = (IsAuthenticated,)


class HomeView(BaseView):
    def get(self, request):
        content = {"message": "Login Successfully"}
        return Response(content)


class UserDetails(BaseView):
    def get(self, request):
        user = request.user
        user_data = {
            "username": user.username,
            "phone_number": user.phone_number,
            "email": user.email,
        }
        return Response(user_data, status=status.HTTP_200_OK)
