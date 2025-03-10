from graphics import *

def guess_progression(number_1):
    while True:
        try:
            user_input=int(input(number_1))
            i=[0, 20, 40, 60, 80, 100, 120]
            
            if user_input in i:
                return user_input
            else:
                print("Out of range !")
                
        except ValueError:
            print("Integer required!")

input_sets = []

progcount = 0
trailcount = 0
retcount = 0
excount = 0
outcome = 0

while True:
  
        
        pass_credits=guess_progression("Enter Your Pass credits value (0-120):")
        defer_credits=guess_progression("Enter Your Defer credits value (0-120):")
        fail_credits=guess_progression("Enter Your fail credits value (0-120):")

        total_credits=pass_credits+defer_credits+fail_credits

        if total_credits!=120:
           print("Sorry! Total Incorrect . Try again !")

        else:
            if pass_credits==120:
                print("Progress!")
                progcount += 1
                outcome += 1
                result = 'Progress'
            elif fail_credits>=80:
                print("Exclude!")
                excount += 1
                outcome += 1
                result = 'Exclude'
            elif defer_credits+fail_credits==20:
                print("Progress(module trailer)!")
                trailcount += 1
                outcome += 1
                result = 'Module Trailer'
            else:
                print("Do not Progress-module retriever")
                retcount += 1
                outcome += 1
                result = 'Module Retriever'

            credit_set = {'Pass Credits': pass_credits,'Defer Credits': defer_credits,'Fail Credits': fail_credits,'Result': result}
            input_sets.append(credit_set)

        
        while True:
            another_guess=input("Do you want to guess another outcome (y/q):").lower()
            if another_guess=="q":
                break
            elif another_guess=="y":
                break
            else:
                print("Invalid input! Please input y or q. ")
        if another_guess=="q":
            break

def histogram(progcount, trailcount, retcount, excount, outcome):
    win = GraphWin("Output Histogram", 800, 600)
    win.setBackground("White")

    myheading = Text(Point(85, 30), 'Histogram')
    myheading.setSize(24)
    myheading.draw(win)

    h_line = Rectangle(Point(20, 450), Point(780,450))
    h_line.setFill("Black")
    h_line.draw(win)

    prog_mod = Text(Point(120,500), "Progress")
    prog_mod.setSize(22)
    prog_mod.draw(win)

    trail_mod = Text(Point(300,500), "Trailer")
    trail_mod.setSize(22)
    trail_mod.draw(win)

    ret_mod = Text(Point(485,500), "Retriver")
    ret_mod.setSize(22)
    ret_mod.draw(win)

    exclude = Text(Point(665,500), "Exclude")
    exclude.setSize(22)
    exclude.draw(win)

    outc = Text(Point(200,565), f"Outcomes in total: {outcome}")
    outc.setSize(22)
    outc.draw(win)

    progbar = Rectangle(Point(35,450), Point(200, 450 - progcount*10))
    progbar.setFill("Green")
    progbar.draw(win)

    trailbar = Rectangle(Point(215,450), Point(380, 450 - trailcount*10))
    trailbar.setFill("Blue")
    trailbar.draw(win)

    retbar = Rectangle(Point(395,450), Point(560, 450 - retcount*10))
    retbar.setFill("Purple")
    retbar.draw(win)

    exbar = Rectangle(Point(575,450), Point(740, 450 - excount*10))
    exbar.setFill("Red")
    exbar.draw(win)

histogram(progcount, trailcount, retcount, excount, outcome)

for credit_set in input_sets:
    print(f"{credit_set['Result']} - {credit_set['Pass Credits']}, {credit_set['Defer Credits']}, {credit_set['Fail Credits']}")

file = open('output.txt', 'w')
for credit_set in input_sets:
    file.write(f"{credit_set['Result']} - {credit_set['Pass Credits']}, {credit_set['Defer Credits']}, {credit_set['Fail Credits']}" + '\n')
file.close()
    
            
            
   
