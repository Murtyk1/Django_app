FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r req.txt 


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

