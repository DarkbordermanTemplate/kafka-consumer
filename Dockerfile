FROM python:3.7.7-slim
RUN pip install pipenv

WORKDIR /kafka/
COPY Pipfile /kafka/Pipfile
COPY Pipfile.lock /kafka/Pipfile.lock
RUN pipenv install
COPY ./kafka/ /kafka/

CMD ["pipenv", "run", "python3", "app.py"]
