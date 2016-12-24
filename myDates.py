import datetime
import time

# strDt = "01/01/2015"
strDt = "21Jun2000"
Dt = datetime.datetime.strptime(strDt, "%d%b%Y")
Dt1 = datetime.datetime.date(Dt)

strDt = "21Jun2001"
Dt = datetime.datetime.strptime(strDt, "%d%b%Y")
Dt2 = datetime.datetime.date(Dt)

strX1 = "19.90"
print strX1

strX2 = "19.99"
print strX2

if strX1 >= strX2:
    print strX1 + " >= " + strX2
else:
    print strX1 + " < " + strX2

X1 = float(strX1)
X2 = float(strX2)
if X1 >= X2:
    print str(X1) + " >= " + str(X2)
else:
    print str(X1) + " < " + str(X2)

print Dt1
print Dt2

if Dt1 >= Dt2:
    print str(Dt1) + " >= " + str(Dt2)
else:
    print str(Dt1) + " < " + str(Dt2)

print Dt.strftime("%Y-%m-%d")


s = "1"
print( type(s))
s = float(s)
print(type(s))