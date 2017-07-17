# VOSpace settings class
# This class checks the state of the service at start up
# Scan the file system to create a dictionary
# Set the service settings

import os
from datetime import datetime
from VoPackage.database import Handler as bdd
from uuid import uuid1

RACINE = "./nodes"
PROTOCOL = {
        'get' : 'ivo://ivoa.net/vospace/core#httpget',
        'post' : 'ivo://ivoa.net/vospace/core#httppost',
        'put' : 'ivo://ivoa.net/vospace/core#httpput',
        'delete' : 'ivo://ivoa.net/vospace/core#httpdelete'
    }
PROPERTIES = {
        'title' : '',
        'creator' : '',
        'subject' : '',
        'description' : '',
        'publisher' : '',
        'contributor' : '',
        'date' : '',
        'type' : '',
        'format' : '',
        'identifier' : '',
        'source' : '',
        'language' : '',
        'relation' : '',
        'coverage' : '',
        'rights' : '',
        'availableSpace' : '',
        'groupread' : '',
        'groupwrite' : '',
        'publicread' : '',
        'quota' : '',
        'length' : '',
        'mtime' : '',
        'ctime' : '',
        'btime' : '',
    }
VIEWS = {
        'default' : 'ivo://ivoa.net/vospace/core#defaultview',
        'anyview' : 'ivo://ivoa.net/vospace/core#anyview',
        'fits' : 'ivo://ivoa.net/vospace/core#fits',
        'votable' : 'ivo://ivoa.net/vospace/core#votable',
        'zip' : 'ivo://ivoa.net/vospace/core#zip',
        'tar.gz' : 'ivo://ivoa.net/vospace/core#targz'
    }

PropertiesDict = {
    'title': {"title":'', "readonly" : "False"},
    'creator': {"creator":'',"readonly" : "False"},
    'subject': {"subject": '', "readonly" : "False"},
    'description': {"description": '', "readonly" : "False"},
    'publisher': {"publisher": '', "readonly" : "False"},
    'contributor': {"contributor": '', "readonly" : "False"},
    'date': {"date": '', "readonly" : "False"},
    'type': {"type": '', "readonly" : "True"},
    'format': {"format": '', "readonly" : "False"},
    'identifier': {"identifier": '', "readonly" : "False"},
    'source': {"source": '',"readonly" : "False"},
    'language': {"language": '',"readonly" : "False"},
    'relation': {"relation": '',"readonly" : "False"},
    'coverage': {"coverage": '',"readonly" : "False"},
    'rights': {"rights": '',"readonly" : "False"},
    'availableSpace': {"availableSpace": '',"readonly" : "False"},
    'groupread': {"groupread": '',"readonly" : "False"},
    'groupwrite': {"groupwrite": '',"readonly" : "False"},
    'publicread': {"publicread": '',"readonly" : "False"},
    'quota': {"quota": '',"readonly" : "False"},
    'length': {"length": '',"readonly" : "False"},
    'mtime': {"mtime": '',"readonly" : "True"},
    'ctime': {"ctime": '',"readonly" : "True"},
    'btime': {"btime": '',"readonly" : "True"},
}

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


def getSizeDir(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return octet(total_size)


# Get FileSystem representation as dictionary
def fsToDictionary(path):
    tempdate = datetime.fromtimestamp(os.path.getmtime(path))
    mdate = tempdate.strftime("%Y-%m-%d %H:%M:%S")
    owner = str(os.stat(path).st_uid)
    fName = os.path.basename(path)

    hierarchy = {
        'node': fName,
        'path': path,
        'ownerId': owner,
        'busy': "False",
        'properties': bdd().getPropertiesDict(),
        'parent': os.path.basename(os.path.abspath(os.path.join(path, os.pardir))),
        'ancestor': [],
        'accepts': [],
        'provides': [],
    }
    hierarchy['properties']['mtime'] = {"mtime" : "Modified "+ mdate, 'readonly': "True"}
    hierarchy['properties']['ctime'] = {"ctime": "MetaData modified "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        'readonly': "True"}
    hierarchy['properties']['btime'] = {
       "btime": "Creation date "+ datetime.fromtimestamp(os.path.getctime(path)).strftime(
            "%Y-%m-%d %H:%M:%S"), 'readonly': "True"}
    if os.path.isdir(path):
        hierarchy['properties']['type'] = {'type': 'ContainerNode', 'readonly': "True"}
    elif os.path.isfile(path):
        hierarchy['properties']['type'] = {'type': 'DataNode', 'readonly': "True"}
    hierarchy['size'] = octet(os.path.getsize(path))
    mathusalem = path.split(os.sep)
    list = [".", "VOTest", "VOSpace", "nodes", hierarchy['parent'], hierarchy['node']]
    for items in mathusalem:
        if items not in list:
            hierarchy['ancestor'].append(items)
    return hierarchy

def populateMeta():
    meta = [{'name': 'PROPERTIES', 'metadata': PROPERTIES, 'service' : 'vospace'},
            {'name': 'PROTOCOL', 'metadata': PROTOCOL, 'service' : 'vospace'},
            {'name': 'propertiesdict', 'metadata': PropertiesDict, 'service' : 'vospace'},
            {'name': 'voprotocols', 'metadata': {
                'accepts': {'get': 'ivo://ivoa.net/vospace/core#httpget',
                            'put': 'ivo://ivoa.net/vospace/core#httpput'},
                'provides': {'get': 'ivo://ivoa.net/vospace/core#httpget',
                             'put': 'ivo://ivoa.net/vospace/core#httpput'}}
                , 'service': 'vospace'},
            {'name': 'voviews', 'metadata': {
                'accepts': {'anyview': 'ivo://ivoa.net/vospace/core#anyview',
                            'fits': 'ivo://ivoa.net/vospace/core#fits',
                            'votable': 'ivo://ivoa.net/vospace/core#votable'},
                'provides': {'default': 'ivo://ivoa.net/vospace/core#defaultview',
                             'fits': 'ivo://ivoa.net/vospace/core#fits',
                             'votable': 'ivo://ivoa.net/vospace/core#votable'}}
                , 'service': 'vospace'},
            {'name': 'voproperties', 'metadata': {
                'accepts': {},
                'provides': {},
                'contains': {'date' : 'ivo://ivoa.net/vospace/core#date'}
            }, 'service' : 'vospace'}]
    for items in meta:
        bdd().insertDB(items)
    print("VOSpace property list OK")
    print("VOSpace protocol list OK")
    print("VOSpace view list OK")
    print("Service's metadata ready")

def populateFiles():
        for dir, subdirs, files in os.walk(RACINE):
            for x in subdirs:
                bdd.insertDB(bdd(), fsToDictionary(os.path.join(dir, x)))
            for y in files:
                bdd.insertDB(bdd(), fsToDictionary(os.path.join(dir, y)))

 # Startup check up, if the app crashed and the DB is empty, it update it from FS
def startup():
    if bdd.connexion(bdd()).find({"service":"vospace"}).count() == 0:
        populateMeta()
    if bdd.connexion(bdd()).find({"node":{ '$exists' : True }}).count() ==0:
        populateFiles()
        print("Database ready")
    else:
        # TO DO : Comparaison FS et DB au lancement.
        # database = []
        # FS = []
        # cursor = bdd.connexion(bdd()).find({'node': { '$exists' : True }},{'_id': False})
        # for items in cursor:
        #     database.append(items)
        # for items in os.listdir("./VOTest/VOSpace/nodes/"):
        #     for dir, subdirs, files in os.walk("./VOTest/VOSpace/nodes/" + items):
        #         for x in subdirs:
        #             FS.append(fsToDict(os.path.join(dir, x)))
        #         for y in files:
        #             FS.append(fsToDict(os.path.join(dir, y)))
        print("Database : OK")


startup()

