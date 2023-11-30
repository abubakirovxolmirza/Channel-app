FROM python:3.11-alpine

RUN pip install --upgrade pip

WORKDIR /posts
COPY . /posts

EXPOSE 8000

ENV NAME posts

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

