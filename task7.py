class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def full_info(self):
        return '{} {} {}'.format(self.name, self.age, self.major)


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve.full_info())
# <name: Steven Schultz, age: 23, major: English>
print(Johnny.full_info())
# <name: Jonathan Rosenberg, age: 24, major: Biology>