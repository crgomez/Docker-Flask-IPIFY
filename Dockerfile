FROM python:3.7

RUN pip3 install Flask requests

WORKDIR /app
COPY app /app

CMD ["python", "ip_ring.py"]