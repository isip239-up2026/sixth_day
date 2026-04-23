from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("student/<int:student_id>/", views.student_detail, name="student_detail"),
    path('skill/<int:skill_id>/', views.skill_filter, name='skill_filter'),
]
