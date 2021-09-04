import pandas as pd
import csv 
import statistics
import plotly.figure_factory as ff

df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\data11.csv")
Brand1=df["Avg Rating"]

x=statistics.mean(Brand1)
print(x)
y=statistics.median(Brand1)
print(y)
z=statistics.mode(Brand1)
print(z)


fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()