FROM python:3.11-slim-buster
WORKDIR /app
RUN chmod 777 /app
COPY /bot /app/bot
COPY start.sh /app
COPY pyproject.toml poetry.lock /app/
COPY ocrserver /app/ocrserver
RUN pip install poetry poetry-core
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main
RUN chmod +x /app/start.sh
RUN chmod +x /app/ocrserver