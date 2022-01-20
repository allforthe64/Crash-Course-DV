import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

myStyle = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=myStyle, x_label_roation=45, show_legend = False)

chart.title = "Python Projects"
chart.x_labels = ["httpie", "django", "flask"]

plotDicts = [
    {"value": 16101, "label": "Description of httpie"},
    {"value": 15028, "label": "Description of django"},
    {"value": 14798, "label": "Description of flask"}
]

chart.add('', plotDicts)
chart.render_to_file("bar_descriptions.svg")