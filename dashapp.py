from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"])


app = Dash(__name__)
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "20px",
        "fontFamily": "Arial"
    },

    children=[
        html.H1(
            children="Soul Foods Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.P(
            "Was there a change in sales before and after the Pink Morsel price increase?",
            style={
                "textAlign": "center",
                "fontSize": "18px",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            style={"textAlign": "center", "marginBottom": "20px"},
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                )
            ]
        ),

        dcc.Graph(
            id="sales-line-chart",
        )
])

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    # group by date and work with sales column only
    daily_sales = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    fig = px.line(daily_sales, x="Date", y="Sales", title="Daily Sales Over Time")
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red", )
    fig.add_annotation(x="2021-01-15", y=daily_sales["Sales"].max(),
                       text="Price Increase (15 Jan 2021)")

    fig.update_layout(xaxis_title="Date", yaxis_title="Total Sales")

    return fig

if __name__ == '__main__':
    app.run(debug=True)