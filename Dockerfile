FROM python:3.10-alpine


RUN mkdir /weather
WORKDIR /weather

COPY requirements.txt /weather/
RUN pip install -r requirements.txt

COPY . /weather/
CMD ["python", "main.py"]
EXPOSE 5000
