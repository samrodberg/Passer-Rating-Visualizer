import DataParser
import plotly
from plotly.graph_objs import Bar, Layout

player_data = DataParser.format_data_list(printing=False)

ratings = [float(player_data[x][-1]) for x in range(0, len(player_data))]
quarterbacks = [player_data[x][1] for x in range(0, len(player_data))]

plotly.offline.plot({
    "data": [Bar(x=quarterbacks, y=ratings)],
    "layout": Layout(title="Passer Ratings")
})
