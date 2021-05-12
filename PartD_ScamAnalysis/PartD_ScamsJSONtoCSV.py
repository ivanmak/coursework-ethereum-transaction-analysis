import json

with open('scams.json') as json_file:
    data = json.load(json_file)

out_file = open('scams.csv', 'w')

for k in data['result'].keys():
    for i in data['result'][k]['addresses']:
        out_file.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(k, data['result'][k]['name'], data['result'][k]['url'], data['result'][k]['coin'], data['result'][k]['category'] if data['result'][k]['category'] != 'Scam' else 'Scamming', data['result'][k]['subcategory'] if 'subcategory' in data['result'][k] else "", i, data['result'][k]['status']))

out_file.close()
