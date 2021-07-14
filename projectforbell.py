import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv('mobile.csv')
fig = pf.create_distplot([df["Avg Rating"].tolist()],["Rating"],show_hist=False)
fig.show()