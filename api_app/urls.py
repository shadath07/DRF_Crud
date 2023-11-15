from django.urls import path
from . import views


urlpatterns = [
    path('studentapi/',views.student_api, name = 'studentapi'),
]