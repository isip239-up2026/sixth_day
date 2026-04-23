from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("student/<int:student_id>/", views.student_detail, name="student_detail"),
    path("/project/<int:project_id>/like/", views.like_project, name="like_project"),
]
