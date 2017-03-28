#import pyxb.utils.domutils
import xml.dom.minidom as DOM
#import VOSpace
import xml.etree.ElementTree as ET
from sys import argv
import os
import functools as fun
import json
#from dicttoxml import dicttoxml




script, file = argv

prefix = 'vos:'
sufix = ":vos"
tran = prefix+'transfer'
targ = prefix+'target'
direct = prefix+'direction'
prot = prefix+'protocol'
endp = prefix+'endpoint'
xmlnsvos = 'xmlns'+sufix
xmnlsw3c = 'xmlns:xs'
w3c_uri = "http://www.w3.org/2001/XMLSchema-instance"
vospace_v = "http://www.ivoa.net/xml/VOSpace/v2.1"
uri_v = "uri"
prop_direct = ''
fichier =''
chemin = "./VOTest"


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
        global fichier
        fichier= node[index].text
        return fichier
    elif string == "direction":
        print(string, "==>", node[index].text)
        global prop_direct
        prop_direct = node[index].text
        return prop_direct
    else:
        print(string)


def print_tag(root):
    for idx, childs in enumerate(root.iter()):
        text(root,childs.tag[38:],idx)


print_tag(root)


print("")
print("==========================Etape 3=============================")
print("Impression des tags et attributs")
print("")

def print_attr(root):
    retour = {}
    for childs in root.iter():
        if len(childs.attrib) > 0:
            tag = childs.tag[38:]
            att = childs.attrib
    retour = {tag: att}
    #print(str(tag) + " " + str(att))
    return retour


print(print_attr(root))


print("")
print("==========================Etape 4=============================")
print("")

def protocol_parser(root):
    tableau = []
    for childs in root.iter():
        if len(childs.attrib) > 0:
            tableau.append(childs.attrib)
            # print("ajout d'un attribut non vide")
            # print(" ")
    # print("Impression du tableau des attributs")
    # print(tableau)
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
print("FileSystem (utilisation et modification d'un snippet mappant un dossier"
      " et ajoutant ses elements a un dictionnaire)")
print("")

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = fun.reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir

#output = open("output.json","w")
#output.write(json.dumps(get_directory_structure(chemin),sort_keys=True, indent=4,separators=(',',':')))

print("")
print("==========================Etape 7=============================")
print("Chercher un dossier dans le FileSystem et en donner le path")
print("")

def recherche_repertoire(cible, path):
    liste = []
    for dirname, dirnames, files in os.walk(path):
        for subdirname in dirnames:
            if subdirname == cible[26:]:
                liste.append(os.path.join(dirname,subdirname))
    return liste

endpoint = recherche_repertoire(fichier, chemin)
#print(endpoint)

def liste_fichiers(path):
    liste = []
    for dirname, dirnames, files in os.walk(path):
        for file in files:
            liste.append(os.path.join(file))
    return liste

print("")
print("==========================Etape 8=============================")
print("Création de XML pour pullFrom, pushTo et getNode")
print("")

def xml_formateur(element):
    chaine_originale = ET.tostring(element)
    reparsed = DOM.parseString(chaine_originale)
    return reparsed.toprettyxml(indent="    ")


def xml_maker(cible, chemin, direction):
        _cible = cible
        _chemin = chemin
        _direction = direction
        top = ET.Element(tran)
        top.set(xmlnsvos,vospace_v)
        target_uri = ET.SubElement(top, targ)
        target_uri.text = _cible
        sens = ET.SubElement(top, direct)
        sens.text = _direction

        pointfinal = recherche_repertoire(_cible, _chemin)
        for path in pointfinal:
            proto = ET.SubElement(top, prot)
            proto.set(uri_v, check)
            endpoint = ET.SubElement(proto, endp)
            endpoint.text = path[1:]
        return xml_formateur(top)


def getNode(chemin):
    uri = []
    cheminNode = chemin
    for item in liste_fichiers(cheminNode):
        uri.append(item)
    top = ET.Element(prefix + 'node')
    top.set(xmlnsvos, vospace_v)
    top.set(xmnlsw3c, w3c_uri)
    top.set(uri_v, cheminNode[1:])
    top.set("xs:type", prefix+"ContainerNode")
    properties = ET.SubElement(top, prefix+'properties')
    for item in propertyGetter(cheminNode):
        x = item.split("=")
        prop = ET.SubElement(properties, prefix+'property')
        prop.set(uri_v,x[0])
        prop.text = x[1]

    acceptViews = ET.SubElement(top,prefix+'accept')
    accept_ = ET.SubElement(acceptViews, prefix+'view')
    accept_.set(uri_v,viewGetter(cheminNode)['accept'].split("\n")[0])

    provideViews = ET.SubElement(top,prefix+'provide')
    provide_ = ET.SubElement(provideViews, prefix + 'view')
    provide_.set(uri_v, viewGetter(cheminNode)['provide'].split("\n")[0])

    capabilities = ET.SubElement(top,prefix+'capabilities')

    noeuds = ET.SubElement(top,prefix+'nodes')
    for item in liste_fichiers(cheminNode):
        noeud = ET.SubElement(noeuds,prefix+'node' )
        noeud.set(uri_v,cheminNode[1:]+item)
        noeud.set("xs:type",prefix+"Datanode")
    return xml_formateur(top)

def propertyGetter(chemin):
    path = chemin+'property.txt'
    prop_ = []
    prop_.append(open(path,'r').readline())
    retour = prop_
    return retour

def viewGetter(chemin):
    accept = chemin + 'view_accept.txt'
    provide = chemin + 'view_provide.txt'
    prop_ = {'accept': '', 'provide' : ''}
    prop_['accept'] = (open(accept, 'r').readline())
    prop_['provide'] = (open(provide, 'r').readline())
    retour = prop_
    return retour

if prop_direct == 'pushToVoSpace':
    dom = xml_maker(fichier, chemin, prop_direct)
    print(dom)
elif prop_direct == 'pullFromVoSpace':
    dom = xml_maker(fichier, chemin, prop_direct)
    print(dom)
elif prop_direct == '':
    dossier = print_attr(root)['node']['uri']
    print(getNode(dossier))
