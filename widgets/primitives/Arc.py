from PyQt5.QtCore import QRectF, QPropertyAnimation
from PyQt5.QtGui import QColor, QPen, QBrush, QPainter
from PyQt5.QtWidgets import QWidget

from widgets.graphics.QGraphicsArcItem import QGraphicsArcItem

ANIMATION_ITERATIONS = -1

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
    def __init__(self, parent=None, angle=ANGLE, thickness=THICKNESS, rotation=ROTATION, offset=OFFSET, diameter=DIAMETER, color=COLOR):
        super().__init__()
        self.parent = parent
        self.angle = angle
        self.thickness = thickness
        self.rotation = rotation
        self.offset = offset
        self.diameter = diameter - offset
        self.radius = round(self.diameter / 2)
        self.color = color

    def boundingRect(self):
        return self._rect

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QBrush(self.color), self.thickness))
        painter.drawArc(self.rect, self.startAngle, self.spanAngle)

    def runAnimation(self):
        self.animation = QPropertyAnimation(self, b"startAngle")

        self.animation.setDuration(1000)
        self.animation.setStartValue(self.startAngle)
        self.animation.setEndValue(360 * 16 + self.startAngle)
        self.animation.setLoopCount(ANIMATION_ITERATIONS)

        self.animation.start()

    def updateGeometry(self):
        self.updateAngles()
        self.rect = self.calculateRect()

    def updateAngles(self):
        self.startAngle = self.calculateStartAngle()
        self.spanAngle = self.calculateSpanAngle()

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
