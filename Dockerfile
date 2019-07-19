FROM python:3.7

RUN pip3 install requests
COPY mac_address.py /

CMD ["python", "./mac_address.py"]
