from parse_serp import get_serp
from dbinit import insert_serp

class Task():
    def __init__(self, key, deep):
        self.key = key
        self.deep = deep
        self.complete = False
        self.error = ''
        self.tries = 3

if __name__ == '__main__':
    tasks = []
    tasks.append(Task('kochetkov', 4))
    tasks.append(Task('kochetkov spb', 3))
    tasks.append(Task('точка росы', 5))
    tasks.append(Task('точка росы расчет', 2))
    tasks.append(Task('утеплитель купить', 6))




    somthong_worng = False
    for _ in range(3):
        for task in tasks:
            if task.complete:
                continue
            if task.tries == 0:
                task.error = 'error'
                somthong_worng = True
                continue

            try:
                rez = get_serp(task.key, task.deep)
            except:
                task.tries -=1

            if len(rez)>0:
                insert_serp(task.key, rez)
                task.complete = True
                print(f'add {len(rez)} rows for {task.key}')

    if not somthong_worng:
        print(f'***************** ALL {len(tasks)} tasks COMPLETE!!! ************')
    else:
        comp = 0
        uncomp = 0
        for task in tasks:
            if task.complete:
                comp +=1
            else:
                uncomp +=1
        print(f'??????? completed {comp}, uncompl {uncomp} ???????')
