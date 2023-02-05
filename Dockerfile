# Используем образ Python
FROM python:3.8-alpine

# Устанавливаем зависимости
RUN apk update && \
    apk add --no-cache build-base postgresql-dev libpq

# Устанавливаем директорию для работы
WORKDIR /app

# Копируем файлы проекта в директорию
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Задаем переменные окружения
ENV PYTHONUNBUFFERED 1

# Запускаем команду
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
