FROM python:3.12-alpine

WORKDIR /app

RUN apk update && \
    apk upgrade && \
    rm -rf /var/cache/apk/*

COPY requirements.txt .

RUN pip install --no-cache-dir pip==26.2.1 && \
    pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY start.sh ./start.sh

RUN chmod 700 ./start.sh

EXPOSE 8000

CMD ["./start.sh"]
