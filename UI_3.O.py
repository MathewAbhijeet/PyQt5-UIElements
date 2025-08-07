import sys
import time
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, 
    QComboBox, QHBoxLayout, QLineEdit, QGroupBox, QMessageBox
)
from PyQt5.QtCore import Qt

class SimpleCOMApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple COM Port Connection")
        self.ser = None

        # Main layout
        layout = QVBoxLayout(self)

        # Connection Group
        conn_group = QGroupBox("Connection")
        conn_layout = QHBoxLayout()
        conn_group.setLayout(conn_layout)
        layout.addWidget(conn_group)

        # COM Port selection
        conn_layout.addWidget(QLabel("COM port"))
        self.port_combo = QComboBox()
        self.populate_ports()
        conn_layout.addWidget(self.port_combo)

        # Baud rate input
        conn_layout.addWidget(QLabel("Baud rate"))
        self.baud_edit = QLineEdit("115200")
        self.baud_edit.setFixedWidth(70)
        conn_layout.addWidget(self.baud_edit)

        # Connect button
        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.toggle_connection)
        conn_layout.addWidget(self.connect_btn)

        # Connection status label
        self.status_label = QLabel("Not connected")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Proper cleanup on window close
        self.destroyed.connect(self.close_port)

    def populate_ports(self):
        """Populate the COM port dropdown with available ports"""
        ports = [p.device for p in serial.tools.list_ports.comports()] or ["COM1"]
        self.port_combo.clear()
        self.port_combo.addItems(ports)

    def toggle_connection(self):
        """Handle connect/disconnect button click"""
        if self.ser and self.ser.is_open:
            # Disconnect
            self.close_port()
            self.connect_btn.setText("Connect")
            self.status_label.setText("Not connected")
            return

        # Connect
        try:
            port = self.port_combo.currentText()
            baud = int(self.baud_edit.text())
            self.ser = serial.Serial(port, baud, timeout=1, dsrdtr=True)
            time.sleep(2)  # Let board settle

            self.connect_btn.setText("Disconnect")
            self.status_label.setText(f"Connected to {port} at {baud} baud")

        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter a valid baud rate (number)")
        except Exception as e:
            QMessageBox.critical(self, "Serial Error", str(e))

    def close_port(self):
        """Close the serial port connection"""
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()
        except Exception:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleCOMApp()
    window.show()
    sys.exit(app.exec_())
