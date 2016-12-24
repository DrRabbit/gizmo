__author__ = 'Alex'

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics import shapes
from reportlab.graphics.charts.axes import YValueAxis, XValueAxis
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker



pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))

def main():
    print 'Scatter Package explicitly run'
    pass


class MyScatterPlot:

    x_margin = 25
    pictSize = 155

    def __init__(self):

        self.xAxis = XValueAxis()
        self.yAxis = YValueAxis()
        self.xGrid = []
        self.yGrid = []
        self.node_dots = []
        self.node_names = []
        self.title = Label()
        self.v_title = Label()
        self.h_title = Label()
        self.CaptureBox = []

    def format(self, d, xData, yData):

        x_margin = MyScatterPlot.x_margin
        pictSize = MyScatterPlot.pictSize

        r, g, b = (89.0/256, 89.0/256, 89.0/256)
        myGray = colors.Color(r, g, b, alpha=1)

        # X-axis
        self.xAxis.setPosition(0, 0, pictSize)
        self.xAxis.valueMin = xData[0][0]
        self.xAxis.valueMax = xData[0][1]
        self.xAxis.valueStep = (xData[0][1]-xData[0][0]) / 8.0
        self.xAxis.labelTextFormat = '%0.2f'
        self.xAxis.configure(xData)

        # Y-axis
        self.yAxis.setPosition(0, 0, pictSize)
        self.yAxis.valueMin = yData[0][0]
        self.yAxis.valueMax = yData[0][1]
        self.yAxis.valueStep = (yData[0][1]-yData[0][0]) / 8.0
        self.yAxis.labelTextFormat = '%0.2f'
        self.yAxis.configure(yData)

        self.xAxis.labels.fontSize = 7
        self.xAxis.labels.fontName = 'Calibri'
        self.xAxis.labels.fillColor = myGray
        self.xAxis.strokeWidth = 0.5

        self.yAxis.labels.fontSize = 7
        self.yAxis.labels.fontName = 'Calibri'
        self.yAxis.labels.fillColor = myGray
        self.yAxis.strokeWidth = 0.5

        self.yAxis.joinToAxis(self.xAxis, 'value', xData[0][0])
        self.xAxis.joinToAxis(self.yAxis, 'value', yData[0][0])

        self.xAxis._x = x_margin
        self.yAxis._x = x_margin

        # add the X-Y axis to the drawing
        d.add(self.yAxis)
        d.add(self.xAxis)

    def create_gridlines(self, d):

        x_margin = MyScatterPlot.x_margin
        pictsize = MyScatterPlot.pictSize

        dx = MyScatterPlot.x_margin
        dy = 0
        for i in range(0, 9):
            a = shapes.Line(MyScatterPlot.x_margin, dy, pictsize + x_margin, dy)
            a.strokeColor = colors.lightgrey
            a.strokeOpacity = 0.5
            a.strokeWidth = 0.25
            self.xGrid.append(a)
            d.add(self.xGrid[i])
            dy += 25

            a = shapes.Line(dx, 0, dx, pictsize)
            a.strokeColor = colors.lightgrey
            a.strokeOpacity = 0.5
            a.strokeWidth = 0.25
            self.yGrid.append(a)
            d.add(self.yGrid[i])
            dx += 25

    def add_nodes_and_labels(self, d, data, tickers):

        pictsize = MyScatterPlot.pictSize

        x_min = self.xAxis.valueMin
        x_max = self.xAxis.valueMax
        y_min = self.yAxis.valueMin
        y_max = self.yAxis.valueMax

        for i in range(0, len(data)):
            c = makeMarker('FilledCircle')
            if tickers[i] == 'BCOMF3T':
                c.fillColor = colors.red
                c.strokeColor = colors.red
            else:
                c.fillColor = colors.black

            c.size = 4
            c.x = (data[i][0] - x_min)/(x_max-x_min) * pictsize
            c.y = (data[i][1] - y_min)/(y_max-y_min) * pictsize
            self.node_dots.append(c)
            d.add(self.node_dots[i])

            lab = Label()
            if tickers[i] == 'BCOMF3T':
                lab.fillColor = colors.red
            else:
                lab.fillColor = colors.black

            lab.setOrigin(0, 0)
            lab.setText(tickers[i])
            lab.fontName = 'Calibri'
            lab.fontSize = 6
            lab.dx = c.x + 20
            lab.dy = c.y

            self.node_names.append(lab)
            d.add(self.node_names[i])

    def chart_title(self, d):

        # add Main title
        self.title.setOrigin(0, 0)
        self.title.setText('1Y: Risk Return Profile')
        self.title.fontName = 'Calibri'
        self.title.fillColor = colors.black
        self.title.fontSize = 9
        self.title.dx = 100
        self.title.dy = 210
        d.add(self.title)

        # add a vertical title
        self.v_title.setOrigin(0, 0)
        self.v_title.angle = 90
        self.v_title.setText('Returns %')
        self.v_title.fontName = 'Calibri'
        self.v_title.fontSize = 7
        self.v_title.fillColor = colors.black
        self.v_title.dx = -10
        self.v_title.dy = 100
        d.add(self.v_title)

        # add a Horizontal title
        self.h_title.setOrigin(0, 0)
        self.h_title.setText('Volatility %')
        self.h_title.fontName = 'Calibri'
        self.h_title.fillColor = colors.black
        self.h_title.fontSize = 7
        self.h_title.dx = 100
        self.h_title.dy = -10
        d.add(self.h_title)

    def capture(self, d):

        capture_colors = [colors.blue, colors.green, colors.pink, colors.red]

        for i in range(0, 4):
            if i == 0:
                dx = 0
                dy = 0
            elif i == 1:
                dx = 100
                dy = 0
            elif i == 2:
                dx = 0
                dy = 100
            else:
                dx = 100
                dy = 100

            rect = shapes.Rect(dx, dy, 100, 100)
            rect.fillColor = capture_colors[i]
            rect.fillOpacity = 0.1
            rect.strokeColor = colors.white

            self.CaptureBox.append(rect)
            d.add(self.CaptureBox[i])

if __name__ == '__main__':
    main()
else:
    print 'My Scatter package loaded successfully'
