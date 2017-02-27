import os
import matplotlib
import matplotlib.pyplot as plt  
import pandas as pd

curdir=os.path.dirname(os.path.realpath(__file__))
#print(curdir)

test_name=input('input the testname you are going on :') or 'present'
test_number=input('input the times now:') or '1'
current_file=test_name+test_number+'.txt'
full_current_file=os.path.join(curdir,current_file)
#print(full_current_file)



present = pd.read_table(full_current_file, sep=' ')
present_year = present.set_index('year')
present_year['boys'].plot()
plt.show()
