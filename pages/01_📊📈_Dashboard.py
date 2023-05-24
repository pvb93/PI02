import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

#st.title('Accidentes aéreos')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

ct_data = st.container()
ct_sidebar = st.container()

with ct_data:
    df = pd.read_csv('data/accidentes.csv')
    df_mortalidad = pd.read_csv('data/mortalidad.csv')
    df_causas = pd.read_csv('data/causas_mu.csv')
    df_usa = pd.read_csv('data/usa_he.csv')


with ct_sidebar:    
    st.sidebar.header('Dashboard `version 0`')

    st.sidebar.subheader('Parámetro de tiempo: métricas y gráficas')
    year_select = st.sidebar.slider('Seleccione año', 1950, 2021, 2000) 

    st.sidebar.subheader('Parámetro de ubicación para gráficas')
    list_continent = list(df.continent.unique())
    continent_select = st.sidebar.multiselect('Seleccione contiente', list_continent, list_continent)

    st.sidebar.markdown('''
    ---
    Created by Paola V Barrera.
    ''')

# Apply filters
df_filter = df[(df.year == year_select)&(df.continent.isin(continent_select))]
df_mf = df_mortalidad[df_mortalidad.year == year_select]
df_cf = df_causas[df_causas.year == year_select]
df_usaf = df_usa[df_usa.year == year_select]

# Calculate ground metrics

# Total ground fatalities
cy_ground = df_filter['ground_fatalities'].sum()
# N accidents with ground
cy_ground_n = df_filter[(df.ground_fatalities != 0)]['ground_fatalities'].count()
# Total ground fatalities previous year
py = year_select - 1
py_ground = df[df.year == py]['ground_fatalities'].sum()
# N accidents with ground previous year
py_ground_n = df[(df.year == py)&(df.ground_fatalities != 0)]['ground_fatalities'].count()
#Percentage change sum
var_ground = round((cy_ground - py_ground)*100/py_ground, 2)
#Percentage change count
var_ground_n = round((cy_ground_n - py_ground_n)*100/py_ground_n, 2)


# Row A
st.markdown('### Métricas')

col1, col2, col3, col4 = st.columns(4)
col1.metric('Tasa de mortalidad', float(df_mf.tasa), float(df_mf.var_tasa), delta_color="inverse")
col2.metric('Porcentaje por causa técnica', float(df_cf.mechanical), float(df_cf.var_mechanical), delta_color="inverse")
col3.metric('Porcentaje por causa indeterminada', float(df_cf.undetermined), float(df_cf.var_undetermined), delta_color="inverse")
col4.metric('Porcentaje por error humano USA & Canada', float(df_usaf.human_error), float(df_usaf.var_human_error), delta_color="inverse")

# Row B

c1, c2 = st.columns((70,30))
with c1:
    st.markdown('### Cantidad de accidentes y sus causas')
    
    # Area chart
    min_year = (year_select - 10)
    accidents = df[(df.year >= min_year)&(df.year <= year_select)&(df.continent.isin(continent_select))].groupby(by=['year','disc_cause']).size()\
                .reset_index().rename(columns = {0:'count'})
    fig1 = px.area(accidents, x='year', y='count',
                    color = 'disc_cause',
                    width = 1200,
                    labels={'year':'Año',
                            'count':'N° de accidentes',
                            'disc_cause': 'Causa'},
                    color_discrete_map={'error humano': '#EF553B',
                                        'indeterminado': '#2d8988',
                                        'técnico': '#FFA15A',
                                        'clima': '#c9e0df',
                                        'seguridad': '#B3B3B3',
                                        'colisión': '#CBD5E8'},
                    category_orders = {'disc_cause':['colisión','clima','indeterminado','seguridad','error humano','técnico']})
    
    st.plotly_chart(fig1, theme= None)

    st.markdown('### Información general: hora, día, ubicación, causa')
    #Bubble chart
    fig2 = px.scatter(df_filter, x='time', y='week_day',
	            size= 'aboard_fatalities', color='disc_cause',
                hover_name='location', size_max=50,
                width = 1200,
                labels={'time':'Hora',
                        'week_day':'Día de la semana',
                        'disc_cause': 'Causa',
                        'aboard_fatalities': 'Fallecidos'},
                color_discrete_map={'error humano': '#EF553B',
                                    'indeterminado': '#2d8988',
                                    'técnico': '#FFA15A',
                                    'clima': '#c9e0df',
                                    'seguridad': '#B3B3B3',
                                    'colisión': '#CBD5E8'
                                    },
                category_orders = {'week_day':['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']},
                template= 'seaborn')
    
    st.plotly_chart(fig2, theme= None)

with c2:
    st.markdown('### Top 5 países')

    by_country = pd.Series(df_filter['country'].value_counts()).reset_index().head(5)
    # Bar chart by country
    fig3 = px.bar(by_country, x='count', y='country', orientation='h',
                width = 600,
                labels= {'count':'Cantidad de accidentes','country':''})

    fig3.update_layout(yaxis={'categoryorder':'total ascending'})
    fig3.update_layout(margin_b= 10, margin_r= 10, margin_t= 0, margin_l= 50)
    fig3.update_traces(marker=dict(color= px.colors.sequential.haline[0]), selector=dict(type="bar"))
    st.plotly_chart(fig3)

    st.markdown('### Top 5 por tipo de aeronave')

    by_ac = pd.Series(df_filter['ac_gral'].value_counts()).reset_index().head(5)
    
    #Bar chart by aircraft
    fig4 = px.bar(by_ac, x='count', y='ac_gral', orientation='h',
                title = 'Top 5',
                width = 600,
                labels= {'count':'Cantidad de accidentes','ac_gral':''})

    fig4.update_layout(yaxis={'categoryorder':'total ascending'})
    fig4.update_layout(margin_b= 10, margin_r= 10, margin_t= 0, margin_l= 50)
    fig4.update_traces(marker=dict(color= px.colors.sequential.haline[0]), selector=dict(type="bar"))
    st.plotly_chart(fig4)

# Row C
rowc1, rowc2, rowc3 = st.columns((60,15,25))

with rowc1:

    st.markdown('### Total de fallecidos y personas abordo por año')

    # Group the DataFrame by 'year' and calculate the sum of 'aboard_fatalities' and 'all_aboard'
    grouped_data = df[(df.year >= min_year)&(df.year <= year_select)&(df.continent.isin(continent_select))]\
                    .groupby('year').agg({'aboard_fatalities': 'sum', 'all_aboard': 'sum'}).reset_index()

    # Create the figure with two subplots
    fig5 = go.Figure()
    # Add a line trace for aboard people
    fig5.add_trace(go.Line(x=grouped_data['year'], y=grouped_data['all_aboard'], name='Personas abordo'))
    # Add a line trace for fatalities
    fig5.add_trace(go.Line(x=grouped_data['year'], y=grouped_data['aboard_fatalities'], name='Falllecidos'))

    # Set the layout and axis labels
    fig5.update_layout(xaxis_title='Año',
                        yaxis_title='N° de personas',
                        width = 1000)
    # Set line colors
    fig5.data[0].line.color = '#38A6A5'
    fig5.data[1].line.color = '#EF553B'
    fig5.update_layout(margin_b= 10, margin_r= 10, margin_t= 10, margin_l= 20)

    st.plotly_chart(fig5)

with rowc2:
    st.markdown('### Fallecidos en tierra')

    # Ground metrics
    st.metric('N° de fallecidos en tierra', cy_ground, var_ground, delta_color="inverse")
    st.metric('N° de accidentes con fallecidos en tierra', cy_ground_n, var_ground_n, delta_color="inverse")

with rowc3:
    st.markdown('### Accidentes por continente')

    # Pie chart continent
    continent_pie = pd.Series(df_filter.continent.value_counts()).reset_index()
    fig6 =  px.pie(continent_pie,values='count',names='continent',hole=0.4, width= 400,
                    color_discrete_sequence = px.colors.sequential.haline)
    fig6.update_layout(margin_b= 10, margin_r= 30, margin_t= 0, margin_l= 0)
    st.plotly_chart(fig6)