
devices_dict = {
    "ONT": "192.168.1.1"
}
while True:
    device_lst = []
    device_name = input("Please enter device name:")
    if device_name == "Exit":
        break
    device_lst.append(device_name)
    device_ip = input("Please enter device IP:")
    device_lst.append(device_ip)
    devices_dict.update({device_lst[0]: device_lst[1]})

#all device name
all_device = devices_dict.keys()

#Search device
if "Gate" in all_device:
    print("Gate is in device list!")
else:
    print("Gate is not in devie list!")
    choice = input("Do you want to add Gate into device list(Y/N)?:")
    if choice == "Y":
        devices_dict.update({"Gate": input("Please enter Gate's IP:")})
    else:
        print("Well done!")

#print device and IP
print(devices_dict)
#print all devices name
print(all_device)