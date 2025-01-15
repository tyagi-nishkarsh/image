FROM python:3.11

RUN apt-get update && apt-get install -y espeak

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "image-captioning.py"
