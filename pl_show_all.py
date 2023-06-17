from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly
import plotly.express as px
import pandas as pd
import sqlite3
import random as rnd


def plot_word(fig, word, row, my_sites):
    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    df = pd.read_sql_query(f'SELECT se.date,se.num, se.site  \
                               ,case when se.site in {str(my_sites).replace("[", "(").replace("]", ")")} then 1 else 0 end as ord\
                               FROM serp as se, querries as q    \
                               where q.id= se.querry and q.querry="{word}" \
                               order by ord \
                               --and se.date>"2023-06-11" \
                               \
                               ', sqlite_connection)
    sqlite_connection.close()
    unique_sites = df["site"].unique()
    for site in unique_sites:
        if site in my_sites:
            num = my_sites.index(site)
            color = px.colors.qualitative.Plotly[num]
        else:
            color = rnd.choice(px.colors.qualitative.Pastel2)
        fig.append_trace({
            'x': df.query(f'site == "{site}"')['date'],
            'y': df.query(f'site == "{site}"')['num'],
            'name': site,
            'text': site,
            'mode': 'lines+markers',
            'type': 'scatter',
            'line': {'color': color}
        }, row, 1)

def plot_all(my_sites, words_list):
    fig = plotly.subplots.make_subplots(rows=len(words_list), cols=1,
                                     shared_xaxes=False,
                                     vertical_spacing=0.03,
                                     horizontal_spacing=0.02,
                                     subplot_titles=words_list )
    # fig.layout.yaxis.range= [1,40]
    for i, word in enumerate(words_list):
        plot_word(fig, word, i+1, my_sites)
    fig.update_yaxes(autorange="reversed", dtick=1, showgrid=True, rangemode ="nonnegative")
    fig.update_traces(marker_line_width=1, marker_size=15, line_width=10)
    fig['layout'].update(height=len(words_list) * 800)

    fig.show()


if __name__ == "__main__":
    my_sites = ['kochetkov.spb.ru', 'теплорасчет.рф']
    words_list = ['kochetkov', 'kochetkov spb', 'точка росы', 'точка росы расчет','утеплитель купить']
    plot_all(my_sites, words_list)