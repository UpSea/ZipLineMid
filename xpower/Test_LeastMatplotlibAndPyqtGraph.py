# -*- coding: utf-8 -*-
import sys,os
xpower = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) # mid path of current file's parent folder
xpower = os.path.abspath(os.path.join(os.path.dirname(__file__),"pyqtgraph-0.9.10"))
sys.path.append(xpower) 

from PyQt4 import QtCore, QtGui
import numpy as np
import pyqtgraph as pg
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes01 = fig.add_subplot(211)
        self.axes02 = fig.add_subplot(212)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
    def compute_initial_figure(self):
        self.axes01.plot([1,2,3,4])
class MyPyqtGraphPlot(pg.PlotWidget):
    def __init__(self):
        super(MyPyqtGraphPlot, self).__init__()
        ## Test large numbers
        curve = self.plot(np.random.normal(size=100)*1e0, clickable=True)
        curve.curve.setClickable(True)
        curve.setPen('w')  ## white pen
        curve.setShadowPen(pg.mkPen((70,70,30), width=6, cosmetic=True))        
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('pyqtgraph example: PlotWidget')
        self.resize(800,800)
        centerwidget = QtGui.QWidget()
        self.setCentralWidget(centerwidget)
        layout = QtGui.QVBoxLayout()
        centerwidget.setLayout(layout)
        
        mplWidget = MyMplCanvas(width=5, height=4, dpi=100)
        layout.addWidget(mplWidget)    
        
        pyqtWidget = MyPyqtGraphPlot()
        layout.addWidget(pyqtWidget)
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    
    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())