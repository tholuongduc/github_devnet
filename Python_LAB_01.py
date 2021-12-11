#Devices list
print("Hay nhap ten cac thiet bi theo 1 hang va cach nhau = dau cach")
devices = map(str, input().split())
devices_lst = list(devices)

print(devices_lst[2])
if "Gate" in devices_lst:
    print("Da co thiet bi Gate")
else:
    print("Khong ton tai thiet bi Gate")
    devices_lst.append(input("Nhap ten thiet bi moi:"))
devices_lst.sort()
print(devices_lst)

