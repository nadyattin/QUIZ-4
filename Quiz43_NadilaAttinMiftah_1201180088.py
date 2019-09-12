print("Welcome to IGRACIAS\n")

listGPA = [2.1,2.5,4,3]

def bonus(gpa):
    tip = 500000
    reward = gpa*tip
    return reward

for gpa in listGPA:
    if gpa > 2.5:
        print("Your GPA", gpa, " so you get a bonus Rp", bonus(gpa))
    else:
        print("Your GPA", gpa, "Sorry. Please try next semester. Good Luck!")  
      