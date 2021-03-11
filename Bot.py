import sqlite3
from creds import database,table
conn=sqlite3.connect(database)
cur=conn.cursor()

def confirm_exists(name):
    cur.execute('SELECT Name FROM '+table+' WHERE Name like \'%'+name+'%\'')# MySQL query to search databse
    # PS:If you want,you can search multiple table simultaneously. just need to use the UNION function in  MySQL
    entries=cur.fetchall()
    return entries


print('Bot:Hello which movie are you looking for?')
while(True):
    user_msg=(input('User:')).lower()
    if(user_msg in ['bye','goodbye','thank you','thanks','tnx','goodnight']):
        print('My pleasure.')
        break
    name=confirm_exists(user_msg.lower())
    if len(name)==0:
        print('Media not found, try again')
        continue
    name=[str(i)[2:-3] for i in name]
    print('Heres what I found...')
    print('\n'.join(name))