FROM python:3.6-alpine3.6

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN apk --update add build-base postgresql-dev gcc python3-dev musl-dev libffi-dev jpeg-dev zlib-dev
RUN pip install -r /requirements/local.txt

COPY ./compose/dev/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/dev/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
