from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly
import plotly.express as px
import pandas as pd
import requests
import random as rnd


def plot_word(fig, word, row, my_sites):
    start_date = '2023-06-01'

    ms_add = ' '.join([f'&my_sites={ms}' for ms in my_sites])
    # response = requests.get(f"http://192.168.1.33:8880/?start_date={start_date}&word={word}{ms_add}")
    response = requests.get(f"http://127.0.0.1:8880/?start_date={start_date}&word={word}{ms_add}")
    if response.ok:
        data = response.json()['data']
        df = pd.DataFrame(data)
    else:
        print("Ошибка при запросе данных")
        return False

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
    return True

def plot_all(my_sites, words_list):
    fig = plotly.subplots.make_subplots(rows=len(words_list), cols=1,
                                     shared_xaxes=False,
                                     vertical_spacing=0.03,
                                     horizontal_spacing=0.02,
                                     subplot_titles=words_list )
    # fig.layout.yaxis.range= [1,40]
    for i, word in enumerate(words_list):
        rez = plot_word(fig, word, i+1, my_sites)
        if not rez:
            return
    fig.update_yaxes(autorange="reversed", dtick=1, showgrid=True, rangemode ="nonnegative")
    fig.update_traces(marker_line_width=1, marker_size=15, line_width=10)
    fig['layout'].update(height=len(words_list) * 800)

    fig.show()


if __name__ == "__main__":
    my_sites = ['kochetkov.spb.ru', 'теплорасчет.рф']
    words_list = ['kochetkov', 'kochetkov spb', 'точка росы', 'точка росы расчет','утеплитель купить']
    plot_all(my_sites, words_list)