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
    df = pd.read_excel('data/ag_trans/DF1_AG_TRANS.xlsx')
    return df


df = get_data()


header_left, header_mid, header_right = st.columns([1,3,1], gap='large')

with header_mid:
    st.title('TRANSACTION DATA ANALYSIS')

with st.sidebar:
    state_filter = st.multiselect (label='Filter State',
                                   options=df['State'].unique(),
                                   default=df['State'].unique())


    transtype_filter = st.multiselect (label='Filter Transaction_type',
                                   options=df['Transaction_type'].unique(),
                                   default=df['Transaction_type'].unique())

    year_filter = st.multiselect (label='Filter Year',
                                   options=df['Year'].unique(),
                                   default=df['Year'].unique())

    quarter_filter = st.multiselect (label='Filter Quarter',
                                   options=df['Quater'].unique(),
                                   default=df['Quater'].unique())


df1 = df.query('State == @state_filter  & Year == @year_filter & Quater == @quarter_filter & Transaction_type == @transtype_filter')

total_transactions = float(df1['Transaction_amount'].sum())
transaction_count = float (df1['Transaction_count'].sum())

total1, total2, total3 = st.columns(3, gap='large')

with total1:
    st.image('images/ico1.png', use_column_width='Auto')
    st.metric(label='TRANSACTIONS', value=numerize(total_transactions))

with total2:
    st.image('images/ico2.png', use_column_width='Auto')
    st.metric(label='COUNT', value=numerize(transaction_count))

# with total3:
#     st.image('images/ico3.png', use_column_width='Auto')
#     st.metric(label='BRAND', value=numerize(userbybrand_count))




Q1,Q2,Q3,Q4 = st.columns(4)


with Q1:
    df11 = df1.groupby(df1['State'])['Transaction_amount'].sum().reset_index()
    fig = px.bar(df11, x='State', y='Transaction_amount', text_auto='.2s',title = f'OVERALL STATE-WISE PERFORMANCE FROM YEAR 2018 TO 2023')
fig

with Q2:
    df11 = df1.groupby(df1['Transaction_type'])['Transaction_amount'].sum().reset_index()
    fig = px.bar(df11, x='Transaction_type', y='Transaction_amount',text_auto='.2s', title= f'TOTAL TRANSACTION BY TRANSACTION TYPE ')
fig



###################################
df1=df1.replace(to_replace='tamil-nadu', value='Tamil Nadu')
df1=df1.replace(to_replace='uttar-pradesh', value='Uttar Pradesh')
df1=df1.replace(to_replace='jammu-&-kashmir', value='Jammu & Kashmir')
df1=df1.replace(to_replace='arunachal-pradesh', value='Arunachal Pradesh')
df1=df1.replace(to_replace='chhattisgarh', value='Chhattisgarh')
df1=df1.replace(to_replace='puducherry', value='Puducherry')
df1=df1.replace(to_replace='maharashtra', value='Maharashtra')
df1=df1.replace(to_replace='meghalaya', value='Meghalaya')
df1=df1.replace(to_replace='sikkim', value='Sikkim')
df1=df1.replace(to_replace='mizoram', value='Mizoram')
df1=df1.replace(to_replace='telangana', value='Telangana')
df1=df1.replace(to_replace='dadra-&-nagar-haveli-&-daman-&-diu', value='Dadra and Nagar Haveli and Daman and Diu')
df1=df1.replace(to_replace='lakshadweep', value='Lakshadweep')
df1=df1.replace(to_replace='manipur', value='Manipur')
df1=df1.replace(to_replace='nagaland', value='Tamil Nadu')
df1=df1.replace(to_replace='punjab', value='Nagaland')
df1=df1.replace(to_replace='tripura', value='Tripura')
df1=df1.replace(to_replace='rajasthan', value='Rajasthan')
df1=df1.replace(to_replace='madhya-pradesh', value='Madhya Pradesh')
df1=df1.replace(to_replace='karnataka', value='Karnataka')
df1=df1.replace(to_replace='gujarat', value='Gujarat')
df1=df1.replace(to_replace='chandigarh', value='Chandigarh')
df1=df1.replace(to_replace='andhra-pradesh', value='Andhra Pradesh')
df1=df1.replace(to_replace='west-bengal', value='West Bengal')
df1=df1.replace(to_replace='himachal-pradesh', value='Himachal Pradesh')
df1=df1.replace(to_replace='uttarakhand', value='Uttarakhand')
df1=df1.replace(to_replace='goa', value='Goa')
df1=df1.replace(to_replace='delhi', value='Delhi')
df1=df1.replace(to_replace='jharkhand', value='Jharkhand')
df1=df1.replace(to_replace='assam', value='Assam')
df1=df1.replace(to_replace='bihar', value='Bihar')
df1=df1.replace(to_replace='andaman-&-nicobar-islands', value='Andaman & Nicobar')
df1=df1.replace(to_replace='kerala', value='Kerala')
df1=df1.replace(to_replace='haryana', value='Haryana')
df1=df1.replace(to_replace='odisha', value='Odisha')
df1=df1.replace(to_replace='ladakh', value='Ladakh')

###################################

##########
with Q3:
    fig = px.choropleth(
        df1,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        # geojson="C:/Users/umesh/PycharmProjects/pythonProject/india_states.geojson",
        featureidkey='properties.ST_NM',
        # locations='state',
        # color='active cases',
        locations='State',
        # color="Bergeron",
        color='Transaction_amount',
        color_continuous_scale='Reds',

    )

    fig.update_geos(fitbounds="locations", visible=False)
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # fig.show()
    fig