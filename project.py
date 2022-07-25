import csv
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

file=pd.read_csv('medium_data.csv')

mean=statistics.mean
stdev=statistics.stdev
def randomsetofmean(counter):
    for i in range(0,counter):
        