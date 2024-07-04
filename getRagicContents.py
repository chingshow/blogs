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

    with open('return.json', 'w', encoding="utf-8") as fJson:
        json.dump(response_dict, fJson, ensure_ascii=False, indent=4)

    with open('return.json', 'r', encoding="utf-8") as fJson:
        load_dict = json.load(fJson)
        print(len(load_dict))
        for i in range(len(load_dict)):
            no = load_dict[f'{i}']['編號']
            f = open(f'./public/documents/txt/{no}.txt', 'w', encoding="utf-8")
            f.write(load_dict[f'{i}']['編號']+'\n')
            f.write(load_dict[f'{i}']['時間']+'\n')
            f.write(load_dict[f'{i}']['文章標題']+'\n')
            f.write(load_dict[f'{i}']['作者']+'\n')
            f.write(load_dict[f'{i}']['文章內容'])

