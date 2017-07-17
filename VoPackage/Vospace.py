# Classe traduisant les instructions en actions
import os
import shutil
from copy import deepcopy
from bson.json_util import dumps
from VoPackage.database import Handler as bdd
from VoPackage.genericbackend import Backend as fs
from VoPackage.settings import fsToDictionary
from VoPackage.voxml import Voxml as xml
from pymongo.errors import CursorNotFound
from datetime import datetime
from pprint import pprint


class Vospace(fs):

    RACINE = './VOTest'


    # Get the service's protocols/views/properties list
    def getVOSpaceSettings(self, meta):
        retour = {}
        coll = bdd().connexion()
        curseur = coll.find({'name': 'vo'+meta})
        if curseur:
            for documents in curseur:
                for keys, values in documents.items():
                    if keys == "metadata":
                        for k, v in values.items():
                                retour[k] = v
        return xml().xml_generator(meta, retour)

    # Get the node data
    def getNode(self, targetPath):
        # Retourne la représentation de la node
            self.target = os.path.basename(targetPath)
            self.parent = "nodes/"+os.path.basename(os.path.split(targetPath)[0])
            meta = bdd().getNode(self.target)
            if meta:
                # type = ''
                # if os.path.isfile(targetPath):
                #     type = 'StructuredDataNode'
                # elif os.path.isdir(targetPath):
                #     type = 'ContainerNode'
                self.node = {
                     # os.path.basename(targetPath) : type,
                        'children' : [],
                        'properties' : {},
                        'accepts' : {},
                        'provides' : {},
                        'busy': '',
                        }

                cursor = bdd().getChildrenNode(self.target)
                if cursor:
                    for items in cursor:
                        self.node['children'].append(items)
                self.node['busy'] = meta['busy']
                self.node['path'] = deepcopy(meta['path'])
                self.node['properties'] = deepcopy(meta['properties'])
                self.node['accepts'] = deepcopy(meta['accepts'])
                self.node['provides'] = deepcopy(meta['provides'])
                return xml().xml_generator('get', self.node)
            else :
                return FileNotFoundError

    def createNode(self, dictionary):
        # Creation de la node
        try:
            self.target = dictionary['cible']
            self.path = dictionary['path']
            if not bdd().getNode(self.target):
                try:
                   os.makedirs(self.path+"/"+self.target)
                except OSError as e:
                    return 'Directory creation failed. Error %s' % e
                try:
                    if os.path.exists(self.path+"/"+self.target):
                        bdd().insertDB(fsToDictionary(self.path+"/"+self.target))
                        self.setNode(self.path+"/"+self.target, dictionary['properties'])
                except OSError as e:
                    return 'BDD update failed. Error %s' % e
            return True
        except FileExistsError as e:
            return e

    def setNode(self, targetPath, properties):
        self.target = os.path.basename(targetPath)
        self.parent = os.path.basename(os.path.split(targetPath)[0])
        readOnly = bdd().getNode(self.target)
        try:
            if readOnly:
                self.properties = properties
                self.validator = {}
                for keys, values in readOnly['properties'].items():
                    for k, v in values.items():
                        self.validator[k] = v
                newProp = set(self.properties)
                oldProp = set(self.validator)
                propDict = bdd().getPropertiesDict()
                for key in newProp.intersection(oldProp):
                    propDict[key] = deepcopy(self.properties[key])
                    if readOnly['properties'][key]['readonly'] not in ["true", "True"]:
                        bdd().updateMeta(targetPath, key, propDict[key])
                #else:
                #   print("readOnly", key, propDict[key] )
            # else:
            #     for key in self.properties:
            #         print("clé", key, self.properties[key])
            #         if self.properties[key]['readOnly']:
            #             if self.properties[key]['readOnly'] != '':
            #                 bdd().updateMeta(target, key, self.properties[key])
            #             else:
            #                 self.properties[key]['readOnly'] = "false"
            #                 bdd().updateMeta(target, key, self.properties[key])
            #         else:
            #             self.properties[key]['readOnly'] = "false"
            #             bdd().updateMeta(target, key, self.properties[key])

        except CursorNotFound as e:
            return e

    def copyNode(self, targetPath, locationPath):
        # Copie la node et ses enfants
        self.loc = locationPath
        temp = {}
        try:
            cursor = bdd().getNode(targetPath)
            for items in cursor:
                for keys, values in items.items():
                    temp[keys] = values
        except:
            pass
        try:
            shutil.copytree(targetPath, self.loc)
            if temp:
                temp['path'] = self.loc
                temp['node'] = os.path.basename(self.loc)
                temp['properties']['mtime'] = {
                    "mtime": "Modified "+datetime.fromtimestamp(os.path.getmtime(targetPath)).strftime(
                        "%Y-%m-%d %H:%M:%S"), "readOnly" : "True"}
                temp['properties']['ctime'] = {
                    "ctime": "MetaData modified "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "readOnly" : "True"}
                temp['properties']['btime'] = {
                    "btime": "Creation date "+datetime.fromtimestamp(os.path.getctime(targetPath)).strftime(
                        "%Y-%m-%d %H:%M:%S"), "readOnly" : "True"}
                bdd().insertDB(temp)
        except shutil.Error as e:
            print('Directory not copied. Error: %s' % e)
            # Copie au même emplacement
        except OSError as e:
            print('Directory not copied. Error: %s' % e)
            # Copie échouée

    def moveNode(self, targetPath, locationPath):
        # Deplace la node et ses enfants
        pass

    def deleteNode(self, targetPath):
        # Supprime la node et ses enfants
        try:
            self.target = os.path.basename(targetPath)
            self.parent = os.path.basename(os.path.split(targetPath)[0])
            if os.path.exists(targetPath):
                if os.path.isdir(targetPath):
                    shutil.rmtree(targetPath)
                elif os.path.isfile(targetPath):
                    os.remove(targetPath)
                try:
                    bdd().connexion().delete_one({'node': self.target, 'parent': self.parent})
                    bdd().connexion().delete_many({'parent': self.target})
                except CursorNotFound:
                    return False
        except FileNotFoundError:
            raise

    def pushToVoSpace(self, targetPath, **kwargs):
        # Execute un push to VOSpace
        pass

    def pushFromVoSpace(self, targetPath, **kwargs):
        # Execute un push from VOSpace
        pass

    def pullFromVoSpace(self, targetPath, **kwargs):
        # Execute un pull from VOSpace
        pass

    def pullToVoSpace(self, targetPath, endpointUri):
        # Execute un pull to VOSpace
        pass

#
#a = Vospace()
# print(bdd().nodeExistsChecker(os.path.basename("./VOTest/VOSpace/nodes/myresult1")))
# a.startup()
# # print(a.getEndpoint("./VOTest/VOSpace/nodes/myresult1"))
# # for k,v in a.getNode("./VOTest/VOSpace/nodes/myresult1")['properties']['type'].items():
# #     print(v)
# # a.createNode("./VOTest/VOSpace/nodes/myresult5", "ContainerNode")
# # print(a.nodeExistsChecker(os.path.basename("./VOTest/VOSpace/nodes/myresult4")))
#a.setNode("./VOTest/VOSpace/nodes/myresult1",{'title' : {"title": "PIF", 'readOnly': 'True'},
#                                            'description' : {"description": "Yet Another Node", 'readOnly': 'false'},
#                                           'contributor' : {"contributor": "Foo", 'readOnly': 'false'},
#                                            'language': {"language": "Allemand", 'readOnly': ''}})
#print(bdd().getNodeProperties("myresult1"))
# # print(a.copyNode("./VOTest/VOSpace/nodes/myresult1", "./VOTest/copy/myresult1"))
# bdd().setViews("./VOTest/VOSpace/nodes/myresult1",{'anyview' : 'ivo://ivoa.net/vospace/core#anyview', 'fits' : 'ivo://ivoa.net/vospace/core#fits' },
#                                                      {'default' : 'ivo://ivoa.net/vospace/core#defaultview', 'fits' :  'ivo://ivoa.net/vospace/core#fits' })

# pprint(bdd().getMeta("./VOTest/copy/myresult1"))
# a.deleteNode("./VOTest/copy/myresult2/metamyresult2")
# print(os.path.exists("./VOTest/copy/myresult2/metamyresult2"))