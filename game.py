#Ryan Blaschke
#Advanced Computer Programming
#11/17/16
#game.py
#Version .1

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
########################

########################################################################
'''This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
##############################################################################


root = Tk()
root.title(string="12 Times Tables Quiz")

def about():
    messagebox.showinfo(title="Version.1", message="Math Trivia game based on the 12 times tables, answer each question as best as you can using your knowledge")



#check answers finish, scoring answers
def checkanswersfinish():
    score = numofcorrect*10
    score = str(score)
    numofcorrectlabel = ttk.Label(root, text="You scored a " + score + "!")
    numofcorrectlabel.grid(column=0, row=11, sticky=E)


def checkten():
    global numofcorrect
    if questiontenanswer.get() == 144:
        numofcorrect += 1
        checkanswersfinish()
    else:
        checkanswersfinish()

def checknine():
    global numofcorrect
    if questionnineanswer.get() == 132:
        numofcorrect += 1
        checkten()
    else:
        checkten()

def checkeight():
    global numofcorrect
    if questioneightanswer.get() == 110:
        numofcorrect += 1
        checknine()
    else:
        checknine()

def checkseven():
    global numofcorrect
    if questionsevenanswer.get() == 81:
        numofcorrect += 1
        checkeight()
    else:
        checkeight()

def checksix():
    global numofcorrect
    if questionsixanswer.get() == 72:
        numofcorrect += 1
        checkseven()
    else:
        checkseven()

def checkfive():
    global numofcorrect
    if questionfiveanswer.get() == 56:
        numofcorrect += 1
        checksix()
    else:
        checksix()

def checkfour():
    global numofcorrect
    if questionfouranswer.get() == 54:
        numofcorrect += 1
        checkfive()
    else:
        checkfive()

def checkthree():
    global numofcorrect
    if questionthreeanswer.get() == 24:
        numofcorrect += 1
        checkfour()
    else:
        checkfour()

def checktwo():
    global numofcorrect
    if questiontwoanswer.get() == 12:
        numofcorrect += 1
        checkthree()
    else:
        checkthree()



def checkone():
    global numofcorrect
    if questiononeanswer.get() == 4:
        numofcorrect=0
        numofcorrect += 1
        checktwo()
    else:
        checktwo()

#start checking answers, one at a time, starting with number one
def checkanswersstart():
    checkone()



#menus
##File menu
TopMenu = Menu(root)
root.config(menu=TopMenu)
SubMenu = Menu(TopMenu)
TopMenu.add_cascade(label="File", menu=SubMenu)
SubMenu.add_command(label="Exit", command=root.quit)

#Help Menu
HelpMenu = Menu(TopMenu)
TopMenu.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About", command=about)

#question variables
questiononeanswer = IntVar()
questiontwoanswer = IntVar()
questionthreeanswer = IntVar()
questionfouranswer = IntVar()
questionfiveanswer = IntVar()
questionsixanswer = IntVar()
questionsevenanswer = IntVar()
questioneightanswer = IntVar()
questionnineanswer = IntVar()
questiontenanswer = IntVar()

#Question one
questiononelabel = ttk.Label(root, text="Question 1. What is 2 X 2?")
questiononelabel.grid(column=0, row=0, sticky=E)
questiononeentry = ttk.Entry(root, width=10, textvariable=questiononeanswer)
questiononeentry.grid(column=1, row=0, sticky=W)

#Question two
questiontwolabel = ttk.Label(root, text="Question 2. What is 3 X 4?")
questiontwolabel.grid(column=0, row=1, sticky=E)
questiontwoentry = ttk.Entry(root, width=10, textvariable=questiontwoanswer)
questiontwoentry.grid(column=1, row=1, sticky=W)

#Question three
questionthreelabel = ttk.Label(root, text="Question 3. What is 4 X 6?")
questionthreelabel.grid(column=0, row=2, sticky=E)
questionthreeentry = ttk.Entry(root, width=10, textvariable=questionthreeanswer)
questionthreeentry.grid(column=1, row=2, sticky=W)

#Question four
questionfourlabel = ttk.Label(root, text="Question 4. What is 6 X 9?")
questionfourlabel.grid(column=0, row=3, sticky=E)
questionfourentry = ttk.Entry(root, width=10, textvariable=questionfouranswer)
questionfourentry.grid(column=1, row=3, sticky=W)

#Question five
questionfivelabel = ttk.Label(root, text="Question 5. What is 7 X 8?")
questionfivelabel.grid(column=0, row=4, sticky=E)
questionfiveentry = ttk.Entry(root, width=10, textvariable=questionfiveanswer)
questionfiveentry.grid(column=1, row=4, sticky=W)

#Question six
questionsixlabel = ttk.Label(root, text="Question 6. What is 8 X 9?")
questionsixlabel.grid(column=0, row=5, sticky=E)
questionsixentry = ttk.Entry(root, width=10, textvariable=questionsixanswer)
questionsixentry.grid(column=1, row=5, sticky=W)

#Question seven
questionsevenlabel = ttk.Label(root, text="Question 7. What is 9 X 9?")
questionsevenlabel.grid(column=0, row=6, sticky=E)
questionsevenentry = ttk.Entry(root, width=10, textvariable=questionsevenanswer)
questionsevenentry.grid(column=1, row=6, sticky=W)

#Question eight
questioneightlabel = ttk.Label(root, text="Question 8. What is 10 X 11?")
questioneightlabel.grid(column=0, row=7, sticky=E)
questioneightentry = ttk.Entry(root, width=10, textvariable=questioneightanswer)
questioneightentry.grid(column=1, row=7, sticky=W)

#Question nine
questionninelabel = ttk.Label(root, text="Question 9. What is 11 X 12?")
questionninelabel.grid(column=0, row=8, sticky=E)
questionnineentry = ttk.Entry(root, width=10, textvariable=questionnineanswer)
questionnineentry.grid(column=1, row=8, sticky=W)

#Question ten
questiontenlabel = ttk.Label(root, text="Question 10. What is 12 X 12?")
questiontenlabel.grid(column=0, row=9, sticky=E)
questiontenentry = ttk.Entry(root, width=10, textvariable=questiontenanswer)
questiontenentry.grid(column=1, row=9, sticky=W)

#Check answer button
ttk.Button(root, text="Check Answers", command=checkanswersstart).grid(column=0, row=10, sticky=E)

#Binding enter key to check answers button
root.bind('<Return>', checkanswers)


#Start the main loop
root.mainloop()
