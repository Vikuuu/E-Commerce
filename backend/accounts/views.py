from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserAccountSerializer, UserSerializer

User = get_user_model()


class registerView(APIView):
    
    def post(self, request, format=None):
        data = request.data

        try:
            serializer = UserAccountSerializer(data=data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.create_user(serializer.validated_data)
            user = UserSerializer(user)

            return Response(user.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": "Something went wrong  " + str(e)})
