import sys
import json
import csv


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


if __name__ == '__main__':
    people_tsv_to_json()
