# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout
# import sys

# def main():
#     #app=QApplication([])
#     app=QApplication(sys.argv)
#     widget = QWidget()
#     widget.resize(250,150)
#     widget.setWindowTitle("PyQt5AppSAmple")
#     widget.show()\
    
#     sys.exit(app.exec_())

# if __name__=='__main__':
#     main()

import sys
from random import choice
from PyQt5.QtCore import Qt



window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QMenu,
    QAction
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        

        self.setWindowTitle("Widgets App")
        self.ver=True

        #layout = QVBoxLayout()
        PB=QPushButton("slot_button")
        #PB.setCheckable(True)
        PB.clicked.connect(self.slotfuntion)
        #layout.addWidget(PB)

        #widget = QWidget(PB)
        #widget.setLayout(layout)
        self.setCentralWidget(PB)

    def slotfuntion(self):
        print("Buntton was clicked ")    


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("checked")

        self.button_is_checked=True

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.setChecked(self.button_is_checked)
        #button.clicked.connect(self.Ischecked)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self, a):
        #print("Checked",a)
        #self.the_button_was_clicked=a
        #self.button_is_checked=a
        print(self.button_is_checked)
        #self.state=a
        #print(self.state)

    # def Ischecked(self,):
    #     print("Clicked!")


class RainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        # button = QPushButton("Press Me!")
        # button.setCheckable(True)
        # button.clicked.connect(self.the_button_was_toggled)
        # button.setChecked(self.button_is_checked)
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    # def the_button_was_toggled(self, checked):
    #     self.button_is_checked = checked

    #     print(self.button_is_checked)
    def the_button_was_toggled(self): 
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

class ZainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("DataFromWidgit")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self): 
        self.button_is_checked = self.button.isChecked()
        self.setWindowTitle("A new window title")
        #self.button.setText("You already clicked me.")
        #self.button.setEnabled(False)

        print(self.button_is_checked)


class DainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.button_is_checked = True

        self.setWindowTitle("New_Window_Title")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        self.windowTitleChanged.connect(self.the_window_title_changed)


        self.setCentralWidget(self.button)

    def the_button_was_released(self): 
        self.button_is_checked = self.button.isChecked()
        self.setWindowTitle("A new window title")
        #self.button.setText("You already clicked me.")
        #self.button.setEnabled(False)
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

        print(self.button_is_checked)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        #if window_title == 'Something went wrong':
             #self.button.setDisabled(True)
            




class GainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WidgetCOmm")
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        # layout.addWidget(self.input)
        
        # layout.addWidget(self.label)

        # self.button = QLabel("hello")

        # self.buttona = QLineEdit("HI")
        container=QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    

class RinWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EventHandler")
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
        super().mousePressEvent(e)
        e.ignore()
        # if e.button() == Qt.LeftButton:
        #     # handle the left-button press in here
        #     self.label.setText("mousePressEvent LEFT")
        # elif e.button() == Qt.MiddleButton:
        #     # handle the middle-button press in here.
        #     self.label.setText("mousePressEvent MIDDLE")

        # elif e.button() == Qt.RightButton:
        #     # handle the right-button press in here.
        #     self.label.setText("mousePressEvent RIGHT")  


class CWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("contextMenu")
        self.label = QLabel("Click window")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())


    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")







app = QApplication(sys.argv)
Swindow = SubWindow()
window = MainWindow()
rin=RinWindow()
win=RainWindow()
Zwin=ZainWindow()
Dwin=DainWindow()
Sin=GainWindow()
Cin=CWindow()

Swindow.show()
window.show()
win.show()
Zwin.show()
Dwin.show()
Sin.show()
rin.show()
Cin.show()
app.exec()
