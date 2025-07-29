from PyQt5.QtWidgets import QApplication,QWidget
import sys

def main():
    #app=QApplication([])
    app=QApplication(sys.argv)
    widget = QWidget()
    widget.resize(250,150)
    widget.setWindowTitle("PyQt5AppSAmple")
    widget.show()\
    
    sys.exit(app.exec_())

if __name__=='__main__':
    main()