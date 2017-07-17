import pymongo as mongo
import os
from datetime import datetime
from bson.json_util import dumps
from copy import deepcopy
from pymongo.errors import ConnectionFailure, CursorNotFound, OperationFailure

class Handler(object):

    def connexion(self):
        try:
            c = mongo.MongoClient('localhost', 27017)
            db = c['vospace']
            coll = db['VOSpaceFiles']
            return coll
        except ConnectionFailure:
            print("Could not connect to MongoDB")


    # Check if node exists in mongoDB
    def nodeExistsChecker(self, cible):
        coll = self.connexion()
        if coll.find({'node': os.path.basename(cible)}).count(True):
            return True
        return False

    # Insert into mongoDB
    def insertDB(self, data):
        try:
            coll = self.connexion()
            coll.insert_one(data)
        except OperationFailure as e:
            return e


    # Get the metadata representation from mongoDB
    def getNode(self, cible):
        try:
            coll = self.connexion()
            curseur = coll.find({'node': cible},{"_id":0})
            temp = {}
            for document in curseur:
                for keys, values in document.items():
                    temp[keys] = values
            return temp
        except CursorNotFound as e:
            return e

    def getNodeProperties(self, node):
        dictionary = {}
        for items in self.connexion().find({"node": os.path.basename(node)}, {"properties": 1, "_id": 0}):
            for keys,values in items.items():
                for k,v in values.items():
                    dictionary[k] = v
        return dictionary

    def getChildrenNode(self, node):
        return self.connexion().find({"parent": node}, {"path":1, "busy":1, "properties": 1, "_id": 0})

    # # Copy node metadata when a node is being copied
    # def copyNode(self, cible, data):
    #     nodeCible = os.path.basename(cible)
    #     donnee = data
    #     if not self.getMeta(nodeCible):
    #         donnee['properties']['mtime'] = {
    #             "mtime": "Modified "+datetime.datetime.fromtimestamp(os.path.getmtime(cible)).strftime(
    #                 "%Y-%m-%d %H:%M:%S"), "readOnly" : "True"}
    #         donnee['properties']['ctime'] = {
    #             "ctime": "MetaData modified "+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "readOnly" : "True"}
    #         donnee['properties']['btime'] = {
    #             "btime": "Creation date "+datetime.datetime.fromtimestamp(os.path.getctime(cible)).strftime(
    #                 "%Y-%m-%d %H:%M:%S"), "readOnly" : "True"}
    #         self.insertionMongo(donnee)

    # Get Property empty dictionary from DB
    def getPropertiesDict(self):
        retour = {}
        coll = self.connexion()
        curseur = coll.find({'name': 'propertiesdict'},{"metadata":1, "_id":0})
        for documents in curseur:
            for keys, values in documents.items():
                    for k,v in values.items():
                        retour[k] = v
        return retour


    # Update node metadata, if not set, create new representation
    def updateMeta(self, targetPath, key, data):
        coll = self.connexion()
        nodeCible = os.path.basename(targetPath)
        cle = key
        donnee = data
        if self.getNode(nodeCible):
                if donnee[1] != '':
                    coll.update({'node' : nodeCible},{"$set" : { 'properties.'+cle+'.'+cle : donnee[0]}})
                elif donnee[0] == "readonly" and donnee[1] == '':
                    donnee[1] = "False"
                    coll.update({'node': nodeCible}, {"$set": {'properties.' + cle+'.'+cle: donnee[0]}})
                else:
                    coll.update({'node': nodeCible}, {"$unset": {'properties.'+cle+'.'+cle : ''}})
        else:
            self.prop_ = {
                'node': nodeCible,
                'path': targetPath,
                'parent': "nodes/"+os.path.basename(os.path.split(targetPath)[0]),
                'ancestor': [],
                'accepts': [],
                'provides': [],
                'properties': {},
            }
            self.prop_['properties'] = self.getPropertiesDict()
            self.prop_['properties']['mtime'] = {
                    "mtime": "Modified "+datetime.fromtimestamp(os.path.getmtime(targetPath)).strftime(
                        "%Y-%m-%d %H:%M:%S"), "readOnly" : "True"}
            self.prop_['properties']['ctime'] = {
                    "ctime": "MetaData modified "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "readOnly" : "True"}
            self.prop_['properties']['btime'] = {
                    "btime": "Creation date "+datetime.fromtimestamp(os.path.getctime(targetPath)).strftime(
                        "%Y-%m-%d %H:%M:%S"), "readOnly" : "True"}
            self.prop_['properties'][cle] = donnee[cle]
            self.insertDB(self.prop_)

    def setViews(self, cible, accepts, provides):
        coll = self.connexion()
        nodeCible = os.path.basename(cible)
        if self.getNode(cible):
            coll.update({'path': cible}, {"$set": {'accepts': accepts, 'provides': provides}})
            with open(cible + "/" + 'meta' + os.path.basename(nodeCible), 'w') as m:
                m.write(dumps(self.getNode(cible)))
                m.close()


# a = Handler()


# pprint(a.getMeta("./VOTest/VOSpace/nodes/myresult1"))
# print(a.nodeExistsChecker('myresult1.txt'))
# print(a.fsToDict('/home/bouchair/PycharmProjects/VOSpace-Py/VOTest/VOSpace/nodes/myresult1/Capability'))
# print(a.getVOSpaceSettings('voviews'))
# print(a.getMeta("./VOTest/VOSpace/nodes/myresult1"))
# a.insertionMongo(a.metaDB("./VOTest/VOSpace/nodes/myresult1"), 'NodeMeta')
# a.insertionMongo(a.metaDB("./VOTest/VOSpace/nodes/myresult2"), 'NodeMeta')
# a.insertionMongo(a.metaDB("./VOTest/VOSpace/nodes/myresult3"), 'NodeMeta')
# meta = a.metaDB("./VOTest/VOSpace/nodes/myresult1")
# if a.modifMeta("myresult3", meta):
#       print("Updated")
# a.insertionMongo(a.fsToDict("./VOTest/VOSpace/nodes/myresult1"), 'VOSpaceFiles')
# a.insertionMongo(a.fsToDict("./VOTest/VOSpace/nodes/myresult2"), 'VOSpaceFiles')
# a.insertionMongo(a.fsToDict("./VOTest/VOSpace/nodes/myresult3"), 'VOSpaceFiles')
