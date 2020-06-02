FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]

