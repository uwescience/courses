import sys
import sqlite3

def main():
    con = sqlite3.connect(sys.argv[1])
    c = con.cursor()

    select = 'select t.term, t.doc_id, t.value, stdn.value'
    from_clause = 'from tfidf as t, stdn'
    where = 'where t.term = stdn.term and t.doc_id = stdn.doc_id and t.value != stdn.value'

    query = select + ' ' + from_clause + ' ' + where
    c.execute(query)
    row = c.fetchone()

    if row:
        print '0;Expected ' + row[2] + ' for (' + row[0] + ',' + row[1] + '), got: ' + row[3]
    else:
        print '1;Good Job!'
    

if __name__ == '__main__':
    main()
