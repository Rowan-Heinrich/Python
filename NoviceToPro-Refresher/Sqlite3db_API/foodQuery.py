import sqlite3, sys
# this program uses sys.argv, therefore must be run in commandline.

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names,row):
        print("%s: %s" % pair)
    print(" ")
conn.close()
