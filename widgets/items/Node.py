from random import randint

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

class Node(QGraphicsView):
    def __init__(self, arcs=None, parent=None):
        super().__init__(parent)

        if arcs is None:
            arcs = []

        self.parent = parent
        self.arcs = []

        self.largestArc = None

        self.addArcs(arcs)
        self.setScene(QGraphicsScene(parent))

    def mousePressEvent(self, QMouseEvent):
        super().mousePressEvent(QMouseEvent)

        for arc in self.arcs:
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)

            arc.color = QColor(red, green, blue)

    def addArc(self, arc):
        if not arc.parent:
            arc.parent = self

        arc.updateGeometry()
        self.updateLargestArc(arc)

        self.arcs.append(arc)
        self.scene().addItem(arc)
        arc.runAnimation()

    def updateLargestArc(self, arc):
        if not self.largestArc:
            self.largestArc = arc
        if arc.diameter + arc.thickness > self.largestArc.diameter + self.largestArc.thickness:
            self.largestArc = arc

    def addArcs(self, arcs):
        for arc in arcs:
            self.addArc(arc)

    def sizeHint(self):
        height = self.largestArc.diameter + (self.largestArc.thickness + self.largestArc.offset) * 3
        width = self.largestArc.diameter + (self.largestArc.thickness + self.largestArc.offset) * 3
        return QSize(height, width)
