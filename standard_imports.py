import numpy as np
import pandas as pd
from IPython.display import display, HTML
from time import strftime, localtime

pd.set_option('max_colwidth', 0)
timenow = lambda: strftime('%Y%m%d_%H%M', localtime())
