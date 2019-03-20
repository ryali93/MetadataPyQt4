from arcgis.gis import GIS

class PublishService(object):
    def __init__(self):
        self.host = "https://ingemmet-peru.maps.arcgis.com"
        self.user = "publicadorapp"
        self.password = "publ1c4d0r"
        self.connectGISpro()

    def connectGISpro(self):
        self.gis = GIS(self.host, self.user, self.password)

    def publishAgol(self, dicc, file):
        file_properties = {
            'title': dicc["title"],
            'summary': dicc["title"],
            'Description': dicc["desc"],
            'tags': dicc["tags"],
            'credit': dicc["resp"],
            'categories': ['/Categories/Geologia'],
            'type': 'Shapefile'
        }
        print(file_properties)
        self.name = dicc["title"]
        self.file_shp = self.gis.content.add(file_properties, file)
        try:
            self.file_shp.publish()
        except:
            pass

    def publishOpenData(self):
        file = self.gis.content.search(self.name, "Feature Layer")[0]
        gid = self.gis.groups.search("Datos Abiertos")[0]
        file.share(groups=[gid.groupid])