from parse_serp import get_serp
from dbinit import insert_serp

if __name__ == '__main__':
    try:
        rez = get_serp('kochetkov')
    except:
        print('error')
        quit()
    if len(rez)>0:
        insert_serp('kochetkov', rez)
    print('add', len(rez), 'rows')