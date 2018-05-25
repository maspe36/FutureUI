import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow

from primitives.Arc import Arc
from widgets.items.Node import Node

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    view = QMainWindow()

    arcs = [Arc(color=Qt.black), Arc(rotation=180, offset=10, color=Qt.red), Arc(angle=45, offset=-10)]
    node = Node(parent=view, arcs=arcs)

    view.setFixedSize(QSize(1000,1000))
    view.setCentralWidget(node)
    view.show()

    sys.exit(app.exec_())
