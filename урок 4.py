import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(1, 50)
y = 1/x
mpl.plot(x,y)
mpl.show()


df = pd.DataFrame([['Яндекс (Москва)', 789, 123],
                   ['Яндекс (Казань)', 543, 342],
                   ['Яндекс (Екатеринбург)', 450, 567]],
                  columns = ['Office', 'Stuff', 'Number'])
print (df)
df_1 = df.query ('Number < 350 & Stuff > 700')
print (df_1)
