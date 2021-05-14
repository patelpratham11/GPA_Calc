# Import Statements
from tkinter import *


mainWindow = Tk()
classes =[]
grades = []

def mainWindowSetup():

    # Setup the main window
    mainWindow.geometry("800x500")
    mainWindow.title("GPA Calculator")
    mainWindow.configure(background="#485460")

    # Add a label
    Label(mainWindow, text="Welcome to the GPA Calculator created by Pratham Patel", bg="#485460", fg="white", font="menlo 22 bold").grid(row=0, column=1, sticky=N)

    # Adding Buttons
    Button(mainWindow, text="Create a New Semester", highlightbackground="#ff5e57", fg="#1e272e", command=newSem, width="20").grid(row=1, column=1, sticky=N)
    Button(mainWindow, text="Calculate from Past", bg="#808e9b", fg="#1e272e", command=oldSem, width="20").grid(row=2, column=1, sticky=N)

    # Actually run the program
    mainWindow.mainloop()


### NEW SEMESTER WORK ###
def newSem():
    newWindow = Tk()
    newWindow.geometry("400x400")
    newWindow.configure(background="#485460")
    mainWindow.iconify()
    newWindow.title("Create a New Semester")

    #Finding out how many classes
    numClasses = Entry(newWindow, width=20, bg="white")
    numClasses.grid(row=0, column=0, sticky=NE)

    Button(newWindow, text="SUBMIT", bg="#0be881", fg="#d2dae2", command= lambda: allClasses(numClasses, newWindow), width="20").grid(row=1, column=0, sticky=NE)

    newWindow.mainloop()

def allClasses(numClasses, newWindow):
    totalClasses = int(numClasses.get())
    numClasses.destroy()
    Label(newWindow, text="Please enter all of your classes here", bg="black", fg="white", font="menlo 12 bold").grid(row=0, column=1, sticky=N)


    #Naming all classes
    for x in range(totalClasses):
        className = Entry(newWindow, width=20, bg="white")
        className.grid(row=x+1, column=1, sticky=N)
        classes.append(className)

    Button(newWindow, text="SUBMIT", bg="#0be881", fg="#d2dae2", command= lambda: outputWrite(newWindow), width="20").grid(row=totalClasses+1, column=1, sticky=N)


def outputWrite(newWindow):

    #Save information into a text file
    textfile = open("semester.txt", "w")
    for value in classes:
        textfile.write(str(value.get()) +",")
    textfile.close()

    # Clear window
    for widget in newWindow.winfo_children():
        widget.destroy()

    #Message saying everything has been saved
    Label(newWindow, text="Your classes have been saved!", bg="black", fg="white", font="menlo 12 bold").grid(row=0, column=1, sticky=N)
    mainWindow.deiconify()
    newWindow.destroy()


### OLD SEMESTER WORK ###
def oldSem():
    oldWindow = Tk()
    oldWindow.geometry("400x400")
    oldWindow.configure(background="#485460")
    oldWindow.title("Semester Grades")

    textfile = open("semester.txt", "r")
    classes = textfile.read().split(",")
    classes.pop()

    for x in range(len(classes)):
        Label(oldWindow, text=classes[x], bg="black", fg="white", font="menlo 12 bold").grid(row=x+1, column=1, sticky=N)
        grade = Entry(oldWindow, width=20, bg="white")
        grade.grid(row=x+1, column=2, sticky=N)
        grades.append(grade)

    Button(oldWindow, text="SUBMIT", bg="#0be881", fg="#d2dae2", command= lambda: mathCalc(oldWindow), width="20").grid(row=len(classes)+1, column=1, sticky=N)

def mathCalc(oldWindow):
    gpa = 0;
    for grade in grades:
        grade = int(grade.get())
        if(grade >= 93):
            gpa += 4.0
        elif(grade < 93 and grade >= 90):
            gpa += 3.75
        elif(grade < 90 and grade >= 87):
            gpa += 3.25
        elif(grade < 87 and grade >= 83):
            gpa += 3.0
        elif(grade < 83 and grade >= 80):
            gpa += 2.75
        elif(grade < 80 and grade >= 77):
            gpa += 2.25
        elif(grade < 77 and grade >= 73):
            gpa += 2
        elif(grade < 73 and grade >= 70):
            gpa += 1.75
        elif(grade < 70 and grade >= 67):
            gpa += 1.25
        elif(grade < 67 and grade >= 63):
            gpa += 1
        elif(grade < 63 and grade >= 60):
            gpa += 0.75
        elif(grade < 60):
            gpa += 0


    gpa = gpa/len(grades)

    for widget in oldWindow.winfo_children():
        widget.destroy()

    Label(oldWindow, text=gpa, bg="black", fg="white", font="menlo 12 bold").grid(row=len(grades)+2, column=1, sticky=N)

mainWindowSetup()
