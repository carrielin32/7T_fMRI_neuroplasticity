
import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np 

df=pd.read_csv('/Users/carrielin/Downloads/session1_transform.csv')

df=df.fillna('0')

df=df.to_csv('/Users/carrielin/Downloads/session1_transform.csv')

