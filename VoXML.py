# Classe traitant les fichiers et XML et les reponses du service

import xml.dom.minidom as DOM
import xml.etree.ElementTree as ET
from sys import argv
import os
import functools as fun
import json
import errno

class VoXML(object):

    def __init__(self):
        prefix = 'vos:'
        suffix = ":vos"
        vostrf = prefix + 'transfer'
        vostarg = prefix + 'target'
        vosdirect = prefix + 'direction'
        vosprot = prefix + 'protocol'
        vosendpoint = prefix + 'endpoint'
        xmlnsvos = 'xmlns' + suffix
        xmnlsw3c = 'xmlns:xs'
        w3c_uri = "http://www.w3.org/2001/XMLSchema-instance"
        vospace_v = "http://www.ivoa.net/xml/VOSpace/v2.1"
        uri_v = "uri"
        attribut_direction = ''
        url_fichier = ''
        vu = ''
        racine = "./VOTest"


script, file = argv
tree = ET.parse(file)
root = tree.getroot()

def tag_read(node, string, idx):
    index = idx - 1
    if string == "target":
        global url_fichier
        url_fichier = node[index].text
    elif string == "direction":
        global attribut_direction
        attribut_direction = node[index].text
    elif string == "view":
        global vu
        vu = node[index].attrib
    else:
        print(string)

def xml_tag_reader(root):
    for idx, childs in enumerate(root.iter()):
        tag_read(root,childs.tag[38:],idx)

def attr(self, root):
    for childs in root.iter():
        if len(childs.attrib) != 0 and len(childs.tag) != 0:
            tag = childs.tag[38:]
            att = childs.attrib
            return {tag: att}

