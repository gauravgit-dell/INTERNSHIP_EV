#the above dataset is obtained from IEA global ev outlook for a better and proper understanding of the global ev market trends and forecasts. 
#the dataset includes the global EV sales in millions and the market share percentage for the years 2020 to 2025.
#the line chart illustrates the growth in global EV sales over the years, while the bar chart shows the increase in market share percentage.
#the graph photo will be attached in the report to visually represent the data and trends in the global EV market.
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

data = {
    "Year": [2020, 2021, 2022, 2023, 2024, 2025],
    "EV Sales Million": [3, 6.6, 10, 13.5, 17, 20],
    "Market Share %": [4, 9, 14, 18, 20, 25]
}

df = pd.DataFrame(data)

app = Dash(__name__)

fig1 = px.line(df, x="Year", y="EV Sales Million",
               title="Global EV Sales Growth")

fig2 = px.bar(df, x="Year", y="Market Share %",
              title="EV Market Share Growth")

app.layout = html.Div([
    html.H1("EV Market Forecast Dashboard"),
    html.H3("Global Trends, Policies and Adoption Rates"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])

if __name__ == "__main__":
    app.run(debug=True)
    
    start_value = 17
end_value = 20
years = 1

cagr = (end_value / start_value) ** (1 / years) - 1
forecast_2030 = end_value * ((1 + cagr) ** 5)

print("CAGR:", round(cagr * 100, 2), "%")
print("2030 Forecast:", round(forecast_2030, 2), "million EVs")
