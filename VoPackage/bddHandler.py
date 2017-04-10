import pymongo as mongo
import os
import datetime
import errno


class Handler(object):

    def metaDB(self, path):
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


    def octet(self, entier):
        taille_ = entier
        retour = ''
        if taille_ >= 1000 and taille_ < 1000000:
            retour = str(round(taille_ / 100, 2)) + 'ko'
        elif taille_ >= 1000000:
            retour = str(round(taille_ / 1000000, 2)) + 'Mo'
        elif taille_ < 1000:
            retour = str(taille_) + 'o'
        return retour

    def getSizeDir(self, start_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
        return self.octet(total_size)

    def fsToDict(self, path):
        taille = self.getSizeDir(path)
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
                hierarchy["subnode : "+str(index)] = self.fsToDict(os.path.join(path, contents))
        except OSError as e:
            if e.errno != errno.ENOTDIR:
                raise
            hierarchy['type'] = 'file'
            hierarchy['size'] = self.octet(os.path.getsize(path))
        return hierarchy

    def connexion(self, collection):
        c = mongo.MongoClient('localhost', 27017)
        db = c['vospace']
        coll = db[collection]
        return coll

    def nodeExistsChecker(self, node):
        coll = self.connexion('arbre')
        if coll.find({'node': node}):
            return True

    def insertionMongo(self, data, collection):
        coll = self.connexion(collection)
        if coll.insert_one(data):
            print("OK")
        else:
            print("Failed")

    def modifMeta(self, cible, data):
        coll = self.connexion('NodeMeta')
        temp = {}
        for keys, values in data.items():
            temp[keys] = values
        for key, values in temp.items():
            coll.update_one({'node' : cible},{"$set" : {key : values}})

    def metaChecker(self, cible):
        coll = self.connexion('NodeMeta')
        curseur = coll.find({'node':cible})
        temp = {}
        for document in curseur:
            for keys, values in document.items():
                if keys != "_id":
                    temp[keys] = values
        return temp


a = Handler()
# a.insertionMongo(a.metaDB("./VOTest/VOSpace/nodes/myresult1"), 'NodeMeta')
# a.insertionMongo(a.metaDB("./VOTest/VOSpace/nodes/myresult2"), 'NodeMeta')
# a.insertionMongo(a.metaDB("./VOTest/VOSpace/nodes/myresult3"), 'NodeMeta')
# meta = a.metaDB("./VOTest/VOSpace/nodes/myresult1")
# if a.modifMeta("myresult3", meta):
#       print("Updated")
# a.insertionMongo(a.fsToDict("./VOTest/VOSpace/nodes/myresult1"), 'arbre')
# a.insertionMongo(a.fsToDict("./VOTest/VOSpace/nodes/myresult2"), 'arbre')
# a.insertionMongo(a.fsToDict("./VOTest/VOSpace/nodes/myresult3"), 'arbre')


# print(a.metaChecker('myresult1'))