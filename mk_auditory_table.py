
import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np 

df=pd.read_csv('/Users/carrielin/Downloads/session1_transform.csv')

df=df.fillna('0')

df=df.to_csv('/Users/carrielin/Downloads/session1_transform.csv')


# convert to array first

#df=np.array(df)

#df=np.savetxt('/Users/carrielin/Downloads/session1_final.txt')


#import csv
csv_file = input('/Users/carrielin/Downloads/session1_final.csv')
txt_file = input('/Users/carrielin/Downloads/session1_final.txt')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()