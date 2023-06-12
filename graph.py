import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import random

from matplotlib.ticker import MultipleLocator

def diagr(word):

    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    df = pd.read_sql_query(f'SELECT se.date,se.num, se.site FROM serp as se, querries as q\
                           where q.id= se.querry and q.querry="{word}" \
                           --and se.date>"2023-06-11"', sqlite_connection)
    sqlite_connection.close()


    sns.set_theme(style="ticks")
    f, ax = plt.subplots()
    plt.xticks(rotation='vertical')
    plt.rcParams['legend.fontsize'] = 6

    unique = df["site"].unique()
    hue_order = unique.tolist()
    if 'kochetkov.spb.ru' in hue_order:
        hue_order.remove('kochetkov.spb.ru')
    hue_order.insert(0,'kochetkov.spb.ru')
    palette = dict()
    for key in unique:
        palette[key] = (0., random.random(), random.random())
    palette['kochetkov.spb.ru'] = (.9, 0., 0.)


    ax.tick_params(axis='x', rotation=90)
    g = sns.relplot(
        data=df,
        x="date", y="num", #size="F",
        hue="site",# col="F",
        kind="line", palette=palette,
        height=10, aspect=0.7, facet_kws=dict(sharex=False), linewidth=3.5, legend='brief'
        ,hue_order=hue_order
    )

    g.axes[0][0].invert_yaxis()
    for ax in g.axes.flatten():
        ax.grid()

    for i, ax in enumerate(g.fig.axes):   ## getting all axes of the fig object
         ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.show()
    g.fig.show()



if __name__ == '__main__':
    diagr('kochetkov spb')