from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("frontend", "Frontend"),
        ("backend",  "Backend"),
        ("db",       "Базы данных"),
        ("other",    "Другое"),
    ]
    name     = models.CharField(max_length=100, verbose_name="Название")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
                                 default="other", verbose_name="Категория")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    name       = models.CharField(max_length=200, verbose_name="Имя")
    group      = models.CharField(max_length=50,  verbose_name="Группа")
    bio        = models.TextField(verbose_name="О себе")
    email      = models.EmailField(verbose_name="Email")
    avatar_url = models.URLField(blank=True, verbose_name="Ссылка на аватар")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.group})"


class StudentSkill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                related_name="skills", verbose_name="Студент")
    skill   = models.ForeignKey(Skill, on_delete=models.CASCADE,
                                related_name="student_skills", verbose_name="Навык")
    level   = models.IntegerField(default=3, verbose_name="Уровень (1–5)")

    class Meta:
        verbose_name = "Навык студента"
        verbose_name_plural = "Навыки студентов"
        unique_together = ["student", "skill"]

    def __str__(self):
        return f"{self.student.name} — {self.skill.name} ({self.level})"

    def level_percent(self):
        return self.level * 20


class Project(models.Model):
    student     = models.ForeignKey(Student, on_delete=models.CASCADE,
                                    related_name="projects", verbose_name="Студент")
    title       = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    tech_stack  = models.CharField(max_length=200, verbose_name="Стек технологий")
    github_url  = models.URLField(blank=True, verbose_name="Ссылка на GitHub")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Like(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE,
                                   related_name="likes", verbose_name="Проект")
    ip_address = models.GenericIPAddressField(verbose_name="IP адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        unique_together = ["project", "ip_address"]

    def __str__(self):
        return f"{self.ip_address} → {self.project.title}"
