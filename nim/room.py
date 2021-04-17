import sys
import json
import csv
from collections import defaultdict, Counter


def room_json_to_csv():
    with open(sys.argv[1]) as f:
        obj = json.load(f)
    w = csv.DictWriter(sys.stdout, ['name', 'id', 'ownerName', 'roomId', 'account'])
    w.writeheader()
    for room in obj['roomId']:
        name = room['ownerName'].rsplit('-', 1)[-1]
        room['name'] = name
        w.writerow(room)


def people_tsv_to_json():
    ans = []
    with open(sys.argv[1]) as f:
        for l in f:
            team, abbr, name, zo48, id_, ownerName, roomId, account = l.split('\t')[:8]
            if not roomId:
                continue
            people = {
                'name': name,
                'roomId': roomId,
                'abbr': abbr,
            }
            ans.append(people)
    print('DataPeople = ', end='')
    json.dump(ans, sys.stdout)
    print(';')


def inspect_store():
    with open(sys.argv[1]) as f:
        obj = json.load(f)
    # keys = set()
    roleId = Counter()
    sessionRole = Counter()
    for key, msg in obj.items():
        if not key.startswith('xoxmsg-'):
            continue
        msg = json.loads(msg)
        custom = msg['custom']
        # print(custom)
        if 'sessionRole' not in custom:
            # print(custom)
            continue
        sessionRole[custom['sessionRole']] += 1
        if custom['sessionRole'] != 0:
            print(custom)
        # keys.update(custom.keys())
        if 'user' not in custom:
            # print(custom)
            continue
        # print(custom['user'])
        roleId[custom['user']['roleId']] += 1
        if custom['user']['roleId'] == 3:
            print(custom)
        if 'text' not in custom:
            # print(custom)
            continue
        # print(custom['text'])
    # print(keys)
    print(roleId)
    print(sessionRole)


if __name__ == '__main__':
    inspect_store()
