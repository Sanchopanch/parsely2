import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import random

def diagr(word):
    number_of_colors = 200
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(number_of_colors)]


    # df = pd.read_csv('queueTable.csv')
    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    df = pd.read_sql_query(f'SELECT se.date,se.num, se.site FROM serp as se, querries as q\
                           where q.id= se.querry and q.querry="{word}"', sqlite_connection)
    sqlite_connection.close()




    df = df.assign(F = 7.5)
    df.loc[df['site']=='kochetkob.spb.ru', 'F'] = 2.0
    # df.loc[df['site']=='kochetkob.spb.ru', 'site'] = 16599713015387340

    sns.set_theme(style="ticks")
    f, ax = plt.subplots()
    plt.xticks(rotation = 'vertical')


    ax.tick_params(axis='x', rotation=90)
    g = sns.relplot(
        data=df,
        x="date", y="num", size="F",
        hue="site", #col="site",
        kind="line" ,#palette=palette,
        height=17, aspect=.6, facet_kws=dict(sharex=False), linewidth=6.5, legend=True
    )

    # plt.setp(g.get_legend().get_texts(), fontsize='22')

    for i, ax in enumerate(g.fig.axes):   ## getting all axes of the fig object
         ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.show()
    g.fig.show()


if __name__ == '__main__':
    diagr('kochetkov spb')