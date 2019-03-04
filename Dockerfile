FROM python:3.7

RUN mkdir /python_app && \
    pip install pipenv
COPY . /python_app
WORKDIR /python_app
RUN pipenv install --system --deploy

CMD ["pipenv", "shell"]
ENTRYPOINT ["python", "src/app.py"]
