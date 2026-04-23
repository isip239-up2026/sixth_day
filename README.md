# Студенческое портфолио — учебный проект

## Быстрый старт

```bash
pip install django
python manage.py migrate
python seed.py          # загрузить тестовые данные
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000

Панель администратора: http://127.0.0.1:8000/admin
Логин: `admin` / Пароль: `admin`

---

## Структура проекта

```
portfolio/
├── portfolio/              # настройки проекта
│   ├── settings.py
│   └── urls.py
├── main/                   # приложение
│   ├── models.py           # Student, Skill, StudentSkill, Project, Like
│   ├── views.py            # index, student_detail
│   ├── urls.py
│   ├── admin.py
│   └── templates/main/
│       ├── base.html
│       ├── index.html
│       └── student_detail.html
├── seed.py
└── db.sqlite3
```

## Модели

```
Student      — name, group, bio, email, avatar_url
Skill        — name, category (frontend/backend/db/other)
StudentSkill — student(FK), skill(FK), level(1–5)
Project      — student(FK), title, description, tech_stack, github_url, created_at
Like         — project(FK), ip_address, created_at
```

## Страницы

| URL | Описание |
|-----|----------|
| `/` | Список всех студентов |
| `/student/<id>/` | Профиль студента |

---

## Задания для студентов

### Task 1 — Навыки на странице профиля
**Файлы:** `main/views.py`, `main/templates/main/student_detail.html`

Студент имеет навыки через модель `StudentSkill`. Нужно вывести их в профиле с визуальным уровнем владения через Bootstrap progress bar.

Что сделать:
1. В view `student_detail` добавить в контекст `skills = StudentSkill.objects.filter(student=student).select_related('skill')`
2. В шаблоне вывести навыки сгруппированными по `skill.category` через `{% regroup skills by skill.category as skill_groups %}`
3. Уровень владения (1–5) показать через Bootstrap `progress` bar — ширина `{{ skill.level_percent }}%` (метод уже есть в модели)
4. Каждую категорию показать как отдельную секцию с заголовком: Frontend, Backend, Базы данных, Другое

---

### Task 2 — Список проектов в профиле
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/student_detail.html`, `main/templates/main/project_detail.html` (создать)

Что сделать:
1. В view `student_detail` добавить в контекст `projects = student.projects.all()`
2. В шаблоне в блоке `ЗАДАНИЕ 2` вывести проекты карточками — название, описание (`truncatewords:15`), стек технологий, ссылка на GitHub
3. Добавить маршрут `/project/<int:project_id>/` в `urls.py` и view `project_detail`
4. Создать `project_detail.html` — полная информация о проекте, имя автора со ссылкой на его профиль

---

### Task 3 — Лайки на проекты
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/project_detail.html`

Лайки без JS — кнопка отправляет POST-форму, страница перезагружается. Один IP может лайкнуть один раз.

Что сделать:
1. Добавить маршрут `/project/<int:project_id>/like/` и view `like_project`
2. В view получить IP через `request.META.get('REMOTE_ADDR')`
3. Проверить `Like.objects.filter(project=project, ip_address=ip).exists()` — если нет, создать лайк
4. После обработки сделать `redirect('project_detail', project_id=project.id)`
5. На странице проекта показать кнопку с количеством лайков `{{ project.likes.count }}`. Если IP уже лайкнул — кнопка с атрибутом `disabled`

---

### Task 4 — Фильтрация студентов по навыку
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/index.html`, `main/templates/main/skill_filter.html` (создать)

Что сделать:
1. Добавить маршрут `/skill/<int:skill_id>/` в `urls.py`
2. Создать view `skill_filter` — находит студентов через `Student.objects.filter(skills__skill=skill).distinct()`
3. Создать `skill_filter.html` — список студентов с заголовком «Студенты со навыком: Python» и счётчиком «Найдено: 4 студента»
4. В `index.html` в блоке `ЗАДАНИЕ 4` под именем студента вывести его навыки как кликабельные Bootstrap-бейджи ведущие на страницу фильтра: `{% url 'skill_filter' skill.skill.id %}`

---

### Task 5 — Поиск студентов
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/base.html`, `main/templates/main/search.html` (создать)

Поиск одновременно по имени студента, группе и названиям его проектов.

Что сделать:
1. В `base.html` в навбар добавить GET-форму с полем `q`
2. Добавить маршрут `/search/` и view `search`
3. В view использовать Q-объекты:
```python
from django.db.models import Q
results = Student.objects.filter(
    Q(name__icontains=q) |
    Q(group__icontains=q) |
    Q(projects__title__icontains=q)
).distinct()
```
4. Создать `search.html` — показывает результаты карточками или сообщение «Никого не найдено», в заголовке страницы выводить запрос: «Результаты поиска: Python»

---

### Task 6 — Сортировка и пагинация на главной
**Файлы:** `main/views.py`, `main/templates/main/index.html`

Сортировка и пагинация должны работать вместе — при переходе на страницу 2 сортировка сохраняется.

Что сделать:
1. Добавить сортировку через `request.GET.get('sort', 'name')` — по имени (`name`), по группе (`group`), по количеству проектов (нужен `annotate(project_count=Count('projects'))`)
2. Добавить пагинацию через `Paginator` — по 3 студента на страницу
3. В шаблоне при формировании ссылок пагинации сохранять сортировку: `?sort={{ request.GET.sort }}&page=2`
4. Выделить активную кнопку сортировки: `{% if request.GET.sort == 'name' %}btn-dark{% else %}btn-outline-dark{% endif %}`

---

### Task 7 — Топ проектов
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/top.html` (создать), `main/templates/main/base.html`

Что сделать:
1. Добавить маршрут `/top/` и view `top_projects`
2. В view получить проекты отсортированные по лайкам:
```python
from django.db.models import Count
projects = Project.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:10]
```
3. Создать `top.html` — нумерованный список топ-10 с именем автора, количеством лайков и ссылкой на проект
4. Первые три места выделить — `text-warning` (1), `text-secondary` (2), `text-danger` (3)
5. В `base.html` добавить ссылку «Топ проектов» в навбар

---

### Task 8 — Сравнение двух студентов
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/index.html`, `main/templates/main/compare.html` (создать)

Что сделать:
1. В `index.html` в блоке `ЗАДАНИЕ 8` у каждого студента добавить кнопку-ссылку «Сравнить» — ведёт на `/compare/?a=<id>`
2. Добавить маршрут `/compare/` и view `compare`
3. View принимает параметры `?a=<id>&b=<id>`. Если передан только `a` — показать список студентов для выбора второго
4. Создать `compare.html` — Bootstrap-таблица: строки это навыки, столбцы — два студента. В ячейках уровень владения или «—» если навыка нет

---

### Task 9 — Форма добавления проекта
**Файлы:** `main/forms.py` (создать), `main/views.py`, `main/urls.py`, `main/templates/main/add_project.html` (создать), `main/templates/main/student_detail.html`

Что сделать:
1. Создать `main/forms.py` с классом `ProjectForm` — поля `title`, `description`, `tech_stack`, `github_url`
2. Добавить валидацию: в методе `clean_github_url` проверить что URL начинается с `https://github.com`, иначе `raise forms.ValidationError(...)`
3. Добавить маршрут `/student/<int:student_id>/add-project/` и view `add_project`
4. View обрабатывает GET (показать форму) и POST (сохранить, привязать к студенту, редирект на профиль)
5. Создать `add_project.html` с Bootstrap-формой, в `student_detail.html` добавить кнопку «Добавить проект»

---

### Task 10 — Экспорт профиля в текстовый файл
**Файлы:** `main/views.py`, `main/urls.py`, `main/templates/main/student_detail.html`

Что сделать:
1. Добавить маршрут `/student/<int:student_id>/export/` и view `export_student`
2. View возвращает `HttpResponse` с заголовком для скачивания:
```python
response = HttpResponse(content_type='text/plain; charset=utf-8')
response['Content-Disposition'] = f'attachment; filename="{student.name}.txt"'
```
3. Записать в ответ: имя, группу, email, bio, список навыков с уровнями, список проектов с описанием и ссылками
4. В `student_detail.html` добавить кнопку «Скачать резюме»
5. Дополнительно: если в URL передан параметр `?format=csv` — вернуть данные через модуль `csv` из стандартной библиотеки Python
