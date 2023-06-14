from parse_serp import get_serp
from dbinit import insert_serp

class Task():
    def __init__(self, key, deep):
        self.key = key
        self.deep = deep
        self.complete = False
        self.error = ''

if __name__ == '__main__':
    keys = ['kochetkov', 'kochetkov spb', 'точка росы']
    tasks = []
    for key in keys:
        tasks.append(Task(key, 4))

    for task in tasks:
        try:
            rez = get_serp(task.key, task.deep)
        except:
            print('error')
            quit()
        if len(rez)>0:
            insert_serp(task.key, rez)
        print(f'add {len(rez)} rows for {task.key}')
    print(f'all {len(tasks)} tasks complete!!!')