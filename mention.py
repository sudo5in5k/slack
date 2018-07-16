# -*- coding: utf-8 -*-


import json
import requests

"""
jsonのデータに従ってslackへ投稿するクラス
"""


class Mention(object):
    def __init__(self):
        with open('./jsons/webhook.json', 'r') as _channel_info:
            _slack_dic = json.load(_channel_info)
        self.WEBHOOK_URL = _slack_dic['info']['URL']
        self.PAYLOAD = _slack_dic['payload']


if __name__ == '__main__':
    mention = Mention()
    r = requests.post(mention.WEBHOOK_URL, data=json.dumps(mention.PAYLOAD))
