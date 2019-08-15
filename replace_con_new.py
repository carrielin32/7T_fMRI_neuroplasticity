import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np 

#parsed=pd.read_csv('/Users/carrielin/Desktop/exp_Visual_Audi/log_file_auditory/session1.csv')

parsed=pd.read_csv('/Users/carrielin/Desktop/V8678_log/log1.csv')



#replace numbers to 0 
replace_values = {'1':0, '2':0, '11':0, '49':0,'66':0, '67':0}
parsed = parsed.replace({"con":replace_values})
parsed = parsed[parsed['con']!=0]


# 3k left
parsed['con_new']=parsed['con'].replace('long, 3k, L','3kL')
parsed['con_new']=parsed['con_new'].replace('short, 3k, L','3kL')

# 3k right
parsed['con_new']=parsed['con_new'].replace('long, 3k, R','3kR')
parsed['con_new']=parsed['con_new'].replace('short, 3k, R','3kR')

# 1k left
parsed['con_new']=parsed['con_new'].replace('long, 1k, L','1kL')
parsed['con_new']=parsed['con_new'].replace('short, 1k, L','1kL')

# 1k right
parsed['con_new']=parsed['con_new'].replace('long, 1k, R','1kR')
parsed['con_new']=parsed['con_new'].replace('short, 1k, R','1kR')

# 8k left
parsed['con_new']=parsed['con_new'].replace('long, 8k, L','8kL')
parsed['con_new']=parsed['con_new'].replace('short, 8k, L','8kL')

# 8k right
parsed['con_new']=parsed['con_new'].replace('long, 8k, R','8kR')
parsed['con_new']=parsed['con_new'].replace('short, 8k, R','8kR')

parsed.to_csv('/Users/carrielin/Desktop/exp_Visual_Audi/log_file_auditory/session1_new_0308.csv')


# same for session2
