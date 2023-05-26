import sqlite3 as sq 

db = sq.connect("main.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE adventures(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE trillers(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE action_movie(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE fantastik(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE drama(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE comedy(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE horrors(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE fantasy(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE family(
name TEXT,
age_group TEXT
)""")

cursor.execute("""CREATE TABLE jobs(
name TEXT,
job,
age_group TEXT
)""")


cursor.execute("""CREATE TABLE users(
user_name TEXT,
needed_time INTEGER
)""")

db.commit()
cursor.close()
db.close