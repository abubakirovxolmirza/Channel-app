FROM python:3.11-alpine

RUN pip install --upgrade pip
RUN pip install -r ruquirements.txt

WORKDIR /posts
COPY . /posts

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

