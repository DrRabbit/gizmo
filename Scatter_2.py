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

    def __init__(self, x_pos, y_pos, desc, fs, dx, dy, rot):
        self.s = ScatterPlot()
        self.s.x = x_pos
        self.s.y = y_pos

        self.v_lab = Lab()
        self.v_lab.format_label(desc=desc[0], fs=fs[0], dx=dx[0], dy=dy[0], rot=rot[0])
        self.h_lab = Lab()
        self.h_lab.format_label(desc=desc[1], fs=fs[1], dx=dx[1], dy=dy[1], rot=rot[1])
        self.m_lab = Lab()
        self.m_lab.format_label(desc=desc[2], fs=fs[2], dx=dx[2], dy=dy[2], rot=rot[2])

    def format_scatter(self, temp_data, x_min, x_max, y_min, y_max, x_step, y_step):
        self.s.width = 155
        self.s.height = 155
        self.s.data = temp_data
        self.s.outerBorderOn = 0
        self.s.yValueAxis.labelTextFormat = '%2.0f'
        self.s.xValueAxis.labelTextFormat = '%2.0f'

        # self.s.xValueAxis.valueStep = x_step
        # self.s.yValueAxis.valueStep = y_step

        self.s.xValueAxis.valueMin = x_min
        self.s.xValueAxis.valueMax = x_max
        self.s.yValueAxis.valueMin = y_min
        self.s.yValueAxis.valueMax = y_max
        self.s.lineLabels.visible = 0
        self.s.xLabel = ''
        self.s.yLabel = ''

        n = 4
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
tickers = ['BCOMTR', 'BCOMF3T', 'CMCITR', 'SPGSCITR']
elements = []

'''
create the graph:
First need to determine the min/max and step size for both x-axis and y-axis
'''
data = [[(8.0, 2.0), (3.0, 6.0), (2.0, 7.0), (10.0, 6.0)]]
x_max = -9999
x_min = 9999
y_max = -9999
y_min = 9999

for i in range(0, len(tickers)):
    if data[0][i][0] > x_max:
        x_max = data[0][i][0]
    if data[0][i][0] < x_min:
        x_min = data[0][i][0]
    if data[0][i][1] > y_max:
        y_max = data[0][i][1]
    if data[0][i][1] < y_min:
        y_min = data[0][i][1]

delta = (x_max - x_min) / len(tickers)
x_axis_max = x_max + delta
x_axis_min = x_min - delta
x_axis_step = (x_axis_max - x_axis_min)/len(tickers)

delta = (y_max - y_min) / len(tickers)
y_axis_max = y_max  # + delta
y_axis_min = y_min  #   - delta
y_axis_step = (y_axis_max - y_axis_min)/len(tickers)




desc = ['Returns %', 'Volatility', '1Y: Risk Return profile']
fs = [7, 7, 9]
dx = [-10, 85, 90]
dy = [95, -10, 170]
rot = [90, 0, 0]
Scat1 = Scatter(x_pos=0, y_pos=0, desc=desc, fs=fs, dx=dx, dy=dy, rot=rot)
Scat1.format_scatter(data, x_min=x_axis_min, x_max=x_axis_max,
                     y_min=y_axis_min, y_max=y_axis_max, x_step=x_axis_step, y_step=y_axis_step)

d.add(Scat1.s, '1st Graph')
d.add(Scat1.v_lab.lab)
d.add(Scat1.h_lab.lab)
d.add(Scat1.m_lab.lab)

# create the labels
dictLabels = {}

for i in range(0, len(tickers)):
    a = Label()
    dx = data[0][i][0]
    dy = data[0][i][1]
    a.x = ((0 + dx - x_axis_min) / abs(x_axis_max - x_axis_min)) * 155
    a.y = ((0 + dy - y_axis_min) / abs(y_axis_max - y_axis_min)) * 155
    a.setText(tickers[i])
    a.fontName = 'Calibri'
    a.fontSize = 6
    a.fillColor = colors.black

    dictLabels[tickers[i]] = a
    d.add(dictLabels[tickers[i]])


# data2 = [[(1.0, 2.0), (1.0, 6.0), (4.0, 10.0), (10, 10)]]
# desc = ['Returns %', 'Volatility', '3Y: Risk Return profile']
# dx = [240, 335, 340]
# dy = [95, -10, 170]
# Scat2 = Scatter(x_pos=250, y_pos=0, desc=desc, fs=fs, dx=dx, dy=dy, rot=rot)
# Scat2.format_scatter(data2, x_min=0, x_max=12, y_min=0, y_max=12)
# d.add(Scat2.s, '2nd Graph')
# d.add(Scat2.v_lab.lab)
# d.add(Scat2.h_lab.lab)
# d.add(Scat2.m_lab.lab)


elements.append(d)
# elements.append(d)

doc.build(elements)