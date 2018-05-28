from random import randint

from PyQt5.QtCore import QRectF, QPropertyAnimation, Qt
from PyQt5.QtGui import QColor, QPen, QBrush, QPainter

from widgets.graphics.QGraphicsArcItem import QGraphicsArcItem

ANIMATION_ITERATIONS = -1

RED = 255
GREEN = 220
BLUE = 61
ALPHA = 200

THICKNESS = 5
ANGLE = 170
ROTATION = 0
OFFSET = 0
DIAMETER = 200
COLOR = QColor(RED, GREEN, BLUE, ALPHA)


class Arc(QGraphicsArcItem):
    def __init__(self, parent=None, angle=ANGLE, thickness=THICKNESS, rotation=ROTATION, offset=OFFSET, diameter=DIAMETER, circleDuration=None, expandDuration=None, shrinkDuration=None, color=COLOR):
        super().__init__()
        self.parent = parent
        self.angle = angle
        self.thickness = thickness
        self.rotation = rotation
        self.offset = offset
        self.diameter = diameter - offset
        self.radius = round(self.diameter / 2)

        if not circleDuration:
            circleDuration = randint(1000, 3000)

        if not expandDuration:
            expandDuration = randint(1000, 3000)

        if not shrinkDuration:
            shrinkDuration = randint(1000, 3000)

        self.circleDuration = circleDuration
        self.expandDuration = expandDuration
        self.shrinkDuration = shrinkDuration
        self.color = color

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        pen = QPen(QBrush(self.color), self.thickness)
        pen.setCapStyle(Qt.FlatCap)

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(pen)
        painter.drawArc(self.drawingRect, self.startAngle, self.spanAngle)

    def runAnimations(self):
        self.runCircleAnimation()
        self.runLengthAnimation()

    def runCircleAnimation(self):
        end = 360 * 16 + self.startAngle
        self.circleAnimation = self.createAnimation(property=b"startAngle", start=self.startAngle, end=end)

        self.circleAnimation.setDuration(self.circleDuration)
        self.circleAnimation.setLoopCount(ANIMATION_ITERATIONS)

        self.circleAnimation.start()
        self.circleAnimation.valueChanged.connect(self.update)

    def runLengthAnimation(self):
        self.extendingAnimation = self.createAnimation(property=b"spanAngle", start=self.spanAngle, end=self.spanAngle * 2)
        self.shrinkingAnimation = self.createAnimation(property=b"spanAngle", start=self.spanAngle * 2, end=self.spanAngle)

        self.extendingAnimation.setDuration(self.expandDuration)
        self.shrinkingAnimation.setDuration(self.shrinkDuration)

        self.extendingAnimation.start()
        self.extendingAnimation.finished.connect(self.shrinkingAnimation.start)
        self.shrinkingAnimation.finished.connect(self.extendingAnimation.start)

        self.extendingAnimation.valueChanged.connect(self.update)
        self.shrinkingAnimation.valueChanged.connect(self.update)

    def createAnimation(self, property, start, end):
        animation = QPropertyAnimation(self, property)
        animation.setStartValue(start)
        animation.setEndValue(end)

        return animation

    def updateGeometry(self):
        self.updateAngles()
        self.drawingRect = self.calculateDrawingRect()
        self.renderRect = self.calculateRenderRect()

    def updateAngles(self):
        self.startAngle = self.calculateStartAngle()
        self.spanAngle = self.calculateSpanAngle()

    def calculateStartAngle(self):
        return (90 * 16) + (self.rotation * 16)

    def calculateSpanAngle(self):
        return -self.angle * 16

    def calculateDrawingRect(self):
        """
        Calculate the size of the rect we will use to draw the arc
        """

        # X and Y are top left
        x = self.parent.rect().center().x() - self.radius
        y = self.parent.rect().center().y() - self.radius

        # Size from the X and Y origin in the top left
        width = self.diameter
        height = self.diameter

        boundingBox = QRectF()
        boundingBox.setX(x)
        boundingBox.setY(y)
        boundingBox.setWidth(width)
        boundingBox.setHeight(height)

        return boundingBox

    def calculateRenderRect(self):
        """
        Calculate the size of the QGraphicsItem itself
        """

        rect = self.calculateDrawingRect()

        rect.setX(rect.x() - self.thickness)
        rect.setY(rect.y() - self.thickness)
        rect.setWidth(rect.width() + self.thickness)
        rect.setHeight(rect.height() + self.thickness)

        return rect
