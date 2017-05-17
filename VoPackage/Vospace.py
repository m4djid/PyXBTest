# Classe traduisant les instructions en actions
import os
import shutil
from copy import deepcopy
from bson.json_util import dumps
from VoPackage.database import Handler as bdd
from VoPackage.genericbackend import Backend as fs
from VoPackage.settings import fsToDict
from VoPackage.voxml import Voxml as xml
from pymongo.errors import CursorNotFound


class Vospace(fs):

    RACINE = './VOTest'


    #
    # # Check if node exists in the FileSystem or DB
    # def nodeExists(self, targetPath):
    #     if os.path.exists(targetPath) or bdd().nodeExistsChecker(os.path.basename(targetPath)):
    #         return True
    #     return False

    # def getDirectory(self, cible, path):
    #     liste = []
    #     for dirname, dirnames, files in os.walk(path):
    #         for subdirname in dirnames:
    #             liste.append(os.path.join(dirname, subdirname)) if subdirname == os.path.basename(cible) else None
    #     return liste

    # # Get endpoint list from the FileSystem
    # def getEndpoint(self, path):
    #     type = ''
    #     list = {}
    #     for file in os.listdir(path):
    #         if os.path.isfile(file):
    #             type = 'StructuredDataNode'
    #         else:
    #             type = 'ContainerNode'
    #         list[os.path.join(file)] = type
    #     return list

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
    def getNode(self, node):
        # Retourne la représentation de la node
        if bdd().nodeExistsChecker(node):
            # type = ''
            # if os.path.isfile(targetPath):
            #     type = 'StructuredDataNode'
            # elif os.path.isdir(targetPath):
            #     type = 'ContainerNode'
            self.node = {
                 # os.path.basename(targetPath) : type,
                    'endpoints' : {},
                    'properties' : {},
                    'accepts' : {},
                    'provides' : {}
                    }
            temp = bdd().getMeta(node)
            for keys, values in temp.items():
                if values in ["ContainerNode", "StructuredDataNode", "UnstructuredDataNode", "LinkNode"]:
                    self.node['endpoints'][keys] = values
            meta = bdd().getMeta(node)
            self.node['path'] = deepcopy(meta['path'])
            self.node['properties'] = deepcopy(meta['properties'])
            self.node['accepts'] = deepcopy(meta['accepts'])
            self.node['provides'] = deepcopy(meta['provides'])
            return xml().xml_generator('get',self.node)
        else :
            return FileNotFoundError

    def createNode(self, targetPath):
        # Creation de la node
        collection = 'VOSpaceFiles'
        try:
            if not bdd().nodeExistsChecker(os.path.basename(targetPath)):
                try:
                    os.makedirs(targetPath)

                except OSError as e:
                    return 'Directory creation failed. Error %s' % e
                try:
                    bdd().insertionMongo(fsToDict(targetPath))
                except OSError as e:
                    return 'BDD update failed. Error %s' % e
        except FileExistsError as e:
            return e

    def setNode(self, targetPath, properties):
        if bdd().nodeExistsChecker(os.path.basename(targetPath)):
            self.properties = properties
            validator = {}
            for documents in bdd().connexion().find({'node': os.path.basename(targetPath)}):
                for keys, values in documents.items():
                    if keys == 'properties':
                        for k, v in values.items():
                            validator[k] = v

            argProp = set(self.properties)
            valProp = set(validator)
            propDict = bdd().getPropertiesDict()
            for key in argProp.intersection(valProp):
                propDict[key] = deepcopy(self.properties[key])
                bdd().updateMeta(targetPath, key, propDict[key])

    def copyNode(self, targetPath, locationPath):
        # Copie la node et ses enfants
        self.loc = locationPath
        temp = deepcopy(bdd().getTree(targetPath))
        try:
            shutil.copytree(targetPath, self.loc)
            bdd().copyNode(self.loc, dumps(bdd().getMeta(targetPath)))
            temp['path'] = self.loc
            temp['node'] = os.path.basename(self.loc)
            bdd().insertionMongo(temp)
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
        # Deplace la node et ses enfants
        if os.path.exists(targetPath):
            if os.path.isdir(targetPath):
                shutil.rmtree(targetPath)
            elif os.path.isfile(targetPath):
                os.remove(targetPath)
            try:
                bdd().connexion().delete_one({'node': os.path.basename(targetPath)})
            except CursorNotFound:
                return False
        else:
            raise FileNotFoundError

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
# a = Vospace()
# print(bdd().nodeExistsChecker(os.path.basename("./VOTest/VOSpace/nodes/myresult1")))
# a.startup()
# # print(a.getEndpoint("./VOTest/VOSpace/nodes/myresult1"))
# # for k,v in a.getNode("./VOTest/VOSpace/nodes/myresult1")['properties']['type'].items():
# #     print(v)
# # a.createNode("./VOTest/VOSpace/nodes/myresult5", "ContainerNode")
# # print(a.nodeExistsChecker(os.path.basename("./VOTest/VOSpace/nodes/myresult4")))
# a.setNode("./VOTest/VOSpace/nodes/myresult1",{'title' : {'IVOA':'ivo://ivoa.net/vospace/core#title', 'readonly': 'false'},
#                                                'description' : {'Yet another node' : 'ivo://ivoa.net/vospace/core#description', 'readonly': 'false'},
#                                                'contributor' : {'Foo' : 'ivo://ivoa.net/vospace/core#contributor', 'readonly': 'false'},
#                                                 'language': {'Farsi' : 'ivo://ivoa.net/vospace/core#language', 'readonly': 'false'}})
# # print(a.copyNode("./VOTest/VOSpace/nodes/myresult1", "./VOTest/copy/myresult1"))
# bdd().setViews("./VOTest/VOSpace/nodes/myresult1",{'anyview' : 'ivo://ivoa.net/vospace/core#anyview', 'fits' : 'ivo://ivoa.net/vospace/core#fits' },
#                                                      {'default' : 'ivo://ivoa.net/vospace/core#defaultview', 'fits' :  'ivo://ivoa.net/vospace/core#fits' })

# pprint(bdd().getMeta("./VOTest/copy/myresult1"))
# a.deleteNode("./VOTest/copy/myresult2/metamyresult2")
# print(os.path.exists("./VOTest/copy/myresult2/metamyresult2"))