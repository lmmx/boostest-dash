import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

from api_utils import create_boostest_url

app = dash.Dash("Hello Boosted World")

app.layout = html.Div([
    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": readable_label, "value": column_name}
            for readable_label, column_name in [
                ("1st doses (%)", "cumVaccinationFirstDoseUptakeByPublishDatePercentage"),
                ("2nd doses (%)", "cumVaccinationSecondDoseUptakeByPublishDatePercentage"),
                ("Boosters (%)", "cumVaccinationThirdInjectionUptakeByPublishDatePercentage"),
                ("LFD tests", "newLFDTestsBySpecimenDate"),
                ("PCR tests", "newPCRTestsByPublishDate"),
            ]
        ],
        value="cumVaccinationThirdInjectionUptakeByPublishDatePercentage"
    ),
    dcc.Graph(id="metric-graph")
], style={"width": "500"})

@app.callback(Output("metric-graph", "figure"), [Input("metric-dropdown", "value")])
def update_graph(selected_dropdown_value):
    df = pd.read_csv(
        "sample_data.csv"
    )
    return {
        "data": [{
            "x": df.date,
            "y": df[selected_dropdown_value],
        }],
        "layout": {"margin": {"l": 40, "r": 0, "t": 20, "b": 30}}
    }

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == "__main__":
    app.run_server()
