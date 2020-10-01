from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, MobileUserRegisterSerializer, MobileUserLoginSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "You have been registered successfully as admin user"
        })

class LoginAPI(generics.GenericAPIView):    
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _,token = AuthToken.objects.create(user) # The Token.objects.create returns a tuple (instance, token). So in order to get token use the index 1
        return JsonResponse({
            "user": UserSerializer(user).data,
            "token": token
        })

class MobileUserRegisterAPI(generics.GenericAPIView):
    serializer_class = MobileUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = MobileUserRegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "You have been registered successfully as an android/ios user"
        })

class MobileUserLoginAPI(generics.GenericAPIView):    
    serializer_class = MobileUserLoginSerializer
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _,token = AuthToken.objects.create(user) # The Token.objects.create returns a tuple (instance, token). So in order to get token use the index 1
        return JsonResponse({
            "user": UserSerializer(user).data,
            "OTP": 'This is OTP'
        })