import sqlite3

db_file = "air_quality.db"

connection = sqlite3.connect(db_file)

cursor = connection.cursor()

sql_query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(sql_query)

print(f"Tables in {db_file}:")
print("  " + str(cursor.fetchall()))

print("\nColumns in table 'Observations':")
data = cursor.execute("""SELECT * FROM Observations""")
for column in data.description:
    print("  " + column[0])

print("\nNumber of rows in table 'Observations':")
nrows = cursor.execute("SELECT COUNT(*) FROM Observations").fetchall()
print("  " + str(nrows[0][0]))

print("\nAverage CO2 and temperature:")
rows = cursor.execute("SELECT AVG(co2), AVG(temp) FROM Observations").fetchall()
print("  CO2 (ppm): " + str(rows[0][0]))
print("  Temp (C):  " + str(rows[0][1]))
