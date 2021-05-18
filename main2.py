import csv
import plotly.express as px

with open('sleep.csv') as tv:
     data = csv.DictReader(tv)
     show1 = px.scatter(data, x='Coffee in ml', y='sleep in hours', title="Sleep")
show1.show()