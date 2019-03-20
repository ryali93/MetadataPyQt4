#!/usr/bin/python
# -*- coding: utf-8 -*-

from scripts.statics import *
from scripts.nls import *
import xlrd
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, MultiPoint
import numpy as np
import math
import fiona
from fiona import drivers

class readFileValidate(object):
    def __init__(self, archivo):
        self.este = u"ESTE"
        self.norte = u"NORTE"
        self.zona = u"ZONA"
        self.codigo = u"CD_MTRA"
        self.msg = Messages()

        self.file = archivo

    def readfile(self, archivo):
        self.namefile = os.path.splitext(os.path.basename(archivo))[0]
        ext = os.path.splitext(archivo)[1]
        if ext in (".xls", ".xlsx"):
            self.wb = xlrd.open_workbook(archivo)
            lws = self.wb.sheet_names()
            return lws
        elif ext in (".shp"):
            shp = fiona.open(archivo)
            return shp


    def readshpfile(self, shp):
        if shp.schema["geometry"] == "Point":
            pass
        elif shp.schema["geometry"] == "Line":
            pass
        elif shp.schema["geometry"] == "Polygon":
            pass

    def readxlsfile(self, nameWs):
        ws = self.wb.sheet_by_index(nameWs)
        data = [tuple(cell.value for cell in ws.row_slice(rowx=nrow, start_colx=0, end_colx=ws.ncols)) for nrow in range(ws.nrows)]
        df = pd.DataFrame(data)
        self.headers = df.iloc[0].apply(lambda x: x.upper())
        ndf  = pd.DataFrame(df.values[1:], columns=self.headers)
        return ndf

    def changeCoord(self, ndf):
        spatial_df = None
        listzones = list(set(ndf[self.zona]))
        zones = {'17S': 'epsg:32717', '18S': 'epsg:32718', '19S': 'epsg:32719', 'WGS84': 'epsg:4326'}
        contador = 0
        self.cdmtraNull = []
        for z in listzones:
            qdf = ndf[ndf[self.zona]==z]
            print(len(list(qdf[self.codigo])))

            self.cdmtraNull = list(qdf[(qdf[self.este] == '') | (qdf[self.norte] == '')][self.codigo])
            if len(self.cdmtraNull) > 0:
                qdf = qdf.query("{} != ''".format(self.este) or "{} != ''".format(self.norte))

            geometry = [Point(xy) for xy in zip(qdf[self.este], qdf[self.norte])]
            gdf = gpd.GeoDataFrame(qdf, geometry=geometry)
            gdf.crs = {'init' :'{}'.format(zones[z.upper()])}
            gdf = gdf.to_crs({'init': '{}'.format(zones["WGS84"])})
            if contador == 0:
                spatial_df = gdf
            else:
                spatial_df = pd.concat([spatial_df, gdf])
            contador = contador + 1
        if spatial_df is  not None:
            spatial_df.index = pd.RangeIndex(len(spatial_df.index))
            self.verifyCoords(spatial_df)


    def verifyCoords(self, spdf):

        coordsPt = [[spdf.geometry[x].bounds[0], spdf.geometry[x].bounds[1], spdf[self.codigo][x]] for x in range(len(spdf))]

        centroidPt = [np.median([x[0] for x in coordsPt]), np.median([x[1] for x in coordsPt])]
        distCent = [[math.sqrt(math.pow(pt[0] - centroidPt[0], 2) + math.pow(pt[1] - centroidPt[1], 2)), pt[2]] for
                    pt in coordsPt]
        labels = ["XWGS", "YWGS", self.codigo]
        coordsDf = pd.DataFrame.from_records(coordsPt, columns=labels)
        distCent = pd.DataFrame.from_records(distCent, columns=["Dist", self.codigo])

        dfcdmtracoords = spdf.merge(coordsDf.set_index(self.codigo), on=self.codigo)
        dfcdmtradists = dfcdmtracoords.join(distCent.set_index(self.codigo), on=self.codigo)

        self.extentXY = [dfcdmtradists['XWGS'].min(), dfcdmtradists['YWGS'].max(), dfcdmtradists['YWGS'].min(), dfcdmtradists['YWGS'].max()]

        q = dfcdmtradists["Dist"].quantile(0.9)
        rtest = dfcdmtradists[dfcdmtradists["Dist"] < q * 1.5]

        if len(dfcdmtradists) != len(rtest):
            print(self.msg.incorrectData)
            self.export2json(dfcdmtradists)
            dicc = self.valuesfromJson(dfcdmtradists)
        else:
            print(self.msg.correctData)
            self.export2json(dfcdmtradists)
            dicc = self.valuesfromJson(dfcdmtradists)



    def export2json(self, filetoexport):
        filetoexport.to_file(os.path.join(JSONFOLDER, self.namefile + ".json"), driver='GeoJSON', encoding='utf-8')
        filetoexport.to_file(os.path.join(SHPFOLDER, self.namefile +  ".shp"), driver='ESRI Shapefile', encoding='utf-8')

        jfile = open(os.path.join(JSONFOLDER, self.namefile + ".json"), "r")
        jread = jfile.read()
        jfile.close()

        jfile = open(os.path.join(JSONFOLDER, "rows.json"), "w")
        jfile.write("var rows = ")
        jfile.write(jread)
        jfile.close()

    def valuesfromJson(self, df):
        arrayValues = []
        for r in range(len(df)):
            rowvalue = df.iloc[r].to_dict()
            dictvalue = {
                "type": "Feature",
                "properties": "",#{k:v for k,v in rowvalue.items() if k not in ("geometry", "type")}
                "geometry": {
                    "type": "Point",
                    "coordinates": [rowvalue["XWGS"], rowvalue["YWGS"]]
                }
            }
            arrayValues.append(dictvalue)
        return arrayValues

    def process(self):
        messages = []
        files = self.readfile(self.file)
        if files.__class__.__name__ in ('list', 'tuple'):
            for ws in range(len(files)):
                try:
                    df = self.readxlsfile(ws)
                    if self.zona in list(self.headers):
                        self.changeCoord(df)
                        messages.append(self.msg.correctData)
                except:
                    messages.append(self.msg.incorrectData)
        elif files.__class__.__name__ in ('GeoDataFrame'):
            self.readshpfile(files)
        messages.append(self.msg.verifyCodes + ','.join(self.cdmtraNull))
        return messages

    def main(self):
        messages = self.process()
        return messages, self.extentXY


# if __name__ == '__main__':
    # archivo = r'D:\RYali\TDR4\metadato\dev\test\Base edafoquimica GR36A_.xlsx'
    # archivo = r'D:\RYali\geocatmin\Geoquimica\GE33b_5 Resultados 3era Campana\BD resultados GQ-OSI-F001-GE33b-5_hdm.xlsx'
    # archivo = r'D:\RYali\TDR4\metadato\dev\test\Geopedologia\GR36B\Base edafoquimica GR36B_.xlsx'
    # poo = readFileValidate(archivo)
    # valcoord = poo.main()
