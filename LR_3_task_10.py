import datetime
import json
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn import covariance, cluster

from matplotlib.finance import qoutes_historical_yahoo_ochl as qoutes_yahoo