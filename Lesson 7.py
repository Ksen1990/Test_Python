import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Гистограмма №1
# data = np.random.randint(1, 50, size=(1, 5))
# df = pd.DataFrame(data, columns= ['A', 'B', 'C', 'D', 'E'])
# print (df)
# df.plot.bar(color = 'black')
# plt.show()

# Гистограмма №2
x = ['A', 'B', 'C', 'D', 'E']
y = [10,15,5,20,8]
sns.barplot(x=x,y=y, color = 'black')
plt.show()

#Ломанная линия
data =pd.Series(np.random.randn(10).cumsum(), index = np.arange (0,100,10))
data.plot(color = 'green', alpha  = 0.9, linestyle='--')
plt.title('Ломанная линия')
plt.show()
