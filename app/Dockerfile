FROM python:3.11 as dbi_pyton_service_template-dependencies
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

FROM  dbi_pyton_service_template-dependencies as dbi_pyton_service_template
COPY ./app /app
CMD [ "python", "./app/server.py" ]
