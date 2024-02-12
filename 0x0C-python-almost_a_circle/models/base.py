#!/usr/bin/python3
"""
this file is for task 1 of this project
"""
import json
import csv


class Base:
    """this is the base class of almost a circle project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the initialization module."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this is a method to return json rep of the list."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls,list_objs):
        """this method right here will save json obj to a file"""
        if (list_objs is None):
            list_objs = []
            save_in_file = cls.__name__ + ".json"
            with open(save_in_file, 'w') as fil:
                js = cls.to_json_string([o.to_dictionary() for o in list_objs])
                fil.write(js) 

    @staticmethod
    def from_json_string(json_string):
        """this is the reverse of to_json_string()"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV format."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from CSV format."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []