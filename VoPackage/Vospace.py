# Classe traduisant les instructions en actions
import os
from VoPackage import GenericBackend

class Vospace(GenericBackend.Backend):

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