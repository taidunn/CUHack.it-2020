FROM python:3.8-alpine

WORKDIR /home/cuhackit

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY website website
COPY application.py application.py

ENV FLASK_APP application.py

ENTRYPOINT ["python"]
CMD ["application.py"]
