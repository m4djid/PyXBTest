# Classe traduisant les instructions en actions
import os
from GenericBackend import Backend


class Vospace(Backend):

    def recherche_repertoire(self, cible, path):
        liste = []
        for dirname, dirnames, files in os.walk(path):
            for subdirname in dirnames:
                liste.append(os.path.join(dirname, subdirname)) if subdirname == os.path.basename(cible) else None

        return liste
    def liste_fichiers(self, path):
        liste = {}
        type = ''
        for file in os.listdir(path):
            if "." in file and (file.split('.')[1] != 'zip' and file.split('.')[1] != 'tar'):
                type = 'DataNode'
            else:
                type = 'ContainerNode'
            liste[os.path.join(file)] = type
        return liste

    def getNode(self, target):
        return self.liste_fichiers(target)

    def setNode(self, target, *args):
        properties = []
        for arg in args:
            properties.append(arg)
        pass

    def copyNode(self, target, location):
        pass

    def moveNode(self, target, location):
        pass

    def deleteNode(self, target):
        pass

    def pushToVoSpace(self, target, view):
        pass

    def pushFromVoSpace(self, target, *args):
        endpoint = []
        for arg in args:
            endpoint.append(arg)
        pass

    def pullFromVoSpace(self, target):
        pass

    def pullToVoSpace(self, target, endpoint):
        pass