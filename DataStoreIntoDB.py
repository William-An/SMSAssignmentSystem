import sqlite3
database=sqlite3.connect("StudentsDatabase.db")
try:
    database.execute('''CREATE TABLE Students118(name text,class text,number int)''')
except sqlite3.OperationalError as err:
    print("Table already exists, "+str(err))
tempdatafile=open("database.txt",encoding="utf-8")
datatemp=[i for i in tempdatafile.readlines()]
data=[]
for i in datatemp:
    i=i.strip()
    i=i.split("|")
    if "18" in i[0]:
        data.append((i[2],i[0],eval(i[1])))
for j in data:
    database.execute('INSERT INTO students118 VALUES(?,?,?)',j)
database.commit()
database.close()