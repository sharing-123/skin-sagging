import json
import numpy as np
import plotly.graph_objects as go

THEMATIC_JSON = '''[{"cluster_id":0,"label_terms":["radiofrequency","skin","tightening","treatment"],"members":["combined","device","face","facial","fractional","laxity","lower","monopolar","monopolar radiofrequency","neck","photoaging","radiofrequency","rejuvenation","skin","skin tightening","tightening","treatment"],"size":17,"centrality":1931,"density":9.559,"total_frequency":932},{"cluster_id":1,"label_terms":["stimulation","electrical","electrical stimulation","muscle"],"members":["electrical","electrical stimulation","muscle","neuromuscular","neuromuscular electrical","neuromuscular electrical stimulation","stimulation"],"size":7,"centrality":423,"density":15.619,"total_frequency":168},{"cluster_id":2,"label_terms":["ultrasound","focused","focused ultrasound","high-intensity"],"members":["focused","focused ultrasound","high-intensity","high-intensity focused","high-intensity focused ultrasound","ultrasound"],"size":6,"centrality":668,"density":20.4,"total_frequency":166},{"cluster_id":3,"label_terms":["body","contouring","reduction","body contouring"],"members":["body","body contouring","contouring","liposuction","noninvasive","reduction"],"size":6,"centrality":565,"density":7.8,"total_frequency":162},{"cluster_id":4,"label_terms":["asian","breast","rhinoplasty","reconstruction"],"members":["asian","breast","reconstruction","rhinoplasty"],"size":4,"centrality":81,"density":4.5,"total_frequency":105}]
'''
KEYWORDS_JSON = '''[{"phrase":"radiofrequency","frequency":162,"rake_score":3.056,"doc_count":157},{"phrase":"skin","frequency":155,"rake_score":2.987,"doc_count":140},{"phrase":"tightening","frequency":81,"rake_score":3.099,"doc_count":81},{"phrase":"treatment","frequency":71,"rake_score":2.465,"doc_count":69},{"phrase":"facial","frequency":63,"rake_score":3.19,"doc_count":62},{"phrase":"skin tightening","frequency":63,"rake_score":3.175,"doc_count":63},{"phrase":"ultrasound","frequency":48,"rake_score":3.062,"doc_count":48},{"phrase":"asian","frequency":44,"rake_score":2.114,"doc_count":44},{"phrase":"monopolar","frequency":43,"rake_score":3.372,"doc_count":43},{"phrase":"face","frequency":41,"rake_score":2.317,"doc_count":40},{"phrase":"device","frequency":40,"rake_score":3.45,"doc_count":40},{"phrase":"body","frequency":37,"rake_score":2.811,"doc_count":37},{"phrase":"rejuvenation","frequency":37,"rake_score":2.514,"doc_count":37},{"phrase":"monopolar radiofrequency","frequency":34,"rake_score":3.206,"doc_count":34},{"phrase":"contouring","frequency":34,"rake_score":2.5,"doc_count":34},{"phrase":"stimulation","frequency":33,"rake_score":3.848,"doc_count":33},{"phrase":"electrical","frequency":32,"rake_score":4.0,"doc_count":32},{"phrase":"focused","frequency":31,"rake_score":3.645,"doc_count":31},{"phrase":"reduction","frequency":28,"rake_score":2.964,"doc_count":28},{"phrase":"neck","frequency":28,"rake_score":1.714,"doc_count":27},{"phrase":"focused ultrasound","frequency":26,"rake_score":3.731,"doc_count":26},{"phrase":"lower","frequency":25,"rake_score":2.8,"doc_count":25},{"phrase":"electrical stimulation","frequency":24,"rake_score":3.792,"doc_count":24},{"phrase":"muscle","frequency":24,"rake_score":3.708,"doc_count":21},{"phrase":"laxity","frequency":24,"rake_score":2.458,"doc_count":24},{"phrase":"fractional","frequency":23,"rake_score":3.478,"doc_count":23},{"phrase":"high-intensity","frequency":22,"rake_score":3.955,"doc_count":22},{"phrase":"photoaging","frequency":22,"rake_score":2.909,"doc_count":22},{"phrase":"high-intensity focused","frequency":21,"rake_score":3.905,"doc_count":21},{"phrase":"breast","frequency":21,"rake_score":3.429,"doc_count":19},{"phrase":"noninvasive","frequency":21,"rake_score":3.286,"doc_count":21},{"phrase":"body contouring","frequency":21,"rake_score":2.762,"doc_count":21},{"phrase":"liposuction","frequency":21,"rake_score":2.571,"doc_count":21},{"phrase":"rhinoplasty","frequency":21,"rake_score":2.381,"doc_count":21},{"phrase":"combined","frequency":20,"rake_score":3.05,"doc_count":20},{"phrase":"neuromuscular","frequency":19,"rake_score":3.947,"doc_count":19},{"phrase":"reconstruction","frequency":19,"rake_score":3.263,"doc_count":19},{"phrase":"neuromuscular electrical","frequency":18,"rake_score":4.056,"doc_count":18},{"phrase":"neuromuscular electrical stimulation","frequency":18,"rake_score":4.056,"doc_count":18},{"phrase":"high-intensity focused ultrasound","frequency":18,"rake_score":3.944,"doc_count":18}]
'''

CLUSTER_PALETTE = ["#FF6B6B", "#4EA8DE", "#FFB84C", "#9B5DE5", "#43AA8B", "#F15BB5", "#00BBF9"]
INK = "#242424"
MUTED = "#8A8A8A"
BACKGROUND = "#FFFFFF"

themes = json.loads(THEMATIC_JSON)
keywords = json.loads(KEYWORDS_JSON)
frequency_lookup = {k["phrase"]: k["frequency"] for k in keywords}

centralities = [t["centrality"] for t in themes]
densities = [t["density"] for t in themes]
median_centrality = float(np.median(centralities))
median_density = float(np.median(densities))
max_total_frequency = max(t["total_frequency"] for t in themes)

x_pad = (max(centralities) - min(centralities)) * 0.40 + 150
y_pad = (max(densities) - min(densities)) * 0.18 + 1
x_range = [min(centralities) - x_pad, max(centralities) + x_pad]
y_range = [min(densities) - y_pad, max(densities) + y_pad]

label_offsets = [(0, 160), (0, -160), (-240, 50), (240, 50), (-220, -90), (220, -90), (0, 200)]

fig = go.Figure()

fig.add_shape(type="line", x0=median_centrality, x1=median_centrality, y0=y_range[0], y1=y_range[1],
              line=dict(color=MUTED, width=1.4, dash="dash"))
fig.add_shape(type="line", x0=x_range[0], x1=x_range[1], y0=median_density, y1=median_density,
              line=dict(color=MUTED, width=1.4, dash="dash"))

quadrant_labels = [
    dict(x=x_range[1], y=y_range[1], text="MOTOR THEMES", xanchor="right", yanchor="top"),
    dict(x=x_range[0], y=y_range[1], text="NICHE THEMES", xanchor="left", yanchor="top"),
    dict(x=x_range[1], y=y_range[0], text="BASIC THEMES", xanchor="right", yanchor="bottom"),
    dict(x=x_range[0], y=y_range[0], text="EMERGING OR DECLINING THEMES", xanchor="left", yanchor="bottom"),
]

for q in quadrant_labels:
    fig.add_annotation(x=q["x"], y=q["y"], text=q["text"], showarrow=False,
                       xanchor=q["xanchor"], yanchor=q["yanchor"],
                       font=dict(size=16, color=MUTED, family="Arial Black"))

for i, theme in enumerate(themes):
    color = CLUSTER_PALETTE[i % len(CLUSTER_PALETTE)]
    size = 45 + 120 * (theme["total_frequency"] / max_total_frequency) ** 0.5
    member_freqs = sorted(
        [(m, frequency_lookup.get(m, 0)) for m in theme["members"]],
        key=lambda pair: pair[1], reverse=True,
    )
    hover_lines = "<br>".join([f"{term}  {freq}" for term, freq in member_freqs])
    hover_text = (
        f"<b>Cluster {theme['cluster_id']}</b><br>"
        f"Centrality {theme['centrality']}<br>"
        f"Density {theme['density']}<br>"
        f"Total frequency {theme['total_frequency']}<br><br>"
        f"{hover_lines}"
    )

    fig.add_trace(go.Scatter(
        x=[theme["centrality"]], y=[theme["density"]],
        mode="markers",
        marker=dict(size=size, color=color, opacity=0.88,
                    line=dict(color="black", width=2)),
        hovertext=hover_text,
        hoverinfo="text",
        hoverlabel=dict(bgcolor="white", bordercolor=color, font=dict(color=INK, size=20), align="left"),
        showlegend=False,
    ))

    label = "<br>".join(theme["label_terms"][:4])
    ox, oy = label_offsets[i % len(label_offsets)]
    fig.add_annotation(
        x=theme["centrality"], y=theme["density"],
        ax=ox, ay=-oy, axref="pixel", ayref="pixel",
        text=label, showarrow=True, arrowhead=0, arrowcolor=MUTED, arrowwidth=1,
        font=dict(size=20, color=INK, family="Arial Black"),
        bgcolor="rgba(255,255,255,0.85)", borderpad=4,
    )

fig.update_layout(
    title=dict(
        text="Thematic Map of Skin Sagging and Facial Rejuvenation Research",
        font=dict(size=28, color=INK, family="Arial Black"),
        x=0.5, xanchor="center",
    ),
    xaxis=dict(title="Relevance Degree, Centrality", range=x_range,
               showgrid=False, zeroline=False, color=INK, title_font=dict(size=18)),
    yaxis=dict(title="Development Degree, Density", range=y_range,
               showgrid=False, zeroline=False, color=INK, title_font=dict(size=18)),
    plot_bgcolor=BACKGROUND,
    paper_bgcolor=BACKGROUND,
    width=1600,
    height=900,
    margin=dict(t=110, b=80, l=90, r=60),
)

fig.write_html("../figures/thematic_map.html")
fig.write_image("../figures/thematic_map.png", scale=2)
