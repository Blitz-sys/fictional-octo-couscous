import json; import os
def confirm():
    if input("If you wish to end type 'End' if you would like to re-input something type 'redo':").lower() == "end":
        print("Thanks")
        return True
    else:
        print("You may redo it now\n")
        return False
def reason():
   return input("Any reason in particular?:")
while True:
#INPUT FEILD
    U_AND_A = (input("Username: "), input("Was active/available during war (yes/no): ").lower())
    if U_AND_A[1] == "no":
        Reason_for_unavailability = reason()
        if confirm():
            break
        else:
            continue
    # FIRST ATTACK STARTS FROM HERE
    if input("First attack done? (yes/no):").lower()== "no":
        First_war_attack_done = False
        Reason_for_not_doing_first_attack = reason()
        if confirm():
            break
        else:
            continue
    else:
        First_war_attack_done = True
        First_war_attack = (int(input("First war attack stars: ")),
                            int(input("First war destruction/damage (only numbers): ")))
    # SECOND ATTACK STARTS FROM HERE
    if input("Second attack done (yes/no): ").lower() == "no":
        reason_for_not_doing_second_war_attack = reason()
        if confirm():
            break
