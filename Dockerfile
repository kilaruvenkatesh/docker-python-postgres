FROM python:3.10-slim

WORKDIR /app

COPY app.py .

# Install PostgreSQL driver
RUN pip install psycopg2-binary

CMD ["python", "app.py"]
