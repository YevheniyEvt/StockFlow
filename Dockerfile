FROM python:3.12-slim

# Копіюємо uv бінарний файл з офіційного образу
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/bin/uv

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо всі файли проекту
COPY . .

# Встановлюємо залежності та проект
RUN uv sync --frozen --no-dev

# Додаємо .venv до PATH
ENV PATH="/app/.venv/bin:$PATH"

# Запуск додатку
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
