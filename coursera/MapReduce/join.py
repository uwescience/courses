import sys
import MapReduce


def data(orders, line_items):
    records = {}

    for order in orders:
        record = order.strip().split('|')
        records.setdefault(record[0], [])
        records[record[0]].append(record[:9])
        
    for line_item in line_items:
        record = line_item.strip().split('|')
        records.setdefault(record[0], [])
        records[record[0]].append(record[:16])

    return records

def is_order(record):
    return len(record) == 9 

def is_line_item(record):
    return len(record) == 16

def cross(orders, line_items):
    results = []

    for order in orders:
        for line_item in line_items:
            results.append(order + line_item)

    return results

def mapper(mr, key, records):
    for record in records:
        mr.emit_intermediate(key, record)

def reducer(mr, key, records):
    records = list(records)
    orders = filter(is_order, records)
    line_items = filter(is_line_item, records)
    join = cross(orders, line_items)
    for record in join:
        mr.emit(record)

def main():
    orders = open(sys.argv[1])
    line_items = open(sys.argv[2])
    MapReduce.execute(data(orders, line_items), mapper, reducer)

if __name__ == '__main__':
    main()
