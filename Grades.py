# Import Statements
from tkinter import *


mainWindow = Tk()
classes =[]
grades = []

def mainWindowSetup():

    # Setup the main window
    mainWindow.geometry("600x500")
    mainWindow.title("GPA Calculator")
    mainWindow.configure(background="#353b48")

    # Add a label
    Label(mainWindow, text="Welcome to the GPA Calculator", bg="#353b48", fg="#f8a5c2", font="menlo 28 bold").place(relx=0.5, y=25, anchor=CENTER)
    Label(mainWindow, text="Created by Pratham Patel", bg="#353b48", fg="#f8a5c2", font="menlo 22 bold").place(relx=0.5, y=400, anchor=CENTER)

    # Adding Buttons
    Button(mainWindow, text="Create a New Semester", highlightbackground="#9c88ff", fg="#596275", command=newSem, width="20", padx="20", pady="20", font="menlo 16 bold" ).place(relx=0.5, y= 150, anchor=CENTER)
    Button(mainWindow, text="Calculate from Past", highlightbackground="#74b9ff", fg="#596275", command=oldSem, width="20", padx="20", pady="20", font="menlo 16 bold").place(relx=0.5, y= 300, anchor=CENTER)

    # Actually run the program
    mainWindow.mainloop()

# function to deiconify
def deiconify(window):
    mainWindow.deiconify()
    window.destroy()

### NEW SEMESTER WORK ###
def newSem():
    newWindow = Tk()
    newWindow.geometry("400x400")
    newWindow.configure(background="#353b48")
    mainWindow.iconify()
    newWindow.title("Create a New Semester")

    #Finding out how many classes
    Label(newWindow, text="Please enter the number of classes", bg="#353b48", fg="#63cdda", font="menlo 16 bold").place(relx=0.5, rely=0.15, anchor=CENTER)
    numClasses = Entry(newWindow, width="20", bg="#7f8fa6", font="menlo 15", fg="#ff9ff3", justify="center")
    numClasses.place(relx=0.5, rely=0.5, anchor=CENTER)

    Button(newWindow, text="SUBMIT", highlightbackground="#1dd1a1", fg="#222f3e", command= lambda: allClasses(numClasses, newWindow), width="20", font="menlo 16 bold", justify="center").place(relx=0.5, rely=0.60, anchor=CENTER)

    newWindow.mainloop()

def allClasses(numClasses, newWindow):
    totalClasses = int(numClasses.get())
    for widget in newWindow.winfo_children():
        widget.destroy()
    Label(newWindow, text="Please enter all of your classes here", bg="#353b48", fg="#63cdda", font="menlo 16 bold").place(relx=0.5, rely=0.15, anchor=CENTER)


    #Naming all classes
    for x in range(totalClasses):
        className = Entry(newWindow, width=20, bg="#7f8fa6", font="menlo 15", fg="#ff9ff3", justify="center")
        className.place(relx=0.5, y=(x*30)+150, anchor=CENTER)
        classes.append(className)

    Button(newWindow, text="SUBMIT", highlightbackground="#1dd1a1", fg="#222f3e", command= lambda: outputWrite(newWindow), width="20", font="menlo 16 bold").place(relx=0.5, y=(totalClasses*30)+200, anchor=CENTER)

# saving all into a text file
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
    Label(newWindow, text="Your classes have been saved!", bg="#353b48", fg="#63cdda", font="menlo 16 bold").place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(newWindow, text="OKAY", highlightbackground="#0be881", fg="#596275", command= lambda: deiconify(newWindow), width="20", font="menlo 16 bold").place(relx=0.45, rely=0.65, anchor=CENTER)


### OLD SEMESTER WORK ###
def oldSem():
    oldWindow = Tk()
    oldWindow.geometry("400x400")
    oldWindow.configure(background="#353b48")
    oldWindow.title("Semester Grades")
    mainWindow.iconify()
    textfile = open("semester.txt", "r")
    classes = textfile.read().split(",")
    classes.pop()

    for x in range(len(classes)):
        Label(oldWindow, text=classes[x], bg="#353b48", fg="#63cdda", font="menlo 16 bold").place(relx=0.3, y=(x*30)+150, anchor=CENTER)
        grade = Entry(oldWindow, width=20, bg="#7f8fa6", justify="center", font="menlo 15", fg="#ff9ff3")
        grade.place(relx=0.67, y=(x*30)+150, anchor=CENTER)
        grades.append(grade)

    Button(oldWindow, text="SUBMIT", highlightbackground="#1dd1a1", fg="#222f3e", command= lambda: mathCalc(oldWindow), width="20", font="menlo 16 bold").place(relx=0.5, y=(len(classes)*30)+200, anchor=CENTER)

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

    Label(oldWindow, text="Your GPA currently is: "+ str(gpa), bg="#353b48", fg="#63cdda", font="menlo 16 bold").place(relx=0.5, rely=0.35, anchor=CENTER)
    Button(oldWindow, text="OKAY", highlightbackground="#0be881", fg="#596275", command= lambda: deiconify(oldWindow), width="20", font="menlo 16 bold").place(relx=0.5, rely=0.55, anchor=CENTER)

mainWindowSetup()
