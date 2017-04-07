import pymongo as mongo
import json
import os
import time
import datetime
import errno
import pprint



def metaDB(path):
    accept = path + '/view_accept.txt'
    provide = path + '/view_provide.txt'
    chemin = path + '/property.txt'
    prop_ = {
        'node' :  os.path.basename(path),
        'path' : path[1:],
        'accepts': [],
        'provides' : [],
        'properties': [],
    }
    print("start : " + path)
    try:
        with open(accept, 'r') as acceptation:
            for ligne in acceptation:
                if ligne == "":
                    break
                prop_['accepts'].append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % accept)

    try:
        with open(provide, 'r') as offerte:
            for ligne in offerte:
                if ligne == "":
                    break
                prop_['provides'].append(ligne.split("\n")[0])
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
    return prop_


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

def connexion(collection):
    c = mongo.MongoClient('localhost', 27017)
    db = c['vospace']
    coll = db[collection]
    return coll

def insertionMongo(data, collection):
    start_time = time.time()
    coll = connexion(collection)
    if coll.insert_one(data):
        print("OK")
    else:
        print("Failed")
    print("--- %s seconds ---" % (time.time() - start_time))

def modifMeta(cible, data):
    coll = connexion('NodeMeta')
    temp = {}
    for keys, values in data.items():
        temp[keys] = values
    for key, values in temp.items():
        coll.update_one({'node' : cible},{"$set" : {key : values}})

def metaChecker(cible):
    start_time = time.time()
    coll = connexion('NodeMeta')
    curseur = coll.find({'node':cible})
    temp = {}
    for document in curseur:
        for keys, values in document.items():
            if keys != "_id":
                temp[keys] = values
    print("--- %s seconds ---" % (time.time() - start_time))
    return temp

# insertionMongo(path_hierarchy("./VOTest/VOSpace/nodes/myresult1"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace/nodes/myresult2"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace/nodes/myresult3"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace2/nodes/myresult1"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace2/nodes/myresult3"), 'arbre')
# insertionMongo(path_hierarchy("./VOTest/VOSpace2/nodes/myresult4"), 'arbre')
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(path_hierarchy("./VOTest/VOSpace/nodes/myresult1"))

# meta = metaDB("./VOTest/VOSpace/nodes/myresult3")
# if modifMeta("myresult3", meta):
#       print("Updated")

# insertionMongo(metaDB("./VOTest/VOSpace/nodes/myresult1"), 'NodeMeta')
# insertionMongo(metaDB("./VOTest/VOSpace/nodes/myresult2"), 'NodeMeta')
# insertionMongo(metaDB("./VOTest/VOSpace/nodes/myresult3"), 'NodeMeta')

print(metaChecker('myresult3'))