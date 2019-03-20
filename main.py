# -*- coding: UTF-8 -*-

import sys
from scripts.index import *
from scripts.fichaMetadato import *
from scripts.validateFile import *
from scripts.setjs import *
from scripts.publishAgol import *
from scripts.modifyXML import *
from scripts.nls import *
import zipfile

class execute(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.validateData.clicked.connect(self.validate)
        self.ui.uploadZip.clicked.connect(self.uploadData)
        self.ui.publishAgol.clicked.connect(self.publish2agol)
        self.ui.publishOpendata.clicked.connect(self.publish2opendata)
        self.ui.publishMetadata.clicked.connect(self.publish2metadata)
        self.ui.generateReport.clicked.connect(self.refreshData)
        self.msg = Messages()
        self.console = []

        self.datafile = None
        self.extent = None

    #Lectura de datos
    def readValues(self):
        self.dicc = {
            "title" : u'%s'%self.ui.text01_title.text(),
            "desc" : u'%s'%self.ui.text02_desc.toPlainText(),
            "method" : u'%s'%self.ui.text03_method.toPlainText(),
            "resp" : u'%s'%self.ui.text04_resp.text(),
            "tags" : u'%s'%self.ui.text05_tags.text(),
            "ubic" : u'%s'%self.ui.text06_ubic.text(),
            "scale" : u'%s'%self.ui.text07_scale.text(),
            "webpage" : u'%s'%self.ui.text08_webpage.text(),
            "geocatmin" : u'%s'%self.ui.text09_geocatmin.text(),
            "obs" : u'%s'%self.ui.text10_obs.toPlainText(),

            "format": u'%s'%self.ui.cb01_format.currentText(),
            "situation": u'%s'%self.ui.cb02_situation.currentText(),
            "actualizacion": u'%s'%self.ui.cb03_update.currentText(),
            "restriccion": u'%s'%self.ui.cb04_restr.currentText(),
            "acceso": u'%s'%self.ui.cb05_access.currentText(),
            "fecha": u'%s'%self.ui.date_edit.date().toString("dd / MMM / yyyy"),

            "capa" : self.ui.ch03_capa.isChecked(),
            "wms" : self.ui.ch04_wms.isChecked(),   
            "shp" : self.ui.ch05_shp.isChecked(),
            "kml" : self.ui.ch06_kml.isChecked(),
            "opendata" : self.ui.ch07_opendata.isChecked(),
            "csvxls" : self.ui.ch08_csvxls.isChecked(),
            "other" : self.ui.ch09_other.isChecked()
        }

    # Validacion de datos
    def validate(self):
        self.addConsole(self.msg.initValidation)
        self.readValues()
        self.openpfile2validate()
        FichaMetadatos(self.dicc)

    def openpfile2validate(self):
        filetypes = "Excel (*.xls *.xlsx);;Delimitado por comas (*.csv) ;;Shapefile (*.shp)"
        self.datafile = str(QtGui.QFileDialog.getOpenFileName(self, "Select file to import", "", filetypes))
        self.validatefiledata(self.datafile)

    def validatefiledata(self, file):
        validate = readFileValidate(file)
        messages, self.extent = validate.main()
        for msg in messages:
            self.addConsole(msg)
        self.setWebMap()
        self.ui.view.reload()
        self.ui.view.show()

    # Adjuntar data
    def uploadData(self):
        if self.datafile != None:
            self.addConsole("Leyendo archivo")
            dirname = SHPFOLDER
            self.namefile = [os.path.splitext(os.path.join(dirname, x))[0] for x in os.listdir(dirname) if os.path.splitext(x)[1] == ".shp"]
            filetozip = [os.path.join(dirname, x) for x in os.listdir(dirname) if (os.path.splitext(os.path.join(dirname, x))[0] == self.namefile[0] or os.path.splitext(x)[1] == ".xml") and os.path.splitext(x)[1] != ".zip"]
            zp = zipfile.ZipFile(os.path.join(dirname, os.path.splitext(self.namefile[0])[0] + ".zip"), "w", zipfile.ZIP_DEFLATED)
            [zp.write(x, os.path.basename(x))for x in filetozip]
            self.zipfile = os.path.join(dirname, os.path.splitext(self.namefile[0])[0] + ".zip")
        else:
            filetypes = "Map document (*.mxd);;Map package (*.mpk);;Zip (*.zip)"
            self.zipfile = QtGui.QFileDialog.getOpenFileName(self, "Select file to import", "", filetypes)
            self.namefile = os.path.splitext(self.zipfile)[0]

    # Publicar al agol
    def publish2agol(self):
        self.readValues()
        self.addConsole("Publicando al ArcGis Online")
        PublishService().publishAgol(self.dicc, self.zipfile)

    # Publicar a Datos Abiertos
    def publish2opendata(self):
        self.addConsole("Compartiendo a Datos abiertos")
        PublishService().publishOpenData()

    # Publicar a Metadata
    def publish2metadata(self):
        self.addConsole("Creando XML para Metadatos")
        self.createXML()

    def setWebMap(self):
        self.addConsole("setWebMap")
        code = SetJS().buildcode
        frame = self.ui.view.page().mainFrame()
        frame.evaluateJavaScript(code)

    def createXML(self):
        self.addConsole("createXML")
        self.readValues()
        MakeMetadata(self.dicc, self.namefile, self.extent).main()

    # Generar reporte
    def refreshData(self):
        self.addConsole("refreshData")
        self.datafile = None

    def addConsole(self, text):
        self.console.append(text)
        self.ui.statusValue.setText('\n'.join(self.console))
        self.ui.statusValue.moveCursor(QtGui.QTextCursor.End)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = execute()
    window.show()
    sys.exit(app.exec_())