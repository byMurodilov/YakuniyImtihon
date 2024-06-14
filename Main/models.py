from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator




class LessonDays(models.Model):
    """Online darslar qaysi kunlarda bo'lishini belgilash uchun"""
    name = models.CharField(max_length=12, unique=True, help_text="Dars kunlari (Hafta kunlari)")

    def __str__(self):
        return self.name




class Course(models.Model):
    """ Kurs haqida qisqacha izoh """
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField()
    duration = models.IntegerField(default=0)    
    added_at = models.DateTimeField(auto_now_add=True)
    lesson_days = models.ManyToManyField(LessonDays)

    def __str__(self) -> str:
        return self.name 
    


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='teachers/') 
    full_name = models.CharField(max_length=77, unique=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    experience = models.IntegerField(help_text="Ish tajribasi")

    def __str__(self) -> str:
        return self.full_name
    



class OnlineLesson(models.Model):
    """ Masofaviy Dars haqida """
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    lesson_vid = models.FileField(upload_to='lesson/videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'WMV'])])
    theme = models.CharField(max_length=50, unique=True)
    about_lesson = models.TextField()

    def __str__(self) -> str:
        return self.theme
    




class Coment(models.Model):
    """ Izoh qoldirish uchun """
    lesson = models.ForeignKey(OnlineLesson, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.lesson.theme} dars uchun {self.user.username} izoh qoldirdi."
    



class Rating(models.Model):
    """ Darsni baholash uchun """
    lesson = models.ForeignKey(OnlineLesson, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    take_like = models.BooleanField()