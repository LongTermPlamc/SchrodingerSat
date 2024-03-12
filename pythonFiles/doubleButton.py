import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class ToggleButtonsExample(QWidget):
    def __init__(self):
        super().__init__()

        self.active_button = None  # Variable to track the active button
        self.init_ui()

    def init_ui(self):
        # Buttons
        self.button1 = QPushButton('Button 1', self)
        self.button1.clicked.connect(lambda: self.toggle_buttons(self.button1))

        self.button2 = QPushButton('Button 2', self)
        self.button2.clicked.connect(lambda: self.toggle_buttons(self.button2))

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Window settings
        self.setWindowTitle('Toggle Buttons Example')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def toggle_buttons(self, clicked_button):
        # Toggle the state of buttons
        if self.active_button is not None:
            self.active_button.setEnabled(True)

        self.active_button = clicked_button
        self.active_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToggleButtonsExample()
    sys.exit(app.exec_())
