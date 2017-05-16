# VOSpace settings class
# This class checks the state of the service at start up
# Scan the file system to create a dictionary
# Set the service settings

import os
import datetime
import errno
from pprint import pprint
from database import Handler as bdd

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
    'title': {"readonly" : "false"},
    'creator': {"readonly" : "false"},
    'subject': {"readonly" : "false"},
    'description': {"readonly" : "false"},
    'publisher': {"readonly" : "false"},
    'contributor': {"readonly" : "false"},
    'date': {"readonly" : "false"},
    'type': {"readonly" : "true"},
    'format': {"readonly" : "false"},
    'identifier': {"readonly" : "false"},
    'source': {"readonly" : "false"},
    'language': {"readonly" : "false"},
    'relation': {"readonly" : "false"},
    'coverage': {"readonly" : "false"},
    'rights': {"readonly" : "false"},
    'availableSpace': {"readonly" : "false"},
    'groupread': {"readonly" : "false"},
    'groupwrite': {"readonly" : "false"},
    'publicread': {"readonly" : "false"},
    'quota': {"readonly" : "false"},
    'length': {"readonly" : "false"},
    'mtime': {"readonly" : "true"},
    'ctime': {"readonly" : "true"},
    'btime': {"readonly" : "true"},
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
    taille = getSizeDir(path)
    tempdate = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    mdate = tempdate.strftime("%Y-%m-%d %H:%M:%S")
    owner = str(os.stat(path).st_uid)
    fName = os.path.basename(path)


    hierarchy = {
        'node': fName,
        'path': path,
        'ownerId': owner,
        'properties': bdd().getPropertiesDict(),
        'parent' : os.path.basename(os.path.abspath(os.path.join(path, os.pardir))),
        'accepts': [],
        'provides': []
    }
    hierarchy['properties']['mtime'] = {'Modified': mdate, 'readonly' : 'true'}
    hierarchy['properties']['ctime'] = {'MetaData modified': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        'readonly' : 'true'}
    hierarchy['properties']['btime'] = {
        'Creation date': datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime(
            "%Y-%m-%d %H:%M:%S"), 'readonly' : 'true'}
    hierarchy['properties']['type'] = {'type': 'ContainerNode', 'readonly' : 'true'}
    try:
        for index, contents in enumerate(os.listdir(path)):
            hierarchy['children'] = [fsToDict(os.path.join(path, contents))]

    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['properties']['type'] = {'type': 'StructuredDataNode', 'readonly' : 'true'}
        hierarchy['size'] = octet(os.path.getsize(path))
    return hierarchy

 # Startup check up, if the app crashed and the DB is empty, it update it from FS
def startup():
    if bdd.connexion(bdd(), 'VOSpaceMeta').find({}).count() == 0:
        print("Metadata's Database empty")
        print("Updating Database from FileSystem")
        meta = [{'name': 'PROPERTIES', 'metadata' : PROPERTIES},{ 'name': 'PROTOCOL', 'metadata': PROTOCOL}, {'name': 'propertiesdict', 'metadata' : PropertiesDict},
                {'name' :'voprotocols', 'metadata' : {
                    'accepts' : {'get' : 'ivo://ivoa.net/vospace/core#httpget','put' : 'ivo://ivoa.net/vospace/core#httpput'},
                    'provides' : {'get' : 'ivo://ivoa.net/vospace/core#httpget','put' : 'ivo://ivoa.net/vospace/core#httpput'}}},
                {'name': 'voviews', 'metadata' : {
                    'accepts': {'anyview' : 'ivo://ivoa.net/vospace/core#anyview',
                                'fits': 'ivo://ivoa.net/vospace/core#fits',
                                'votable': 'ivo://ivoa.net/vospace/core#votable'},
                    'provides': {'default' : 'ivo://ivoa.net/vospace/core#defaultview',
                                 'fits': 'ivo://ivoa.net/vospace/core#fits',
                                 'votable': 'ivo://ivoa.net/vospace/core#votable'}}},
                {'name': 'voproperties', 'metadata' : {
                    'accepts' : {},
                    'provides' : {},
                    'contains' : {}
                }}]
        for items in meta:
            bdd().insertionMongo(items,'VOSpaceMeta')
        print("VOSpace property list OK")
        print("VOSpace protocol list OK")
        print("VOSpace view list OK")
        print("Database ready")
    else:
        print("Database : OK")

    if bdd.connexion(bdd(), 'VOSpaceFiles').find({}).count() == 0:
        for dir in os.listdir(RACINE + '/VOSpace/nodes'):
            bdd().insertionMongo(fsToDict(RACINE + '/VOSpace/nodes/' + dir), 'VOSpaceFiles')
        print("File's Database ready")

        print("Database ready")
    else:
        print("Database : OK")


startup()
# print(os.listdir(RACINE + '/VOSpace/nodes'))
# for dir in os.listdir(RACINE + '/VOSpace/nodes'):
#     pprint(fsToDict(RACINE + '/VOSpace/nodes/' + dir))
#     print('**************')

