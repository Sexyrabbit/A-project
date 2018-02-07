import pandas as pd
import numpy as np


bins=np.arange(0,90,10)


print bins


'''
raw_data['Age_group'] = pd.cut(raw_data['Age'], bins)
raw_data.groupby('Age_group').size()

'''