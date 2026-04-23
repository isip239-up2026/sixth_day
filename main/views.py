from django.shortcuts import render, get_object_or_404
from .models import Student, Skill, StudentSkill, Project


def index(request):
    students = Student.objects.all()
    return render(request, "main/index.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "main/student_detail.html", {"student": student})


def skill_filter(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    students = Student.objects.filter(
        studentskills__skill=skill
    ).distinct()

    count = students.count()

    return render(request, 'main/skill_filter.html', {
        'skill': skill,
        'students': students,
        'count': students.count
    })
