import sqlite3
from creds import database,table
conn=sqlite3.connect(database)# your database name
cur=conn.cursor()

def confirm_exists(name):
    cur.execute('SELECT Name FROM '+table+' WHERE Name like \'%'+name+'%\'')# MySQL query to search databse
    # PS:If you want,you can search multiple table simultaneously. just need to use the UNION function in  MySQL
    entries=cur.fetchall()
    return entries

def lookup(user_msg):
    if(user_msg.lower() in ['bye','thank you']):# you can add as many phrase you like
        return 'Happy to help.'
    name=confirm_exists(user_msg.capitalize())
    if len(name)==0:
        return 'Oops, the media you are looking isn\'t in your collection.'
    name=[str(i)[2:-3] for i in name] # strign manipulation to make the message look appealing
    out='Heres what I found...\n'+'\n'.join(name)
    return out