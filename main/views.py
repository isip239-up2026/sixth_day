from django.shortcuts import render, get_object_or_404

from seed import skills 
from .models import Student, Project, StudentSkill


def index(request):
    students = Student.objects.all()
    return render(request, "main/index.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    skills=StudentSkill.objects.filter(student=student).select_related('skill')
    return render(request, "main/student_detail.html",
                  {"student": student,
                  "skills": skills})


