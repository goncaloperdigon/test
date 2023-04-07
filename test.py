
import dash
from dash import dcc
from dash import html
import pandas as pd
import base64
import datetime as dt
import plotly.express as px
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go

data = pd.read_csv('Austin_Animal_Center_Intakes.csv', index_col=0, na_values=r'\N')

condition = data['Intake Condition']
type = data['Intake Type']
breed = data['Breed']
foundIn = data['Found Location']
age= data['Age upon Intake']



#FrontEnd

site = dash.Dash(__name__, assets_folder='front')