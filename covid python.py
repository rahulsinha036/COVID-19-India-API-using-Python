#install requests module pip install requests for windows
import requests

state = input('Enter the state name: ').lower()
api_address = "https://api.covid19india.org/data.json"
json_data = requests.get(api_address).json()
num=range(0,30)
for n in num:
    if state == json_data['statewise'][n]['state'].lower():
        formatted_json = json_data['statewise'][n]['confirmed']
    n+= 1
print(f"Active Case in {state} is {formatted_json}")


