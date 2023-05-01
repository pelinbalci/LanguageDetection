FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

EXPOSE 80

# Start server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]