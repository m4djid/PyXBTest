from flask import Flask, request, Response, abort
from VoPackage.voxml import Voxml as xml
from VoPackage.vospace import Vospace as vo
import xml.etree.ElementTree as ET
from VoPackage import settings as start
import os

app = Flask(__name__)


def xmlParser(xml):
    xmlToDict = {
        "accepts": [],
        "provides": [],
        "capabilities": [],
    }

    root = ET.fromstring(xml)

    for k, v in root.attrib.items():
        if "type" in k:
            xmlToDict['properties'] = {'type': [v[v.rfind(":"):][1:], "True"]}
        elif k == "uri":
            parent, cible = os.path.split(v[v.rfind("!"):][1:])
            xmlToDict['cible'] = cible
            xmlToDict['parent'] = os.path.basename(parent)
            xmlToDict['path'] = parent

    for childrens in root:
        if "properties" in childrens.tag:
            ind = ''
            for subchildrens in childrens:
                for k, v in subchildrens.items():
                    if k == "uri":
                        ind = v[v.rfind("#"):][1:]
                        xmlToDict['properties'][ind] = [subchildrens.text]
                    else:
                        xmlToDict['properties'][ind].append(v)
        elif "accepts" in childrens.tag:
            for subchildrens in childrens:
                for k, v in subchildrens.items():
                    xmlToDict['accepts'].append(v)
        elif "provides" in childrens.tag:
            for subchildrens in childrens:
                for k, v in subchildrens.items():
                    xmlToDict['provides'].append(v)
        elif "target" in childrens.tag:
            xmlToDict['target'] = childrens.text
        elif "direction" in childrens.tag:
            xmlToDict['direction'] = childrens.text
        elif "protocol" in childrens.tag:
            xmlToDict['protocol'] = childrens.attrib

    return xmlToDict

@app.route('/', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_root():
    if request.method == 'GET':
        return "VOSpace"


@app.route("/nodes/<path:varargs>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_node(varargs):
    if request.method == 'GET':
        #try:
        retour = vo().getNode(varargs)
        if retour:
            return Response(retour, status=200, content_type='text/xml')
        # else:
        #   abort(404)

    if request.method == 'POST':
        xmlToDict = xmlParser(request.data.decode("utf-8"))
        vo().setNode(xmlToDict['path']+"/"+xmlToDict['cible'], xmlToDict['properties'])
        return Response(vo().getNode(xmlToDict['cible']), status=200, content_type='text/xml')

    if request.method == 'PATCH':
        return "ECHO: PACTH\n"

    if request.method == 'PUT':
        xmlToDict = xmlParser(request.data.decode("utf-8"))
        vo().createNode(xmlToDict)
        return Response(vo().getNode(xmlToDict['cible']), status=200, content_type='text/xml')


    if request.method == 'DELETE':
        vo().deleteNode("nodes/"+varargs)
        return Response(os.path.basename(varargs)+" Deleted\n", status=200, content_type='text/xml')



@app.route("/protocols")
def api_protocols():
    body = vo().getVOSpaceSettings("protocols")
    if body:
        return Response(body, status='200', content_type='text/xml')
    else:
        return Response("Internal Error", status=500, content_type='text/xml')

@app.route("/views")
def api_views():
    body = vo().getVOSpaceSettings("views")
    if body:
        return Response(body, status='200', content_type='text/xml')
    else:
        return Response("Internal Error", status=500, content_type='text/xml')

@app.route("/properties")
def api_properties():
    body = vo().getVOSpaceSettings("properties")
    if body:
        return Response(body, status='200', content_type='text/xml')
    else:
        return Response("Internal Error", status=500, content_type='text/xml')


@app.route('/transfers')
def api_transfers():
    pass

@app.route('/synctrans')
def api_synctrans():
    pass

if __name__ == '__main__':
    app.run()
