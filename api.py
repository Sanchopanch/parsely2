from fastapi import FastAPI
from datetime import datetime
import sqlite3
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root(start_date: str, word: str):
    conn = sqlite3.connect('baseSerp.db', timeout=10)
    c = conn.cursor()
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    c.execute(f'SELECT se.date,se.num, se.site  \
                               FROM serp as se, querries as q    \
                               where q.id= se.querry and q.querry="{word}"\
                               and se.date>="{start_date}" \
                               \
                               ')
    rows = c.fetchall()
    results = []
    for row in rows:
        result = {'date': row[0], 'num': row[1], 'site': row[2]}
        results.append(result)
    conn.close()
    return {'data': results}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8880)