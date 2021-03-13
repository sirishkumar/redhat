FROM python:3.9-alpine

# Create system account and user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
WORKDIR /app
COPY --chown=appuser:appgroup . /app/

COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python app.py