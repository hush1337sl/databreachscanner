# GET YOUR API KEY FROM https://www.ipqualityscore.com/create-account

import requests
from colorama import Fore, Style, init
import os
import json

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()
init()

email = input("Enter an email to look up: ")
api_key = "FW8d9f8eEUJnFRnsKynI48PXHBBjPFQT"
api_type = "email"
url = f"https://www.ipqualityscore.com/api/json/leaked/{api_type}/{api_key}/{email}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    if data.get("exposed") == True:
        print(f"{Fore.RED}Email was detected in leaked data{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{json.dumps(data, indent=4)}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Email is not leaked{Style.RESET_ALL}")
except requests.exceptions.RequestException as e:
    print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
except ValueError:
    print(f"{Fore.RED}Invalid response received from the API{Style.RESET_ALL}")