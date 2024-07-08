import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import json


def main():
    params = {'api': '', 'v': 3}
    # 设置API密钥和URL
    load_dotenv()
    api_key = os.getenv('RAGIC_API')
    base_url = 'https://ap12.ragic.com/chingshow'
    tag = "blogs"
    sheet_id = "2"

    ENDPOINT = f'{base_url}/{tag}/{sheet_id}'
    response = requests.get(ENDPOINT, params=params, headers={'Authorization': 'Basic '+api_key})

    response_dict = response.json()

    print(json.dumps(response_dict, indent=4))



