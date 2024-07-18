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
    sheet_id = "5"

    ENDPOINT = f'{base_url}/{tag}/{sheet_id}'
    response = requests.get(ENDPOINT, params=params, headers={'Authorization': 'Basic '+api_key})

    response_dict = response.json()

    print(json.dumps(response_dict, indent=4))

    # 構建圖片檔案的下載 URL
    image_url = 'https://www.ragic.com/your_account/attachments/YOUR_FORM_ID/046IA6C40S/javascript.jpg'

    # 設定 headers 包含 API 金鑰
    headers = {
        'Authorization': 'Basic {}'.format(api_key)
    }

    # 下載圖片檔案
    image_response = requests.get(image_url, headers=headers)

    # 將圖片檔案保存到本地
    with open('javascript', 'wb') as f:
        f.write(image_response.content)

main()

