FROM python:3.11 as $PROJECT_NAME$-dependencies
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

FROM  $PROJECT_NAME$-dependencies as $PROJECT_NAME$
COPY ./app /app
CMD [ "python", "./app/server.py" ]
