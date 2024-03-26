FROM python:3.10.12-slim-buster
WORKDIR /app
RUN chmod 777 /app
RUN python3 -m pip install -U pip
COPY . .
RUN pip3 install --no-cache-dir -U -r requirements.txt
CMD ["python3", "-m", "bot"]
