FROM python:2.7

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD app1.py /app/app1.py

EXPOSE 80

CMD ["python", "app1.py"]
