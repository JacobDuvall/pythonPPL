# Author: Jacob Duvall
# Date: April 22, 2019

# store student's information
# a student has an id number, name, grade, type, and optional location

# beginning of html
def starthtml(output):
    output.write('<html>')
    output.write('<style> table { border-collapse: collapse; width: 15%; } table td { width: 50%; text-align: left;}  '
                 'table , td, th { border: 1px solid black; } </style>')
    output.write('<body>')
    output.write('<table>')

# bulk of html data for students
def html(output, student):
    output.write('<tr>')
    output.write('<td>')
    output.write(student.id)
    output.write('</td>')
    output.write('<td>')
    output.write(student.first_name)
    output.write('</td>')
    output.write('<td>')
    output.write(student.last_name)
    output.write('</td>')
    output.write('<td>')
    output.write(student.letter)
    output.write('</td>')
    output.write('</tr>')

# end of html
def endhtml(output):
    output.write('</table>')
    output.write('</body>')
    output.write('</html>')

# stores student information: id, first name, last name, grade, type, location, and letter
class Student:

    # constructor for all variables
    def __init__(self, id, first_name, last_name, grade, type, location, letter = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.type = type
        self.location = location

    # sets letter grade variable
    def set_letter_grade(self, letter):
        self.letter = letter


def main():

    list = []  # input list with all parameters
    student = []  # student list of objects
    number_of_students = 0  # number of students created

    # Read in the input file
    with open("input.txt") as file:
        for line in file:
            for word in line.split():
                list.append(word)

    # Create student objects
    while list:

        location = ""  # student location
        count = 0  # count for location
        counter = 0  # count to pop list items based on location length
        student_info = []  # list of ID, Name, Grade, Type, and Location used to create student objects

        # append student ID
        student_info.append(list.pop(0))

        # append student First Name
        student_info.append(list.pop(0))

        # append student Last Name
        student_info.append(list.pop(0))

        # append student Grade
        student_info.append(list.pop(0))

        # append student Type
        student_info.append(list.pop(0))

        # append student Location
        for i in list:
            if i[0] is not "1" and i[0] is not "2" and i[0] is not "3" and i[0] is not "4" \
                    and i[0] is not "5" and i[0] is not "6" and i[0] is not "7"\
                    and i[0] is not "8" and i[0] is not "9" and i[0] is not "0":
                location += i
                location += " "
                count += 1
            else:
                break
        while counter != count:
            list.pop(0)
            counter += 1
        student_info.append(location)

        # Create student object
        student.append(Student(student_info[0], student_info[1], student_info[2], student_info[3],
                               student_info[4], student_info[5]))
        number_of_students += 1

    # Sort student objects based on grade and type (if tied, type E goes ahead of type L)
    newlist = sorted(student, key=lambda x: (x.grade, False if x.type == "L" else True), reverse=True)

    # Assign letter grades (top 1/3 = A, middle 1/3 = B, bottom 1/10 = F, else decided by type)
    # Assign A's
    A = int(number_of_students * 1/3)
    for i in range(0, A):
        newlist[i].set_letter_grade("A")

    # Assign B's
    B = 2*A
    for i in range(A, B):
        newlist[i].set_letter_grade("B")

    # Assign C's and D's
    Fnum = int(number_of_students * 1/10) + (number_of_students // 1/10 > 0)
    F = number_of_students - Fnum
    for i in range(B, F):
        if newlist[i].type == "E":
            newlist[i].set_letter_grade("C")
        else:
            newlist[i].set_letter_grade("D")

    # Assign F's
    for i in range(F, number_of_students):
        newlist[i].set_letter_grade("F")

    # Sort list by Last Name, then sort list by First Name, then sort list by ID
    alphabetical_list = sorted(newlist, key=lambda x: (x.last_name, x.first_name, x.id), reverse=False)

    # Display the beautiful finished product
    for i in range(0, number_of_students):
        print(alphabetical_list[i].id, alphabetical_list[i].first_name,
              alphabetical_list[i].last_name, alphabetical_list[i].letter)

    # create output.html file
    output = open("output.html", "w")

    # start html output
    starthtml(output)

    # create html output for students
    for i in range(0, number_of_students):
        html(output, alphabetical_list[i])

    # end html output
    endhtml(output)

# run program
if __name__ == "__main__": main()