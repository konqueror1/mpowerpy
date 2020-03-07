FROM debian

RUN apt update && apt install -y python3 python3-pip

COPY . ./app
WORKDIR ./app

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]