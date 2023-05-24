import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

st.set_page_config(page_title = 'Introducción', initial_sidebar_state='expanded')

st.title('Accidentes Aéreos')

df = pd.read_csv('data/accidentes.csv')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('Accidentes Aéreos')

st.markdown('***')
st.markdown('## Contexto')

st.write('''<p style='text-align: justify;'>
Los accidentes aéreos son eventos inesperados e indeseados que resultan en daños físicos tanto a las personas como a las aeronaves involucradas. \
Pueden afectar cualquier tipo de aeronave, ya sea comercial, privada, helicópteros, planeadores o globos aerostáticos.

Estos accidentes pueden ser causados por diversos factores, como errores humanos, fallos en el equipo, condiciones meteorológicas adversas, \
problemas de mantenimiento, deficiencias en la gestión del tráfico aéreo, defectos de diseño o fabricación. \
Las consecuencias de los accidentes pueden ser devastadoras tanto en términos de pérdidas humanas como económicas.

Es por eso que la industria de la aviación, las autoridades reguladoras y los investigadores trabajan incansablemente para mejorar \
la seguridad y prevenir futuros accidentes.

Para lograr esto, es fundamental analizar los datos históricos de los accidentes aéreos. \
La recopilación y el análisis sistemático de estos datos ayudan a los investigadores a identificar patrones, \
tendencias y factores contribuyentes que pueden conducir a mejoras en la seguridad. \
Estos datos son valiosos para mejorar la capacitación de los pilotos y el personal de mantenimiento, \
así como para mejorar el diseño y la fabricación de aviones y equipos de aviación.

Este reporte esta enfocado a la Organización de Aviación Civil Internacional (OACI), organización intergubernamental que se dedica a promover la seguridad y eficiencia de la aviación civil internacional.

Los 193 países que cooperan a través de la OACI están trabajando actualmente hacia su objetivo global acordado de cero fatalidades para el año 2030, \
en conjunto con el fortalecimiento de sus capacidades regulatorias, al tiempo que persiguen una serie de programas y objetivos relevantes para las \
áreas centrales actuales de planificación de seguridad de la aviación mundial, supervisión y mitigación de riesgos.
</p>''', unsafe_allow_html=True)

st.markdown('***')
st.markdown('## Objetivo')

st.write('''

Utilizando la base de datos de accidentes aéreos de todo el mundo entre 1908 y 2021, se llevó a cabo un análisis exhaustivo y una visualización de datos relevantes \
con el objetivo de identificar patrones, tendencias y factores contribuyentes que puedan mejorar la seguridad.

Para comprender los datos y alinearlos con los objetivos de la organización, se tuvieron en cuenta los siguientes indicadores claves de rendimiento (KPIs):

- Reducir anualmente en un 5 % la tasa de mortalidad, calculada como el número de fallecidos en accidentes aéreos en relación con el total de personas en los vuelos involucrados.
- Disminuir en un 5 % el porcentaje de accidentes cuya causa principal son fallas técnicas en un período de 5 años.
- Reducir en un 10 % las causas indeterminadas de accidentes aéreos en un período de 5 años.
- Reducir en un 5 % los accidentes donde la principal causa es el error humano, en un período de 5 años en los países de Estados Unidos y Canadá
''')

st.markdown('***')
st.markdown('## Resumen del análisis')

st.write('En esta sección se provee un informe con los factores más relevantes visualizados en el análisis.')

st.markdown('### Número de accidentes y total fallecidos')

st.write('''<p style='text-align: justify;'>
En las siguientes gráficas se visualizan la variación de la cantidad de accidentes y fallecidos a través de los años. \
En la Fig.1 se observa un pico en la cantidad de accidentes en el año 1946 y un comienzo de declive en 1989. \
Si lo comparamos con la Fig.2 se observa que el período de pico del total de fallecidos, no coincide, ya que el primer pico de este \
gráfico se encuentra en 1962 y el último en 1996. Igualmente, observando la misma figura, concluimos que hay una alta correlación \
entre la cantidad de pasajeros a bordo y el total de fallecidos. Por lo tanto, una menor cantidad de accidentes, no significa \
necesariamente, una menor cantidad de fallecidos. En otras palabras, puede existir un solo accidente con un alto número de personas \
fallecidas.
Finalmente, observando la figura 3, nos encontramos que en la mayoría de los años hubo una baja cantidad de fallecidos en tierra, con \
la excepción del año 2001, debido al atentado del 11 de Septiembre a Las Torres Gemelas (Tabla1). 
</p>''', unsafe_allow_html=True)

year_acc = pd.Series(df.year.value_counts()).sort_index()
fig1 = px.line(year_acc, x=year_acc.index, y=year_acc.values, title='Accidentes por año', labels={'year':'Año','y':'N° de accidentes'})
fig1.update_layout(margin_b= 50, margin_r= 10, margin_t= 60, margin_l= 50)
fig1.update_traces(line_color='#EF553B')
st.plotly_chart(fig1, theme= None)

st.markdown('**Fig.1:** Accidentes aéreos por año')

# Group the DataFrame by 'year' and calculate the sum of 'aboard_fatalities' and 'all_aboard'
grouped_data = df.groupby('year').agg({'aboard_fatalities': 'sum', 'all_aboard': 'sum'}).reset_index()

# Create the figure with two subplots
fig2 = go.Figure()

# Add a line trace for aboard people
fig2.add_trace(go.Line(x=grouped_data['year'], y=grouped_data['all_aboard'], name='Personas abordo'))

# Add a line trace for fatalities
fig2.add_trace(go.Line(x=grouped_data['year'], y=grouped_data['aboard_fatalities'], name='Fallecidos abordo'))

# Set the layout and axis labels
fig2.update_layout(title='Total de fallecidos y personas abordo',
                  xaxis_title='Año',
                  yaxis_title='N° de personas',
                  width = 900)
fig1.update_layout(margin_b= 50, margin_r= 80, margin_t= 60, margin_l= 50)

# Set line colors
fig2.data[0].line.color = '#38A6A5'
fig2.data[1].line.color = '#EF553B'
st.plotly_chart(fig2, theme= None)

st.markdown('**Fig.2:** Cantidad de personas abordo y fallecidos por año')

ground = df.groupby('year').agg({'ground_fatalities': 'sum'}).reset_index()
fig3 = px.line(ground, x='year', y='ground_fatalities', title='Fallecidos en tierra',
               labels={'year':'Año','ground_fatalities':'Fallecidos en tierra'})
fig3.update_layout(margin_b= 50, margin_r= 10, margin_t= 60, margin_l= 50)
fig3.update_traces(line_color='#EF553B')
st.plotly_chart(fig3, theme= None)

st.markdown('**Fig.3:** Cantidad de fallecidos en tierra por año')

atentado = df[df.ground_fatalities == 2750][['date','location','all_aboard','aboard_fatalities', 'ground_fatalities']]
atentado['all_aboard'] = atentado['all_aboard'].astype(int)
atentado['aboard_fatalities'] = atentado['aboard_fatalities'].astype(int)
atentado['ground_fatalities'] = atentado['ground_fatalities'].astype(int)

st.table(atentado)

st.markdown('**Tabla1:** Atentado del 11 de septiembre')

st.markdown('### Accidentes por país')

st.write('''<p style='text-align: justify;'>
En la siguiente gráfica se representa la cantidad de registros encontrada en la base de datos por país. \
Es importante señalar que el número de accidentes por sí solo no indica necesariamente el desempeño de seguridad de un país. \
Como se observa en la gráfica, Estados Unidos tiene el mayor número de accidentes. Sin embargo, esto podría atribuirse al hecho \
de que la base de datos contiene una mayor cantidad de registros de los Estados Unidos. Esto puede deberse al sistema de informes del país \
y a exhaustivos esfuerzos de recopilación de datos.

Al sacar conclusiones o hacer generalizaciones, es crucial considerar este desequilibrio de información entre países. \
Confiar en los números de accidentes sin tener en cuenta las variaciones en la disponibilidad de datos puede conducir a evaluaciones inexactas. \
Por lo tanto, se debe ser precavido y considerar el contexto y la confiabilidad de los datos antes de hacer generalizaciones o juicios.
</p>''', unsafe_allow_html=True)

#Code for the chart

#Import map
world_count = json.load(open('resource/world_countries.geojson','r'))
#Create country id dictionary
country_id_map = {}
for feature in world_count['features']:
    feature['id'] = feature['properties']['ISO_A3']
    country_id_map[feature['properties']['ADMIN']] = feature['id']
# Extract valid countries for the chart
df_country = pd.Series(df['country'].value_counts()).rename_axis('countries').reset_index(name='count').head(100)
df_country = df_country[~df_country['countries'].isin(['Atlantic Ocean','North Sea','North Atlantic Ocean','English Channel','Pacific Ocean','Virgin Islands','Bahamas'])]
#Create columnns neccesaries for the chart
df_country['id'] = df_country['countries'].apply(lambda x: country_id_map[x])
df_country['log_count'] = np.log10(df_country['count'])

fig4 = px.choropleth_mapbox(df_country, locations = 'id', geojson= world_count,
                        color = 'log_count', 
                        hover_name= 'countries',
                        hover_data = {'count':True,'log_count':False},
                        mapbox_style= 'carto-positron',
                        center = {'lat':25,'lon':0},
                        opacity = 0.5,
                        zoom = 1,
                        color_continuous_scale = px.colors.sequential.YlOrRd,
                        height = 700, width = 1100,
                        labels= {'count':'N° accidentes', 'log_count':'escala'})
fig4.update_layout(margin_b= 10, margin_r= 70, margin_t= 10, margin_l= 0)
st.plotly_chart(fig4, theme= None)

st.markdown('**Fig.4:** Cantidad de accidentes por país en la base de datos')

st.markdown('### Causas principales de los accidentes')

st.write('''<p style='text-align: justify;'>
Se ha realizado una clasificación de los accidentes en base a sus respectivas descripciones, con el objetivo de identificar \
las principales causas. Es crucial reconocer que esta clasificación no es perfecta y debe someterse a una revisión de expertos \
para mejorar su precisión. No obstante, esta clasificación inicial ha servido de base para determinar los KPIs más significativos \
en este análisis. El objetivo es identificar las áreas con mayor impacto en los accidentes e identificar áreas plausibles de mejora.

Si bien la clasificación preliminar proporciona información valiosa, es esencial reconocer la necesidad de aportes de expertos para refinar \
y validar la categorización. Esto garantizará que el análisis posterior y la identificación de áreas de mejora se basen en datos precisos y \
confiables.
</p>''', unsafe_allow_html=True)

# Define the bins and labels for the year intervals
bins = list(range(1910, 2021, 5))
bins.insert(0, 1908)
bins[-1] = 2021
labels = bins[1:]
# Create a new column 'year_group' based on the 'year' column
df['year_group'] = pd.cut(df['year'], bins=bins, labels=labels, right=False)

# Group the DataFrame by 'year' and calculate the sum of 'fatalities'
accidents_5year = df.groupby(by=['year_group','disc_cause']).size().reset_index().rename(columns = {0:'count'})
fig5 = px.area(accidents_5year, x='year_group', y='count',
            color = 'disc_cause',
            title='Causas de accidentes',
            width = 900,
            labels={'year_group':'Año',
                    'count':'N° de accidentes',
                    'disc_cause': 'Causa'},
            color_discrete_map={'error humano': '#EF553B',
                                'indeterminado': '#2d8988',
                                'técnico': '#FFA15A',
                                'clima': '#c9e0df',
                                'seguridad': '#B3B3B3',
                                'colisión': '#CBD5E8'},
            category_orders = {'disc_cause':['colisión','clima','indeterminado','seguridad','error humano','técnico']})
fig5.update_layout(margin_b= 50, margin_r= 70, margin_t= 60, margin_l= 50)
st.plotly_chart(fig5, theme= None)

st.markdown('**Fig.5:** Cantidad de accidentes por tipo de causa')

st.markdown('### Conclusiones')

st.write('''<p style='text-align: justify;'>
El número de accidentes por año presenta una variabilidad significativa. Como la mayoría de los accidentes registrados ocurrieron después de 1950, \
con una disminución notable de las muertes por accidentes aéreos a partir de 1972, se consideró apropiado incluir años a partir de 1950 en el dashboard. \
Estos registros son más representativos y ofrecen un análisis más significativo.

Además, al examinar las causas deducidas de los accidentes aéreos, se hace evidente que el error humano es el factor principal seguido \
de las fallas mecánicas a lo largo de los años. A la luz de esta observación, el análisis se centra en la disminución porcentual de estas causas, \
ya que son áreas donde se pueden realizar mejoras factibles a través de la implementación de medidas y regulaciones apropiadas. Los esfuerzos para \
reducir el error humano y abordar las fallas mecánicas son prometedores para mejorar la seguridad de la aviación.
''', unsafe_allow_html=True)

st.markdown('## Disclaimer')

st.write('''<p style='text-align: justify;'>
Este proyecto personal fue desarrollado con fines de aprendizaje. Al explorar los contenidos del mismo y su repositorio asociado,\
la información presentada y los resultados obtenidos **no deben** ser utilizados para tomar decisiones en el mundo real.
''', unsafe_allow_html=True)
