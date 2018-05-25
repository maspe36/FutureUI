from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor

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

class Arc(object):
    def __init__(self, angle=ANGLE, thickness=THICKNESS, rotation=ROTATION, offset=OFFSET, diameter=DIAMETER, color=COLOR):
        self.angle = angle
        self.thickness = thickness
        self.rotation = rotation
        self.offset = offset
        self.diameter = diameter - offset
        self.radius = round(self.diameter / 2)
        self.color = color

    def getDrawingVariables(self, origin):
        startAngle = (90 * 16) + (self.rotation * 16)
        spanAngle = -self.angle * 16

        # X and Y are top left
        x = origin.rect().center().x() - self.radius + self.thickness
        y = origin.rect().center().y() - self.radius + self.thickness

        # Size from the X and Y origin in the top left
        width = self.diameter - self.thickness
        height = self.diameter - self.thickness

        drawingRect = QRect()
        drawingRect.setX(x)
        drawingRect.setY(y)
        drawingRect.setWidth(width)
        drawingRect.setHeight(height)

        return drawingRect, startAngle, spanAngle