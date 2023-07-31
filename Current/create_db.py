import sqlite3

con = sqlite3.connect("expenses")

cur = con.cursor()

cur.execute("""CREATE TABLE expenses
            (id INTEGER PRIMARY KEY,
            Date DATE,
            description TEXT,
            category TEXT,
            price REAL)""")

con.commit()
con.close()