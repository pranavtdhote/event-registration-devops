FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install Flask

CMD ["python", "app.py"]