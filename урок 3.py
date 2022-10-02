import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

data  = {'Количество кликов' : [100, 135, 220, 300],
         'Количество показов' : [678, 1100, 2450, 2730],
         'CTR, %' : [14.74926254, 12.27272727, 8.979591837, 10.98901099]}

frame = pd.DataFrame (data)
print (frame.get ('CTR, %'))

x = data ['Количество кликов']
y = data ['Количество показов']


mpl.plot(x,y)
mpl.show()



            
