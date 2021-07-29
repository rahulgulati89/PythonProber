FROM python:3.9.6-alpine3.14

COPY pythonprober /tmp/pythonprober
COPY requirements.txt /tmp

RUN cd /tmp && pip3 install -r requirements.txt
#RUN cd /tmp && python3 setup.py install 

CMD ["python3","/tmp/pythonprober/pythonprober.py"]
