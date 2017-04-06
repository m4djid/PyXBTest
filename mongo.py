import pymongo as mongo
import json
import os
import time
import datetime
import errno
import pprint
# with open('VoJson.json', 'r') as j:
#     jdic = json.load(j)
#
# print(isinstance(jdic, dict))


# c = mongo.MongoClient('localhost', 27017)
# db = c['vospace']
# coll = db['arbre']
# for x in jdic:
#     for index, item in enumerate(x):
#             if coll.insert_one(item[index]):
#                print("OK")
#             else:
#                print("Failed")


def metaDB(path):
    accept = path + '/view_accept.txt'
    provide = path + '/view_provide.txt'
    chemin = path + '/property.txt'
    prop_ = {
        'node' :  os.path.basename(path),
        'path' : path[1:],
        'accept': [],
        'provide' : [],
        'properties': [],
    }
    print("start : " + path)
    try:
        with open(accept, 'r') as acceptation:
            for ligne in acceptation:
                if ligne == "":
                    break
                prop_['accept'].append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % accept)

    try:
        with open(provide, 'r') as offerte:
            for ligne in offerte:
                if ligne == "":
                    break
                prop_['provide'].append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % provide)

    try:
        with open(chemin, 'r') as p:
            for ligne in p:
                if ligne == "":
                    break
                prop_['properties'].append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % chemin)



def octet(entier):
    taille_ = entier
    retour = ''
    if taille_ >= 1000 and taille_ < 1000000:
        retour = str(round(taille_ / 100, 2)) + 'ko'
    elif taille_ >= 1000000:
        retour = str(round(taille_ / 1000000, 2)) + 'Mo'
    elif taille_ < 1000:
        retour = str(taille_) + 'o'
    return retour

def get_size_dir(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
    return octet(total_size)

def path_hierarchy(path):
    taille = get_size_dir(path)
    tempdate = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    mdate =  tempdate.strftime("%Y-%m-%d %H:%M:%S")
    owner = str(os.stat(path).st_uid)
    fName = os.path.basename(path)
    hierarchy = {
        'type': 'folder',
        'name': fName,
        'path': path,
        'size': taille,
        'modified': mdate,
        'ownerId' : owner,
    }

    try:
        for index, contents in enumerate(os.listdir(path)):
            hierarchy["subnode : "+str(index)] = path_hierarchy(os.path.join(path, contents))
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['type'] = 'file'
        hierarchy['size'] = octet(os.path.getsize(path))
    return hierarchy

def insertionMongo(data, collection):
    start_time = time.time()
    c = mongo.MongoClient('localhost', 27017)
    db = c['vospace']
    coll = db[collection]
    if coll.insert_one(data):
        print("OK")
    else:
        print("Failed")
    print("--- %s seconds ---" % (time.time() - start_time))

# insertionMongo(path_hierarchy("./VOTest/VOSpace/nodes/myresult1"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace/nodes/myresult2"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace/nodes/myresult3"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace2/nodes/myresult1"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace2/nodes/myresult3"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace2/nodes/myresult4"), 'arbre')
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(path_hierarchy("./VOTest/VOSpace/nodes/myresult1"))