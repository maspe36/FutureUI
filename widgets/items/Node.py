from PyQt5.QtCore import QSize, pyqtSignal, Qt
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from widgets.primitives.Arc import Arc


class Node(QGraphicsView):
    clicked = pyqtSignal()

    def __init__(self, arcs=None, parent=None):
        super().__init__(parent)

        if arcs is None:
            arcs = self.defaultArcs()

        self.parent = parent
        self.arcs = []

        self.largestArc = None

        self.setScene(QGraphicsScene(parent))
        self.addArcs(arcs)

    def defaultArcs(self):
        return [Arc(thickness=30),
                Arc(angle=45, offset=26, color=Qt.red),
                Arc(angle=60, offset=16, color=Qt.cyan),
                Arc(angle=80, offset=6, color=Qt.magenta),
                Arc(angle=100, offset=-4, color=Qt.black),
                Arc(angle=45, offset=-14, color=Qt.green),
                Arc(angle=45, offset=-24, color=Qt.blue)]

    def mousePressEvent(self, QMouseEvent):
        super().mousePressEvent(QMouseEvent)
        self.clicked.emit()

    def addArc(self, arc):
        if not arc.parent:
            arc.parent = self

        arc.updateGeometry()
        self.updateLargestArc(arc)

        self.arcs.append(arc)
        self.scene().addItem(arc)
        arc.runAnimations()

    def updateLargestArc(self, arc):
        if not self.largestArc:
            self.largestArc = arc

        if arc.diameter + arc.thickness > self.largestArc.diameter + self.largestArc.thickness:
            self.largestArc = arc

        self.updateMinimumSize()

    def updateMinimumSize(self):
        self.setMinimumSize(self.sizeHint())

    def addArcs(self, arcs):
        for arc in arcs:
            self.addArc(arc)

    def sizeHint(self):
        sideLength = self.largestArc.diameter + (self.largestArc.thickness + self.largestArc.offset) * 3
        return QSize(sideLength, sideLength)
