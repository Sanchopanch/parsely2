import plotly.express as px
import pandas as pd
import sqlite3
import random as rnd

word = 'kochetkov spb'
my_sites = ['kochetkov.spb.ru', 'теплорасчет.рф']

sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
df = pd.read_sql_query(f'SELECT se.date,se.num, se.site  \
                       ,case when se.site in {str(my_sites).replace("[","(").replace("]",")")} then 1 else 0 end as ord\
                       FROM serp as se, querries as q    \
                       where q.id= se.querry and q.querry="{word}" \
                       order by ord \
                       --and se.date>"2023-06-11" \
                       \
                       ', sqlite_connection)
sqlite_connection.close()
unique = df["site"].unique()
num_yours, num_others = 0, 0
palette = []
for s in unique:
    num_yours =   num_yours + 1 if     s in my_sites else num_yours
    num_others = num_others + 1 if not s in my_sites else num_others

for _ in range(num_others):
    palette.append(rnd.choice(px.colors.qualitative.Pastel2))
for i,_ in enumerate(range(num_yours)):
    palette.append(px.colors.qualitative.Plotly[i])

fig = px.line(df, x="date", y="num", color="site", markers=True, title=word,
              color_discrete_sequence=palette
              )
fig.update_traces(textposition="bottom right")
fig.update_layout(yaxis=dict(autorange="reversed", title=word))
fig.update_yaxes(dtick=1, showgrid=True)

fig.update_traces(marker_line_width=1, marker_size=15, line_width=10)
fig.show()