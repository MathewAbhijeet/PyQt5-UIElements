import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QDial,
    QWidget,
    QVBoxLayout,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = QLabel("Hello")
        #this method return copyes therefor needing a temp obj
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
       
        # widget.font().setPointSize(30)
        # widget.setFont(widget.font())
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)


class CheckBoxWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My CheckBox")
        #wid = QLabel("checkbox")
        widget = QCheckBox("CheckBox")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setCheckState(Qt.Unchecked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)
        #wid.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.setCentralWidget(widget)
        

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


class checkbox2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.checkbox = QCheckBox("Check me")
        self.checkbox.stateChanged.connect(self.show_state)
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def show_state(self, state):
        print(f"State changed: {state}")  # Prints 0 or 2

class QCom_Box(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCom_Box")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # Sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        widget.currentTextChanged.connect( self.text_changed )
        widget.setEditable(True)

        self.setCentralWidget(widget)

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)



class scrollableList(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i): # Not an index, i is a QListWidgetItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)        


class FieldBox(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FieldBox")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        #widget.setReadOnly(True) # uncomment this to make it read-only

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)




class spin_Box(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("egwindow")

        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


class S_lider(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSlider()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")




class Dial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
#Mwindow = MainWindow()
# Fwindow = CheckBoxWindow()
# Twindow = checkbox2()
Fiwindow = QCom_Box()
sixwindow=scrollableList()
sixwindow.show()
sewindow =FieldBox()
sewindow.show()
egwindow=spin_Box()
egwindow.show()
niwindow=S_lider()
niwindow.show()
tenwindow=Dial()
tenwindow.show()
#Mwindow.show()
# Fwindow.show()
# Twindow.show()
Fiwindow.show()
app.exec()
