import sys
import sqlite3
sys.path.append('../../../resources/lib/')
import grade_helper

def main():
    con = sqlite3.connect(sys.argv[1])
    c = con.cursor()

    select = 'select c.row_num, c.col_num, c.value, stdn.value'
    from_clause = 'from c, stdn'
    where = 'where c.row_num = stdn.row_num and c.col_num = stdn.col_num and c.value != stdn.value'

    query = select + ' ' + from_clause + ' ' + where
    c.execute(query)
    row = c.fetchone()

    if row:
        grade_helper.fail('Expected ' + str(row[2]) + ' at (' + str(row[0]) + ',' + str(row[1]) + '), got: ' + str(row[3]))
    else:
        grade_helper.success()
    

if __name__ == '__main__':
    main()
