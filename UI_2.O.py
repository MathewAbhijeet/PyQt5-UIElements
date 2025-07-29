import sys
import time
import serial
import serial.tools.list_ports

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QLineEdit, QGroupBox, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer

class JogApp(QWidget):
    STEP = 10  # mm per click

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple G-code Jogger (PyQt5)")

        self.xpos = 0
        self.ser = None

        layout = QVBoxLayout(self)
        # Connection Group
        conn_group = QGroupBox("Connection")
        conn_layout = QHBoxLayout()
        conn_group.setLayout(conn_layout)
        layout.addWidget(conn_group)

        conn_layout.addWidget(QLabel("COM port"))
        self.port_combo = QComboBox()
        self.populate_ports()
        conn_layout.addWidget(self.port_combo)

        conn_layout.addWidget(QLabel("Baud rate"))
        self.baud_edit = QLineEdit("115200")
        self.baud_edit.setFixedWidth(70)
        conn_layout.addWidget(self.baud_edit)

        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.toggle_connection)
        conn_layout.addWidget(self.connect_btn)

        # Jogging Group
        jog_group = QGroupBox("Jog X-axis")
        jog_layout = QVBoxLayout()
        jog_group.setLayout(jog_layout)
        layout.addWidget(jog_group)

        self.pos_lbl = QLabel(f"X = {self.xpos} mm")
        self.pos_lbl.setAlignment(Qt.AlignCenter)
        jog_layout.addWidget(self.pos_lbl)

        btn_row = QHBoxLayout()
        self.btn_minus = QPushButton("X-")
        self.btn_minus.clicked.connect(self.step_minus)
        btn_row.addWidget(self.btn_minus)

        self.btn_home = QPushButton("X home")
        self.btn_home.clicked.connect(self.home_axis)
        btn_row.addWidget(self.btn_home)

        self.btn_plus = QPushButton("X+")
        self.btn_plus.clicked.connect(self.step_plus)
        btn_row.addWidget(self.btn_plus)

        jog_layout.addLayout(btn_row)

        # Buttons disabled until connected
        for b in [self.btn_minus, self.btn_home, self.btn_plus]:
            b.setEnabled(False)

        # Proper cleanup on window close
        self.destroyed.connect(self.close_port)

    def populate_ports(self):
        ports = [p.device for p in serial.tools.list_ports.comports()] or ["COM1"]
        self.port_combo.clear()
        self.port_combo.addItems(ports)

    def toggle_connection(self):
        if self.ser and self.ser.is_open:
            self.close_port()
            self.connect_btn.setText("Connect")
            for b in [self.btn_minus, self.btn_home, self.btn_plus]:
                b.setEnabled(False)
            return
        # Connect
        try:
            port = self.port_combo.currentText()
            baud = int(self.baud_edit.text())
            self.ser = serial.Serial(port, baud, timeout=1, dsrdtr=True)
            time.sleep(2)  # Let board settle
        except Exception as e:
            QMessageBox.critical(self, "Serial error", str(e))
            return
        self.connect_btn.setText("Disconnect")
        for b in [self.btn_minus, self.btn_home, self.btn_plus]:
            b.setEnabled(True)

    def close_port(self):
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()
        except Exception:
            pass

    def send_gcode(self, cmd):
        try:
            self.ser.write((cmd + "\n").encode())
            self.ser.flush()
        except Exception:
            QMessageBox.critical(self, "Serial error", "Lost connection.")
            self.toggle_connection()

    def update_pos_label(self):
        self.pos_lbl.setText(f"X = {self.xpos} mm")

    def step_plus(self):
        self.xpos += self.STEP
        self.send_gcode(f"G0 X{self.xpos}")
        self.update_pos_label()

    def step_minus(self):
        self.xpos -= self.STEP
        self.send_gcode(f"G0 X{self.xpos}")
        self.update_pos_label()

    def home_axis(self):
        self.xpos = 0
        self.send_gcode("G28 X")
        self.update_pos_label()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = JogApp()
    w.show()
    sys.exit(app.exec_())
