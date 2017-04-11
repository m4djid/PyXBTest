# Classe traduisant les instructions en actions
import os
from GenericBackend import Backend as fs
from bddHandler import Handler as bdd
from copy import deepcopy
import datetime
import errno


class Vospace(fs, bdd):

    _RACINE = './VOTest'
    _PROTOCOL = [
        'ivo://ivoa.net/vospace/core#httpget',
        'ivo://ivoa.net/vospace/core#httppost',
        'ivo://ivoa.net/vospace/core#httpput',
        'ivo://ivoa.net/vospace/core#httpdelete'
    ]
    _PROPERTIES = {
        'title' : 'ivo://ivoa.net/vospace/core#title',
        'creator' : ' ivo://ivoa.net/vospace/core#creator',
        'subject' : ' ivo://ivoa.net/vospace/core#subject',
        'description' : 'ivo://ivoa.net/vospace/core#description',
        'publisher' : 'ivo://ivoa.net/vospace/core#publisher',
        'contributor' : 'ivo://ivoa.net/vospace/core#contributor',
        'date' : 'ivo://ivoa.net/vospace/core#date',
        'type' : 'ivo://ivoa.net/vospace/core#type',
        'format' : 'ivo://ivoa.net/vospace/core#format',
        'identifier' : 'ivo://ivoa.net/vospace/core#identifier',
        'source' : 'ivo://ivoa.net/vospace/core#source',
        'language' : 'ivo://ivoa.net/vospace/core#language',
        'relation' : 'ivo://ivoa.net/vospace/core#relation',
        'coverage' : 'ivo://ivoa.net/vospace/core#coverage',
        'rights' : 'ivo://ivoa.net/vospace/core#rights',
        'availableSpace' : 'ivo://ivoa.net/vospace/core#availableSpace',
        'groupread' : 'ivo://ivoa.net/vospace/core#groupread',
        'groupwrite' : 'ivo://ivoa.net/vospace/core#groupwrite',
        'publicread' : 'ivo://ivoa.net/vospace/core#publicread',
        'quota' : 'ivo://ivoa.net/vospace/core#quota',
        'length' : 'ivo://ivoa.net/vospace/core#length',
        'mtime' : 'ivo://ivoa.net/vospace/core#mtime',
        'ctime' : 'ivo://ivoa.net/vospace/core#ctime',
        'btime' : 'ivo://ivoa.net/vospace/core#btime',
    }
    def startup(self):
        self.verif = bdd.connexion(self, 'arbre')
        if self.verif.find({}).count() == 0:
            for dir in os.listdir(self.RACINE + '/VOSpace/nodes'):
                self.modifMeta(self.RACINE + '/VOSpace/nodes/' + dir,'')
                self.insertionMongo(bdd.fsToDict(self, self.RACINE + '/VOSpace/nodes/' + dir), 'arbre')
            print("Database ready")

    def nodeExists(self, targetUri):
        if os.path.exists(targetUri) or self.nodeExistsChecker(os.path.basename(targetUri)):
            return True
        return False

    def getDirectory(self, cible, path):
        liste = []
        for dirname, dirnames, files in os.walk(path):
            for subdirname in dirnames:
                liste.append(os.path.join(dirname, subdirname)) if subdirname == os.path.basename(cible) else None
        return liste

    def getEndpoint(self, path):
        type = ''
        list = {}
        for file in os.listdir(path):
            if os.path.isfile(file):
                if  (file.split('.')[1] is 'zip' or file.split('.')[1] is 'tar.gz'):
                    type = 'StructuredDataNode'
                else:
                    type = 'UnstructuredDataNode'
            else:
                type = 'ContainerNode'
            list[os.path.join(file)] = type
        return list

    # def octet(self, entier):
    #     taille_ = entier
    #     retour = ''
    #     if taille_ >= 1000 and taille_ < 1000000:
    #         retour = str(round(taille_ / 100, 2)) + 'ko'
    #     elif taille_ >= 1000000:
    #         retour = str(round(taille_ / 1000000, 2)) + 'Mo'
    #     elif taille_ < 1000:
    #         retour = str(taille_) + 'o'
    #     return retour
    #
    # def getSizeDir(self, start_path):
    #     total_size = 0
    #     for dirpath, dirnames, filenames in os.walk(start_path):
    #         for f in filenames:
    #                 fp = os.path.join(dirpath, f)
    #                 total_size += os.path.getsize(fp)
    #     return self.octet(total_size)
    #
    # def fsToDict(self, path):
    #     taille = self.getSizeDir(path)
    #     tempdate = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    #     mdate =  tempdate.strftime("%Y-%m-%d %H:%M:%S")
    #     owner = str(os.stat(path).st_uid)
    #     fName = os.path.basename(path)
    #     hierarchy = {
    #         'type': 'ContainerNode',
    #         'name': fName,
    #         'path': path,
    #         'size': taille,
    #         'modified': mdate,
    #         'ownerId' : owner,
    #     }
    #
    #     try:
    #         for index, contents in enumerate(os.listdir(path)):
    #             hierarchy["subnode : "+str(index)] = self.fsToDict(os.path.join(path, contents))
    #     except OSError as e:
    #         if e.errno != errno.ENOTDIR:
    #             raise
    #         hierarchy['type'] = 'DataNode'
    #         hierarchy['size'] = self.octet(os.path.getsize(path))
    #     return hierarchy

    def getNode(self, targetUri):
        # Retourne la représentation XML de la node
        if self.nodeExists(targetUri):
            if os.path.isfile(targetUri):
                type = 'DataNode'
            type = 'ContainerNode'
            node = {
                 os.path.basename(targetUri) : type,
                    'endpoints' : {},
                    'properties' : {},
                    'accepts' : {},
                    'provides' : {}
                    }
            node['endpoints'] = self.getEndpoint(targetUri)
            meta = self.getMeta(os.path.basename(targetUri))
            node['properties'] = deepcopy(meta['properties'])
            node['accepts'] = deepcopy(meta['accepts'])
            node['provides'] = deepcopy(meta['provides'])
            return node
        return "Node Not Found"



    def createNode(self, targetUri, type):
        # Creation de la node
        collection = 'arbre'
        if not self.nodeExists(targetUri):
            try:
                if os.makedirs(targetUri):
                    print(os.path.basename(targetUri) + ' type = ' + type + ' created')
            except:
                print('Directory creation failed')
            try:
                if self.insertionMongo(self.fsToDict(targetUri), collection):
                    print('BDD updated for ' + targetUri)
            except:
                print('BDD update failed')

    def setNode(self, targetUri, properties):
        if self.nodeExists(targetUri):
            self.properties = properties
            validator = self._PROPERTIES
            argProp = set(self.properties)
            valProp = set(validator)
            propDict = {
                'title': {},
                'creator': {},
                'subject': {},
                'description': {},
                'publisher': {},
                'contributor': {},
                'date': {},
                'type': {},
                'format': {},
                'identifier': {},
                'source': {},
                'language': {},
                'relation': {},
                'coverage': {},
                'rights': {},
                'availableSpace': {},
                'groupread': {},
                'groupwrite': {},
                'publicread': {},
                'quota': {},
                'length': {},
                'mtime' : {'Modified' : datetime.datetime.fromtimestamp(os.path.getmtime(targetUri)).strftime("%Y-%m-%d %H:%M:%S")},
                'ctime': {'MetaData modified' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
                'btime': {'Creation date' : datetime.datetime.fromtimestamp(os.path.getctime(targetUri)).strftime("%Y-%m-%d %H:%M:%S")},
            }
            for name in argProp.intersection(valProp):
                propDict[name] = deepcopy(self.properties[name])
            self.modifMeta(os.path.basename(targetUri), propDict)

    def copyNode(self, targetUri, locationUri):
        # Copie la node et ses enfants
        pass

    def moveNode(self, targetUri, locationUri):
        # Deplace la node et ses enfants
        pass

    def deleteNode(self, targetUri):
        # Deplace la node et ses enfants
        pass

    def pushToVoSpace(self, targetUri, **kwargs):
        # Execute un push to VOSpace
        pass

    def pushFromVoSpace(self, targetUri, **kwargs):
        # Execute un push from VOSpace
        pass

    def pullFromVoSpace(self, targetUri, **kwargs):
        # Execute un pull from VOSpace
        pass

    def pullToVoSpace(self, targetUri, endpointUri):
        # Execute un pull to VOSpace
        pass


a = Vospace()
a.startup()

# print(a.getNode("./VOTest/VOSpace/nodes/myresult1"))
#a.createNode("./VOTest/VOSpace/nodes/myresult5", "ContainerNode")
# print(a.nodeExistsChecker(os.path.basename("./VOTest/VOSpace/nodes/myresult4")))
a.setNode("./VOTest/VOSpace/nodes/myresult5",{'title' : {'Victoire' : 'ivo://ivoa.net/vospace/core#title'},
                                              'test' : {'ceci est un test' : 'Shoryuken'},
                                              'description' : {'Du grand n\'importe quoi' : 'ivo://ivoa.net/vospace/core#description'},
                                              'contributor' : {'Foo' : 'ivo://ivoa.net/vospace/core#contributor'}})