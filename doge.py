import requests
from decimal import Decimal
import json


class DingTalk_Base:
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.url = ''
    def send_msg(self,text):
        json_text = {
            "msgtype": "text",
            "text": {
                "content": text
            },
            "at": {
                "atMobiles": [
                    ""
                ],
                "isAtAll": True
            }
        }
        return requests.post(self.url, json.dumps(json_text), headers=self.__headers).content
class DingTalk_Disaster(DingTalk_Base):
    def __init__(self):
        super().__init__()
        # 填写机器人的url
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=ed67643de366bb6d9a917a87707fa1dbcd038d5933df99c7b7fc7de70a5571a5'
if __name__ == '__main__':
    
    dogeUrl = 'https://api.hbdm.com/linear-swap-ex/market/history/kline?contract_code=DOGE-USDT&period=1min&size=1'
    dogeResponse =  requests.get(dogeUrl)
    dogeJson = json.loads(dogeResponse.text)
    dogeData = dogeJson['data']
    dogeData = dogeData[-1]
    print(dogeData)
    
    cny = 6.5555
    dogeHeight = Decimal(dogeData['high'] * cny).quantize(Decimal('0.000000'))
    dogeLow = Decimal(dogeData['low'] * cny).quantize(Decimal('0.000000'))
    dogeClose = Decimal(dogeData['close'] * cny).quantize(Decimal('0.000000'))
    msgContent = '狗狗币\n最新价位: {} 最高价 {}  最低价 {} \nusdt价格: {} 最高价 {}  最低价 {}\t '.format(dogeClose,dogeHeight,dogeLow,dogeData['close'],dogeData['high'],dogeData['low'])
    #print(dogeJson['data'])
    
    ding = DingTalk_Disaster()
    ding.send_msg(msgContent)
    