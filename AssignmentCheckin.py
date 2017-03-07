import sqlite3
database=sqlite3.connect("StudentsDatabase.db")
#name=database.execute('SELECT * from students WHERE number=?',(2015530115,))
#print(name.fetchone()[1])
t=input("Scan to start\n")
finished=[]
file=open("unfinished.txt","w",encoding="utf-8")
while (t!="STOPCHECK"):
    student=database.execute('SELECT * from students118 WHERE number=?',(t,))
    try:
        print(student.fetchone()[1]+" "+student.fetchone()[0])
        finished.append(eval(t))
    except TypeError as err:
        print("Not in the DB, "+str(err))
    t=input("NEXT!\n")
unfinished=set(database.execute("SELECT * from students118").fetchall())
try:
    for i in finished:
        unfinished.intersection(set(database.execute("SELECT * from students118 WHERE number <> ?",(i,)).fetchall())) #不行，这样print出了除了一个以外的students
except sqlite3.ProgrammingError as err:
    print("Wrong operation, "+str(err))
for i in unfinished:
    print(i[:2])
    file.write(i[0]+","+i[1]+"\n")
database.commit()
database.close()