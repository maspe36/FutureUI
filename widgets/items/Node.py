from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

class Node(QGraphicsView):
    def __init__(self, arcs=None, parent=None):
        super().__init__(parent)

        if arcs is None:
            arcs = []

        self.parent = parent
        self.arcs = []

        self.addArcs(arcs)
        self.setScene(QGraphicsScene(parent))

    def addArc(self, arc):
        if not arc.parent:
            arc.parent = self

        arc.updateGeometry()
        self.arcs.append(arc)
        self.scene().addItem(arc)

    def addArcs(self, arcs):
        for arc in arcs:
            self.addArc(arc)
