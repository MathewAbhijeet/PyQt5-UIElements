import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton ,QDialogButtonBox,QVBoxLayout,QLabel,QMessageBox

class CustomDialog(QDialog,):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    # def button_clicked(self, s):
    #     print("click", s)

    #     #dlg = QDialog(self)
    #     # dlg= CustomDialog(self)
    #     # dlg.setWindowTitle("HELLO!")
    #     # if dlg.exec():
    #     #     print("Success!")
    #     # else:
    #     #     print("Cancel!")
    #     dlg = QMessageBox(self)
    #     dlg.setWindowTitle("I have a question!")
    #     dlg.setText("This is a simple dialog")
    #     dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    #     dlg.setIcon(QMessageBox.Question)
    #     button = dlg.exec()

    #     if button == QMessageBox.Yes:
    #         print("Yes!")
    #     else:
    #         print("No!")
        
    # def button_clicked(self, s):
    #     button = QMessageBox.question(
    #         self,
    #         "Question dialog",
    #         "The longer message",
    #     )

    #     if button == QMessageBox.StandardButton.Yes:
    #         print("Yes!")
    #     else:
    #         print("No!")

    def button_clicked(self, s):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()