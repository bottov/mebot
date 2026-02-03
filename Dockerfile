FROM python:3.12-slim
WORKDIR /app
COPY . .
# Если есть зависимости, раскомментируйте следующую строку и добавьте requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
CMD ["python", "bot.py"]

