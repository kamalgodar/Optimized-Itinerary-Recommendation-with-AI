from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer, UserPasswordUpdateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserPasswordUpdate(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer

