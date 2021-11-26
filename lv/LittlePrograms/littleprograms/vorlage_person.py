class Person:
    def __init__(self, vname, zname):
        self.vname = vname
        self.zname = zname

    def get_info(self):
        return f'{self.vname} {self.zname}'


class Student(Person):
    def get_info(self):
        return f'Student*in {self.vname} {self.zname}'


class Lektor(Person):
    def __init__(self, vname, zname, fb):
        super().__init__(vname, zname)
        self.fachbereich = fb
    def get_info(self):
        return f'Lektor*in {self.vname} {self.zname} im Fachbereich {self.fachbereich}'


class Mentor(Lektor):
    # kein init da keine eigenen neuen attribute
    def get_info(self):
        return f'Mentor*in {self.vname} {self.zname} kann gut zuhören'


if __name__ == '__main__':
    bunch_of_people = []
    bunch_of_people.append(Person("Hansi", "Hinterseer"))
    bunch_of_people.append(Student("Maria", "Musterstudi"))
    bunch_of_people.append(Lektor("Sandra", "Schuster", "Data Science"))
    bunch_of_people.append(Mentor("Kurti", "Hoergut", "Informatik"))

    for person in bunch_of_people:
        print(person.get_info())


