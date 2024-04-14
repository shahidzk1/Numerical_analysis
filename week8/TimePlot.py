# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:48:54 2022

@author: abz1e14
"""

from pandas import read_excel
from matplotlib import pyplot
series = read_excel('ClayBricks.xls', sheetname='BRICKSQ', header=0,
              index_col=0, parse_dates=True, squeeze=True)
series.plot()
pyplot.show()