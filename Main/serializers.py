from rest_framework import serializers
from .models import LessonDays, Course, Teacher, OnlineLesson, Coment, Rating
from django.contrib.auth.models import User




class LessonDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDays
        fields = ['id', 'name']



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'about', 'duration', 'added_at', 'lesson_days']



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user_id', 'photo', 'full_name', 'phone', 'address', 'experience']



class OnlineLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineLesson
        fields = ['id', 'course', 'teacher', 'lesson_vid', 'theme', 'about_lesson']



class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coment
        fields = ['id', 'lesson', 'user', 'comment', 'added_at']



class eMailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    text = serializers.CharField()


class RatingSerializer(serializers.Serializer):
    lesson = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']