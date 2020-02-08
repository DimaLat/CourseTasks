import json
import os

students_path = "files/students.json"
rooms_path = "files/rooms.json"


def parsing_reading(parsing_filename):
    """This function helps to parse data from files"""
    with open(os.path.join(parsing_filename), 'r') as file:
        return json.load(file)


class Rooms:
    """This class contains list of parsing rooms"""

    def __init__(self, file_path):
        self.list_object = parsing_reading(file_path)


class Students:
    """This class contains list of parsing students"""

    def __init__(self, file_path):
        self.list_object = parsing_reading(file_path)


class Unite:
    """This class is for unite data from objects Rooms and Students """

    def __init__(self, *, student: Students, room: Rooms):
        self.students_data = student.list_object
        self.rooms_data = room.list_object

    def relocate(self):
        total_data = self.rooms_data
        for student in self.students_data:
            if "students_names" in total_data[student["room"]]:
                total_data[student["room"]]["students_names"] += [student["name"]]
            else:
                total_data[student["room"]]["students_names"] = [student["name"]]
        return total_data


def save_in_json(data):
    with open(os.path.join('.', 'files/students_relocation.json'), 'w') as f:
        json.dump(data, f, indent=4)


rooms = Rooms(file_path=rooms_path)
students = Students(file_path=students_path)
processed_data = Unite(student=students, room=rooms).relocate() # убрать принт
save_in_json(processed_data)
