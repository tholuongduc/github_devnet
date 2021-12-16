#Parsing contact.xml file
import xml.etree.ElementTree as ET

xml = ET.parse("contact.xml")
root = xml.getroot()

#print(root)

#get name
name_lst = []
company_lst = []
phone_lst = []
for name in root.iter('name'):
        name_lst.append(name.text)
for company in root.iter('company'):
        company_lst.append(company.text)
for phone in root.iter('phone'):
        phone_lst.append(phone.text)

#print contact list
for i in range(len(name_lst)):
    print(f'Name:{name_lst[i]}\nCompany:{company_lst[i]}\nPhone:{phone_lst[i]}')