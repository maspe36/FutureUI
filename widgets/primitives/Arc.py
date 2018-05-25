from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QPen, QBrush

from widgets.graphics.QGraphicsArcItem import QGraphicsArcItem

RED = 255
GREEN = 200
BLUE = 61
ALPHA = 200

THICKNESS = 5
ANGLE = 180
ROTATION = 0
OFFSET = 0
DIAMETER = 200
COLOR = QColor(RED, GREEN, BLUE, ALPHA)


class Arc(QGraphicsArcItem):
    def __init__(self, parent, angle=ANGLE, thickness=THICKNESS, rotation=ROTATION, offset=OFFSET, diameter=DIAMETER, color=COLOR):
        super().__init__()
        self.parent = parent
        self.angle = angle
        self.thickness = thickness
        self.rotation = rotation
        self.offset = offset
        self.diameter = diameter - offset
        self.radius = round(self.diameter / 2)
        self.color = color

        self.updateGeometry()

    def updateGeometry(self):
        self.setStartAngle(self.calculateStartAngle())
        self.setSpanAngle(self.calculateSpanAngle())
        self.setRect(self.calculateRect())

    def calculateStartAngle(self):
        return (90 * 16) + (self.rotation * 16)

    def calculateSpanAngle(self):
        return -self.angle * 16

    def calculateRect(self):
        # X and Y are top left
        x = self.parent.rect().center().x() - self.radius + self.thickness
        y = self.parent.rect().center().y() - self.radius + self.thickness

        # Size from the X and Y origin in the top left
        width = self.diameter - self.thickness
        height = self.diameter - self.thickness

        boundingBox = QRectF()
        boundingBox.setX(x)
        boundingBox.setY(y)
        boundingBox.setWidth(width)
        boundingBox.setHeight(height)

        return boundingBox

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.setPen(QPen(QBrush(self.color), self.thickness))
        QPainter.drawArc(self.rect(), self.startAngle(), self.spanAngle())
