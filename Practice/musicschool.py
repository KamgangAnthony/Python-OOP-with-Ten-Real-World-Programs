class MusicSchool:

    students = {
        "Gino": [15, "653-235-345", ["Piano", "Guitar"]],
        "Talina": [28, "555-765-452", ["Cello"]],
        "Eric": [12, "583-356-223", ["Singing"]]
    }

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue


    def print_students_data(self):
        for student in MusicSchool.students:
            self.print_student(student)

    def print_student(self, name):
        print(f"Student: {name} who is {MusicSchool.students[name][0]} years old and is taking {MusicSchool.students[name][2]}")

    def add_student(self, name, list_of_information):
        MusicSchool.students[name] = [list_of_information[0], list_of_information[1], [list_of_information[2]]]

new_music_school = MusicSchool(8, 15000)
new_music_school.print_students_data()
new_music_school.print_student("Gino")
new_music_school.add_student("Jack", [60, "562-234-234", "Piano"])

new_music_school.print_student("Jack")