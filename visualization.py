from PyQt5 import QtGui
import pyqtgraph as pg
import numpy as np

class Visualizer_2D:
    def __init__(self):
        self.app = pg.mkQApp()
        self.win = pg.ScatterPlotWidget()
        self.win.setFields([
            ('x_pos', {'units': 'm'}),
            ('x_dot', {'units': 'm/s'})
        ])
        self.pos_plot = self.win.addPlot()
        self.times = np.array([])
        self.states = np.array([])
        self.pos_plot.plot(self.times, self.states)
        self.inputs = np.array([])

    def update(self, time, state, inputs):
        self.times = [time]
        self.states = [state]
        self.pos_plot.setData(self.times, self.states)