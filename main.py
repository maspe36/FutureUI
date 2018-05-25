import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QGraphicsView

from widgets.primitives.Arc import Arc
from widgets.items.Node import Node

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main = QMainWindow()


    node = Node()
    view = QGraphicsView()

    arcs = [Arc(parent=node, color=Qt.black),
            Arc(parent=node, rotation=180, offset=10, color=Qt.red),
            Arc(parent=node, angle=45, offset=-10, color=Qt.blue)]

    node.addArcs(arcs)

    # main.setFixedSize(QSize(800, 480))
    main.setCentralWidget(node)
    main.show()

    sys.exit(app.exec_())
