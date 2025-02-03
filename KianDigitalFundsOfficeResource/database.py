import pymysql
from sqlalchemy import create_engine
import sqlite3
import pandas as pd     # pip install pandas

# Step 1: Create a table
connection = sqlite3.connect('persons.db')
# connection = sqlite3.connect(':memory')


# Step 2: Create a table
sql_create_table = """
CREATE TABLE persons (
    phone_number TEXT PRIMARY KEY,
    national_code TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    applications TEXT
)
"""

cursor = connection.cursor()
try:
    cursor.execute(sql_create_table)
    connection.commit()
except Exception as e:
    connection.rollback()



# Insert records
cursor = connection.cursor()
cursor.execute("INSERT INTO persons VALUES ('09375613855','1926655141','قدوسی','سمانه','email11@gmail.com')")
cursor.execute("INSERT INTO persons VALUES ('09375613845','3696511651','مرادی','سامان','email98@gmail.com')")
cursor.execute("INSERT INTO persons VALUES ('09375613832','5376938719','شهرابی','محمد','email772@gmail.com')")
cursor.execute("INSERT INTO persons VALUES ('09375613898','9517868340','شیری','فرزاد','email224@gmail.com')")
cursor.execute("INSERT INTO persons VALUES ('09375613874','3192113332','سهرابی','افسانه','email44@gmail.com')")
cursor.execute("INSERT INTO persons VALUES ('09375613866','2272273874','سهرابی زاد','سما','email16@gmail.com')")
connection.commit()



# Query records
sql_query = """
SELECT * FROM persons LIMIT 5
"""
rows = cursor.execute(sql_query)
columns = [col[0] for col in rows.description]
records = rows.fetchall()
connection.close()
print(columns)
print(records)

df = pd.DataFrame(records, columns=columns)
print(df.to_csv('data.csv'))




#
#
#
# # Using WITH statement to auto close connections
# from contextlib import closing
# import sqlite3
# import pandas as pd # pip install pandas
#
# with closing(sqlite3.connect('persons.db')) as connection2:
#     with closing(connection.cursor()) as cursor2:
#         cursor2.execute("INSERT INTO persons VALUES ('09375613855','1926655141','قدوسی','سمانه','email11@gmail.com')")
#         cursor2.execute("INSERT INTO persons VALUES ('09375613845','3696511651','مرادی','سامان','email98@gmail.com')")
#         cursor2.execute("INSERT INTO persons VALUES ('09375613832','5376938719','شهرابی','محمد','email772@gmail.com')")
#         cursor2.execute("INSERT INTO persons VALUES ('09375613898','9517868340','شیری','فرزاد','email224@gmail.com')")
#         cursor2.execute("INSERT INTO persons VALUES ('09375613874','3192113332','سهرابی','افسانه','email44@gmail.com')")
#         cursor2.execute("INSERT INTO persons VALUES ('09375613866','2272273874','سهرابی زاد','سما','email16@gmail.com')")
#         connection.commit()
#
#         rows2 = cursor2.execute()
#         columns2 = [col[0] for col in rows2.description]
#         records2 = rows.fetchall()
#         df = pd.DataFrame(records, columns=columns)
# print(df)
#
