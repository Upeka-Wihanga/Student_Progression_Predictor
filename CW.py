import graphics

def guess_progression(pass_creddits, defer_credits, fail_credits):
    
    
    if pass_credits not in [0,20,40,60,80,100,120] or defer_credits not in [0,20,40,60,80,100,120] or fail_credits not in [0,20,40,60,80,100,120]:
        return"Sorry ! Out of range , Try again !"
    if pass_credits==120:
        return"Progress!"
    elif fail_credits>=80:
        return"Exclude!"
    elif defer_credits+fail_credits==20:
        return"Progress(module trailer)!"
    else:
        return"Do not Progress-module retriever"

while True:
    try:
        
        pass_credits=int(input("Enter Your Pass credits value (0-120):"))
        defer_credits=int(input("Enter Your Defer credits value (0-120):"))
        fail_credits=int(input("Enter Your fail credits value (0-120):"))

        total_credits=pass_credits+defer_credits+fail_credits

        if total_credits!=120:
           print("Sorry! Total Incorrect . Try again !")
           break
        
        outcome=guess_progression(pass_credits, defer_credits, fail_credits)
        print("Final progression:", outcome)

        another_guess=input("Do you want to guess another outcome (yes/no):").lower()

        if another_guess!="yes":
         break
    except ValueError:
        print("Integer Required : Sorry ! Please Enter an integer value as credits .")
    
