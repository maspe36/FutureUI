from PyQt5.QtWidgets import QGraphicsEllipseItem


class QGraphicsArcItem(QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.setPen(self.pen())
        QPainter.setBrush(self.brush())
        QPainter.drawArc(self.rect(), self.startAngle(), self.spanAngle())
