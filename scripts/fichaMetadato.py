#!/usr/bin/python
# -*- coding: utf-8 -*-

from scripts.statics import *
from reportlab.platypus import Image, Spacer, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

LogoIngemmet = os.path.join(IMGFOLDER, "ingemmet_logo.png")

def FichaMetadatos(dicc):
    h1 = PS(
        name='Heading1',
        fontSize=13,
        leading=12,
        alignment=TA_CENTER
    )

    h2 = PS(
        name='Normal',
        fontSize=8,
        leading=10,
        alignment=TA_LEFT
    )

    h3 = PS(
        name='Justify',
        fontSize=6.5,
        leading=10,
        alignment=TA_JUSTIFY
    )

    h4 = PS(
        name='Middle',
        fontSize=6.5,
        leading=10,
        alignment=TA_CENTER
    )

    h_sub_tile = PS(
        name='Heading1',
        fontSize=7,
        leading=12,
        alignment=TA_JUSTIFY
    )

    Elementos = []
    Titulo = Paragraph(u'<strong>FORMATO</strong>', h1)
    Titulo2 = Paragraph(u'<strong>FICHA DE METADATOS ENTREGA DE INFORMACIÓN GEOGRÁFICA</strong>', h1)
    SubTitulo = Paragraph(u'Código: OSI-F-001<br/>Versión  :02<br/>Fecha aprob.:21/12/2016<br/>Página    :1 de 2', h_sub_tile)

    CabeceraPrincipal = [[Image(LogoIngemmet, width=115, height=50), Titulo, SubTitulo], ['', Titulo2, '']]
    Tabla0 = Table(CabeceraPrincipal, colWidths=[4 * cm, 11 * cm, 4 * cm])
    Tabla0.setStyle( TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (0, 0), (0, 1)),
        ('SPAN', (2, 0), (2, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))

    Elementos.append(Tabla0)
    Elementos.append(Spacer(0,10))

    # Informacion de publicacion
    f = {"Pdf": " ", "Shp": " ", "Csv": " ", "Otros": " "}
    f[dicc["format"]] = " X "
    formato = u'({}) Pdf       ({}) Shp       ({}) Csv       ({})Otros:...'.format(f["Pdf"], f["Shp"], f["Csv"], f["Otros"])

    fecha = dicc["fecha"]

    s = {"Proceso": " ", "Terminado": " "}
    s[dicc["situation"]] = " X "
    situacion = u'Estado : ({}) En Proceso        ({}) Terminado'.format(s["Proceso"], s["Terminado"])

    a = {"Mensual": " ", "Anual": " ", "Otros": " "}
    a[dicc["actualizacion"]] = " X "
    actualizacion = u'Actualización : ({}) Mensual        ({}) Anual        ({}) Otros: Según POI'.format(a["Mensual"], a["Anual"], a["Otros"])

    r = {"Referencial": " ", "Definitivo": " "}
    r[dicc["restriccion"]] = " X "
    restriccion = u'De Uso : ({}) Referencial        ({}) Definitivo'.format(r["Referencial"], r["Definitivo"])

    acc = {"Restringido": " ", "Publico": " ", "Otros": " "}
    acc[dicc["acceso"]] = " X "
    acceso = u'De acceso : ({}) Restringido        ({}) Público        ({}) Otros'.format(acc["Restringido"], acc["Publico"], acc["Otros"])

    Filas = [
                [Paragraph(u'<b>Información de Metadatos</b>', h2)],
                [Paragraph(u'<b>1. Título</b>', h3), Paragraph(u'{}'.format(dicc["title"]), h3)],
                [Paragraph(u'<b>2. Breve Descripción</b>', h3), Paragraph(u'{}'.format(dicc["desc"].replace("\n", "<br/>")), h3)],
                [Paragraph(u'<b>3. Metodología</b>', h3), Paragraph(u'{}'.format(dicc["method"]), h3)],
                [Paragraph(u'<b>4. Responsable</b>', h3), Paragraph(u'{}'.format(dicc["resp"]), h3)],
                [Paragraph(u'<b>5. Palabras clave</b>', h3), Paragraph(u'{}'.format(dicc["tags"]), h3)],
                [Paragraph(u'<b>6. Ubicación referencial</b>', h3), Paragraph(u'{}'.format(dicc["ubic"]), h3)],
                [Paragraph(u'<b>7. Escala y fuente</b>', h3), Paragraph(u'{}'.format(dicc["scale"]), h3)],
                [Paragraph(u'<b>8. Formato</b>', h3), Paragraph(formato, h3), Paragraph(u'Fecha de creación: %s'%fecha, h3)],
                [Paragraph(u'<b>9. Situación</b>', h3), Paragraph(situacion, h3), Paragraph(u'%s'%actualizacion, h3)],
                [Paragraph(u'<b>10. Restricciones</b>', h3), Paragraph(restriccion, h3), Paragraph(u'%s'%acceso, h3)]
            ]

    Tabla1 = Table(Filas, colWidths=[4 * cm, 8 * cm, 7 * cm])

    Tabla1.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.2, colors.black),
    ('SPAN', (0, 0), (2, 0)),
    ('SPAN', (1, 1), (2, 1)),
    ('SPAN', (1, 2), (2, 2)),
    ('SPAN', (1, 3), (2, 3)),
    ('SPAN', (1, 4), (2, 4)),
    ('SPAN', (1, 5), (2, 5)),
    ('SPAN', (1, 6), (2, 6)),
    ('SPAN', (1, 7), (2, 7)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BACKGROUND', (0, 0), (2, 0), colors.Color(220.0 / 255, 220.0 / 255, 220.0 / 255))
    ]))

    Elementos.append(Tabla1)
    Elementos.append(Spacer(0,10))

    aut = {"capa": " ", "wms": " ", "shp": " ", "kml": " ", "opendata": " ", "csvxls": " ", "other": " "}
    for i in aut.keys():
        if dicc[i] == True:
            aut[i] = " X "
    acceso = u'({}) Capa<pre>&#9</pre>({}) WMS y WFS<pre>&#9</pre>({}) Shapefile<pre>&#9</pre>({}) KML     ({}) Datos abiertos     ({}) CSV o Excel     ({}) Otros'.format(aut["capa"], aut["wms"], aut["shp"], aut["kml"], aut["opendata"], aut["csvxls"], aut["other"])

    Filas2 = [
                [Paragraph(u'<b>Información de Publicación</b>', h2), '', ''],
                [Paragraph(u'<b>Publicación</b><br/>Formatos reusables en Datos Abiertos(Csv, shapefile)', h3), Paragraph(u'\N{heavy check mark} En página web', h3)],
                ['', Paragraph(u'<i>{}</i>'.format(dicc["webpage"]), h3), Paragraph(u'Autorización para publicar', h3)],
                ['', Paragraph(u'\N{heavy check mark} En Geocatmin', h3), Paragraph(acceso, h3)],
                ['', Paragraph(u'<i>{}</i>'.format(dicc["geocatmin"]), h3)]
            ]

    Tabla2 = Table(Filas2, colWidths=[4 * cm, 8 * cm, 7 * cm])

    Tabla2.setStyle(TableStyle([
    ('GRID', (0, 0), (2, 0), 0.2, colors.black),
    ('GRID', (0, 0), (0, 4), 0.2, colors.black),
    ('BOX', (1, 1), (2, 4), 0.2, colors.black),
    ('SPAN', (0, 0), (2, 0)),
    ('SPAN', (0, 1), (0, 4)),
    ('SPAN', (2, 3), (2, 4)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BACKGROUND', (0, 0), (2, 0), colors.Color(220.0 / 255, 220.0 / 255, 220.0 / 255))
    ]))

    Elementos.append(Tabla2)
    Elementos.append(Spacer(0,10))

    obs = dicc["obs"].replace("\n", "<br/>")

    Filas3 = [
                [Paragraph(u'<br/>'*4+u'.'*80+u'<br/><i>FIRMA RESPONSABLE DE PROYECTO</i>', h4), Paragraph(u'<br/>'*4+u'.'*80+u'<br/><i>FIRMA DIRECTOR QUE ENTREGA INFORMACIÓN</i>', h4)],
                [Paragraph(u'<b>Observación:</b><br/>{}'.format(obs), h3)]
            ]

    Tabla3 = Table(Filas3, colWidths=[9.5 * cm, 9.5 * cm])

    Tabla3.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.2, colors.black),
    ('SPAN', (0, 1), (1, 1)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    Elementos.append(Tabla3)
    Elementos.append(Spacer(0,10))

    PathPDF = u"test.pdf"

    pdf = SimpleDocTemplate(PathPDF, pagesize = A4, rightMargin=65,
                        leftMargin=65,
                        topMargin=0.5 *cm,
                        bottomMargin=0.5 *cm,)

    pdf.build(Elementos)


    final = "Finalizado"
    return final
# FichaMetadatos()