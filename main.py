import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from widgets.items.Node import Node

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main = QMainWindow()
    layout = QHBoxLayout()

    layout.addWidget(Node())
    layout.addWidget(Node())

    widget = QWidget()
    widget.setLayout(layout)

    main.setCentralWidget(widget)
    main.show()

    sys.exit(app.exec_())
