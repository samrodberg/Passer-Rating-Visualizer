import PRFormulas as pr
import plotly
from plotly.graph_objs import Bar, Layout

brady = pr.calculate_pr_nfl(195.0, 133.0, 1702.0, 11.0, 1.0)
palmer = pr.calculate_pr_nfl(227.0, 136.0, 1573.0, 6.0, 5.0)
smith = pr.calculate_pr_nfl(158.0, 121.0, 1391.0, 11.0, 0.0)
rodgers = pr.calculate_pr_nfl(189.0, 126.0, 1367.0, 13.0, 3.0)

quarterback = ['Tom Brady', 'Carson Palmer', 'Alex Smith', 'Aaron Rodgers']
ratings = [brady, palmer, smith, rodgers]

plotly.offline.plot({
    "data": [Bar(x=quarterback, y=ratings)],
    "layout": Layout(title="Passer Ratings")
})
