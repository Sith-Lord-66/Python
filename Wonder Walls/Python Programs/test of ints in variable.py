number = input("Please add their phone number: ")
checkNum = False
while checkNum == False:
    if not number.isdigit():
        print("not a valid entry, please enter an approiate entry")
        number = input("Please add their phone number: ")
        checkNum = False
    else:
        checkNum = True
