import os, re
import json
import requests
# look ip mac address on linux 
mycmd = os.popen('ip link show').read()

# regex expression for mac address 
p = re.compile(r'^[a-fA-F0-9:]{17}|[a-fA-F0-9]{12}$', re.IGNORECASE)
# eliminate two following address:
f='ff:ff:ff:ff:ff:ff'
e='00:00:00:00:00:00'

# convert a string to a list
m= mycmd.split(' ')

# find mac address
for x in m:
    x=x.strip()
    if re.match(p,x): 
        mac= re.findall(p, x)
        if mac != f or mac !=e:
            break
        
# convert to string data type
mac=mac[0]

# url for api.macaddress.io with api key
url='https://api.macaddress.io/v1?apiKey=at_POa24ggdz4rJA14m04hAHcBk8dsa6&output=json&search='

# concatenate api.macaddress and mac address
mac_url=url+mac

# get mac address from url
r = requests.get(url = mac_url) 

# convert to json format
data = r.json()

# find company name of the mac address
company = data['vendorDetails']['companyName']

print(company)



