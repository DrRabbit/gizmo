import matplotlib.pyplot as plt
import seaborn
from matplotlib import colors

labels = ['Energy', 'Grains', 'Softs', 'Livestock']

labels_2 = ['WTI', 'Crude','Natgas', 'Lean Hogs', 'Live Cattle', 'Feeder Cattle',
           'Sugar', 'Cotton', 'Coffee', 'Wheat Chicago','Wheat Kansas', 'Heating Oil']

sizes = [15, 30, 45, 10]

dc = {'myBlue': (91 / 255., 155 / 255., 213 / 255., 1),
      'myLightBlue': (91 / 255., 155 / 255., 213 / 255., 0.3),
      'myGreen': (169 / 255., 208 / 255., 142 / 255., 1),
      'myLightGreen': (169 / 255., 208 / 255., 142 / 255., 0.5),
      'myPink': (244 / 255., 176 / 255., 132 / 255., 1),
      'myLightPink': (244 / 255., 176 / 255., 122 / 255., 0.4),
      'myGray': (177 / 255., 113 / 255., 113 / 255., 1),
      'myLightGray': (177 / 255., 113 / 255., 113 / 255., 0.4),
      'myDarkGray': (42 / 255., 42 / 255., 42 / 255., 1)}

c = [dc['myPink'], dc['myBlue'], dc['myGreen'], dc['myGray']]
# colors = 12 *['white']


c_2 = [dc['myLightGreen']] * 12
explode = (0, 0, 0, 0)  # explode a slice if require
explode_2 = (1, 0, 0, 0)  # explode a slice if require

sizes_2 = [15, 30, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10]

plt.figure(figsize=(4, 4))

# large
patches, texts, autotexts = plt.pie(sizes_2,
                                    colors=c_2,
                                    labels= labels_2,
                                    autopct='%1.1f%%',
                                    shadow=False,
                                    startangle=0,
                                    pctdistance=0.8,
                                    radius=2)

for i in range(0, 1):
    patches[i].set_color(dc['myLightPink'])

for i in range(1, 2):
    patches[i].set_color(dc['myLightBlue'])

for i in range(2, 11):
    patches[i].set_color(dc['myLightGreen'])

for i in range(11, 12):
    patches[i].set_color(dc['myLightGray'])

for i in range(0, 12):
    patches[i].set_edgecolor('white')
    patches[i].set_linewidth(2)

for t in texts:
    t.set_size(9)
    t.set_color(dc['myDarkGray'])

# --------------------------------------------------------------------


# small
patches, texts, autotexts = plt.pie(sizes,
                                    explode=explode,
                                    colors=c,
                                    labels=labels,
                                    autopct='%1.1f%%',
                                    shadow=False,
                                    startangle=0,
                                    pctdistance=0.8,
                                    labeldistance=0.4,
                                    radius=1.25)

for t in texts:
    t.set_size(12)
    t.set_style('oblique')
    t.set_color('white')

for t in autotexts:
    t.set_size(11)
    t.set_color(dc['myDarkGray'])

url = 'C:\\Users\\Alex\\Desktop\\donut.png'
plt.savefig(url, bbox_inches='tight', dpi=600)
