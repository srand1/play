import sys
import json
from collections import defaultdict, Counter
import datetime


def scan():
    with open(sys.argv[1]) as f:
        msgs = json.load(f)
    fields = defaultdict(Counter)
    for msg in msgs:
        for k, v in msg.items():
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
    # print(fields['from'])
    # print(fields['idClient'])
    # print(fields['file'])
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
        if card > 10 and k != 'messageType':
            continue
        for v, f in c.most_common():
            print('\t', v, f)
    # print(fields['config'])
    # print(fields['text'])
    # print(fields['user'])
    # print(fields['giftInfo'])
    print(fields['sessionRole'])


def html():
    with open(sys.argv[1]) as f:
        msgs = json.load(f)
    divs = []
    for msg in msgs:
        custom = json.loads(msg['custom'])
        render = globals().get('render_'+custom['messageType'])
        if not render:
            continue
        try:
            divs.append(render(msg, custom))
        except Exception as e:
            print(e, custom, file=sys.stderr)
    ans = HTML.format('\n'.join(divs))
    print(ans)


def render_TEXTx(msg, custom):
    dt = datetime.datetime.fromtimestamp(msg['time'] / 1000.)
    roleId = custom.get('user', {}).get('roleId')
    x = {
        'roleId': roleId,
    }
    return '''\
    <div class="msg {messageType}">
        <span>{datetime}</span>
        <span>{user[nickName]}({sessionRole})</span>
        <span>{text}</span>
    </div>\
    '''.format(
        datetime=dt.isoformat(' '),
        x=x,
        **custom,
    )


def render_PRESENT_TEXT(msg, custom):
    dt = datetime.datetime.fromtimestamp(msg['time'] / 1000.)
    roleId = custom.get('user', {}).get('roleId')
    x = {
        'roleId': roleId,
    }
    return '''\
    <div class="msg {messageType}">
        <span>{datetime}</span>
        <span>{user[nickName]}({sessionRole})</span>
        <span>{giftInfo[giftName]}</span>
    </div>\
    '''.format(
        datetime=dt.isoformat(' '),
        x=x,
        **custom,
    )


def main():
    # scan()
    html()


HTML = '''\
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Msgs</title>

<div id="msgs">
{}
</div>\
'''


'''
jq '. | map(select(.custom | fromjson | .sessionRole == 3)) | .[].custom | fromjson'
'''


'''
chatroomId 1
	 67362271 2308
custom 1911
file 60
flow 1
	 in 2308
from 265
fromAvatar 1
	  2308
fromClientType 3
	 iOS 1318
	 Server 640
	 Android 350
fromCustom 1
	  1668
fromNick 2
	  1691
	 不是革青韦 617
idClient 2308
resend 2
	 False 2304
	 True 4
status 1
	 success 2308
text 3
	  2293
	 偶像翻牌 10
	 分享消息 5
time 2305
type 3
	 text 2248
	 image 49
	 video 11
userUpdateTime 632
-----
answer 10
	 {"url":"/2021/0619/qix87i7dy0vmlk4mewznr0x.aac","duration":22,"size":0} 1
	 {"url":"/2021/0618/8x2oj15q1a36454i62xm0co.aac","duration":10,"size":0} 1
	 {"url":"/2021/0617/e0v4rnoahjntsz58kg7dz8j.aac","duration":16,"size":0} 1
	 {"url":"/2021/0617/nqp1892qqej7xni0pfsxayu.aac","duration":12,"size":0} 1
	 {"url":"/2021/0617/to35t9rbknmhamufd27grfx.aac","duration":21,"size":0} 1
	 {"url":"/2021/0617/h5uvp76de93ldairrrzd81b.aac","duration":5,"size":0} 1
	 早上好呀！！高考结束啦！！是不是很快乐hhhhhh也谢谢你喜欢我捏 1
	 谢谢你嗷～这次时间仓促准备不了太多，希望有几乎你可以来国内看我喔 1
	 hhhhhh平手在舞台上真的就是天赋呀，可惜没能在她在团的时候看现场，以后机会更渺茫了 1
	 谢谢你嗷！也希望你天天好心情嘞！以后也要一直陪着我嗷 1
answerId 10
	 1215890 1
	 1214097 1
	 1211929 1
	 1210222 1
	 1210219 1
	 1210205 1
	 1205184 1
	 1201508 1
	 1196717 1
	 1196714 1
answerType 2
	 2 6
	 1 4
bubbleId 26
config 189
fromApp 1
	 201811 2307
giftInfo 48
jumpPath 4
	 live/playdetail?id=612326956873879552 1
	 post/detail?id=612049400106913792 1
	 live/playdetail?id=610630767686258688 1
	 post/detail?id=603675978297577472 1
jumpType 1
	 APP_PAGE 4
keyWordStatus 1
	 False 1318
liveCover 7
	 /2021/0619/327597x2hl40xy28x86mqqool1xj9a.jpg 1
	 /2021/0619/327597x1jltbfrxk69q5h0b8t3xfq0.jpg 1
	 /2021/0618/327597xui5tgz7p1m2o9s8wvruth4g.jpg 1
	 /2021/0617/327597xsxt4t8dqa6r0719b93h7sxy.jpg 1
	 /2021/0615/327597xvptf4g0410m1vrof0yb7ulo.jpg 1
	 /2021/0614/327597xps7on9dhxrmhaeyehsjqs2i.jpg 1
	 /2021/0612/327597xlf2j1wsyg8jo4j2iy4zyokn.jpg 1
liveId 7
	 613140801334874112 1
	 612798453920894976 1
	 612459642284216320 1
	 612434318888603648 1
	 611689226498281472 1
	 611315652230975488 1
	 610266490328649728 1
liveTitle 1
	 十分钟 7
liveUserName 2
	 BEJ48-黄妍菲 1
	 BEJ48-任蔓琳 1
md5 1326
messageType 14
	 TEXT 909
	 PRESENT_TEXT 616
	 PRESENT_FULLSCREEN 598
	 REPLY 81
	 IMAGE 49
	 PRESENT_NORMAL 19
	 VIDEO 11
	 LIVEPUSH 7
	 FLIPCARD_AUDIO 6
	 FLIPCARD 4
	 GIFTREPLY 3
	 SHARE_LIVE 2
	 SHARE_POSTS 2
	 DISABLE_SPEAK 1
module 2
	 session 1668
	 SESSION 639
question 10
	 ...
questionId 10
	 610620514739490816 1
	 609904152735977472 1
	 609869337307451392 1
	 609830353038544896 1
	 609826752446664704 1
	 609815981507547136 1
	 608532723184504832 1
	 607866789667082240 1
	 607298097917005824 1
	 607192611905409024 1
replyMessageId 84
replyName 69
replyText 84
roomId 1
	 67362271 2307
sessionRole 5
	 2 1013
	 0 622
	 0 619
	 3 36
	 2 17
shareDesc 5
	 帖子分享 1
	 2021-06-17 16:48:42 1
	 被433带的沉迷星座[嘘] 1
	 2021-06-13 00:28:39 1
	 惨哥应该是中心最丑的猫咪吧？ 1
sharePic 4
	 http://source.48.cn/resize_300x300/2021/0617/45285677xmjjgtf6pautl27jnk7nswui.jpg 1
	 /2021/0616/50856760x13ucf7kz340ldysqq7v46zu.jpg 1
	 /2021/0613/831078xq4a5cvin26dho11i8t7t67z.jpg 1
	 /20210524/1621857168006wb9mr6avi2.jpg 1
shareTitle 4
	 嗨 1
	 最近沉迷星座 1
	 芜湖！ 1
	 小东西还挺别致 1
shortPath 7
	 live/playdetail?id=613140801334874112 1
	 live/playdetail?id=612798453920894976 1
	 live/playdetail?id=612459642284216320 1
	 live/playdetail?id=612434318888603648 1
	 live/playdetail?id=611689226498281472 1
	 live/playdetail?id=611315652230975488 1
	 live/playdetail?id=610266490328649728 1
sourceId 1
	 67362271 2308
targetId 1
	 42140013 1
teamLogo 2
	 /20200904/15992025288054qD21JfZgU.png 1
	  1
text 918
user 561
'''


if __name__ == '__main__':
    main()
