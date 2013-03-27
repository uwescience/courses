import sys
import sqlite3    
import MapReduce


def data(db_conn):
    curs = db_conn.cursor()
    records = {}
    
    curs.execute('select * from a where a.row_num <= 10 and a.col_num <= 10')
    a_rows = curs.fetchall()
    curs.execute('select * from b where b.row_num <= 10 and b.col_num <= 10')
    b_rows = curs.fetchall()

    for ai, aj, avalue in a_rows:
        for bi, bj, bvalue in b_rows:
            records[(ai, aj, bi, bj)] = (avalue, bvalue) # from

    return records # joined rows

# key = (ai, aj, bi, bj)
# val = (aval,  bval)
def mapper(mr, key, val):
    if key[1] == key[2]: # where filter
        mr.emit_intermediate((key[0], key[3]), val) # group by

#keys should be in the form (a.row, b.col)
#records shuld be (a.row, a.col, a.val, b.row, b.col, b.val)
#for all records, a.col == b.row
def reducer(mr, key, values):
    result = 0
    for aval, bval in values:
        result = result + aval * bval
    mr.emit((key[0], key[1], result))

def main():
    conn = sqlite3.connect(sys.argv[1])
    MapReduce.execute(data(conn), mapper, reducer)

if __name__ == '__main__':
    main()
