import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#make an api call and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#store api response in a variable
responseDict = r.json()
print(f"Total repositories: {responseDict['total_count']}")

#explore information about the repositories
repoDicts = responseDict["items"]

names, stars = [], []
for repoDict in repoDicts:
    names.append(repoDict["name"])
    stars.append(repoDict["stargazers_count"])

#make visualization
myStyle = LS("#333366", base_style=LCS)

myConfig = pygal.Config()
myConfig.x_label_rotation = 45
myConfig.show_legend = False
myConfig.title_font_size = 24
myConfig.label_font_size = 14
myConfig.major_lable_cont_size = 18
myConfig.truncate_label = 15
myConfig.show_y_guides = False
myConfig.width = 1000

chart = pygal.Bar(myConfig, style=myStyle)
chart.title = "Most Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file("python_repos.svg")



