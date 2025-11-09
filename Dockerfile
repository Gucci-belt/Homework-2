FROM python:3.10-slim

WORKDIR /app

COPY calculator.py .

CMD ["python", "calculator.py"]