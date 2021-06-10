import pandas as pd
from plotnine import * 

df = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")

#df.head()
df_plotted = df.loc[:, ['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']]
df_plotted.head()

(ggplot(df_plotted, aes(x='Mortality rate, infant (per 1,000 live births)', y='GDP per capita (constant 2010 US$)')) +
        # add scatter points
        geom_point(alpha = 0.5) +
        # log-scale the x-axis
        scale_y_log10() +
        # change labels
        labs(title="Mortality against GDP per capita",
             x="Mortality rate, infant (per 1,000 live births)",
             y="GDP per capita (constant 2010 US$)")
)

"""
(ggplot(df_plotted, aes(x='Mortality rate, infant (per 1,000 live births)', y='GDP per capita (constant 2010 US$)', color='Country Name')) +
        # add scatter points
        geom_point(alpha = 0.5) +
        # log-scale the x-axis
        scale_y_log10() +
        # change labels
        labs(title="mortality against GDP per capita",
             x="Mortality rate, infant (per 1,000 live births)",
             y="GDP per capita (constant 2010 US$)",
             color="Country Name")
)
"""

"""
Then pull out the columns:

‘Mortality rate, infant (per 1,000 live births)’
‘GDP per capita (constant 2010 US$)’
‘Country Name’
and plot mortality against GDP per capita.
"""


