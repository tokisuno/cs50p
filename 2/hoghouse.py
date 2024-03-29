students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"}

for student in students:
    # key: student
    # * students[student] indexes student value
    #       into key to get corresponding house
    print(student, students[student], sep=", ")
