FROM python:3.7.10-alpine

RUN pip install pipenv

RUN pipenv --three

RUN pipenv install flask

RUN pipenv install marshmallow

COPY . ./produto

RUN chmod +x ./produto/bootstrap.sh

CMD ["./produto/bootstrap.sh"]