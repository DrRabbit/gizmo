
from reportlab.lib import colors
from reportlab.platypus import Table, Image
import csv
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import inch
from reportlab.graphics.shapes import Drawing

pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))


elements = []

# ----------------------------------------------------------------
colorPalette = {}

r, g, b = (89./256, 89./256, 89./256)   # FIG title
colorPalette['Heading'] = colors.Color(r, g, b, alpha=1)

r, g, b = (148./256, 138./256, 84./256)   # line color for the line under the Heading
colorPalette['lineColor'] = colors.Color(r, g, b, alpha=1)

r, g, b = (54./256, 95./256, 145./256)   # for the first ticker row, i.e. the main index
colorPalette['Blue'] = colors.Color(r, g, b, alpha=1)

r, g, b = (221./256, 217./256, 195./256)   # cell color for the column fields
colorPalette['yellow'] = colors.Color(r, g, b, alpha=1)

r, g, b = (74./256, 68./256, 42./256)   # font color for the cell headings
colorPalette['darkGray'] = colors.Color(r, g, b, alpha=1)

r, g, b = (238./256, 236./256, 225./256)   # row color for the alternating rows
colorPalette['rowColor'] = colors.Color(r, g, b, alpha=1)

r, g, b = (231./256, 230./256, 230./256)   # row color for the alternating rows
colorPalette['new'] = colors.Color(r, g, b, alpha=1)
# ----------------------------------------------------------------




def create_heading(text, size):

    h = [[text, 'Top'], ['', '']]

    tableStyle = [('FONT', (0, 0), (1, 0), 'Helvetica-Bold'),
                  ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                  ('FONTSIZE', (0, 0), (0, 0), 11),
                  ('TEXTCOLOR', (0, 0), (0, 0), colorPalette['Heading']),
                  ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                  ('FONTSIZE', (1, 0), (1, 0), 8),
                  ('TEXTCOLOR', (1, 0), (1, 0), colorPalette['Blue']),
                  ('SPAN', (0, 1), (1, 1)),
                  ('LINEBELOW', (0, 0), (1, 0), 0.25, colorPalette['lineColor'])]

    t = Table(h, hAlign='LEFT')
    t.setStyle(tableStyle)

    t._argW[0] = 3.5 * inch
    t._argW[1] = (size/72.0 - 3.5 - 1) * inch
    t._argH[1] = 0.15*inch

    return t


def create_table(data_url, size):

    with open(data_url, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
    source = ('Source: ETF Securities', '', '', '', '', '', '', '', '', '', '', '', '', '')
    data.append(source)

    t = Table(data, hAlign='LEFT',
              style=[

                   ('BACKGROUND', (0, 0), (13, 1), colorPalette['yellow']),

                   ('TEXTCOLOR', (0, 0), (13, 1), colorPalette['darkGray']),
                   ('TEXTCOLOR', (0, 2), (13, 2), colorPalette['Blue']),
                   ('FONT', (0, 0), (13, 1), 'Helvetica-Bold'),
                   ('FONT', (0, 2), (13, len(data)-1), 'Calibri'),
                   ('FONTSIZE', (0, 0), (13, len(data)-1), 7),

                   ('SPAN', (0, 0), (1, 0)),
                   ('SPAN', (2, 0), (5, 0)),
                   ('SPAN', (6, 0), (9, 0)),
                   ('SPAN', (10, 0), (13, 0)),
                   ('SPAN', (0, 7), (13, len(data)-1)),

                   ('INNERGRID', (1, 0), (2, 0), 0.25, colors.white),
                   ('INNERGRID', (5, 0), (6, 0), 0.25, colors.white),
                   ('INNERGRID', (9, 0), (10, 0), 0.25, colors.white),

                   ('ALIGN', (0, 0), (13, len(data)-2), 'CENTER'),
                   ('VALIGN', (0, 0), (13, len(data)-2), 'TOP'),
                   ('ALIGN', (0, len(data)-1), (13, len(data)-1), 'RIGHT'),
                   ('ALIGN', (0, 2), (1, len(data)-2), 'LEFT'),

                   ('TEXTCOLOR', (0, 3), (13, len(data)-2), colorPalette['darkGray']),
                   ('TEXTCOLOR', (0, len(data)-1), (0, len(data)-1), colorPalette['darkGray']),

                   ('LINEBELOW', (0, len(data)-2), (13, len(data)-2), 0.25, colors.gray)

               ])

    for i in range(3, len(data)-2, 2):
        x = [('BACKGROUND', (0, i), (13, i), colorPalette['rowColor'])]
        t.setStyle(x)

    for i in range(5, 13):
        x = [('INNERGRID', (i, 1), (i+1, 1), 0.25, colors.white)]
        t.setStyle(x)

    for i in range(0, 5):
        x = [('INNERGRID', (i, 1), (i+1, 1), 0.25, colors.white)]
        t.setStyle(x)

    t._argW[0] = 2.5*inch
    t._argW[1] = 1*inch

    for i in range(2, 14):
        t._argW[i] = (size/72.0 - 1 - 2.5 - 1)/12 * inch

    for i in range(0, len(data)):
        t._argH[i] = 0.2*inch

    return t


def page_heading(text, size):

    # url = 'C:\\Users\\Alex\\Desktop\\Data\\logo.jpg'
    # logo = Image(url, width=0.5*inch, height=0.5*inch)

    text = [(text, '', ''), ('', '', ''), ('', '', '')]

    t = Table(text, hAlign='LEFT',
              style=[
                  ('LINEABOVE', (0, 0), (1, 0), 0.25, colors.black),
                  ('LINEABOVE', (0, 2), (1, 2), 0.25, colors.black),
                  ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
                  ('ALIGN', (0, 0), (1, 0), 'CENTER'),
                  ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
                  ('FONT', (0, 0), (1, 0), 'Helvetica-Bold'),
                  ('TEXTCOLOR', (0, 0), (1, 0), colorPalette['Blue']),
                  ('FONTSIZE', (0, 0), (1, 0), 14),
                  ('SPAN', (0, 0), (2, 0))
              ])
    t._argW[0] = (size/72.0 - 1.17) * inch
    t._argH[0] = 0.50 * inch
    a = 0.01
    t._argH[1] = a * inch
    t._argH[2] = a * inch

    return t
