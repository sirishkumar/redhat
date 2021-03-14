FROM python:3.9-alpine

# Create system account and user
WORKDIR /app
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
COPY requirements.txt /app
RUN pip install -r requirements.txt

USER appuser
COPY --chown=appuser:appgroup . /app/

EXPOSE 5000
CMD python app.py