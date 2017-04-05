#import pyxb.utils.domutils
import xml.dom.minidom as DOM
#import VOSpace
import xml.etree.ElementTree as ET
from sys import argv
import os
import functools as fun
import json
import errno
import uuid
import datetime
#from dicttoxml import dicttoxml




script, file = argv

prefix = 'vos:'
suffix = ":vos"
tran = prefix+'transfer'
targ = prefix+'target'
direct = prefix+'direction'
prot = prefix+'protocol'
endp = prefix+'endpoint'
xmlnsvos = 'xmlns'+suffix
xmnlsw3c = 'xmlns:xs'
w3c_uri = "http://www.w3.org/2001/XMLSchema-instance"
vospace_v = "http://www.ivoa.net/xml/VOSpace/v2.1"
uri_v = "uri"
attribut_direction = ''
vu = ''
attribut_security = ''
url_fichier = ''
racine = "./VOTest"


#doc = VOSpace.CreateFromDocument(open(file).read())
tree = ET.parse(file)
root = tree.getroot()



print("==========================Etape 1=============================")
print("Impression du nom de la balise root")
print("")

print(root.tag[38:])


print("")
print("==========================Etape 2=============================")
print("Impression des tags du XML")
print("")

def text(node, string, idx):
    index = idx - 1
    if string == "target":
        print(string, "==>",node[index].text)
        global url_fichier
        url_fichier = node[index].text
    elif string == "direction":
        print(string, "==>", node[index].text)
        global attribut_direction
        attribut_direction = node[index].text
    elif string == "view":
        print(string, "==>", node[index].attrib)
        global vu
        vu = node[index].attrib
    else:
        print(string)

def print_tag(root):
    for idx, childs in enumerate(root.iter()):
        text(root,childs.tag[38:],idx)


print_tag(root)
print(attribut_security)

print("")
print("==========================Etape 3=============================")
print("Impression des tags et attributs")
print("")

def attr(root):
    retour = {}
    for childs in root.iter():
        if len(childs.attrib) != 0 and len(childs.tag) != 0:
            tag = childs.tag[38:]
            att = childs.attrib
            retour = {tag: att}
            # print(str(tag) + " " + str(att))
            return retour




print(attr(root))


print("")
print("==========================Etape 4=============================")
print("")

def protocol_parser(root):
    tableau = []
    for childs in root.iter():
        x = childs.tag
        y = childs.attrib
        z = childs.text
        print(x[38:],y, z)
        if len(childs.attrib) > 0:
            tableau.append(childs.attrib)
            # print("ajout d'un attribut non vide")
            # print(" ")
    # print("Impression du tableau des attributs")
    print(tableau)
    return tableau
retour = protocol_parser(root)


print("")
print("==========================Etape 5=============================")
print("Impression du protocol demande")
print("")

def protocol_checker(tableau):
    requete = ''
    for verif in retour:
        if verif.get("uri") == "ivo://ivoa.net/vospace/core#httpget":
            print("GET")
            requete = 'ivo://ivoa.net/vospace/core#httpget'
        elif verif.get("uri") == "ivo://ivoa.net/vospace/core#httppost":
             print("POST")
             requete = 'ivo://ivoa.net/vospace/core#httppost'
        elif verif.get("uri") == "ivo://ivoa.net/vospace/core#httpput":
            print("PUT")
            requete = 'ivo://ivoa.net/vospace/core#httpput'
        elif verif.get("uri") == "ivo://ivoa.net/vospace/core#httpdelete":
           print("DELETE")
           requete = 'ivo://ivoa.net/vospace/core#httpdelete'
    return requete

check = protocol_checker(retour)
print('protocol :',check)

print("")
print("==========================Etape 6=============================")
print("Chercher un dossier dans le FileSystem et en donner le path")
print("")

def recherche_repertoire(cible, path):
    liste = []
    for dirname, dirnames, files in os.walk(path):
        for subdirname in dirnames:
            if subdirname == cible[26:]:
                liste.append(os.path.join(dirname,subdirname))
    return liste

endpoint = recherche_repertoire(url_fichier, racine)
print(endpoint)

def liste_fichiers(path):
    liste = {}
    type = ''
    for file in os.listdir(path):
        if "." in file and (file.split('.')[1] != 'zip' and file.split('.')[1] != 'tar'):
                type = 'DataNode'
        else: type = 'ContainerNode'
        liste[os.path.join(file)] = type
    return liste

print("")
print("==========================Etape 7=============================")
print("FileSystem (utilisation et modification d'un snippet mappant un dossier)"
      " Création d'un json simple")
print("")

#def get_directory_structure(rootdir):
    # """
    # Creates a nested dictionary that represents the folder structure of rootdir
    # """
    # dir_dictionnary = {}
    # rootdir = rootdir.rstrip(os.sep)
    # start = rootdir.rfind(os.sep) + 1
    # for path, dirs, files in os.walk(rootdir):
    #     folders = path[start:].split(os.sep)
    #     subdir = dict.fromkeys(files)
    #     parent = fun.reduce(dict.get, folders[:-1], dir_dictionnary)
    #     parent[folders[-1]] = subdir
    #     if os.path.isfile(path):
    #         dir_dictionnary['size'] = os.walk(rootdir)
    # return dir_dictionnary

#VoJson = json.dumps(get_directory_structure(racine),sort_keys=True, indent=2,separators=(',',':'))
def octet(entier):
    taille_ = entier
    retour = ''
    if taille_ >= 1000 and taille_ < 1000000:
        retour = str(round(taille_ / 100, 2)) + 'ko'
    elif taille_ >= 1000000:
        retour = str(round(taille_ / 1000000, 2)) + 'Mo'
    elif taille_ < 1000:
        retour = str(taille_) + 'o'
    return retour

def get_size_dir(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

    return octet(total_size)


def path_hierarchy(path):
    taille = get_size_dir(path)
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
        hierarchy[os.path.basename(path)] = [
            path_hierarchy(os.path.join(path, contents))
            for contents in os.listdir(path)
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['type'] = 'file'
        hierarchy['size'] = octet(os.path.getsize(path))
    return hierarchy


def endpoint_filesystem_to_json():
    if endpoint:
        retour = json.dumps(path_hierarchy(endpoint[0]), sort_keys=True, indent=2, separators=(',', ':'))
        return retour
    else:
        return



EndpointJson = endpoint_filesystem_to_json()
print(EndpointJson)

# a = open('VoJson.json','w')
# a.write(VoJson)
# a.close()


print("")
print("==========================Etape 8=============================")
print("Création de XML pour pullFrom, pushTo et getNode")
print("")

def xml_formateur(element):
    chaine_originale = ET.tostring(element)
    reparsed = DOM.parseString(chaine_originale)
    return reparsed.toprettyxml(indent="    ")


def xml_maker(cible, path, direction):
        _cible = cible
        _chemin = path
        _direction = direction
        top = ET.Element(tran)
        top.set(xmlnsvos,vospace_v)
        target_uri = ET.SubElement(top, targ)
        target_uri.text = _cible
        sens = ET.SubElement(top, direct)
        sens.text = _direction

        pointfinal = recherche_repertoire(_cible, _chemin)
        for acces in pointfinal:
            proto = ET.SubElement(top, prot)
            proto.set(uri_v, check)
            endpoint = ET.SubElement(proto, endp)
            endpoint.text = acces[1:]
        return xml_formateur(top)


def getNode(path):
    cheminNode = path
    top = ET.Element(prefix + 'node')
    top.set(xmlnsvos, vospace_v)
    top.set(xmnlsw3c, w3c_uri)
    top.set(uri_v, cheminNode[1:])
    top.set("xs:type", prefix+"ContainerNode")

    properties = ET.SubElement(top, prefix+'properties')
    for line in propertyGetter(cheminNode):
        x = line.split("=")
        prop = ET.SubElement(properties, prefix+'property')
        prop.set(uri_v,x[0])
        prop.text = x[1]

    acceptViews = ET.SubElement(top,prefix+'accept')
    for line in viewGetter(cheminNode)['accept']:
        accept_ = ET.SubElement(acceptViews, prefix+'view')
        accept_.set(uri_v,line)

    provideViews = ET.SubElement(top,prefix+'provide')
    for line in viewGetter(cheminNode)['provide']:
        provide_ = ET.SubElement(provideViews, prefix + 'view')
        provide_.set(uri_v, line)

    capabilities = ET.SubElement(top,prefix+'capabilities')

    noeuds = ET.SubElement(top,prefix+'nodes')
    for name, type in liste_fichiers(cheminNode).items():
        noeud = ET.SubElement(noeuds,prefix+'node' )
        noeud.set(uri_v,cheminNode[1:]+name)
        noeud.set("xs:type", type)
    return xml_formateur(top)

def propertyGetter(path):
    chemin = path+'property.txt'
    prop_ = []
    try:
        with open(chemin,'r') as p:
            for ligne in p:
                prop_.append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % chemin)
    return prop_

def viewGetter(path):
    accept = path + 'view_accept.txt'
    provide = path + 'view_provide.txt'
    prop_ = {
        'accept': [],
        'provide' : [],
    }
    try:
        with open(accept, 'r') as acceptation:
            for ligne in acceptation:
                prop_['accept'].append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % accept)

    try:
        with open(provide, 'r') as offerte:
            for ligne in offerte:
                prop_['provide'].append(ligne.split("\n")[0])
    except Exception:
        print('%s not found' % provide)

    retour = prop_
    return retour


directionList = ['pullFromVoSpace','pullToVoSpace', 'pushFromVoSpace', 'pushToVoSpace']

if attribut_direction in directionList:
    dom = xml_maker(url_fichier, racine, attribut_direction)
    print(attribut_direction + " : " + str(uuid.uuid1()))
    print(dom)


elif attribut_direction == '':
    dossier = attr(root)['node']['uri']
    recupereNode = getNode(dossier)
    print("getNode : " + str(uuid.uuid1()))
    print(recupereNode)

print("")
print("==========================Etape 9=============================")
print("A faire : Travail sur le JSON")
print("")

