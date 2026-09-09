print("===== Student Grade Manager =====")
students=[]

def add():
    name = input("Enter Your Name: ")
    mark = int(input("Enter Your Marks: "))
    sub = input("Enter Your Subject: ")

    student = {
    "name": name,
    "mark": mark,
    "sub": sub
    }

    students.append(student)
    print("-----Added Successfully-----")
    print()

def show():
    if len(students)==0:
        print("Student Not Found")
    else:
        for i in students:
            print("Name:",i["name"])
            print("Marks:".i["mark"])
            print("Subject:",i["sub"])
            print("----------")
def search():
    x = input("Enter Name: ")
    for i in students:
        if i["name"]==x:
            print("---Student Found---")
            print("Name:",i["name"])
            print("Marks:",i["mark"])
            print("Subject:",i["sub"])
            print("------0------")
            break
    else:
        print("Student Not Found!")
def grade():
    for i in students:
        if i["mark"] >= 80:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: A+")
            print("---------------")
        elif i["mark"] >= 70:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: A")
            print("---------------")
        elif i["mark"] >=60:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: A-")
            print("---------------")
        elif i["mark"]>=50:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: B")
            print("---------------")
        elif i["mark"]>=40:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: C")
            print("---------------")
        elif i["mark"]>=33:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: D")
            print("---------------")
        else:
            print("Name:",i["name"])
            print("Subject:",i["sub"])
            print("Grade: F")
            print("---------------")     
while True:
    print()
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Show Grade")
    print("5. Exit")
    print()

    option = int(input("Enter Your Option: "))
    print("---------------")

    if option==1:
        add()
    elif option==2:
        show()
    elif option==3:
        search()
    elif option==4:
        grade()
    elif option==5:
        break
    else:
        print("Try Again!")
