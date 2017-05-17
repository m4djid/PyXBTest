# VOSpace settings class
# This class checks the state of the service at start up
# Scan the file system to create a dictionary
# Set the service settings

import os
import datetime
from VoPackage.database import Handler as bdd
from uuid import uuid1

RACINE = "./VOTest"
PROTOCOL = {
        'get' : 'ivo://ivoa.net/vospace/core#httpget',
        'post' : 'ivo://ivoa.net/vospace/core#httppost',
        'put' : 'ivo://ivoa.net/vospace/core#httpput',
        'delete' : 'ivo://ivoa.net/vospace/core#httpdelete'
    }
PROPERTIES = {
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
VIEWS = {
        'default' : 'ivo://ivoa.net/vospace/core#defaultview',
        'anyview' : 'ivo://ivoa.net/vospace/core#anyview',
        'fits' : 'ivo://ivoa.net/vospace/core#fits',
        'votable' : 'ivo://ivoa.net/vospace/core#votable',
        'zip' : 'ivo://ivoa.net/vospace/core#zip',
        'tar.gz' : 'ivo://ivoa.net/vospace/core#targz'
    }

PropertiesDict = {
    'title': {"readonly" : False},
    'creator': {"readonly" : False},
    'subject': {"readonly" : False},
    'description': {"readonly" : False},
    'publisher': {"readonly" : False},
    'contributor': {"readonly" : False},
    'date': {"readonly" : False},
    'type': {"readonly" : True},
    'format': {"readonly" : False},
    'identifier': {"readonly" : False},
    'source': {"readonly" : False},
    'language': {"readonly" : False},
    'relation': {"readonly" : False},
    'coverage': {"readonly" : False},
    'rights': {"readonly" : False},
    'availableSpace': {"readonly" : False},
    'groupread': {"readonly" : False},
    'groupwrite': {"readonly" : False},
    'publicread': {"readonly" : False},
    'quota': {"readonly" : False},
    'length': {"readonly" : False},
    'mtime': {"readonly" : True},
    'ctime': {"readonly" : True},
    'btime': {"readonly" : True},
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
def fsToDict(path):
    tempdate = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    mdate = tempdate.strftime("%Y-%m-%d %H:%M:%S")
    owner = str(os.stat(path).st_uid)
    fName = os.path.basename(path)

    hierarchy = {
        'node': fName,
        'path': path,
        'ownerId': owner,
        'properties': bdd().getPropertiesDict(),
        'parent': os.path.basename(os.path.abspath(os.path.join(path, os.pardir))),
        'ancestor': [],
        'accepts': [],
        'provides': [],
    }
    hierarchy['properties']['mtime'] = {'Modified': mdate, 'readonly': True}
    hierarchy['properties']['ctime'] = {'MetaData modified': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        'readonly': True}
    hierarchy['properties']['btime'] = {
        'Creation date': datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime(
            "%Y-%m-%d %H:%M:%S"), 'readonly': True}
    if os.path.isdir(path):
        hierarchy['properties']['type'] = {'type': 'ContainerNode', 'readonly': True}
    elif os.path.isfile(path):
        hierarchy['properties']['type'] = {'type': 'DataNode', 'readonly': True}
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
        bdd().insertionMongo(items)
    print("VOSpace property list OK")
    print("VOSpace protocol list OK")
    print("VOSpace view list OK")
    print("Service's metadata ready")

def populateFiles():
        for dir, subdirs, files in os.walk("./VOTest/VOSpace/nodes/" ):
            for x in subdirs:
                bdd.insertionMongo(bdd(), fsToDict(os.path.join(dir, x)))
            for y in files:
                bdd.insertionMongo(bdd(), fsToDict(os.path.join(dir, y)))

 # Startup check up, if the app crashed and the DB is empty, it update it from FS
def startup():
    if bdd.connexion(bdd()).find({}).count() == 0:
        populateMeta()
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

