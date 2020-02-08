import json
import os

rooms_location = "files/rooms.json"
students_location = "files/students.json"


# format


def parsing_reading(parsing_filename):
    """This function is for parsing data from files"""
    with open(os.path.join(parsing_filename), 'r') as file:
        return json.load(file)


class Rooms:
    """This class is for list of parsing rooms"""

    def __init__(self, file_location):
        self.list_object = parsing_reading(file_location)


class Students:
    """This class is for list of parsing students"""

    def __init__(self, file_location):
        self.list_object = parsing_reading(file_location)


class Unite:
    """This class is for unite data from objects Rooms and Students """

    def __init__(self, room: Rooms, student: Students):
        self.rooms_data = room.list_object
        self.students_data = student.list_object

    def relocate(self):
        relocation_list = self.rooms_data
        for student in self.students_data:
            if "students_name" in relocation_list[student["room"]]:
                relocation_list[student["room"]]["students_name"] += [student["name"]]
            else:
                relocation_list[student["room"]]["students_name"] = [student["name"]]
        return relocation_list


def save_as_json(relocation_list):
    with open(os.path.join('files/students_relocation.json'), 'w') as file:
        json.dump(relocation_list, file, indent=4)


def main():
    rooms = Rooms(file_location=rooms_location)
    students = Students(file_location=students_location)
    students_relocation_list = Unite(student=students, room=rooms).relocate()
    save_as_json(students_relocation_list)


main()
