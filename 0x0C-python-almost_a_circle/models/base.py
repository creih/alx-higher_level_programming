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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this is a method to return json rep of the list."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this method right here will save json obj to a file"""
        if (list_objs is None):
            list_objs = []
            save_in_file = Base + ".json"
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
                for dictionary in dictionaries:
                    instances = cls.create(**dictionary)
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV format."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                elif cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

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
                        instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[0])
                                )
                    elif cls.__name__ == "Square":
                        instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[0])
                                )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics."""
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")
        screen.setup(width=800, height=600)
        screen.tracer(1)

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.end_fill()

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        screen.update()
        turtle.done()
