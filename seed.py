import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from django.contrib.auth.models import User
from main.models import Student, Skill, StudentSkill, Project, Like

Student.objects.all().delete()
Skill.objects.all().delete()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin")
    print("Создан администратор: логин=admin пароль=admin")

skills_data = [
    ("HTML",       "frontend"), ("CSS",        "frontend"), ("Bootstrap", "frontend"),
    ("JavaScript", "frontend"), ("Python",      "backend"),  ("Django",   "backend"),
    ("FastAPI",    "backend"),  ("PostgreSQL",  "db"),       ("SQLite",   "db"),
    ("Git",        "other"),    ("Linux",       "other"),    ("Docker",   "other"),
]
skills = {}
for name, cat in skills_data:
    skills[name] = Skill.objects.create(name=name, category=cat)

students_data = [
    {
        "name": "Артём Беков", "group": "ИС-21",
        "bio": "Увлекаюсь бэкенд-разработкой. Пишу на Python и Django. Хочу работать в крупной IT-компании после окончания университета.",
        "email": "bekov@student.edu",
        "avatar_url": "https://i.pravatar.cc/300?img=11",
        "skills": [("Python", 5), ("Django", 4), ("PostgreSQL", 3), ("Git", 4), ("Linux", 3)],
        "projects": [
            ("Библиотечная система", "Система учёта книг с возможностью бронирования и управления читателями. Реализованы роли администратора и читателя.", "Django, PostgreSQL, Bootstrap", "https://github.com/bekov/library"),
            ("Погодный бот", "Telegram-бот который присылает прогноз погоды по запросу. Использует OpenWeatherMap API.", "Python, aiogram, requests", "https://github.com/bekov/weather-bot"),
        ]
    },
    {
        "name": "Дана Сейткали", "group": "ИС-22",
        "bio": "Frontend-разработчик. Люблю создавать красивые и удобные интерфейсы. В свободное время изучаю UX-дизайн.",
        "email": "seitkali@student.edu",
        "avatar_url": "https://i.pravatar.cc/300?img=25",
        "skills": [("HTML", 5), ("CSS", 5), ("Bootstrap", 4), ("JavaScript", 3), ("Python", 2), ("Git", 3)],
        "projects": [
            ("Портфолио сайт", "Личный сайт-портфолио с анимациями и адаптивным дизайном. Сделан без фреймворков на чистом HTML/CSS.", "HTML, CSS, JavaScript", "https://github.com/seitkali/portfolio"),
            ("Кулинарный блог", "Блог с рецептами, Django-бэкенд, Bootstrap-фронтенд. Есть поиск по ингредиентам и категориям.", "Django, Bootstrap, SQLite", "https://github.com/seitkali/food-blog"),
        ]
    },
    {
        "name": "Марат Джаксыбеков", "group": "ИС-21",
        "bio": "Full-stack разработчик. Умею и бэкенд и фронтенд. Интересуюсь DevOps и автоматизацией.",
        "email": "jaksybekov@student.edu",
        "avatar_url": "https://i.pravatar.cc/300?img=15",
        "skills": [("Python", 4), ("Django", 4), ("HTML", 4), ("CSS", 3), ("Bootstrap", 4), ("Docker", 3), ("Git", 5), ("PostgreSQL", 4)],
        "projects": [
            ("Трекер задач", "Kanban-доска для управления задачами. Поддерживает несколько проектов и участников.", "Django, Bootstrap, PostgreSQL", "https://github.com/jaksybekov/tasktracker"),
            ("Чат приложение", "Простой чат на Django с сохранением истории сообщений в базе данных.", "Django, SQLite, Bootstrap", "https://github.com/jaksybekov/chat"),
            ("Деплой скрипты", "Набор bash и Python скриптов для автоматического деплоя Django-приложений.", "Python, Docker, Linux", "https://github.com/jaksybekov/deploy-scripts"),
        ]
    },
    {
        "name": "Айгерим Нурова", "group": "ИС-22",
        "bio": "Занимаюсь базами данных и аналитикой. Прохожу стажировку в финтех-компании. Пишу дипломную работу по оптимизации запросов.",
        "email": "nurova@student.edu",
        "avatar_url": "https://i.pravatar.cc/300?img=32",
        "skills": [("PostgreSQL", 5), ("SQLite", 4), ("Python", 4), ("Django", 3), ("Git", 3), ("Linux", 2)],
        "projects": [
            ("Анализ успеваемости", "Система анализа успеваемости студентов с визуализацией данных и экспортом отчётов.", "Django, PostgreSQL, Chart.js", "https://github.com/nurova/gradebook"),
        ]
    },
    {
        "name": "Руслан Сейтов", "group": "ИС-23",
        "bio": "Студент третьего курса. Только начинаю. Изучаю Python и Django. Хочу попасть на стажировку летом.",
        "email": "seitov@student.edu",
        "avatar_url": "https://i.pravatar.cc/300?img=18",
        "skills": [("Python", 3), ("Django", 2), ("HTML", 3), ("CSS", 2), ("Git", 2)],
        "projects": [
            ("Конвертер валют", "Простой сайт для конвертации валют. Курсы обновляются при каждом запросе через внешний API.", "Django, Bootstrap", "https://github.com/seitov/currency"),
        ]
    },
    {
        "name": "Жанна Абенова", "group": "ИС-23",
        "bio": "Интересуюсь мобильной разработкой и вебом. Участвовала в двух хакатонах. Изучаю FastAPI в свободное время.",
        "email": "abenova@student.edu",
        "avatar_url": "https://i.pravatar.cc/300?img=44",
        "skills": [("Python", 4), ("FastAPI", 3), ("HTML", 4), ("Bootstrap", 3), ("PostgreSQL", 2), ("Git", 4)],
        "projects": [
            ("REST API для ToDo", "Полноценный REST API с авторизацией, CRUD операциями и документацией через Swagger.", "FastAPI, PostgreSQL", "https://github.com/abenova/todo-api"),
            ("Новостной агрегатор", "Парсит новости с нескольких сайтов и показывает их в едином интерфейсе.", "Python, Django, Bootstrap", "https://github.com/abenova/news-aggregator"),
        ]
    },
]

for s in students_data:
    student = Student.objects.create(
        name=s["name"], group=s["group"], bio=s["bio"],
        email=s["email"], avatar_url=s["avatar_url"]
    )
    for skill_name, level in s["skills"]:
        StudentSkill.objects.create(student=student, skill=skills[skill_name], level=level)
    for title, desc, tech, url in s["projects"]:
        Project.objects.create(student=student, title=title, description=desc,
                               tech_stack=tech, github_url=url)

print(f"Готово: {Student.objects.count()} студентов, "
      f"{Project.objects.count()} проектов, "
      f"{Skill.objects.count()} навыков.")
