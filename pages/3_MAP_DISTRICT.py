import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from numerize.numerize import numerize
# import pandas as pd
# import dash
# # from dash import dcc, html, Input, Output, DataTable
from dash import dcc, html, Input, Output
from dash import dash_table
import plotly.express as px
from urllib.request import urlopen
import json

st.set_page_config(page_title='STATE-WISE TRANSACTION DATA ANALYSIS FOR PRODUCT-xPAY',
                   layout='wide',
                   initial_sidebar_state='expanded')
@st.cache_data
def get_data():
    df3 = pd.read_excel('data/map/DF3_MAPDATA_DISTRICT.xlsx')
    return df3


df3 = get_data()


header_left, header_mid, header_right = st.columns([1,3,1], gap='large')

with header_mid:
    st.title('TRANSACTION DATA ANALYSIS DISTRICT-WISE')

with st.sidebar:
    mapbystate_filter = st.multiselect(label='Filter User by State',
                                      options=df3['State'].unique(),
                                      default=df3['State'].unique())

    mapbyyear_filter = st.multiselect(label='Filter User by Year',
                                        options=df3['Year'].unique(),
                                        default=df3['Year'].unique())

    mapbyquarter_filter = st.multiselect(label='Filter User by Quarter',
                                       options=df3['Quater'].unique(),
                                       default=df3['Quater'].unique())

    mapbydistrict_filter = st.multiselect(label='Filter User by District',
                                         options=df3['District'].unique(),
                                         default=df3['District'].unique())



df3 = df3.query('State == @mapbystate_filter & Year == @mapbyyear_filter & Quater == @mapbyquarter_filter & District == @mapbydistrict_filter ')

mapbydistrict_count = float(df3['Count'].sum())

total1, total2, total3 = st.columns(3, gap='large')

with total1:
    st.image('images/ico1.png', use_column_width='Auto')
    st.metric(label='District', value=numerize(mapbydistrict_count))

Q1,Q2 = st.columns(2)

with Q1:
    df33 = df3.groupby(df3['District'])['Count'].sum().reset_index()
    fig = px.bar(df33, x='District', y='Count', text_auto='.2s', title=f'USERS TRANSACTION DISTRICT-WISE ')
fig