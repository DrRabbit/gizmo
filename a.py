from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.graphics.shapes import Drawing, String
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.lineplots import ScatterPlot




pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
path = 'C:\\Users\\Alex\\Desktop\\Quant_Report.pdf'

doc = SimpleDocTemplate(path, pagesize=letter, leftMargin = 0.5 * inch, rightMargin=0.5 * inch,
                        topMargin=0.5 * inch, bottomMargin=0.5 * inch, font='Calibri')

d = Drawing(160, 170)
elements = []


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
        self.s.x = y_pos

        self.v_lab = Lab()
        self.v_lab.format_label(desc='Returns %', fs=7, dx=-10, dy=95, rot=90)
        self.h_lab = Lab()
        self.h_lab.format_label(desc='Volatility %', fs=7, dx=85, dy=5, rot=0)
        self.m_lab = Lab()
        self.m_lab.format_label(desc='1Y: Risk Return Profile', fs=9, dx=90, dy=185, rot=0)

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


data = [[[1, 1]], [[2, 2]], [[2.5, 1]], [[3, 3]]]
Scat = Scatter(x_pos=0, y_pos=0)
Scat.format_scatter(data, x_min=0, x_max=12, y_min=0, y_max=12)



d.add(Scat.s)
d.add(Scat.v_lab.lab)
d.add(Scat.h_lab.lab)
d.add(Scat.m_lab.lab)

elements.append(d)
doc.build(elements)




# d.add(s1)
# d.add(s2)
# elements.append(d)
# doc.build(elements)



#
# def format_label(lab, desc, fs, dx, dy, rot):
#         lab.setOrigin(0, 0)
#         lab.angle = rot
#         lab.setText(desc)
#         lab.fontName = 'Calibri'
#         lab.fontSize = fs
#         lab.fillColor = colors.black
#         lab.dx = dx
#         lab.dy = dy
#         d.add(lab)



# v_lab = Label()
# format_label(v_lab, desc='Returns %', fs=7, dx=-10, dy=80, rot=90, )
# h_lab = Label()
# format_label(h_lab, desc='Volatility %', fs=7, dx=80, dy=-10, rot=0)
# title_lab = Label()
# format_label(title_lab, desc='1Y: Risk Return Profile', fs=9, dx=80, dy=170, rot=0)



# s1 = ScatterPlot()
# scatter_chart_format(s1, data, x_min=0, x_max=12, y_min=0, y_max=12)
# s1.x = 0
# s1.y = 0

#
# s2 = ScatterPlot()
# scatter_chart_format(s2, data, x_min=0, x_max=12, y_min=0, y_max=12)
# s2.x = 255
# s2.y = 0



