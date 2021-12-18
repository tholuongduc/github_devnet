# Fill in this file with the code from parsing XML exercise
import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()
#print root tag
print(root)
#get namespace of root tag
ns = re.match('{.*}', root.tag).group(0)
#get the child of root tag
edit_config = root.find("{}edit-config".format(ns))
#get the child of edit_config
def_operation = edit_config.find(f'{ns}default-operation')
test_option = edit_config.find(f'{ns}test-option')
#print value of default-operation and test-option
print(f'The default-operation contains: {def_operation.text}')
print(f'The test-option contains: {test_option.text}')
