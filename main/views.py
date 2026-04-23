from django.shortcuts import render, get_object_or_404
from .models import Student, Project

def index(request):
    students = Student.objects.all()
    return render(request, "main/index.html", {"students": students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    projects = student.projects.all()
    return render(request, "main/student_detail.html", {
        "student": student,
        "projects": projects
    })

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "main/project_detail.html", {"project": project})