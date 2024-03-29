from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from .models import Profile

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Message': 'No user'})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user.pk
        profile = User.objects.get(pk=user)
        if profile:
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_404_NOT_FOUND)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Message': 'No Profile.'})


class ProfileRetrieveUpdate(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return None

    def get(self, request, pk):
        profile = self.get_object(pk)
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        if profile:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_404_NOT_FOUND)


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
            'author_id': user.user_profile.id,
            'email': user.email,
            'username': user.username
        })


user_list_create = UserAPIView.as_view()
user_delete = UserDeleteAPIView.as_view()
profile_list = ProfileAPIView.as_view()
profile_detail_update = ProfileRetrieveUpdate.as_view()


