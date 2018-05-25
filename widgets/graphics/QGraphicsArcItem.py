from PyQt5.QtCore import pyqtProperty, QRectF
from PyQt5.QtWidgets import QGraphicsObject


class QGraphicsArcItem(QGraphicsObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._rect = QRectF()
        self._startAngle = 0
        self._spanAngle = 0

    def boundingRect(self):
        return self._rect

    @pyqtProperty(QRectF)
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

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
