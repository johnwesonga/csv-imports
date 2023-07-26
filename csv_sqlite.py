import pandas as pd
import sqlite3

conn = sqlite3.connect('my_data.db')
c = conn.cursor()

# load the data into a Pandas DataFrame
birthdays = pd.read_csv('birthdays.csv')
# write the data to a sqlite table
birthdays.to_sql('birthdays', conn, if_exists='append', index = False)
# read schema
c.execute("PRAGMA table_info('birthdays')") 
for row in c.fetchall():
    print(row)
# query table
#r = c.execute(f"SELECT * FROM birthdays").fetchall()
# print(r)
