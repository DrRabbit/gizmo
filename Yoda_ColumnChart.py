from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))

def main():
    print 'Yoda_ColumnChart Package explicitly run'
    pass




class MyColumnChart:

    def __init__(self, temp_data, tks):

        self.data = temp_data
        self.bc = VerticalBarChart()
        self.leg = Legend()
        self.title = Label()
        self.v_title = Label()
        self.h_title = Label()
        self.myColors = colors
        self.tickers = tks

        alpha = 0.5
        t_pink = colors.Color(192./256, 80./256, 77./256, alpha=alpha)
        t_blue = colors.Color(79./256, 129./256, 189./256, alpha=alpha)
        t_green = colors.Color(155./256, 187./256, 89./256, alpha=alpha)
        t_purple = colors.Color(128./256, 100./256, 162./256, alpha=alpha)
        t_orange = colors.Color(247./256, 150./256, 70./256, alpha=alpha)
        self.myColors = [t_pink, t_blue, t_green, t_purple, t_orange]

    def barChartFormat(self, d, a):

        for i in range(0, len(self.data)):
            self.bc.bars[i].fillColor = self.myColors[i]
            self.bc.bars[i].strokeColor = self.myColors[i]

        self.bc.barWidth = 5
        self.bc.bars.strokeWidth = 0.5

        x = 125
        self.bc.height = x
        self.bc.width = x
        self.bc.data = self.data
        self.bc.categoryAxis.categoryNames = ['1Y', '3Y', '5Y', '10Y']

        self.bc.valueAxis.valueMin = 0
        self.bc.valueAxis.valueMax = 25
        self.bc.valueAxis.valueStep = 5

        self.bc.categoryAxis.labels.fontName = 'Calibri'
        self.bc.valueAxis.labels.fontName = 'Calibri'

        self.bc.categoryAxis.labels.fontSize = 7
        self.bc.valueAxis.labels.fontSize = 7

        self.bc.valueAxis.strokeWidth = 0.5
        self.bc.valueAxis.strokeColor = colors.black

        self.bc.categoryAxis.strokeWidth = 0.5
        self.bc.categoryAxis.strokeColor = colors.black

        self.bc.categoryAxis.visibleGrid = 1
        self.bc.categoryAxis.gridStrokeColor = colors.lightgrey
        self.bc.valueAxis.visibleGrid = 1
        self.bc.valueAxis.gridStrokeColor = colors.lightgrey

        self.bc.x = 20 + 300 * a
        self.bc.y = 0
        # add to drawing
        d.add(self.bc)

    def addLegend(self, d, a):

        x = 125
        self.leg.x = 165 + 300 * a
        self.leg.y = x

        # distant between the swatches
        self.leg.deltay = 11

        self.leg.columnMaximum = len(self.tickers)
        self.leg.fontSize = 7
        self.leg.fontName = 'Calibri'

        items = []
        for i in range(0, len(self.tickers)):
            items.append((self.myColors[i], self.tickers[i]))

        self.leg.colorNamePairs = items
        self.leg.strokeColor = colors.white

        # size of the swathes, i.e. the colored boxes
        self.leg.dx = 7
        self.leg.dy = 7

        # add to drawing
        d.add(self.leg)

    def chart_title(self, d, title, v_title, h_title, a):

        # add Main title
        self.title.setOrigin(0, 0)
        self.title.setText(title)
        self.title.fontName = 'Calibri'
        self.title.fillColor = colors.black
        self.title.fontSize = 9
        self.title.dx = 90 + 300 * a
        self.title.dy = 140
        d.add(self.title)

        # add a vertical title
        self.v_title.setOrigin(0, 0)
        self.v_title.angle = 90
        self.v_title.setText(v_title)
        self.v_title.fontName = 'Calibri'
        self.v_title.fontSize = 7
        self.v_title.fillColor = colors.black
        self.v_title.dx = -5 + 300 * a
        self.v_title.dy = 75
        d.add(self.v_title)

        # add a Horizontal title
        self.h_title.setOrigin(0, 0)
        self.h_title.setText(h_title)
        self.h_title.fontName = 'Calibri'
        self.h_title.fillColor = colors.black
        self.h_title.fontSize = 7
        self.h_title.dx = 85 + 300 * a
        self.h_title.dy = -20
        d.add(self.h_title)


if __name__ == '__main__':
    main()
else:
    print 'My ColumnChart package loaded successfully'

