from django.conf import settings
from rest_framework import generics
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import generics, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny 
from Main.models import (LessonDays, Course, Teacher, 
                         OnlineLesson, Coment, Rating)

from Main.serializers import (LessonDaysSerializer, CourseSerializer,
                               TeacherSerializer, OnlineLessonSerializer,
                               ComentSerializer, eMailSerializer,
                               RatingSerializer, UserSerializer)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=15)




class LessonDaysAPIList(ModelViewSet):
    queryset = LessonDays.objects.all()
    serializer_class = LessonDaysSerializer
    permission_classes = [AllowAny]




class CourseListAPIview(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class CourseRetUpdDesAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class TeacherAPIList(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class OnlineLessonAPIList(ModelViewSet):
    queryset = OnlineLesson.objects.all()
    serializer_class = OnlineLessonSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['theme', 'about_lesson', 'teacher__full_name', 'course__name']




class ComentAPIList(ModelViewSet):
    queryset = Coment.objects.all()
    serializer_class = ComentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class SendeMailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = eMailSerializer()
        return Response(serializer.data)


    def post(self, request):
        serializer = eMailSerializer(data=request.data)
        serializer.is_valid()

        users = User.objects.all()
        for user in users:
            subject = serializer.validated_data.get('name')
            message = f"Salom {user.username} {serializer.validated_data.get('text')}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail(subject, message, email_from, recipient_list)
        return Response({'Green Way': 'Matn yuborildi!'})




class RatingAPIview(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        serializer = RatingSerializer()
        return Response(serializer.data)


    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid()

        value = serializer.validated_data.get('like', False)
        lesson_id = serializer.validated_data.get('lesson')
        lesson = OnlineLesson.objects.get(pk=lesson_id)

        try:
            like = Rating.objects.get(lesson=lesson, user=request.user)
            like.delete()
        except Rating.DoesNotExist:
            pass

        Rating.objects.create(
            lesson=lesson,
            user=request.user,
            take_like=value,
        )
        return Response()




class RegisterAPIview(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    



class LoginAPIview(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]


    def get(self, request):
        return Response({"detail": "Autentifikatsiya ma`lumotlari taqdim etilmagan." })


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, 
                            username=username,
                            password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Hisob ma`lumotlaringiz yaroqsiz deb topildi!'})




class LogoutAPIview(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Siz muvafaqqiyatli tizimdan chiqib ketdingiz!'})




class UserProfilAPIview(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    


def home(request):
    return render(request, 'index.html')