file = open("device.txt","a")
#Add new device
while True:
    new_device = input("Please enter your new device:")
    if new_device == "Exit":
        print("All done!")
        break
    file.write(new_device + "\n")
#print all switch devices
file = open("device.txt","r")
for item in file:
    item = item.strip()
    if "Switch" in item:
        print(item)

file.close()