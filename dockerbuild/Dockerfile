FROM python:3.9

WORKDIR .

COPY ./scripts/requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./scripts/projection_cleanup.py" ]