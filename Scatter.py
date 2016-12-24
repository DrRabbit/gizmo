from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.shapes import _DrawingEditorMixin

pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
path = 'C:\\Users\\Alex\\Desktop\\Quant_Report.pdf'

doc = SimpleDocTemplate(path, pagesize=letter, leftMargin = 0.5 * inch, rightMargin=0.5 * inch,
                        topMargin=0.5 * inch, bottomMargin=0.5 * inch, font='Calibri')


class Lab:

    def __init__(self):
        self.lab = Label()

    def format_label(self, desc, fs, dx, dy, rot):
        self.lab.setOrigin(0, 0)
        self.lab.angle = rot
        self.lab.setText(desc)
        self.lab.fontName = 'Calibri'
        self.lab.fontSize = fs
        self.lab.fillColor = colors.black
        self.lab.dx = dx
        self.lab.dy = dy


class Scatter:

    def __init__(self, x_pos, y_pos):
        self.s = ScatterPlot()
        self.s.x = x_pos
        self.s.y = y_pos

        self.v_lab = Lab()
        self.v_lab.format_label(desc='Returns %', fs=7, dx=-10, dy=95, rot=90)
        self.h_lab = Lab()
        self.h_lab.format_label(desc='Volatility %', fs=7, dx=85, dy=-10, rot=0)
        self.m_lab = Lab()
        self.m_lab.format_label(desc='1Y: Risk Return Profile', fs=9, dx=90, dy=170, rot=0)

    def format_scatter(self, temp_data, x_min, x_max, y_min, y_max):
        self.s.width = 155
        self.s.height = 155
        self.s.data = temp_data
        self.s.outerBorderOn = 0
        self.s.yValueAxis.labelTextFormat = '%2.0f'
        self.s.xValueAxis.labelTextFormat = '%2.0f'
        self.s.xValueAxis.valueMin = x_min
        self.s.xValueAxis.valueMax = x_max
        self.s.yValueAxis.valueMin = y_min
        self.s.yValueAxis.valueMax = y_max
        self.s.lineLabels.visible = 0
        self.s.xLabel = ''
        self.s.yLabel = ''

        n = len(temp_data)
        for i in range(0, n):
            self.s.lines[i].symbol.kind = 'Circle'
            self.s.lines[i].symbol.size = 4
            self.s.lines[i].symbol.strokeColor = colors.black
            self.s.lines[i].symbol.fillColor = colors.black

        self.s.xValueAxis.labels.fontSize = 7
        self.s.xValueAxis.labels.fontName = 'Calibri'
        self.s.yValueAxis.labels.fontSize = 7
        self.s.yValueAxis.labels.fontName = 'Calibri'

        # set the grid properties
        self.s.xValueAxis.visibleGrid = 1
        self.s.yValueAxis.visibleGrid = 1
        self.s.xValueAxis.gridStrokeColor = colors.lightgrey
        self.s.yValueAxis.gridStrokeColor = colors.lightgrey


d = Drawing(400, 170)
elements = []


data = [[(8.0, 2.0), (3.0, 6.0), (2.0, 7.0), (10.0, 6.0)]]
Scat1 = Scatter(x_pos=0, y_pos=0)
Scat1.format_scatter(data, x_min=0, x_max=12, y_min=0, y_max=12)
d.add(Scat1.s, '1st Graph')
d.add(Scat1.v_lab.lab)
d.add(Scat1.h_lab.lab)
d.add(Scat1.m_lab.lab)


data2 = [[(1.0, 2.0), (1.0, 6.0)]]
Scat2 = Scatter(x_pos=250, y_pos=0)
Scat2.format_scatter(data2, x_min=0, x_max=12, y_min=0, y_max=12)
d.add(Scat2.s, '2nd Graph')


elements.append(d)
elements.append(d)

doc.build(elements)