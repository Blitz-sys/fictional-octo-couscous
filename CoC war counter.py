#SETUP
import sys; import json
def confirm():
    if input("If you wish to end type 'End' if you would like to re-input something type anyhting other than 'End':").lower() == "end":
        print("Thanks")
        return True
    else:
        print("You may redo it now\n")
        return False
def reason():
    return input("Any reason in particular?:")

while True:
#INPUT FEILD
    username = input("Username: ")
    available = input("Was active/available during war (true/false): ").lower()
    if available == "false":
        reason_for_unavailability = reason()
        if confirm():
            print("Thanks")
            break
        else:
            print("You may redo it now\n")
            continue
    # FIRST ATTACK STARTS FROM HERE
    if input("First attack done? (yes/no):").lower()== "no":
        First_war_attack_done = False
        Reason_for_not_doing_first_attack = reason()
        if confirm():
            print("Thanks")
            break
        else:
            print("You may redo it now\n")
            continue
    else:
        First_war_attack_done = True
        First_war_attack = [int(input("Total war stars: ")),
                            int(input("First war destruction/damage (only numbers): "))]
    # SECOND ATTACK STARTS FROM HERE
    if input("Second attack done (yes/no): ").lower() == "no":
        reason_for_not_doing_second_war_attack = reason()
        if confirm():
            print("Thanks")
            break
        else:
            print("You may redo it now\n")
            continue
    
    Second_war_attack = [int(input("Second war attack stars: ")), int(input("Second war attack destruction/damage (only numbers): "))]
    # CALCULATIONS
    # Index 0 is stars, Index 1 is destruction
    print(f"\nTotal war stars: {First_war_attack[0] + Second_war_attack[0]}")
    print(f"Total destruction: {First_war_attack[1] + Second_war_attack[1]}%")
    if confirm():
        print("Thanks")
        break
    else:
        print("You may redo it now\n")
        continue
