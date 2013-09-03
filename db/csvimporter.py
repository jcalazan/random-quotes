import csv
import sqlite3

with open('db/randomquotes.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        if not row[1] or row[1] == 'NULL':
            row[1] = 'Anonymous'
        
        try:
            conn = sqlite3.connect('db/randomquotes')
            c = conn.cursor()
            query = "INSERT INTO quotes (quote, author) VALUES ('%s', '%s')" % \
                    (row[0].replace("'", "''"), row[1].replace("'", "''"))
            print query
            c.execute(query)
            conn.commit() 
        except sqlite3.Error, e:
            print e.message
        finally:
            conn.close()