import json

with open ('Data.json') as json_file:
    data_json = json.load(json_file)
#get value of key response
device_data = data_json["response"]
#Get IP of device
for i in range(len(device_data)):
    print(f'Hostname: {device_data[i]["hostname"]}\nManagement IP: {device_data[i]["managementIpAddress"]}')
