from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"])

# group by date and work with sales column only
daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

fig = px.line(daily_sales, x="Date", y="Sales", title="Daily Sales Over Time")
fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red",)
fig.add_annotation(x="2021-01-15",y=daily_sales["Sales"].max(),
                   text="Price Increase (15 Jan 2021)")

fig.update_layout(xaxis_title="Date", yaxis_title="Total Sales")

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(
        children="Soul Foods Sales Visualiser",
        style={"textAlign": "center"}
    ),

    html.Div(
        children="Was there a change in sales before and after the Pink Morsel price increase?",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)