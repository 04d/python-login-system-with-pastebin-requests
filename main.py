import json
import requests
import os
import time

url = "YOUR PASTEBIN RAW LINK HERE"
r = requests.get(url)

def input_data():
    liste = []
    counter = -1

    for users in r.json():
        counter+=1
        request_json_username = r.json()[counter]["user_username"]
        request_json_password = r.json()[counter]["user_password"]
        dico_data = {request_json_username : request_json_password}
        liste.append(dico_data)

    username = str(input("Please enter your username : "))
    password = str(input("Please enter your password : "))
    data_user = {username : password}

    if data_user in liste:
        print(f"You are now logged as {username}")
        time.sleep(5)
    else: 
        os.system('cls||clear')
        print("The password or the username is invalid, please retry !")
        input_data()

input_data()

# Your code here
