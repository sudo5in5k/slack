# -*- coding: utf-8 -*-

import requests
import json

"""
jsonのデータに従ってslackのチャンネルでの発言のデータを取得するクラス
"""


class Slack:
    def __init__(self):
        with open('./jsons/channel_params.json', 'r') as _channel_info:
            _slack_dic = json.load(_channel_info)
        self.SLACK_URL = _slack_dic['channel']['URL']
        self.SLACK_CHANNEL_ID = _slack_dic['channel']['ID']
        self.TOKEN = _slack_dic['channel']['TOKEN']

    @property
    def channel_id(self):
        return self.SLACK_CHANNEL_ID

    @channel_id.setter
    def channel_id(self, another):
        self.SLACK_CHANNEL_ID = another

    @property
    def json_channel_data(self):
        payload = {
            "channel": self.SLACK_CHANNEL_ID,
            "token": self.TOKEN
        }
        _response = requests.get(self.SLACK_URL, payload)
        _json_data = _response.json()
        return _json_data

    @property
    def msg(self):
        _data = self.json_channel_data
        return _data['messages']

    @property
    def text(self):
        return [msg['text'] for msg in self.msg]
