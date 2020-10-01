FROM python:3.8

WORKDIR /src

COPY . .

RUN pip install pipenv

RUN pipenv install --ignore-pipfile --system --deploy

CMD ["python", "/src/main.py"]