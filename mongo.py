import pymongo as mongo
import json


with open('VoJson.json', 'r') as j:
    jdic = json.load(j)

print(isinstance(jdic, dict))


# c = mongo.MongoClient('localhost', 27017)
# db = c['vospace']
# coll = db['arbre']
# for x in jdic:
#     for index, item in enumerate(x):
#             if coll.insert_one(item[index]):
#                print("OK")
#             else:
#                print("Failed")








