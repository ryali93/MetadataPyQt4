import os

__author__ = 'INGEMMET'
__copyright__ = 'INGEMMET 2019'
__credits__ = ['Roy Yali S.']
__version__ = '1.0.1'
__maintainer__ = ['Roy Yali S.']
__mail__ = 'ryali93@gmail.com'
__status__ = 'Development'

BASE_DIR = os.path.abspath(os.path.join(__file__, '..\..\..'))

STATIC = os.path.join(BASE_DIR, "dev\static")
JSONFOLDER = os.path.join(STATIC, "json")
SHPFOLDER = os.path.join(STATIC, "shp")
IMGFOLDER = os.path.join(STATIC, "img")
XMLFOLDER = os.path.join(STATIC, "xml")
DOCFOLDER = os.path.join(STATIC, "docs")


class Template(object):
    def __init__(self):
        self.xmltemplate = os.path.join(XMLFOLDER, "metadato_ejemplo.xml")
        self.guideuser = os.path.join(DOCFOLDER, 'UserGuide.pdf')
        self.xmlout = os.path.join(XMLFOLDER, "outxml.xml")
        print(self.xmltemplate)