
1. implement python on this assignment using linux platform

2. we look at mac address using 'ip link show wifi0' on linux command line

3. to find mac address, we use regular expression 're.complie', and 're.findall'

4. to use api.macaddress.io, we should register macaddress.io, and we should query-based authentication and get api address 

5. to find company name of mac address, we loop at mac address on macaddress.io api, and get api with json format.

6. use dictionary implementation to find company name of the mac address.

7. run it on linux:
	python3 mac_address.python
	
8. create docker file
	nano Docketfile on linux command
	
	in the file,
	
	# for python3 
	
	FROM python:3.7
	
	# install requests
	
	RUN pip3 install requests
	
	# copy mac_address.py file to docker container
	
	COPY mac_address.py /
	
	# run mac_address.py on python	

9. build docker file
	docker build -t <docker file name> .
	


10. run docker file
	docker run <docker file name>
  

