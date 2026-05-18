students = {}

file = open("students.txt", "r")

for line in file:

    line = line.strip()

    info = line.split(",")

    sid = info[0]
    last = info[1]
    first = info[2]
    major = info[3]
    gpa = info[4]

    students[sid] = [last, first, major, gpa]

file.close()

choice = ""

while choice != "3":

    print("\nChoose an option:")
    print("1) Search by Last Name")
    print("2) Search by Major")
    print("3) Quit")

    choice = input("Enter choice: ")

    if choice == "1":

        lname = input("Enter last name: ")

        for sid in students:

            data = students[sid]

            if data[0] == lname:

                print(sid, data[0], data[1], data[2], data[3])

    elif choice == "2":

        major_search = input("Enter major: ")

        for sid in students:

            data = students[sid]

            if data[2] == major_search:

                print(sid, data[0], data[1], data[2], data[3])

    elif choice == "3":

        print("Goodbye")

    else:

        print("Invalid choice")