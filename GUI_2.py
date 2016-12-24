import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 700)

        title = 'Yoda'
        self.setWindowTitle(title)
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.progress.show()
        self.question_box = QtGui.QMessageBox()

        url = 'C:\\Users\\Alex\\Desktop\\yoda.png'
        self.setWindowIcon(QtGui.QIcon(url))

        self.textbox = QtGui.QTextEdit(self)

        # self.textbox = QtGui.QLineEdit(self)
        self.textbox.move(100, 10)
        self.textbox.resize(100, 60)

        self.home()

    def home(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(100, 100)
        btn.move(100, 100)

        btn2 = QtGui.QPushButton('download', self)
        btn2.resize(100, 100)
        btn2.move(200, 100)
        btn2.clicked.connect(self.run_progress_bar)

        url = 'C:\\Users\\Alex\\Desktop\\yoda.png'
        size = 200
        label = QtGui.QLabel(self)
        pic = QtGui.QPixmap(url)
        pic = pic.scaled(size, size, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pic)

        label.move(10, 400)
        label.resize(size, size)

        self.show()

    def run_progress_bar(self):
        complete = 0

        while complete < 100:
            complete += 0.00001
            self.progress.setValue(complete)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self.question_box, 'Extract', 'Exit ?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print('Yoda has been closed')
            sys.exit()
        else:
            pass


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lbl = QtGui.QLabel(self)
        self.lbl.resize(100,20)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):

        self.lbl.setText(date.toString())





def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    ex = Example()
    sys.exit(app.exec_())


run()
