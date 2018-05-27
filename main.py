import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from widgets.primitives.Arc import Arc
from widgets.items.Node import Node

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main = QMainWindow()

    arcs = [Arc(thickness=30),
            Arc(angle=45, offset=26, color=Qt.red),
            Arc(angle=60, offset=16, color=Qt.cyan),
            Arc(angle=80, offset=6, color=Qt.magenta),
            Arc(angle=100, offset=-4, color=Qt.black),
            Arc(angle=45, offset=-14, color=Qt.green),
            Arc(angle=45, offset=-24, color=Qt.blue)]

    node = Node()
    node.addArcs(arcs)

    main.setCentralWidget(node)
    main.show()

    sys.exit(app.exec_())
