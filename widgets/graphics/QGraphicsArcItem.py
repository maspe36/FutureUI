from PyQt5.QtCore import pyqtProperty, QRectF
from PyQt5.QtWidgets import QGraphicsObject


class QGraphicsArcItem(QGraphicsObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._drawingRect = QRectF()
        self._renderRect = QRectF
        self._startAngle = 0
        self._spanAngle = 0

    def boundingRect(self):
        return self._renderRect

    @pyqtProperty(QRectF)
    def drawingRect(self):
        return self._drawingRect

    @drawingRect.setter
    def drawingRect(self, value):
        self._drawingRect = value

    @pyqtProperty(QRectF)
    def renderRect(self):
        return self._renderRect

    @renderRect.setter
    def renderRect(self, value):
        self._renderRect = value

    @pyqtProperty(float)
    def startAngle(self):
        return self._startAngle

    @startAngle.setter
    def startAngle(self, value):
        self._startAngle = value

    @pyqtProperty(float)
    def spanAngle(self):
        return self._spanAngle

    @spanAngle.setter
    def spanAngle(self, value):
        self._spanAngle = value
