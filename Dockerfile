FROM python:latest

WORKDIR /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY req.txt req.txt

RUN pip3 install --no-cache-dir --upgrade -r req.txt

COPY ./ app

CMD ["uvicorn", "app.core.app:app", "--host", "0.0.0.0", "--port", "8000"]