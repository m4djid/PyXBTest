# Classe traduisant les instructions en actions
import os
from GenericBackend import Backend as fs
from bddHandler import Handler as bdd
from copy import deepcopy
import datetime
import errno


class Vospace(fs, bdd):

    def __init__(self):
        self.RACINE = './VOTest'


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
            if os.path.isfile(file) and (file.split('.')[1] is not 'zip' and file.split('.')[1] is not 'tar.gz'):
                type = 'DataNode'
            else:
                type = 'ContainerNode'
            list[os.path.join(file)] = type
        return list

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
                hierarchy["subnode : "+str(index)] = self.path_hierarchy(os.path.join(path, contents))
        except OSError as e:
            if e.errno != errno.ENOTDIR:
                raise
            hierarchy['type'] = 'file'
            hierarchy['size'] = self.octet(os.path.getsize(path))
        return hierarchy

    def getNode(self, targetUri):
        # Retourne la représentation XML de la node
        node = {'endpoints': {},
                'properties' : {},
                'accepts' : {},
                'provides' : {}
                }
        if bdd.nodeExistsChecker(self, targetUri) and os.path.exists(targetUri):
            node['endpoints'] = self.getEndpoint(targetUri)
            meta = self.metaChecker(os.path.basename(targetUri))
            node['properties'] = deepcopy(meta['properties'])
            node['accepts'] = deepcopy(meta['accepts'])
            node['provides'] = deepcopy(meta['provides'])
        return node

    def createNode(self, targetUri, type):
        # Creation de la node
        collection = 'arbre'
        if os.path.exists(targetUri) and bdd.nodeExistsChecker(self, os.path.basename(targetUri)):
            print(targetUri + ' already exists')
            return None
        if os.makedirs(targetUri):
            print(os.path.basename(targetUri) + ' created')
        if bdd.insertionMongo(self, self.fsToDict(targetUri), collection):
            print('BDD updated for ' + targetUri)
        else:
            print('Update failed')





    def setNode(self, targetUri, **kwargs):
        # Initialise la node
        pass

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
print(a.getNode("./VOTest/VOSpace/nodes/myresult1"))
a.createNode("./VOTest/VOSpace/nodes/myresult4", "z")