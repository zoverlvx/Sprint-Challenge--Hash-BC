#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import HashTable, hash_table_insert, hash_table_retrieve


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # gives me an index of the weight and gives me the weight
    for index, weight in enumerate(weights):
        # inserts a hashtable, weight, and its index
        hash_table_insert(ht, weight, index)

    for index, weight in enumerate(weights):
        eq = limit - weight
        ind = hash_table_retrieve(ht, eq)
        if ind:
            if index > ind:
                return (index, ind)
            else:
                return (ind, index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
