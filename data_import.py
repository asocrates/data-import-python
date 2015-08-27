

import numpy as np
import pylab
from StringIO import StringIO
import sys
from pylab import *



def data_in(file):

    return np.genfromtxt(file , delimiter = '\t', dtype = None, invalid_raise = False)
