import csv


def main():
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})

    # lambda can be used to call a function as a parametre
    # if it's only going to be used and called once
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")

    print("-------")

    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student['name']} is from {student['home']}")


if __name__ == "__main__":
    main()
