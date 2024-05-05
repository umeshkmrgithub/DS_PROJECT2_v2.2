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

st.set_page_config(page_title='USER-WISE TRANSACTION DATA ANALYSIS FOR PRODUCT-xPAY',
                   layout='wide',
                   initial_sidebar_state='expanded')
@st.cache_data
def get_data2():
    df2 = pd.read_excel('data/ag_users/DF2_AG_USERS.xlsx')
    return df2


df2 = get_data2()


header_left, header_mid, header_right = st.columns([1,3,1], gap='large')

with header_mid:
    st.title('TRANSACTION DATA ANALYSIS USERS MOBILE-WISE')

with st.sidebar:
    userbybrand_filter = st.multiselect(label='Filter User by Device Brand',
                                    options=df2['Brand'].unique(),
                                    default=df2['Brand'].unique())

    userbystate_filter = st.multiselect(label='Filter User by State',
                                      options=df2['State'].unique(),
                                      default=df2['State'].unique())

    userbyyear_filter = st.multiselect(label='Filter User by Year',
                                        options=df2['Year'].unique(),
                                        default=df2['Year'].unique())

    userbyquarter_filter = st.multiselect(label='Filter User by Quarter',
                                       options=df2['Quater'].unique(),
                                       default=df2['Quater'].unique())


df2 = df2.query('State == @userbystate_filter & Year == @userbyyear_filter & Quater == @userbyquarter_filter & Brand == @userbybrand_filter')

userbybrand_count = float(df2['Count'].sum())

total1, total2, total3 = st.columns(3, gap='large')
# total1 = st.columns(1, gap='large')

# with total1:
#     st.image('images/ico1.png', use_column_width='Auto')
#     st.metric(label='BRAND', value=numerize(userbybrand_count))

with total1:
    st.image('images/ico3.png', use_column_width='Auto')
    st.metric(label='BRAND', value=numerize(userbybrand_count))

###################################
df2=df2.replace(to_replace='tamil-nadu', value='Tamil Nadu')
df2=df2.replace(to_replace='uttar-pradesh', value='Uttar Pradesh')
df2=df2.replace(to_replace='jammu-&-kashmir', value='Jammu & Kashmir')
df2=df2.replace(to_replace='arunachal-pradesh', value='Arunachal Pradesh')
df2=df2.replace(to_replace='chhattisgarh', value='Chhattisgarh')
df2=df2.replace(to_replace='puducherry', value='Puducherry')
df2=df2.replace(to_replace='maharashtra', value='Maharashtra')
df2=df2.replace(to_replace='meghalaya', value='Meghalaya')
df2=df2.replace(to_replace='sikkim', value='Sikkim')
df2=df2.replace(to_replace='mizoram', value='Mizoram')
df2=df2.replace(to_replace='telangana', value='Telangana')
df2=df2.replace(to_replace='dadra-&-nagar-haveli-&-daman-&-diu', value='Dadra and Nagar Haveli and Daman and Diu')
df2=df2.replace(to_replace='lakshadweep', value='Lakshadweep')
df2=df2.replace(to_replace='manipur', value='Manipur')
df2=df2.replace(to_replace='nagaland', value='Tamil Nadu')
df2=df2.replace(to_replace='punjab', value='Nagaland')
df2=df2.replace(to_replace='tripura', value='Tripura')
df2=df2.replace(to_replace='rajasthan', value='Rajasthan')
df2=df2.replace(to_replace='madhya-pradesh', value='Madhya Pradesh')
df2=df2.replace(to_replace='karnataka', value='Karnataka')
df2=df2.replace(to_replace='gujarat', value='Gujarat')
df2=df2.replace(to_replace='chandigarh', value='Chandigarh')
df2=df2.replace(to_replace='andhra-pradesh', value='Andhra Pradesh')
df2=df2.replace(to_replace='west-bengal', value='West Bengal')
df2=df2.replace(to_replace='himachal-pradesh', value='Himachal Pradesh')
df2=df2.replace(to_replace='uttarakhand', value='Uttarakhand')
df2=df2.replace(to_replace='goa', value='Goa')
df2=df2.replace(to_replace='delhi', value='Delhi')
df2=df2.replace(to_replace='jharkhand', value='Jharkhand')
df2=df2.replace(to_replace='assam', value='Assam')
df2=df2.replace(to_replace='bihar', value='Bihar')
df2=df2.replace(to_replace='andaman-&-nicobar-islands', value='Andaman & Nicobar')
df2=df2.replace(to_replace='kerala', value='Kerala')
df2=df2.replace(to_replace='haryana', value='Haryana')
df2=df2.replace(to_replace='odisha', value='Odisha')
df2=df2.replace(to_replace='ladakh', value='Ladakh')

###################################


Q1,Q2 = st.columns(2)

with Q1:
    fig = px.choropleth(
        df2,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        # geojson="data/india_states.geojson",
        featureidkey='properties.ST_NM',
        # locations='state',
        # color='active cases',
        locations='Brand',
        # color="Bergeron",
        color='Count',
        color_continuous_scale='Viridis',

    )

    fig.update_geos(fitbounds="locations", visible=False)
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # fig.show()
    fig

with Q2:
    df22 = df2.groupby(df2['Brand'])['Count'].sum().reset_index()
    fig = px.bar(df22, x='Brand', y='Count', text_auto='.2s', title=f'USERS TRANSACTION BY MOBILE DEVICE BRAND ')
fig
