FROM python:3.9.4-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./src .
COPY requirements.txt .
RUN pip install -r requirements.txt


CMD ["uvicorn", "--host", "0.0.0.0", "--reload", "--reload-dir", "/src", "src.main:app"]
