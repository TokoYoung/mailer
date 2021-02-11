from python:3.7.9-buster
WORKDIR /src
RUN apt update && apt install -y\
    bash 

COPY  . . 
RUN pip install -r requirements.txt
EXPOSE 8080 
CMD ["python3", "app.py"]