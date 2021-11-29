from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# CM4125 Data Viz Coursework - Damon Kopsidas 1713268
This visualization aims to provide a visual representation of the "Happiness Score"
each country got in the [World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness), together with an estimated Atheism Percentage by country.
"""

#Importing Datasets
world_happiness = pd.read_csv('https://www.dropbox.com/s/6ibxe989vqextvq/world_happiness_data.csv?dl=1')
atheist_pop = pd.read_csv('https://www.dropbox.com/s/2mfjjndhz4vxj03/Atheist_Population.csv?dl=1')

fig = px.scatter_geo(world_happiness, locations="ISO", 
                     color="Country",
                     hover_name="Country", size="Happiness Score",
                     animation_frame="Year",
                     #projection="natural earth"
                     projection="orthographic"
                     )
fig.update_geos(showcountries=True, countrycolor="black")
fig.update_layout(height=700, width=1000)
                     
fig.show()
