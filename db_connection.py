import csv
import sqlite3 as sql

def csv_read(name):
    file = open("spreadsheets/%s.csv"%(name))
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows

#connection to the database
def connection():
    con=sql.connect('database.db')
    cursor=con.cursor()
    return con,cursor

def add_quote(a):
    return '"{0}"'.format(a)

if __name__=="__main__":
    con,cur=connection()
    # cur.execute('insert into users values({},{},"sdg","sdf")'.format('"1003"','"kudd"'))
    # con.commit()
    
    for value in csv_read("user_login"):
        cur.execute('insert into users values("{0}","{1}","{2}","{3}")'.format(value[0],value[1],value[2],value[3]))
    con.commit()
    
    for value in csv_read("police_records"):
        cur.execute('insert into police_records values("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8]))
    con.commit()
    cur.close()
    con.close()
    





