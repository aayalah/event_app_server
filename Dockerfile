FROM python:3.11.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

CMD ["unicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]