# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork
from scripts.statics import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(846, 749)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(846, 749))
        MainWindow.setMaximumSize(QtCore.QSize(846, 749))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(IMGFOLDER, "icon.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        ## Pushbutton
        self.validateData = QtGui.QPushButton(self.centralwidget)
        self.validateData.setGeometry(QtCore.QRect(10, 620, 111, 23))
        self.validateData.setObjectName(_fromUtf8("validateData"))
        self.validateData.raise_()

        self.uploadZip = QtGui.QToolButton(self.centralwidget)
        self.uploadZip.setGeometry(QtCore.QRect(160, 620, 111, 23))
        self.uploadZip.setObjectName(_fromUtf8("uploadZip"))
        self.uploadZip.raise_()

        self.publishAgol = QtGui.QToolButton(self.centralwidget)
        self.publishAgol.setGeometry(QtCore.QRect(310, 620, 101, 23))
        self.publishAgol.setObjectName(_fromUtf8("publishAgol"))
        self.publishAgol.raise_()

        self.publishOpendata = QtGui.QToolButton(self.centralwidget)
        self.publishOpendata.setGeometry(QtCore.QRect(450, 620, 101, 23))
        self.publishOpendata.setObjectName(_fromUtf8("publishOpendata"))
        self.publishOpendata.raise_()

        self.publishMetadata = QtGui.QToolButton(self.centralwidget)
        self.publishMetadata.setGeometry(QtCore.QRect(590, 620, 101, 23))
        self.publishMetadata.setObjectName(_fromUtf8("publishMetadata"))
        self.publishMetadata.raise_()

        self.generateReport = QtGui.QToolButton(self.centralwidget)
        self.generateReport.setGeometry(QtCore.QRect(770, 615, 50, 41))
        self.generateReport.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(IMGFOLDER, "refresh.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateReport.setIcon(icon)
        self.generateReport.setIconSize(QtCore.QSize(20, 20))
        self.generateReport.setObjectName(_fromUtf8("generateReport"))
        self.generateReport.raise_()

        ## Grupos
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InfoMetadata = QtGui.QGroupBox(self.centralwidget)
        self.InfoMetadata.setGeometry(QtCore.QRect(10, 20, 411, 401))
        self.InfoMetadata.setFont(font)
        self.InfoMetadata.setObjectName(_fromUtf8("InfoMetadata"))

        self.InfoPublication = QtGui.QGroupBox(self.centralwidget)
        self.InfoPublication.setGeometry(QtCore.QRect(10, 430, 411, 181))
        self.InfoPublication.setFont(font)
        self.InfoPublication.setObjectName(_fromUtf8("InfoPublication"))

        self.InfoObservacion = QtGui.QGroupBox(self.centralwidget)
        self.InfoObservacion.setGeometry(QtCore.QRect(440, 480, 391, 131))
        self.InfoObservacion.setFont(font)
        self.InfoObservacion.setObjectName(_fromUtf8("InfoObservacion"))

        self.InfoObservacion.raise_()
        self.InfoPublication.raise_()
        self.InfoMetadata.raise_()

        # ids
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.id01_title = QtGui.QLabel(self.InfoMetadata)
        self.id01_title.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.id01_title.setFont(font)
        self.id01_title.setObjectName(_fromUtf8("id01_title"))

        self.id02_desc = QtGui.QLabel(self.InfoMetadata)
        self.id02_desc.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.id02_desc.setFont(font)
        self.id02_desc.setObjectName(_fromUtf8("id02_desc"))

        self.id03_method = QtGui.QLabel(self.InfoMetadata)
        self.id03_method.setGeometry(QtCore.QRect(20, 150, 111, 16))
        self.id03_method.setFont(font)
        self.id03_method.setObjectName(_fromUtf8("id03_method"))

        self.id04_resp = QtGui.QLabel(self.InfoMetadata)
        self.id04_resp.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.id04_resp.setFont(font)
        self.id04_resp.setObjectName(_fromUtf8("id04_resp"))

        self.id05_tags = QtGui.QLabel(self.InfoMetadata)
        self.id05_tags.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.id05_tags.setFont(font)
        self.id05_tags.setObjectName(_fromUtf8("id05_tags"))

        self.id06_ubic = QtGui.QLabel(self.InfoMetadata)
        self.id06_ubic.setGeometry(QtCore.QRect(20, 240, 111, 16))
        self.id06_ubic.setFont(font)
        self.id06_ubic.setObjectName(_fromUtf8("id06_ubic"))

        self.id07_scale = QtGui.QLabel(self.InfoMetadata)
        self.id07_scale.setGeometry(QtCore.QRect(20, 270, 111, 16))
        self.id07_scale.setFont(font)
        self.id07_scale.setObjectName(_fromUtf8("id07_scale"))

        self.id08_format = QtGui.QLabel(self.InfoMetadata)
        self.id08_format.setGeometry(QtCore.QRect(20, 300, 111, 16))
        self.id08_format.setFont(font)
        self.id08_format.setObjectName(_fromUtf8("id08_format"))

        self.id09_date = QtGui.QLabel(self.InfoMetadata)
        self.id09_date.setGeometry(QtCore.QRect(220, 300, 111, 20))
        self.id09_date.setFont(font)
        self.id09_date.setObjectName(_fromUtf8("id09_date"))

        self.id10_situation = QtGui.QLabel(self.InfoMetadata)
        self.id10_situation.setGeometry(QtCore.QRect(20, 330, 111, 16))
        self.id10_situation.setFont(font)
        self.id10_situation.setObjectName(_fromUtf8("id10_situation"))

        self.id11_update = QtGui.QLabel(self.InfoMetadata)
        self.id11_update.setGeometry(QtCore.QRect(220, 330, 111, 20))
        self.id11_update.setFont(font)
        self.id11_update.setObjectName(_fromUtf8("id11_update"))

        self.id12_restr = QtGui.QLabel(self.InfoMetadata)
        self.id12_restr.setGeometry(QtCore.QRect(20, 360, 111, 16))
        self.id12_restr.setFont(font)
        self.id12_restr.setObjectName(_fromUtf8("id12_restr"))

        self.id13_access = QtGui.QLabel(self.InfoMetadata)
        self.id13_access.setGeometry(QtCore.QRect(220, 360, 111, 20))
        self.id13_access.setFont(font)
        self.id13_access.setObjectName(_fromUtf8("id13_access"))

        self.id14_autorization = QtGui.QLabel(self.InfoPublication)
        self.id14_autorization.setGeometry(QtCore.QRect(20, 110, 161, 16))
        self.id14_autorization.setFont(font)
        self.id14_autorization.setObjectName(_fromUtf8("id14_autorization"))

        # Textos
        self.text01_title = QtGui.QLineEdit(self.InfoMetadata)
        self.text01_title.setGeometry(QtCore.QRect(130, 30, 261, 20))
        self.text01_title.setFont(font)
        self.text01_title.setObjectName(_fromUtf8("text01_title"))

        self.text02_desc = QtGui.QTextEdit(self.InfoMetadata)
        self.text02_desc.setGeometry(QtCore.QRect(130, 60, 261, 81))
        self.text02_desc.setFont(font)
        self.text02_desc.setObjectName(_fromUtf8("text02_desc"))

        self.text03_method = QtGui.QTextEdit(self.InfoMetadata)
        self.text03_method.setGeometry(QtCore.QRect(130, 150, 261, 20))
        self.text03_method.setFont(font)
        self.text03_method.setObjectName(_fromUtf8("text03_method"))

        self.text04_resp = QtGui.QLineEdit(self.InfoMetadata)
        self.text04_resp.setGeometry(QtCore.QRect(130, 180, 261, 20))
        self.text04_resp.setFont(font)
        self.text04_resp.setObjectName(_fromUtf8("text04_resp"))

        self.text05_tags = QtGui.QLineEdit(self.InfoMetadata)
        self.text05_tags.setGeometry(QtCore.QRect(130, 210, 261, 20))
        self.text05_tags.setFont(font)
        self.text05_tags.setObjectName(_fromUtf8("text05_tags"))

        self.text06_ubic = QtGui.QLineEdit(self.InfoMetadata)
        self.text06_ubic.setGeometry(QtCore.QRect(130, 240, 261, 20))
        self.text06_ubic.setFont(font)
        self.text06_ubic.setObjectName(_fromUtf8("text06_ubic"))

        self.text07_scale = QtGui.QLineEdit(self.InfoMetadata)
        self.text07_scale.setGeometry(QtCore.QRect(130, 270, 261, 20))
        self.text07_scale.setFont(font)
        self.text07_scale.setObjectName(_fromUtf8("text07_scale"))

        self.text08_webpage = QtGui.QLineEdit(self.InfoPublication)
        self.text08_webpage.setGeometry(QtCore.QRect(20, 40, 371, 20))
        self.text08_webpage.setFont(font)
        self.text08_webpage.setObjectName(_fromUtf8("text08_webpage"))

        self.text09_geocatmin = QtGui.QLineEdit(self.InfoPublication)
        self.text09_geocatmin.setGeometry(QtCore.QRect(20, 80, 371, 20))
        self.text09_geocatmin.setFont(font)
        self.text09_geocatmin.setObjectName(_fromUtf8("text09_geocatmin"))

        self.text10_obs = QtGui.QTextEdit(self.InfoObservacion)
        self.text10_obs.setGeometry(QtCore.QRect(10, 20, 371, 101))
        self.text10_obs.setObjectName(_fromUtf8("text10_obs"))

        # Combos
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cb01_format = QtGui.QComboBox(self.InfoMetadata)
        self.cb01_format.setGeometry(QtCore.QRect(130, 300, 81, 22))
        self.cb01_format.setFont(font)
        self.cb01_format.setObjectName(_fromUtf8("cb01_format"))
        self.cb01_format.addItem(_fromUtf8(""))
        self.cb01_format.addItem(_fromUtf8(""))
        self.cb01_format.addItem(_fromUtf8(""))
        self.cb01_format.addItem(_fromUtf8(""))
        self.cb01_format.addItem(_fromUtf8(""))

        self.cb02_situation = QtGui.QComboBox(self.InfoMetadata)
        self.cb02_situation.setGeometry(QtCore.QRect(130, 330, 81, 22))
        self.cb02_situation.setFont(font)
        self.cb02_situation.setObjectName(_fromUtf8("cb02_situation"))
        self.cb02_situation.addItem(_fromUtf8(""))
        self.cb02_situation.addItem(_fromUtf8(""))

        self.cb03_update = QtGui.QComboBox(self.InfoMetadata)
        self.cb03_update.setGeometry(QtCore.QRect(300, 330, 91, 22))
        self.cb03_update.setFont(font)
        self.cb03_update.setObjectName(_fromUtf8("cb03_update"))
        self.cb03_update.addItem(_fromUtf8(""))
        self.cb03_update.addItem(_fromUtf8(""))
        self.cb03_update.addItem(_fromUtf8(""))

        self.cb04_restr = QtGui.QComboBox(self.InfoMetadata)
        self.cb04_restr.setGeometry(QtCore.QRect(130, 360, 81, 22))
        self.cb04_restr.setFont(font)
        self.cb04_restr.setObjectName(_fromUtf8("cb04_restr"))
        self.cb04_restr.addItem(_fromUtf8(""))
        self.cb04_restr.addItem(_fromUtf8(""))

        self.cb05_access = QtGui.QComboBox(self.InfoMetadata)
        self.cb05_access.setGeometry(QtCore.QRect(300, 360, 91, 22))
        self.cb05_access.setFont(font)
        self.cb05_access.setObjectName(_fromUtf8("cb05_access"))
        self.cb05_access.addItem(_fromUtf8(""))
        self.cb05_access.addItem(_fromUtf8(""))
        self.cb05_access.addItem(_fromUtf8(""))

        # Checkbox
        self.ch01_webpage = QtGui.QCheckBox(self.InfoPublication)
        self.ch01_webpage.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.ch01_webpage.setFont(font)
        self.ch01_webpage.setChecked(True)
        self.ch01_webpage.setObjectName(_fromUtf8("ch01_webpage"))

        self.ch02_geocatmin = QtGui.QCheckBox(self.InfoPublication)
        self.ch02_geocatmin.setGeometry(QtCore.QRect(20, 60, 101, 17))
        self.ch02_geocatmin.setFont(font)
        self.ch02_geocatmin.setChecked(True)
        self.ch02_geocatmin.setObjectName(_fromUtf8("ch02_geocatmin"))

        self.ch03_capa = QtGui.QCheckBox(self.InfoPublication)
        self.ch03_capa.setGeometry(QtCore.QRect(20, 130, 101, 17))
        self.ch03_capa.setFont(font)
        self.ch03_capa.setObjectName(_fromUtf8("ch03_capa"))

        self.ch04_wms = QtGui.QCheckBox(self.InfoPublication)
        self.ch04_wms.setGeometry(QtCore.QRect(100, 130, 101, 17))
        self.ch04_wms.setFont(font)
        self.ch04_wms.setObjectName(_fromUtf8("ch04_wms"))

        self.ch05_shp = QtGui.QCheckBox(self.InfoPublication)
        self.ch05_shp.setGeometry(QtCore.QRect(200, 130, 101, 17))
        self.ch05_shp.setFont(font)
        self.ch05_shp.setObjectName(_fromUtf8("ch05_shp"))

        self.ch06_kml = QtGui.QCheckBox(self.InfoPublication)
        self.ch06_kml.setGeometry(QtCore.QRect(20, 150, 101, 16))
        self.ch06_kml.setFont(font)
        self.ch06_kml.setObjectName(_fromUtf8("ch06_kml"))

        self.ch07_opendata = QtGui.QCheckBox(self.InfoPublication)
        self.ch07_opendata.setGeometry(QtCore.QRect(100, 150, 101, 17))
        self.ch07_opendata.setFont(font)
        self.ch07_opendata.setObjectName(_fromUtf8("ch07_opendata"))

        self.ch08_csvxls = QtGui.QCheckBox(self.InfoPublication)
        self.ch08_csvxls.setGeometry(QtCore.QRect(200, 150, 101, 16))
        self.ch08_csvxls.setFont(font)
        self.ch08_csvxls.setObjectName(_fromUtf8("ch08_csvxls"))

        self.ch09_other = QtGui.QCheckBox(self.InfoPublication)
        self.ch09_other.setGeometry(QtCore.QRect(290, 140, 101, 17))
        self.ch09_other.setFont(font)
        self.ch09_other.setObjectName(_fromUtf8("ch09_other"))

        # Date
        self.date_edit = QtGui.QDateEdit(self.InfoMetadata)
        # self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.date_edit.setGeometry(QtCore.QRect(290, 300, 110, 22))
        self.date_edit.setFont(font)
        self.date_edit.setObjectName(_fromUtf8("date_edit"))

        # ViewStatus
        self.statusValue = QtGui.QTextEdit(self.centralwidget)
        self.statusValue.setGeometry(QtCore.QRect(10, 660, 821, 71))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.statusValue.setTextColor(QtGui.QColor(153, 0, 0))
        self.statusValue.setFont(font)
        self.statusValue.setFrameShadow(QtGui.QFrame.Sunken)
        self.statusValue.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.statusValue.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.statusValue.setTabChangesFocus(False)
        self.statusValue.setReadOnly(True)
        self.statusValue.setObjectName(_fromUtf8("statusValue"))

        self.redColor = QtGui.QColor(255, 0, 0)

        # Html
        self.view = QtWebKit.QWebView(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(440, 30, 391, 441))
        self.view.setUrl(QtCore.QUrl(_fromUtf8(os.path.join(STATIC, 'index.html'))))
        self.view.setObjectName(_fromUtf8("webView"))

        cache = QtNetwork.QNetworkDiskCache()
        cache.setCacheDirectory(os.path.join(BASE_DIR, "cache"))
        self.view.page().networkAccessManager().setCache(cache)
        self.view.page().networkAccessManager()

        self.view.page().mainFrame().addToJavaScriptWindowObject("MainWindow", MainWindow)
        self.view.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
        self.view.loadFinished.connect(self.onLoadFinished)
        self.view.linkClicked.connect(QtGui.QDesktopServices.openUrl)

        # MainWindow
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.validateData.setText(_translate("MainWindow", "Validar y crear ficha", None))
        self.uploadZip.setText(_translate("MainWindow", "Adjuntar (*.zip)", None))
        self.publishAgol.setText(_translate("MainWindow", "Subir Agol", None))
        self.publishOpendata.setText(_translate("MainWindow", "Subir OpenData", None))
        self.publishMetadata.setText(_translate("MainWindow", "Subir Metadata", None))
        # self.generateReport.setText(_translate("MainWindow", "...", None))

        self.InfoMetadata.setTitle(_translate("MainWindow", "Información de metadatos", None))
        self.InfoPublication.setTitle(_translate("MainWindow", "Información de Publicación", None))
        self.InfoObservacion.setTitle(_translate("MainWindow", "Observación", None))

        self.id01_title.setText(_translate("MainWindow", "Título", None))
        self.id02_desc.setText(_translate("MainWindow", "Descripción", None))
        self.id03_method.setText(_translate("MainWindow", "Metodología", None))
        self.id04_resp.setText(_translate("MainWindow", "Responsable", None))
        self.id05_tags.setText(_translate("MainWindow", "Palabras clave", None))
        self.id06_ubic.setText(_translate("MainWindow", "Ubicación referencial", None))
        self.id07_scale.setText(_translate("MainWindow", "Escala y fuente", None))
        self.id08_format.setText(_translate("MainWindow", "Formato", None))
        self.id09_date.setText(_translate("MainWindow", "Fecha", None))
        self.id10_situation.setText(_translate("MainWindow", "Situación", None))
        self.id11_update.setText(_translate("MainWindow", "Actualización: ", None))
        self.id12_restr.setText(_translate("MainWindow", "Restricciones", None))
        self.id13_access.setText(_translate("MainWindow", "De acceso:", None))
        self.id14_autorization.setText(_translate("MainWindow", "Autorización para publicar", None))

        self.cb01_format.setItemText(0, _translate("MainWindow", "Pdf", None))
        self.cb01_format.setItemText(1, _translate("MainWindow", "Shp", None))
        self.cb01_format.setItemText(2, _translate("MainWindow", "Csv", None))
        self.cb01_format.setItemText(3, _translate("MainWindow", "Otros", None))

        self.cb02_situation.setItemText(0, _translate("MainWindow", "Proceso", None))
        self.cb02_situation.setItemText(1, _translate("MainWindow", "Terminado", None))

        self.cb03_update.setItemText(0, _translate("MainWindow", "Mensual", None))
        self.cb03_update.setItemText(1, _translate("MainWindow", "Anual", None))
        self.cb03_update.setItemText(2, _translate("MainWindow", "Otros: Según POI", None))

        self.cb04_restr.setItemText(0, _translate("MainWindow", "Referencial", None))
        self.cb04_restr.setItemText(1, _translate("MainWindow", "Definitivo", None))

        self.cb05_access.setItemText(0, _translate("MainWindow", "Restringido", None))
        self.cb05_access.setItemText(1, _translate("MainWindow", "Publico", None))
        self.cb05_access.setItemText(2, _translate("MainWindow", "Otros", None))

        self.ch01_webpage.setText(_translate("MainWindow", "En Página Web", None))
        self.ch02_geocatmin.setText(_translate("MainWindow", "En Geocatmin", None))

        self.ch03_capa.setText(_translate("MainWindow", "Capa", None))
        self.ch04_wms.setText(_translate("MainWindow", "WMS y WFS", None))
        self.ch05_shp.setText(_translate("MainWindow", "Shapefile", None))
        self.ch06_kml.setText(_translate("MainWindow", "KML", None))
        self.ch07_opendata.setText(_translate("MainWindow", "Datos abiertos", None))
        self.ch08_csvxls.setText(_translate("MainWindow", "CSV o Excel", None))
        self.ch09_other.setText(_translate("MainWindow", "Otros", None))

    def onLoadFinished(self):
        with open(os.path.join(STATIC, 'index.js'), 'r') as f:
            frame = self.view.page().mainFrame()
            frame.evaluateJavaScript(f.read())