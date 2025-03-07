# -*- coding: utf-8 -*-
import os
import json
import generateHtml


def main():
    with open('content.json', 'r', encoding="utf-8") as fJson:
        load_dict = json.load(fJson)

    documents = load_dict['documents']['items']
    folder_path = './public/documents/txt/'

    documentLocal = []
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            documentLocal.append(file)
            #print(file)

    exist = 0
    for document in documentLocal:
        exist = 0
        for item in documents:
            if item['no'] + ".txt" == document:
                exist = 1
                break
        # 發現不存在這個文章 --> 開始產生html
        generateHtml.main(document, exist)

    # --- sort json --- #

    with open('content.json', 'r', encoding="utf-8") as fJson:
        load_dict = json.load(fJson)

        documents = load_dict['documents']['items']
        for i in range(len(documents)-1, -1, -1):
            for j in range(i-1, -1, -1):
                if documents[i]['no'] > documents[j]['no']:
                    temp = documents[i]
                    documents[i] = documents[j]
                    documents[j] = temp

    with open('content.json', 'w', encoding="utf-8") as fJson:
        json.dump(load_dict, fJson, ensure_ascii=False, indent=4)


main()

