import numpy as np
import random
import sys, os
import pandas as pd
save_dir = sys.argv[1]
save_name = '2_ordering.csv'
order_list = ["S", "S", "O", "O" ]
np.random.shuffle(order_list)
data = pd.DataFrame(order_list, index=[1,2,3,4])
save_as = '../subjects/'+save_dir+'/matrix/'+save_name
data.to_csv(save_as)

print('This file is :', save_as)
print(pd.read_csv(save_as))
