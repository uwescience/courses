import sys
import networkx
import MapReduce

def get_label(g, node):
    return g.node[node]['label']

def data(gml):
    results = {}
    g = networkx.read_gml(gml)
    nodes = g.nodes()
    for node in nodes:
        label = get_label(g, node)
        if label in results:
            raise Exception('namespace collision!')
        else:
            results[label] = []
        neighbors = g.neighbors(node)
        for neighbor in neighbors:
            results[label].append(get_label(g,neighbor))

    return results

def mapper(mr, person, friends):
    for friend in friends:
        mr.emit_intermediate(person, friend)

def reducer(mr, person, friend_list):
    count = len(friend_list)
    mr.emit((person, count))

def main():
    persons = data(sys.argv[1])
    MapReduce.execute(persons, mapper, reducer)

if __name__ == '__main__':
    main()
