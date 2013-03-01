import sys
import sqlite3

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
        print '0;Expected ' + row[2] + ' at (' + row[0] + ',' + row[1] + '), got: ' + row[3]
    else:
        print '1;Good Job!'

if __name__ == '__main__':
    main()
