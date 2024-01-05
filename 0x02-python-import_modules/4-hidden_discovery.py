#!/usr/bin/python3
import dis
import hidden_4

def discover_names(module):
    """
    this is a function
    """
    names = [name for name in dir(module) if not name.startswith("__")]
    names.sort()
    return names

if __name__ == "__main__":
    module_names = discover_names(hidden_4)
    for name in module_names:
        print(name)
