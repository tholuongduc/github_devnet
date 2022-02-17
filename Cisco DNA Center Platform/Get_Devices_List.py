import requests
from requests.auth import HTTPBasicAuth
import json

requests.packages.urllib3.disable_warnings()

#Get Auth token
def get_auth_token():
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    authCreds = ("devnetuser", "Cisco123!")
    #Make POST request
    r = requests.post(url, auth=authCreds, verify = False)
    if r.status_code == 200:
        return r.json()["Token"]
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")


#def get devices list function
def get_all_devices():
    global token
    global hdr
    url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    r = requests.get(url, headers = hdr) #Create GET request
    if r.status_code == 200:
        jsondata = r.json()  #Save response from DNA as Json format
        devices_lst = jsondata["response"]
        print("{0:20}{1:17}{2:20}{3:15}{4:20}{5:17}{6:16}{7:15}".format("Hostname", "MGMT IP", "MAC Address", "Serial Number", "Platform ID", "SoftwareVersion", "Role", "Uptime"))
        for i in range(len(devices_lst)):
            each_device = devices_lst[i]
            print("{0:20}{1:17}{2:20}{3:15}{4:20}{5:17}{6:16}{7:15}".format(each_device["hostname"],each_device["managementIpAddress"],each_device["macAddress"],each_device["serialNumber"],each_device["platformId"],each_device["softwareVersion"],each_device["role"],each_device["upTime"]))
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to get all books information.")
#Define get interface status of device filtering by device's IP
def get_intf_status(Para_key,Para_value):
    global token
    global hdr
    url = "https://sandboxdnac.cisco.com/api/v1/interface"
    querystring = {Para_key: Para_value}
    r = requests.get(url, headers=hdr, params=querystring)
    if r.status_code == 200:
        jsondata = r.json()
        interfaces_list = jsondata["response"]
        print("{0:40}{1:7}{2:20}{3:7}{4:20}{5:20}".format("portName","vlanID","portType","status","pid","lastUpdated"))
        for i in range(len(interfaces_list)):
            each_intf = interfaces_list[i]
            print("{0:40}{1:7}{2:20}{3:7}{4:20}{5:20}".format(each_intf["portName"],each_intf["vlanId"],each_intf["portType"],each_intf["status"],each_intf["pid"],each_intf["lastUpdated"]))
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to get all books information.")

#Main

token = get_auth_token() #Get token
hdr = {"x-auth-token":token, "content-type": "application/json"} #Build header infor
#Select mode
mode = int(input("1 - Show all devices\n2 - Show interface status\n"))
if mode == 1:
    print("Show all devices!")
    all_devices = get_all_devices()
elif mode == 2:
    print("Show interface status")
    Para_key = input("Enter KEY (Ex:pid):")
    Para_value = input("Enter Value (Ex:C9300-24U:")
    all_intfaces = get_intf_status(Para_key,Para_value)
else:
    print("Wrong mode! Enter 1 or 2")

