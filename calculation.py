import pandas as pd
import csv
import plotly.express as px
import statistics

df=pd.read_csv("data.csv")
student_df=df.loc[df["student_id"]=="TRL_abc"]
mean=statistics.mean(student_df.groupby("level")["attempt"])
print()
fig=px.scatter(mean,x=["attempt1"],y=["level1","level2","level3","level4"])


fig.show()