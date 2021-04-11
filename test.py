import requests
import json
headers = {
    'Authorization': ''
}
src = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
print (src['id'])