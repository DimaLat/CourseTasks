import json
import os

with open('files/rooms.json') as f:
    room_list = json.load(f)

with open('files/students.json') as file:
    student_list = json.load(file)


relocation_list = []

for student_dict in student_list:
    for room_dict in room_list:
        new_dict = {}
        if student_dict['room'] == room_dict['id']:
            new_dict["student_name"] = student_dict['name']
            new_dict.update(room_dict)
            relocation_list.append(new_dict)

with open(os.path.join('.', 'files/students_relocation.json'), 'w') as f:
        json.dump(relocation_list, f, indent=4)
