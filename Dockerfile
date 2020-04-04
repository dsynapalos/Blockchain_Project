FROM python:3.8
RUN mkdir ./project
COPY ["main.py", "requirements.txt", "./project/"]
RUN pip3 install -r ./project/requirements.txt
CMD python3 ./project/main.py
EXPOSE 5000