from django.shortcuts import render, get_object_or_404
from .models import Student, Project


def index(request):
    students = Student.objects.all()
    return render(request, "main/index.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "main/student_detail.html", {"student": student})
