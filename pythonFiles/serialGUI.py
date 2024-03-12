import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort

class SerialPortExplorer(QWidget):
    def __init__(self):
        super().__init__()

        self.serial = QSerialPort()

        self.init_ui()

    def init_ui(self):
        # Widgets
        self.port_label = QLabel('Serial Port:')
        self.port_combobox = QComboBox(self)
        self.populate_serial_ports()

        self.baud_label = QLabel('Baud Rate:')
        self.baud_edit = QLineEdit(self)
        self.baud_edit.setText('9600')  # Default baud rate

        self.connect_button = QPushButton('Connect', self)
        self.connect_button.clicked.connect(self.connect_to_serial)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_combobox)
        layout.addWidget(self.baud_label)
        layout.addWidget(self.baud_edit)
        layout.addWidget(self.connect_button)

        # Window settings
        self.setWindowTitle('Serial Port Explorer')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def populate_serial_ports(self):
        ports = [info.portName() for info in QSerialPortInfo.availablePorts()]
        self.port_combobox.addItems(ports)

    def connect_to_serial(self):
        port_name = self.port_combobox.currentText()
        baud_rate = int(self.baud_edit.text())

        if self.serial.isOpen():
            self.serial.close()
            self.connect_button.setText('Connect')
        else:
            self.serial.setPortName(port_name)
            self.serial.setBaudRate(baud_rate)
            
            if self.serial.open(QSerialPort.ReadWrite):
                self.connect_button.setText('Disconnect')
                print(f"Connected to {port_name} at {baud_rate} baud.")
            else:
                print(f"Failed to connect to {port_name} at {baud_rate} baud.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SerialPortExplorer()
    sys.exit(app.exec_())