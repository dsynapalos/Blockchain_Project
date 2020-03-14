FROM python:3.8
COPY . .
RUN pip3 install -r ./Blockchain/requirements.txt
CMD python3 ./Blockchain/main.py