import sys
import json
from collections import defaultdict, Counter


def main():
    with open(sys.argv[1]) as f:
        msgs = json.load(f)
    fields = defaultdict(Counter)
    for msg in msgs:
        for k, v in msg.items():
            fields[k][v] += 1
    for k, c in sorted(fields.items(), key=lambda kc: (kc[0], len(kc[1].keys()))):
        card = len(c.keys())
        print(k, card)
        if card > 10:
            continue
        for v, f in c.most_common():
            print('\t', v, f)
    # print(fields['from'])
    # print(fields['idClient'])
    print('-----')
    fields.clear()
    for msg in msgs:
        for k, v in json.loads(msg['custom']).items():
            if isinstance(v, dict):
                # print(k, v)
                # continue
                v = json.dumps(v)
            fields[k][v] += 1
    for k, c in sorted(fields.items(), key=lambda kc: (kc[0], len(kc[1].keys()))):
        card = len(c.keys())
        print(k, card)
        if card > 10:
            continue
        for v, f in c.most_common():
            print('\t', v, f)
    # print(fields['config'])
    # print(fields['text'])
    # print(fields['user'])
    print(fields['sessionRole'])


'''
jq '. | map(select(.custom | fromjson | .sessionRole == 3)) | .[].custom | fromjson'
'''


'''
chatroomId 1
         67362271 100
custom 94
flow 1
         in 100
from 88
fromAvatar 1
          100
fromClientType 3
         Android 61
         iOS 33
         Server 6
fromCustom 1
          94
fromNick 2
          94
         不是革青韦 6
idClient 100
resend 1
         False 100
status 1
         success 100
text 1
          100
time 100
type 1
         text 100
userUpdateTime 91
-----
bubbleId 13
config 79
fromApp 1
         201811 100
giftInfo 3
         {"giftId": 888001, "giftName": "1\u6295\u7968\u6743", "picPath": "/2021/0612/000x2q71d7a96kn1nuu10bfx6nv.png", "switchTime": 63, "click": false, "special": true, "giftNum": 1, "zipPath": "/2021/0614/zx_gift_1_01.zip", "sourceId": "67362271", "acceptUser": {"userId": 327597, "userAvatar": "/mediasource/avatar/20180829/1535545582428vP45t8wGVs.jpg", "userName": "SNH48-\u82cf\u6749\u6749"}, "ext": "{\"vote\":1}"} 6
         {"sourceId": "67362271", "adaptUser": 0, "giftName": "1\u6295\u7968\u6743", "isGif": false, "businessId": "67362271", "roomId": "67362271", "giftId": 888001, "businessCode": 2, "isLive": false, "messageType": "PRESENT_NORMAL", "giftModuleId": 0, "giftNum": 1, "useTime": 0, "additionalData": 0, "melee": 0, "giftTypeMd": "", "vip": false, "isVote": true, "crm": "QvAcHngU/c+sLUVJf/Jf2w==", "acceptUserId": 327597, "acceptUserName": "SNH48-\u82cf\u6749\u6749", "sendTimes": 0, "click": false, "isNoSHow": false, "switchTime": 63, "userId": 0, "picPath": "/2021/0612/000x2q71d7a96kn1nuu10bfx6nv.png", "special": true, "money": 1, "typeId": 888} 5
         {"fullPicPath": "https://source.48.cn/2021/0612/000x2q71d7a96kn1nuu10bfx6nv.png", "picPath": "/2021/0612/000x2q71d7a96kn1nuu10bfx6nv.png", "click": false, "adaptUser": 0, "isVote": true, "special": true, "additionalData": 0, "giftNum": 1, "giftTypeMd": "", "giftId": "888001", "money": 1, "giftName": "1\u6295\u7968\u6743", "typeId": "888"} 1
keyWordStatus 1
         False 89
md5 36
messageType 3
         TEXT 88
         PRESENT_TEXT 6
         PRESENT_FULLSCREEN 6
module 2
         session 94
         SESSION 6
roomId 1
         67362271 100
sessionRole 2
         0 94
         0 6
sourceId 1
         67362271 100
text 70
user 90
'''


if __name__ == '__main__':
    main()
