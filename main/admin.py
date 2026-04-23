from django.contrib import admin
from .models import Student, Skill, StudentSkill, Project, Like


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter  = ["category"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ["name", "group", "email"]
    search_fields = ["name", "group"]


@admin.register(StudentSkill)
class StudentSkillAdmin(admin.ModelAdmin):
    list_display = ["student", "skill", "level"]
    list_filter  = ["skill"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ["title", "student", "tech_stack", "created_at"]
    search_fields = ["title", "student__name"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["project", "ip_address", "created_at"]
