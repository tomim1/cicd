FROM python:3.11-alpine
WORKDIR /app
RUN apk add --no-cache libpq-dev python3-dev g++ make
RUN pip install --upgrade pip
RUN pip install flask psycopg2
COPY ./app.py /app
ENV FLASK_APP=app.py
ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]

