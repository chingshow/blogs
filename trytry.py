import requests
from dotenv import load_dotenv
import os
import json
import base64
import urllib.parse


def download_image(image_field_value, web_id, base_url, api_key):
    if '@' in image_field_value:
        file_id, filename = image_field_value.split('@')
        print(f'Downloading image {filename}...')

        # 构建图片文件的下载 URL
        encoded_filename = urllib.parse.quote(filename)
        image_url = f'{base_url}/sims/file.jsp?a=chingshow&f={file_id}@{encoded_filename}'
        print('Image URL:', image_url)


        # 下载图片文件
        image_response = requests.get(image_url, headers={'Authorization': 'Basic ' + api_key})
        if image_response.status_code != 200:
            print(f'Failed to download image {filename}:', image_response.status_code, image_response.text)
            return

        # 将图片文件保存到本地
        with open(f'image_test/{web_id}/{filename}', 'wb') as f:
            f.write(image_response.content)
        print(f'图片已下载并保存为 {filename}')
    else:
        print('Invalid image field value format')


def main():
    params = {'api': '', 'v': 3}
    # 设置API密钥和URL
    load_dotenv()
    api_key = os.getenv('RAGIC_API')

    base_url = 'https://ap12.ragic.com'
    tag = "chingshow/blogs"
    sheet_id = "5"

    ENDPOINT = f'{base_url}/{tag}/{sheet_id}'
    response = requests.get(ENDPOINT, params=params, headers={'Authorization': 'Basic ' + api_key})

    response_dict = response.json()

    print(json.dumps(response_dict, indent=4))

    web_id = 0
    # 假设图片字段名为 'image_field' 并且我们取得其值
    record = response_dict[f'{web_id}']  # 根据实际结构可能需要调整
    os.makedirs(f'image_test/{web_id}', exist_ok=True)

    # 主记录中的图片字段
    image_fields = ['image', 'Agenda', 'Co-organizor', 'Sponsor']
    for field in image_fields:
        if field in record:
            download_image(record[field], web_id, base_url, api_key)

    # 处理子表
    for subtable_key in ['_subtable_1000033', '_subtable_1000034', '_subtable_1000035']:
        if subtable_key in record:
            subtable = record[subtable_key]
            for subrecord_key in subtable:
                subrecord = subtable[subrecord_key]
                if 'Image' in subrecord:
                    download_image(subrecord['Image'], web_id, base_url, api_key)


main()
