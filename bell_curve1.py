import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv('mobile_brands.csv')
fig = ff.create_distplot([df["Avg Rating"].tolist()],["AVERAGE RATINGS"],show_hist=False)
fig.show()