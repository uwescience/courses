import sys
import json
import MapReduce

def is_order(record):
    return record[0] == 'order'

def is_line_item(record):
    return record[0] == 'line_item'

def strip_tag(record):
    return record[1:]

def cross(orders, line_items):
    results = []

    for order in orders:
        for line_item in line_items:
            results.append(order + line_item)

    return results

def mapper(mr, dataline):
    record = json.loads(dataline)
    mr.emit_intermediate(record[1], record)

def reducer(mr, key, records):
    records = list(records)
    orders = filter(is_order, records)
    orders = map(strip_tag, orders)
    line_items = filter(is_line_item, records)
    line_items = map(strip_tag, line_items)
    join = cross(orders, line_items)
    for record in join:
        mr.emit(record)

def main():
    data = open(sys.argv[1])
    MapReduce.execute(data, mapper, reducer)

if __name__ == '__main__':
    main()
