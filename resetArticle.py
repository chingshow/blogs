# -*- coding: utf-8 -*-
import os
import json
import generateHtml

with open('content.json', 'r', encoding="utf-8") as fJson:
    load_dict = json.load(fJson)

load_dict['documents']['items'] = []

with open('content.json', 'w', encoding="utf-8") as fJson:
    json.dump(load_dict, fJson, ensure_ascii=False, indent=4)
