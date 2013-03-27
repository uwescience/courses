import sys
import sqlite3
sys.path.append('../../../resources/lib/')
import grade_helper

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
        grade_helper.fail('Expected ' + str(row[2]) + ' for (' + str(row[0]) + ',' + str(row[1]) + '), got: ' + str(row[3]))
    else:
        grade_helper.success()
    
if __name__ == '__main__':
    main()
