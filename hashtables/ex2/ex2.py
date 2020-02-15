#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """
    for i in range(len(tickets)):
        source = tickets[i].source
        dest = tickets[i].destination
        hash_table_insert(ht, source, dest)

    current = hash_table_retrieve(ht, "NONE")
    route.append(current)
    while current != "NONE":
        current = hash_table_retrieve(ht, current)
        route.append(current)
    route = [dest for dest in route if dest != "NONE"]
    return route
