from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import numpy as np

# dash_daq is basically a wrapper around dash_core_components
# it provides a collection of pre-built components that can be used to create interactive dashboards
# link: https://dash.plotly.com/dash-daq
import dash_daq as daq

app = Dash()

# 1. Risk Heatmaps: Use color-coded maps to identify high-risk areas within the organization's infrastructure.
# 2. Trend Graphs: Implement interactive line charts to showcase the frequency and types of cyber threats over time.
# 3. Compliance Gauges: Incorporate gauge charts to represent the current compliance status with various cybersecurity frameworks.
# 4. Incident Timelines: Develop timelines that detail the sequence and impact of security incidents.

# Risk Heatmapss
risk_heatmap_data = {
    "Department": ["Finance", "HR", "IT", "Operations", "Sales"],
    "Phishing": [7, 5, 9, 6, 4],
    "Malware": [6, 4, 8, 5, 3],
    "Ransomware": [5, 3, 7, 4, 2],
    "Insider Threat": [4, 2, 6, 3, 1],
    "DDoS": [3, 1, 5, 2, 0],
}
risk_heatmap_data_frame = pd.DataFrame(risk_heatmap_data)
risk_heatmap_data_frame_fig = px.imshow(
    risk_heatmap_data_frame.set_index("Department"),
    labels=dict(x="Threat Category", y="Department", color="Risk Level"),
    x=risk_heatmap_data_frame.columns[1:],
    y=risk_heatmap_data_frame["Department"],
    color_continuous_scale="Reds",
    text_auto=True,
    title="Risk Heatmap",
)
risk_heatmap_data_frame_fig.update_xaxes(side="top")


# Trend Graph
# Generate a date range for 1 year
date_range = pd.date_range(start="2024-01-01", end="2024-12-31", freq="ME")
trend_graph_data = {
    "Date": date_range,
    "Phishing": np.random.poisson(lam=5, size=len(date_range)),
    "Malware": np.random.poisson(lam=3, size=len(date_range)),
    "Ransomware": np.random.poisson(lam=2, size=len(date_range)),
    "Insider Threat": np.random.poisson(lam=1, size=len(date_range)),
    "DDoS": np.random.poisson(lam=4, size=len(date_range)),
}
trend_graph_data = pd.DataFrame(trend_graph_data)

trend_graph_fig = px.line(
    trend_graph_data,
    x="Date",
    y=["Phishing", "Malware", "Ransomware", "Insider Threat", "DDoS"],
    labels={"value": "Number of Incidents", "variable": "Threat Type"},
    title="Monthly Cyber Threat Incidents Over 2024",
)
trend_graph_fig.update_layout(xaxis_title="Month", yaxis_title="Number of Incidents")

# Compliance Gauges
compliance_gauges_data = {
    "Department": ["Finance", "HR", "IT", "Operations", "Sales"],
    "Compliance": [95, 88, 92, 85, 90],
}
compliance_gauges_data_frame = pd.DataFrame(compliance_gauges_data)
compliance_guages_data_fig = html.Div(
    [
        daq.Gauge(
            id=f"gauge-{dept.lower()}",
            label=f"{dept} Compliance",
            value=compliance,
            min=0,
            max=100,
            showCurrentValue=True,
            units="%",
            size=200,
            color={
                "gradient": True,
                "ranges": {
                    "green": [80, 100],
                    "yellow": [50, 79],
                    "red": [0, 49],
                },
            },
        )
        for dept, compliance in zip(
            compliance_gauges_data_frame["Department"],
            compliance_gauges_data_frame["Compliance"],
        )
    ],
    style={"display": "flex", "justify-content": "space-around"},
)

# Incident Timelines
incident_timelines_data = {
    "Incident": ["Phishing Attack", "Malware Infection", "Data Breach", "DDoS Attack"],
    "Start": ["2025-01-10", "2025-02-15", "2025-03-01", "2025-03-20"],
    "End": ["2025-01-12", "2025-02-18", "2025-03-05", "2025-03-22"],
    "Category": ["Phishing", "Malware", "Data Breach", "DDoS"],
}

incident_timelines_data_frame = pd.DataFrame(incident_timelines_data)
incident_timelines_data_frame["Start"] = pd.to_datetime(
    incident_timelines_data_frame["Start"]
)
incident_timelines_data_frame["End"] = pd.to_datetime(
    incident_timelines_data_frame["End"]
)

incident_timelines_fig = px.timeline(
    incident_timelines_data_frame,
    x_start="Start",
    x_end="End",
    y="Incident",
    color="Category",
    title="Incident Timeline",
)
incident_timelines_fig.update_yaxes(categoryorder="total ascending")


app.layout = [
    html.Li(
        children="Risk Assessment: Visualize the organization's current cyber risk posture, highlighting areas of high vulnerability."
    ),
    html.Li(
        children="Threat Monitoring: Display real-time data on emerging threats and incidents."
    ),
    html.Li(
        children="Compliance Tracking: Monitor adherence to cybersecurity standards and regulations."
    ),
    html.Li(
        children="Incident Analysis: Provide detailed insights into past security incidents to inform future prevention strategies."
    ),
    html.H4(children="Note: This is Dummy Data."),
    html.Hr(),
    dcc.Graph(figure=risk_heatmap_data_frame_fig),
    html.Hr(),
    dcc.Graph(figure=trend_graph_fig),
    html.Hr(),
    # dcc.Graph(figure=compliance_guages_data_fig),
    compliance_guages_data_fig,
    html.Hr(),
    dcc.Graph(figure=incident_timelines_fig),
]


if __name__ == "__main__":
    app.run(debug=True)
