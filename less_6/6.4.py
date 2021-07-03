import json
from datetime import timedelta


def ac_dc_duration():
    with open('acdc.json', 'r+') as file:
        dict_ac_dc = json.load(file)
        tracks = dict_ac_dc['album']['tracks']['track']
        total = [int(track['duration']) for track in tracks]
        print(sum(total))
        print(str(timedelta(seconds=sum(total))))

ac_dc_duration()