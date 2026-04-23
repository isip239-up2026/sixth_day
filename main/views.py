from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Project, Like


def index(request):
    students = Student.objects.all()
    return render(request, "main/index.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "main/student_detail.html", {"student": student})

def like_project(request, project_id):
    ip = request.META.get('REMOTE_ADDR')
    project = get_object_or_404(Project, id=project_id)
    if Like.objects.filter(project=project, ip_address=ip).exists():
        Like.objects.create(ip_address=ip)
        Like.save()
        return redirect('project_detail', project_id=project.id)

    return render(request, "main/project_detail.html", {"gugugaga": Like.objects.values('ip_address').count()})