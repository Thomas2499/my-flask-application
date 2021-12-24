# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /app
ENV HOSTNAME=0.0.0.0
ENV PORT=2499
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]