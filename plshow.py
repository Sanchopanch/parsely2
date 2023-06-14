import plotly.express as px
import pandas as pd
import sqlite3

word = 'kochetkov spb'

df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
df = pd.read_sql_query(f'SELECT se.date,se.num, se.site FROM serp as se, querries as q\
                       where q.id= se.querry and q.querry="{word}" \
                       --and se.date>"2023-06-11"', sqlite_connection)
sqlite_connection.close()

fig = px.line(df, x="date", y="num", color="site", markers=True, title=word,
              color_discrete_sequence=px.colors.qualitative.Pastel
              )
fig.update_traces(textposition="bottom right")
fig.update_layout(yaxis=dict(autorange="reversed", title=word))
fig.update_yaxes(dtick=1, showgrid=True)

fig.update_traces(marker_line_width=1, marker_size=15, line_width=10)
fig.show()