# Classe traitant les fichiers et XML et les reponses du service

import xml.dom.minidom as DOM
import xml.etree.ElementTree as ET
from sys import argv
import os
import json
import errno


class Voxml(object):
    def __init__(self):
        self.prefix = 'vos:'
        self.suffix = ':vos'
        self.vosnode = self.prefix + 'node'
        self.vostransfer = self.prefix + 'transfer'
        self.vostarget = self.prefix + 'target'
        self.vosdirect = self.prefix + 'direction'
        self.vosprot = self.prefix + 'protocol'
        self.vosendpoint = self.prefix + 'endpoint'
        self.xmlnsvos = 'xmlns' + self.suffix
        self.xmnlsw3c = 'xmlns:xs'
        self.w3c_uri = 'http://www.w3.org/2001/XMLSchema-instance'
        self.vospace_v = 'http://www.ivoa.net/xml/VOSpace/v2.1'
        self.uri_v = 'uri'
        self.attribut_direction = ''
        self.url_fichier = ''
        self.vu = ''
        self.distant = {}
        self.racine = './VOTest'


    def var_assign(self, node, string, idx):
        global url_fichier, attribut_direction, vu

        index = idx - 1
        if string == 'target':
            self.url_fichier = node[index].text
        elif string == 'direction':
            self.attribut_direction = node[index].text
        elif string == 'view':
            self.vu = node[index].attrib

    def xml_tag_reader(self, root):
        retour = {}
        global distant
        i = 1
        for index, childs in enumerate(root.iter()):
            self.var_assign(root, childs.tag[38:], index)
            for subchild in childs:
                if 'endpoint' in subchild.tag:
                    self.distant[subchild.tag[38:] + str(i)] = {'destination': subchild.text}
                    i += 1
            if len(childs.attrib) != 0 and len(childs.tag) != 0:
                tag = childs.tag[38:]
                att = childs.attrib
                retour[tag] = att
        return retour

    def protocol_parser(self, dictionary):
        requete = ''
        if 'protocol' in dictionary:
            if 'ivo://ivoa.net/vospace/core#httpget' in dictionary['protocol'].values():
                requete = 'ivo://ivoa.net/vospace/core#httpget'
            elif 'ivo://ivoa.net/vospace/core#httppost' in dictionary['protocol'].values():
                requete = 'ivo://ivoa.net/vospace/core#httppost'
            elif 'ivo://ivoa.net/vospace/core#httpput' in dictionary['protocol'].values():
                requete = 'ivo://ivoa.net/vospace/core#httpput'
            elif 'ivo://ivoa.net/vospace/core#httpdelete' in dictionary['protocol'].values():
                requete = 'ivo://ivoa.net/vospace/core#httpdelete'
        return requete


    # Generateur de réponse XML
    def xml_formateur(self, element):
        chaine_originale = ET.tostring(element)
        reparsed = DOM.parseString(chaine_originale)
        return reparsed.toprettyxml(indent="    ")

    def xml_generator(self, *args):
        action, path, target, direction, location = args
        return

class main(object):

    script, file = argv
    tree = ET.parse(file)
    root = tree.getroot()
    go = Voxml()