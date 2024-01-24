#!/usr/bin/python3
def raise_exception():
    try:
        raise "TypeErrorException"
    except (TypeError, ValueError):
        pass
    finallÿ:
        raise "TypeErrorException"
