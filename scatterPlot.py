import pandas as pd
import plotly.express as px

df = pd.read_csv("scatter_plot.csv")
fig = px.scatter(df, x="Date", y="Cases",color="Country")
fig.show()
