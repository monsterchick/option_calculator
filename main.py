import sys

import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,QLabel


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # initializing information or setting
        self.setWindowTitle('Commission Calculator')
        self.setGeometry(100, 100, 500, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        lbl_strike_price = QLabel('strike price:')
        inp_strike_price = QLineEdit()
        inp_strike_price.setContentsMargins(0,20,270,20)

        lbl_quantity = QLabel('quantity:')
        inp_quantity = QLineEdit()
        inp_quantity.setContentsMargins(0,20,270,20)

        lbl_price = QLabel('price:')
        self.inp_price = QLineEdit()
        self.inp_price.setContentsMargins(0,20,270,20)

        btn_check = QPushButton('check')
        btn_check.clicked.connect(self.on_button_click)

        # set position
        layout.addWidget(lbl_strike_price,0,0)
        layout.addWidget(inp_strike_price,0,1)
        layout.addWidget(lbl_quantity,1,0)
        layout.addWidget(inp_quantity,1,1)
        layout.addWidget(lbl_price,2,0)
        layout.addWidget(self.inp_price,2,1)
        layout.addWidget(btn_check,3,0)

    def on_button_click(self):
        self.inp_price.setText('100')
    # layout.addWidget(inp_box1,1,0)
    # layout.addWidget(inp_box2,2,0)
    # layout.addWidget(inp_box3,3,0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())  # close the window after pressing 'close' button
