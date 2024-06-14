from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Main.views import (LessonDaysAPIList, CourseListAPIview, CourseRetUpdDesAPIview,
                        TeacherAPIList, OnlineLessonAPIList,
                        ComentAPIList, SendeMailAPI, RatingAPIview,)



router = DefaultRouter()

router.register('lessondays/', LessonDaysAPIList)
router.register('teachers/', TeacherAPIList)
router.register('lessons/', OnlineLessonAPIList)
router.register('comments/', ComentAPIList)


urlpatterns = [
    path('', include(router.urls)),
    path('courses/', CourseListAPIview.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetUpdDesAPIview.as_view(), name='course-detail'),
    path('send-mail/', SendeMailAPI.as_view()),
    path('take-like/', RatingAPIview.as_view()),
]