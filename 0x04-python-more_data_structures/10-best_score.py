#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b_k = max(a_dictionary, key=lambda k: a_dictionary[k])
        return b_k
    else:
        return None
