import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import random

from matplotlib.ticker import MultipleLocator

def diagr(word):
    number_of_colors = 200
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(number_of_colors)]


    # df = pd.read_csv('queueTable.csv')
    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    df = pd.read_sql_query(f'SELECT se.date,se.num, se.site FROM serp as se, querries as q\
                           where q.id= se.querry and q.querry="{word}"', sqlite_connection)
    sqlite_connection.close()




    df = df.assign(F = 3.0)
    df.loc[df['site']=='kochetkov.spb.ru', 'F'] = 5.0
    # df.loc[df['site']=='kochetkob.spb.ru', 'site'] = 16599713015387340

    sns.set_theme(style="ticks")
    # sns.set_style("darkgrid")
    f, ax = plt.subplots()
    plt.xticks(rotation = 'vertical')
    plt.rcParams['legend.fontsize'] = 6

    unique = df["site"].unique()
    palette = dict(zip(unique, sns.color_palette(n_colors=len(unique))))
    # palette.update({"Total": "k"})
    palette['kochetkov.spb.ru'] = (0., 0., 0.)

    ax.tick_params(axis='x', rotation=90)
    g = sns.relplot(
        data=df,
        x="date", y="num", sizes="F",
        hue="site",# col="F",
        kind="line", palette=palette,
        height=10, aspect=0.7, facet_kws=dict(sharex=False), linewidth=3.5, legend='full'

    )

    g.axes[0][0].invert_yaxis()
    for ax in g.axes.flatten():
        ax.grid()

    for i, ax in enumerate(g.fig.axes):   ## getting all axes of the fig object
         ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    # plt.gridd()
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.show()
    g.fig.show()



if __name__ == '__main__':
    diagr('kochetkov spb')