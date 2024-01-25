FROM python:3.10.13-alpine3.19

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "main-gui", "run", "--host=0.0.0.0"]