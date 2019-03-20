# -*- coding: utf-8 -*-

nm = {
        'schemaLocation': "{http://www.isotc211.org/2005/gmd http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd}",
        'gmd': "{http://www.isotc211.org/2005/gmd}",
        'gco': "{http://www.isotc211.org/2005/gco}",
        'xsi': "{http://www.w3.org/2001/XMLSchema-instance}",
        "gml": "{http://www.opengis.net/gml}",
        "xlink": "{http://www.w3.org/1999/xlink}"}

class ElementXML(object):
    def __init__(self):
        self.namespaces = nm

        self.MD_DataIdentification = './{}identificationInfo/{}MD_DataIdentification'.format(nm["gmd"], nm["gmd"])
        self.referenceSystemInfo = "./{}referenceSystemInfo/{}MD_ReferenceSystem/{}referenceSystemIdentifier/{}RS_Identifier".format(nm["gmd"], nm["gmd"], nm["gmd"], nm["gmd"])
        self.citation = '{}/{}citation/{}CI_Citation'.format(self.MD_DataIdentification, nm["gmd"], nm["gmd"])
        self.pointcontact = '{}/{}pointOfContact/{}CI_ResponsibleParty'.format(self.MD_DataIdentification, nm["gmd"], nm["gmd"])
        self.contactRC = '{}/{}contactInfo/{}CI_Contact'.format(self.pointcontact, nm["gmd"], nm["gmd"])
        self.addressRC = '{}/{}address/{}CI_Address'.format(self.contactRC, nm["gmd"], nm["gmd"])
        self.descriptiveKeywords = '{}/{}descriptiveKeywords/{}MD_Keywords'.format(self.MD_DataIdentification, nm["gmd"], nm["gmd"])
        self.spatialResolution = '{}/{}spatialResolution/{}MD_Resolution/{}equivalentScale/{}MD_RepresentativeFraction'.format(self.MD_DataIdentification, nm["gmd"], nm["gmd"], nm["gmd"], nm["gmd"])
        self.extent = '{}/{}extent/{}EX_Extent/{}geographicElement/{}EX_GeographicBoundingBox'.format(self.MD_DataIdentification, nm["gmd"], nm["gmd"], nm["gmd"], nm["gmd"])

        self.xml = {
            "dateStamp": './{}dateStamp/{}DateTime'.format(nm["gmd"], nm["gco"]),
                "referenceSystemInfo":{
                "code": "{}/{}code/{}CharacterString".format(self.referenceSystemInfo, nm["gmd"], nm["gco"]),
                "codeSpace": "{}/{}codeSpace/{}CharacterString".format(self.referenceSystemInfo, nm["gmd"], nm["gco"]),
            },
            "identificationInfo":{
                "title": '{}/{}title/{}CharacterString'.format(self.citation, nm["gmd"], nm["gco"]),
                "CI_Date": '{}/{}date/{}CI_Date/{}date/{}DateTime'.format(self.citation, nm["gmd"], nm["gmd"], nm["gmd"], nm["gco"]),
                "abstract": '{}/{}abstract/{}CharacterString'.format(self.MD_DataIdentification, nm["gmd"], nm["gco"]),
                "pointcontact": {
                    "individualName": "{}/{}individualName/{}CharacterString".format(self.pointcontact, nm["gmd"], nm["gco"]),
                    "organisationName": "{}/{}organisationName/{}CharacterString".format(self.pointcontact, nm["gmd"], nm["gco"]),
                    "electronicMailAddressRC": "}/{}electronicMailAddress/{}CharacterString".format(self.addressRC, nm["gmd"], nm["gco"]),
                },
                "keyword": '{}/{}keyword/{}CharacterString'.format(self.descriptiveKeywords, nm["gmd"], nm["gco"]),
                "spatialResolution": '{}/{}denominator/{}Integer'.format(self.spatialResolution, nm["gmd"], nm["gco"]),
                "language": '{}/{}language/{}CharacterString'.format(self.MD_DataIdentification, nm["gmd"], nm["gco"]),
                "extent": {
                    "west": '{}/{}westBoundLongitude/{}Decimal'.format(self.extent, nm["gmd"], nm["gco"]),
                    "east": '{}/{}eastBoundLongitude/{}Decimal'.format(self.extent, nm["gmd"], nm["gco"]),
                    "south": '{}/{}southBoundLatitude/{}Decimal'.format(self.extent, nm["gmd"], nm["gco"]),
                    "north": '{}/{}northBoundLatitude/{}Decimal'.format(self.extent, nm["gmd"], nm["gco"])
                }
            }
        }
