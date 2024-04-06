# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:08:03 2024

@author: SWRM
"""

from dash import Dash, html,dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from src.components.data_ingestion import DataIngestion

app=Dash(__name__,external_stylesheets=[dbc.themes.LITERA])


data_ingestor_obj=DataIngestion()
data=data_ingestor_obj.DataIngestor()


#variables for our layout
card_one=(((data["Assistance"]=="Yes").sum())/(data["Assistance"].count())) *100
card_two=(((data["Membership"]=="Yes").sum())/(data["Membership"].count())) *100

#graphs
#most serviced car fig
fig1=px.histogram(data,x=data["Model"],barmode="group",histfunc="count")

#churn rate fig
fig2=px.histogram(data,x=data["Churn"],barmode="group",histfunc="count")

#most serviced segment fig
fig3=px.histogram(data,x=data["Segment"],barmode="group",histfunc="count")

#most serviced age group
fig4=px.histogram(data,x=data["Customer_age_group"],barmode="group",histfunc="count")

#price levels for members
data_members=data[data["Membership"]=="Yes"]
fig5=px.histogram(data_members,x=data_members["Servicing-Price"],barmode="group",histfunc="count")

#price levels for non members
data_non_members=data[data["Membership"]=="No"]
fig6=px.histogram(data_non_members,x=data_non_members["Servicing-Price"],barmode="group",histfunc="count")

#churn rate based on gender
data_churned=data[data["Churn"]=="Yes"]
fig7=px.histogram(data_churned,x=data_churned["Gender"],barmode="group",histfunc="count")

#gender ration based on membership
fig8=px.histogram(data_members,x=data_members["Gender"],barmode="group",histfunc="count")






app.layout=dbc.Container([
    
    dbc.Row(html.H1('Car servicing report dashboard', className="text-center")),
    html.Hr(),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.Card(
            
            dbc.CardBody(f"Assisted to unassisted percentage {card_one}", className="text-center"), color="success"
            ),width=6),
        
        dbc.Col(dbc.Card(
            
            dbc.CardBody(f"Members to non members percentage {card_two}", className="text-center"), color="success"
            ),width=6)
        
        
        
        
        
        
        ]),
    
    dbc.Row([
        dbc.Col([
            html.H1("Car model serviced graph", className="text-center"),
            dcc.Graph(id="most_serviced_model",figure=fig1)
            
            ],width=3),
        
        dbc.Col([
            html.H1("Churn counts", className="text-center"),
            dcc.Graph(id="churn",figure=fig2)
            
            ],width=3),
        
        dbc.Col([
            html.H1("Car segment serviced coutns", className="text-center"),
            dcc.Graph(id="most_serviced_segment",figure=fig3)
            
            ],width=3),
        dbc.Col([
            html.H1("Customer age group counts", className="text-center"),
            dcc.Graph(id="most_serviced_age_group",figure=fig4)
            
            ],width=3)
       
       
       ]),
    html.Hr(),
    html.Br(),
    
    
    dbc.Row([
        
        dbc.Col([
            html.H1("Prices applied to members", className="text-center"),
            dcc.Graph(id="price_for_members",figure=fig5)
            
            ],width=3),
        
        dbc.Col([
            html.H1("Price applied to non members", className="text-center"),
            dcc.Graph(id="price_for_members",figure=fig6)
            
            ],width=3),
        
        dbc.Col([
            html.H1("Churn rate based on gender", className="text-center"),
            dcc.Graph(id="gender_churned",figure=fig7)
            
            ],width=3),
        
        dbc.Col([
            html.H1("Membership gender distribution", className="text-center"),
            dcc.Graph(id="membership_gender",figure=fig8)
            
            ],width=3),
        
        
        
        
        ])
    
    ])

'''
def visualizes():
    return(
        fig1,
        fig2,
        fig3,
        fig4,
        fig5,
        fig6,
        fig7,
        fig8
        )
'''

if __name__=='__main__':
    app.run(debug=True)
    
                                       