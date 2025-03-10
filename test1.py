import graphics

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
            elif fail_credits>=80:
                print("Exclude!")
            elif defer_credits+fail_credits==20:
                print("Progress(module trailer)!")
            else:
                print("Do not Progress-module retriever")

        
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
            
            
   
