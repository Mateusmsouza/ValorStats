ARG REQUIREMENTS_PATH=./requirements/development.txt
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r ./requirements/development.txt

ENTRYPOINT python main.py