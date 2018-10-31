import csv
from mongoengine import *
from csvload import *

loadData = [{'id': int, 'data': int, 'FactorConfigId': int, 'createdAt': str}]
csv_file = csv.DictReader(open("testData.csv"))
#dataset = [i for i in csv_file if i['data'] > 0  i['data'] != '' ]
for d in map(dict, csv_file):
    loadData.append(d)

print(loadData)

connect(host='mongodb+srv://sugandanrg:changednow!@cluster0-hd2ly.mongodb.net/coindesk')
