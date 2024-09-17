from enum import Enum


class Options(Enum):
    ADD = 1
    DISPLAY = 2
    DELETE = 3
    UPDATE = 4
    EXIT = 5


class Student:
    def __init__(self, name, age, major):
        self.__name = name
        self.__age = age
        self.__major = major

    def nameInput(self, input_value):
        if input_value and len(input_value) > 1:
            self.__name = input_value

    def ageInput(self, input_age):
        if input_age > 0:
            self.__age = input_age

    def majorInput(self, input_major):
        if len(input_major) > 0:
            self.__major = input_major

    def to_json(self):
        return {"name": self.__name, "age": self.__age, "major": self.__major}


class School:
    student_list = []

    @classmethod
    def display_students(cls):
        if not cls.student_list:
            print("No students enrolled.")
        else:
            for idx, student in enumerate(cls.student_list, 1):
                print(f"{idx}. {student.to_json()}")


class Actions:
    @staticmethod
    def add():
        name = input("Input student name: ")
        try:
            age = int(input("Input student age: "))
        except ValueError:
            print("Invalid age. Please enter a valid integer.")
            return
        major = input("Input student major: ")
        School.student_list.append(Student(name, age, major))
        print(f"Student {name} added to the school.\n")

    @staticmethod
    def display():
        School.display_students()

    @staticmethod
    def delete():
        if not School.student_list:
            print("No students to delete.")
            return
        School.display_students()
        try:
            index = int(input("Enter the number of the student to delete: ")) - 1
            if 0 <= index < len(School.student_list):
                removed_student = School.student_list.pop(index)
                print(f"Student {removed_student.to_json()['name']} has been removed from the school.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    @staticmethod
    def update():
        if not School.student_list:
            print("No students to update.")
            return
        School.display_students()
        try:
            index = int(input("Enter the number of the student to update: ")) - 1
            if 0 <= index < len(School.student_list):
                name = input("Input new student name: ")
                try:
                    age = int(input("Input new student age: "))
                except ValueError:
                    print("Invalid age input. Please enter a valid integer.")
                    return
                major = input("Input new student major: ")
                School.student_list[index] = Student(name, age, major)
                print(f"Student {index + 1} has been updated.\n")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    @staticmethod
    def exit():
        print("Exiting program.")
        exit()


def menu():
    while True:
        for option in Options:
            print(f'{option.name} - {option.value}')
        try:
            user_input = int(input("Please select an option: "))
            if user_input in Options._value2member_map_:
                return user_input
            else:
                print("Invalid option. Please select a valid number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    actions_map = {
        Options.ADD.value: Actions.add,
        Options.DISPLAY.value: Actions.display,
        Options.DELETE.value: Actions.delete,
        Options.UPDATE.value: Actions.update,
        Options.EXIT.value: Actions.exit,
    }

    while True:
        selected_option = menu()
        action = actions_map.get(selected_option)
        if action:
            action()
        else:
            print("This option is not yet implemented.")
