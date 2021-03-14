FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache uwsgi-python3
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
COPY requirements.txt /app
RUN pip install -r requirements.txt

USER appuser
COPY --chown=appuser:appgroup . /app/

CMD python app.py
#ENTRYPOINT ["uwsgi", "--master", "--processes", "4", "--threads", "2", "--http-socket", ":5000", "--mount", "/=app:app"]