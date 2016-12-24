__author__ = 'Alex'

import ScatterPackage as sct
import Yoda_ColumnChart as CC
import myTables as tables
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate, PageBreak, Paragraph, Image
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.styles import getSampleStyleSheet
import webbrowser
import csv



# --------------------------------------------------
elements = []
styles = getSampleStyleSheet()
path = 'C:\\Users\\Alex\\Desktop\\Data\\Quant_Report.pdf'

doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=0.5 * inch, rightMargin=0.5 * inch,
                        topMargin=0.5 * inch, bottomMargin=0.5 * inch, font='Calibri')
size = doc.pagesize[0]
# --------------------------------------------------


# add the page heading
PageHeading = tables.page_heading(text='RISK RETURN STATS', size=size)
elements.append(PageHeading)

text = """ <br/> <br/> <br/> <br/> """
P = Paragraph(text=text, style=styles['Normal'])
elements.append(P)


# Add the capture ratio scatter plot
draw = Drawing(400, 200)
url = 'C:\\Users\\Alex\\Desktop\\Data\\data.csv'
with open(url, 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

s_data = []
s_tickers = []
x_min = 9999
x_max = -9999
y_min = 9999
y_max = -9999
for i in range(0, 4):
    s_tickers.append(data[2+i][1])
    s_data.append((float(data[i+2][2]), float(data[i+2][6])))
    if s_data[i][0] < x_min:
        x_min = s_data[i][0]
    if s_data[i][0] > x_max:
        x_max = s_data[i][0]
    if s_data[i][1] < y_min:
        y_min = s_data[i][1]
    if s_data[i][1] > y_max:
        y_max = s_data[i][1]

x_delta = (x_max-x_min)/10.0
y_delta = (y_max-y_min)/10.0
x_max += x_delta
x_min -= x_delta
y_max += y_delta
y_min -= y_delta


xData = [(x_min, x_max)]
yData = [(y_min, y_max)]


S = sct.MyScatterPlot()
S.dx = 10


# S.capture(d=draw)
S.create_gridlines(d=draw)
S.format(d=draw, xData=xData, yData=yData)
S.chart_title(d=draw)
S.add_nodes_and_labels(d=draw, data=s_data, tickers=s_tickers)

# draw.scale(0.5, 0.5)

elements.append(draw)
elements.append(PageBreak())

# -------------------------------------------------------------------------------

# # insert the first table
# url = 'C:\\Users\\Alex\\Desktop\\Data\\data.csv'
# heading1 = tables.create_heading(text='FIG 1: SUMMARY STATS', size=size)
# t = tables.create_table(data_url=url, size=size)
#
# elements.append(heading1)
# elements.append(t)
#
#
#
#
# text = """ <br/> <br/> <br/> """
# P = Paragraph(text=text, style=styles['Normal'])
# elements.append(P)
# heading2 = tables.create_heading(text='FIG 2.A: RISK RETURN PROFILES', size=size)
# elements.append(heading2)
#
# tickers = ['BCOMF3', 'LOFEMLU', 'JEDDF', 'BCOMF0', 'BAXGHGG']
# data = [(13, 5, 20, 22), (14, 6, 21, 23), (4, 5, 10, 5), (10, 2, 11, 8), (5, 5, 4, 9)]
# draw1 = Drawing(425, 160)  # this is 450 (not 400) to increase headroom between chart above
#
# # chart 1
# c = CC.MyColumnChart(temp_data=data, tks=tickers)
# c.chart_title(d=draw1, title='1Y: Risk Return Profile', v_title='Returns %', h_title='Volatility %', a=0)
# c.barChartFormat(d=draw1, a=0)
# c.addLegend(d=draw1, a=0)
#
# # chart 2
# c1 = CC.MyColumnChart(temp_data=data, tks=tickers)
# c1.chart_title(d=draw1, title='3Y: Risk Return Profile', v_title='Returns %', h_title='Volatility %', a=1)
# c1.barChartFormat(d=draw1, a=1)
# c1.addLegend(d=draw1, a=1)
#
# elements.append(draw1)
#
# # chart 3
# draw2 = Drawing(425, 210)
#
# c2 = CC.MyColumnChart(temp_data=data, tks=tickers)
# c2.chart_title(d=draw2, title='5Y: Risk Return Profile', v_title='Returns %', h_title='Volatility %', a=0)
# c2.barChartFormat(d=draw2, a=0)
# c2.addLegend(d=draw2, a=0)
#
# c2 = CC.MyColumnChart(temp_data=data, tks=tickers)
# c2.chart_title(d=draw2, title='10Y: Risk Return Profile', v_title='Returns %', h_title='Volatility %', a=1)
# c2.barChartFormat(d=draw2, a=1)
# c2.addLegend(d=draw2, a=1)
#
# elements.append(draw2)


aaa = 'C:\\Users\\Alex\\Desktop\\movie\\test.mp4'

im = Image(aaa)
elements.append(aaa)

doc.build(elements)
webbrowser.open_new(r'file://' + path)
