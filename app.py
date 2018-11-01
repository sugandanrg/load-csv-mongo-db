import csv
from mongoengine import *
from csvload import * #model import
from config import conf as config #mongodb instance connection details

loadData = []
csvFile = csv.DictReader(open("testData.csv"))
#dataset = [i for i in csv_file if i['data'] > 0  i['data'] != '' ]
#{'id': int, 'data': int, 'FactorConfigId': int, 'createdAt': str}  //if int(i['data']) > 0 and int(i['data']) != ''
for d in map(dict, csvFile):
    loadData.append(d)

#validData = [i for i in loadData i]

for i in loadData:
    if int(i['data']) > 0 and int(i['data']) != '':
        print(int(i['data']))

connect(host='mongodb+srv://' + config['username'] + ':'
                              + config['pwd'] + '@cluster0-hd2ly.mongodb.net/'
                              + config['db'])

print(coincaps.objects.count())
print(len(validData))
