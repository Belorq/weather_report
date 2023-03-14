FROM python:3.10


RUN mkdir /weather
WORKDIR /weather

COPY requirements.txt /weather/
RUN pip install -r requirements.txt

COPY . /weather/
CMD ["flask", "run", "--host=0.0.0.0:80"]
EXPOSE 80