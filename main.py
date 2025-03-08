import os
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# import numpy as np

# dash_daq is basically a wrapper around dash_core_components
# it provides a collection of pre-built components that can be used to create interactive dashboards
# link: https://dash.plotly.com/dash-daq
import dash_daq as daq

app = Dash()

base_dir = os.path.dirname(os.path.abspath(__file__))

## Adware Data
adware_csv_path = os.path.join(base_dir, "cyber-data", "Adware_after_reboot_Cat.csv")
adware_data_frame = pd.read_csv(adware_csv_path, usecols=["Category", "Family"])
adware_data = {
    # "Category": adware_data_frame["Category"].value_counts(),
    "Category": adware_data_frame["Category"].max(),
    "Family": adware_data_frame["Family"].value_counts().count(),
}
adware_custom_data_frame = pd.DataFrame(adware_data, index=[0])
# print(adware_data_frame.head())
# print(adware_data_frame.columns)

# print(adware_data_frame["Category"].max())
# print(adware_data_frame["Category"].value_counts())
# print(adware_data_frame["Family"].value_counts().count())


## Backdoor Data
backdoor_csv_path = os.path.join(
    base_dir, "cyber-data", "Backdoor_after_reboot_Cat.csv"
)
backdoor_data_frame = pd.read_csv(backdoor_csv_path, usecols=["Category", "Family"])
backdoor_data = {
    # "Category": backdoor_data_frame["Category"].value_counts(),
    "Category": backdoor_data_frame["Category"].max(),
    "Family": backdoor_data_frame["Family"].value_counts().count(),
}
backdoor_custom_data_frame = pd.DataFrame(backdoor_data, index=[1])


## File Infector Data
file_infector_csv_path = os.path.join(
    base_dir, "cyber-data", "FileInfector_after_reboot_Cat.csv"
)
file_infector_data_frame = pd.read_csv(
    file_infector_csv_path, usecols=["Category", "Family"]
)
file_infector_data = {
    # "Category": file_infector_data_frame["Category"].value_counts(),
    "Category": file_infector_data_frame["Category"].max(),
    "Family": file_infector_data_frame["Family"].value_counts().count(),
}
file_infector_custom_data_frame = pd.DataFrame(file_infector_data, index=[2])

## PUA Data
## PUA full form is "Personal User Agent"
pua_csv_path = os.path.join(base_dir, "cyber-data", "PUA_after_reboot_Cat.csv")
pua_data_frame = pd.read_csv(pua_csv_path, usecols=["Category", "Family"])
pua_data = {
    # "Category": pua_data_frame["Category"].value_counts(),
    "Category": pua_data_frame["Category"].max(),
    "Family": pua_data_frame["Family"].value_counts().count(),
}
pua_custom_data_frame = pd.DataFrame(pua_data, index=[3])

## Ransomware Data
ransomware_csv_path = os.path.join(
    base_dir, "cyber-data", "Ransomware_after_reboot_Cat.csv"
)
ransomware_data_frame = pd.read_csv(ransomware_csv_path, usecols=["Category", "Family"])
ransomware_data = {
    # "Category": ransomware_data_frame["Category"].value_counts(),
    "Category": ransomware_data_frame["Category"].max(),
    "Family": ransomware_data_frame["Family"].value_counts().count(),
}
ransomware_custom_data_frame = pd.DataFrame(ransomware_data, index=[4])

## Riskware
riskware_csv_path = os.path.join(
    base_dir, "cyber-data", "Riskware_after_reboot_Cat.csv"
)
riskware_data_frame = pd.read_csv(riskware_csv_path, usecols=["Category", "Family"])
riskware_data = {
    # "Category": riskware_data_frame["Category"].value_counts(),
    "Category": riskware_data_frame["Category"].max(),
    "Family": riskware_data_frame["Family"].value_counts().count(),
}
riskware_custom_data_frame = pd.DataFrame(riskware_data, index=[5])

## Scareware Data
scareware_csv_path = os.path.join(
    base_dir, "cyber-data", "Scareware_after_reboot_Cat.csv"
)
scareware_data_frame = pd.read_csv(scareware_csv_path, usecols=["Category", "Family"])
scareware_data = {
    # "Category": scareware_data_frame["Category"].value_counts(),
    "Category": scareware_data_frame["Category"].max(),
    "Family": scareware_data_frame["Family"].value_counts().count(),
}
scareware_custom_data_frame = pd.DataFrame(scareware_data, index=[6])

## Torjan Data
torjan_csv_path = os.path.join(base_dir, "cyber-data", "Trojan_after_reboot_Cat.csv")
torjan_data_frame = pd.read_csv(torjan_csv_path, usecols=["Category", "Family"])
torjan_data = {
    # "Category": torjan_data_frame["Category"].value_counts(),
    "Category": torjan_data_frame["Category"].max(),
    "Family": torjan_data_frame["Family"].value_counts().count(),
}
torjan_custom_data_frame = pd.DataFrame(torjan_data, index=[7])

## Zero Day Data
zero_day_csv_path = os.path.join(
    base_dir, "cyber-data", "Zero_Day_after_reboot_Cat.csv"
)
zero_day_data_frame = pd.read_csv(zero_day_csv_path, usecols=["Category", "Family"])
zero_day_data = {
    # "Category": zero_day_data_frame["Category"].value_counts(),
    "Category": zero_day_data_frame["Category"].max(),
    "Family": zero_day_data_frame["Family"].value_counts().count(),
}
zero_day_custom_data_frame = pd.DataFrame(zero_day_data, index=[8])

# Concatenate Data
custom_data_frame = pd.concat(
    [
        adware_custom_data_frame,
        backdoor_custom_data_frame,
        file_infector_custom_data_frame,
        pua_custom_data_frame,
        ransomware_custom_data_frame,
        riskware_custom_data_frame,
        scareware_custom_data_frame,
        torjan_custom_data_frame,
        zero_day_custom_data_frame,
    ]
)
# print(custom_data_frame)

# Plot Merged Data
custom_data_frame_fig = px.bar(
    custom_data_frame,
    x="Category",
    y="Family",
    orientation="v",
    color="Family",
    labels={"Category": "Category", "Family": "Number of Families"},
    log_y=True,
)


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
import random
import math


def poisson_random_variable(lam):
    L = math.exp(-lam)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


date_range = pd.date_range(start="2024-01-01", end="2024-12-31", freq="ME")
# trend_graph_data = {
#     "Date": date_range,
#     "Phishing": np.random.poisson(lam=5, size=len(date_range)),
#     "Malware": np.random.poisson(lam=3, size=len(date_range)),
#     "Ransomware": np.random.poisson(lam=2, size=len(date_range)),
#     "Insider Threat": np.random.poisson(lam=1, size=len(date_range)),
#     "DDoS": np.random.poisson(lam=4, size=len(date_range)),
# }
trend_graph_data = {
    "Date": date_range,
    "Phishing": [poisson_random_variable(5) for _ in range(len(date_range))],
    "Malware": [poisson_random_variable(3) for _ in range(len(date_range))],
    "Ransomware": [poisson_random_variable(2) for _ in range(len(date_range))],
    "Insider Threat": [poisson_random_variable(1) for _ in range(len(date_range))],
    "DDoS": [poisson_random_variable(4) for _ in range(len(date_range))],
}
trend_graph_data = pd.DataFrame(trend_graph_data)

trend_graph_fig = px.line(
    trend_graph_data,
    x="Date",
    y=["Phishing", "Malware", "Ransomware", "Insider Threat", "DDoS"],
    labels={"value": "Number of Incidents", "variable": "Threat Type"},
    title="Trend Graph of Monthly Cyber Threat Incidents Over 2024",
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
    html.H4(children="Please wait a bit to load the data..."),
    html.H4(children="Note: This is Dummy Data."),
    html.Hr(),
    html.A(
        children="Click here for the original data",
        href="https://www.unb.ca/cic/datasets/andmal2020.html",
    ),
    dcc.Graph(figure=custom_data_frame_fig),
    html.Hr(),
    html.Div(
        children=".",
        style={"margin-top": "70px", "margin-bottom": "70px"},
    ),
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
