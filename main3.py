import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
     coffee = []
     sleep = []
     with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
               coffee.append(float(row["Coffee in ml"]))
               sleep.append(float(row["sleep in hours"]))
     return {"x": coffee, "y": sleep}

def findCorrelation(dataSource):
     correlation = np.corrcoef(dataSource["x"],dataSource["y"])
     print('Coffee vs Sleep: \n',correlation[0,1])

def setup():
     data_path = 'sleep.csv'
     dataSource = getDataSource(data_path)
     findCorrelation(dataSource)

setup()