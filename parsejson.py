# Fill in this file with the code from parsing JSON exercise
import json
import yaml

with open ('myfile.json') as json_file:
    ourjson = json.load(json_file)
print(ourjson)
#print token value
#access token
print(f'The access token is: {ourjson["access_token"]}')
print(f'The  access token expires in {ourjson["expires_in"]}')
#refresh token
print(f'The refresh token is: {ourjson["refresh_token"]}')
print(f'The  access token expires in {ourjson["refreshtokenexpires_in"]}')