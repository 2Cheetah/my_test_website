FROM python:3-slim

WORKDIR /website

COPY . .

EXPOSE 8000

RUN pip install --no-cache -r requirements.txt

CMD ["python", "webapp/main.py"]