import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np 

parsed=pd.read_csv('/Users/carrielin/Desktop/exp_Visual_Audi/log_file_auditory/session1.csv')

# 3k long
parsed['con_new']=parsed['con'].replace('long, 3k, L','3kL')
parsed['con_new']=parsed['con_new'].replace('long, 3k, R','3kL')

# 3k short 
parsed['con_new']=parsed['con_new'].replace('short, 3k, L','3kS')
parsed['con_new']=parsed['con_new'].replace('short, 3k, R','3kS')

# 1k long
parsed['con_new']=parsed['con_new'].replace('long, 1k, L','1kL')
parsed['con_new']=parsed['con_new'].replace('long, 1k, R','1kL')

# 1k short
parsed['con_new']=parsed['con_new'].replace('short, 1k, L','1kS')
parsed['con_new']=parsed['con_new'].replace('short, 1k, R','1kS')

# 8k long 
parsed['con_new']=parsed['con_new'].replace('long, 8k, L','8kL')
parsed['con_new']=parsed['con_new'].replace('long, 8k, R','8kL')

# 8k short
parsed['con_new']=parsed['con_new'].replace('short, 8k, L','8kS')
parsed['con_new']=parsed['con_new'].replace('short, 8k, R','8kS')

parsed.to_csv('/Users/carrielin/Desktop/exp_Visual_Audi/log_file_auditory/session1_new.csv')


# similar as session2