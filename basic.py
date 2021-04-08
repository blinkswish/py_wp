from flask import Flask, jsonify
import requests
import json
import base64


#config

## Credentials. Put this in a cfg file if you wish. 
applicationuser = "username" ## username
applicationpassword = "app pw" ## application password 


## Concatenate credentials to prep for encoding 
cred = applicationuser + ':' + applicationpassword

## Create the encoded token
token = base64.b64encode(cred.encode())


# Header and token decoded for requests 
header = {'Authorization': 'Basic' + token.decode('utf-8')}


# Base URL for requests
host = "https://example.com/wp-json/"

#init
app = Flask(__name__)



#Define routes 

route1 = "wp/v2/"
#route2 = ""
#route3 = ""
#route4 = ""
#route5 = ""


url = host + route


#Send request
r = requests.get(url, headers=header)
print(r.text)


#run server
if __name__ == '__main__':
    app.run(debug=True)
