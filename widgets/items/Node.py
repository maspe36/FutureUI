from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget

RED = 255
GREEN = 200
BLUE = 61
ALPHA = 200

THICKNESS = 20
ANGLE = 180
ROTATION = 0
OFFSET = 0
COLOR = QColor(RED, GREEN, BLUE, ALPHA)


class Node(QWidget):
    def __init__(self, arcs=None, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.arcs = arcs

        if arcs is None:
            self.arcs = []

    def paintEvent(self, QPaintEvent):
        """
        Draw all arc primitives
        """

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for arc in self.arcs:
            pen = QPen(QBrush(arc.color), arc.thickness)
            painter.setPen(pen)

            boundingBox, startAngle, spanAngle = arc.getDrawingVariables(self)
            painter.drawArc(boundingBox, startAngle, spanAngle)

    def drawArcAndSelfCenter(self, boundingBox, painter):
        painter.setPen(QPen(QBrush(Qt.blue), 1))
        painter.drawPoint(boundingBox.center().x(), boundingBox.center().y())
        painter.setPen(QPen(QBrush(Qt.red), 1))
        painter.drawPoint(self.rect().center().x(), self.rect().center().y())

    def drawArcBoundingBoxMinMax(self, boundingBox, painter):
        painter.setPen(QPen(QBrush(Qt.black), 1))
        painter.drawPoint(boundingBox.x(), boundingBox.y())
        painter.setPen(QPen(QBrush(Qt.black), 1))
        painter.drawPoint(self.parent.rect().width() - boundingBox.x(), self.parent.rect().height() - boundingBox.y())