FROM python:3.9-buster

WORKDIR /app

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
COPY requirements.txt /app
RUN pip install -r requirements.txt

USER appuser
COPY --chown=appuser:appgroup . /app/

CMD python app.py
#ENTRYPOINT ["uwsgi", "--master", "--processes", "4", "--threads", "2", "--http-socket", ":5000", "--mount", "/=app:app"]