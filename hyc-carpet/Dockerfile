FROM python

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .

USER 1000

CMD [ "gunicorn", "-w 4", "-b", "0.0.0.0:8000", "main:app" ]