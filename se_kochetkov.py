from parse_serp import get_serp
from datetime import date

if __name__ == '__main__':
    today = date.today()
    rez = get_serp('kochetkov')
    lines = []
    for i, app in enumerate(rez):
        lines.append("%s,%i,%s\n"%(today,i+1,app))
    file1 = open("kochetkov.csv", "a")
    file1.writelines(lines)
    file1.close()  # to change file access modes
    print('add', len(lines), 'rows')