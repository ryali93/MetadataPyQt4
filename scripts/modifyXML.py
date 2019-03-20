# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from xml.dom import minidom
from scripts.model_metadatos import *
from scripts.statics import *

class MakeMetadata(object):
    def __init__(self, dicc, namefile, extent):
        self.xmltemplate = Template().xmltemplate
        self.info = dicc
        self.xml = ElementXML().xml
        self.tree = ET.parse(self.xmltemplate)
        self.xmlout = namefile
        self.extent = extent

    def getXML(self):
        ET.register_namespace('gco', "http://www.isotc211.org/2005/gco")
        ET.register_namespace('gmd', "http://www.isotc211.org/2005/gmd")
        ET.register_namespace('geonet', "http://www.fao.org/geonetwork")

        self.xmlparams = {
            "title": self.tree.find(self.xml["identificationInfo"]["title"]),
            "desc": self.tree.find(self.xml["identificationInfo"]["abstract"]),
            "fecha" : self.tree.find(self.xml["dateStamp"]),
            "tags": self.tree.find(self.xml["identificationInfo"]["keyword"]),
            "scale": self.tree.find(self.xml["identificationInfo"]["spatialResolution"]),
            "language": self.tree.find(self.xml["identificationInfo"]["language"]),

            "referenceSystemInfoCode": self.tree.find(self.xml["referenceSystemInfo"]["code"]),
            "referenceSystemInfocodeSpace": self.tree.find(self.xml["referenceSystemInfo"]["codeSpace"]),

            "resp"  : self.tree.find(self.xml["identificationInfo"]["pointcontact"]["individualName"]),
            "direction" : self.tree.find(self.xml["identificationInfo"]["pointcontact"]["organisationName"]),
            "emailresp" : self.tree.find(self.xml["identificationInfo"]["pointcontact"]["electronicMailAddressRC"]),

            "west" : self.tree.find(self.xml["identificationInfo"]["extent"]["west"]),
            "east" : self.tree.find(self.xml["identificationInfo"]["extent"]["east"]),
            "south" : self.tree.find(self.xml["identificationInfo"]["extent"]["south"]),
            "north" : self.tree.find(self.xml["identificationInfo"]["extent"]["north"]),
        }

    def setMetadataMXD(self):
        for x in self.xmlparams.items():
            for y in self.info.items():
                if x[0] == y[0]:
                    self.xmlparams[x[0]].text = self.info[x[0]]
        self.updateExtent()

    def updateExtent(self):
        if self.extent:
            self.xmlparams["west"].text = self.extent[0]
            self.xmlparams["east"].text = self.extent[1]
            self.xmlparams["south"].text = self.extent[2]
            self.xmlparams["north"].text = self.extent[3]

    def exportXML(self):
        filexml = os.path.join(XMLFOLDER, self.xmlout + ".xml")
        self.tree.write(filexml, "UTF-8")

    def process(self):
        self.getXML()
        self.setMetadataMXD()
        self.exportXML()

    def main(self):
        self.process()

# MakeMetadata(dicc=None).main()