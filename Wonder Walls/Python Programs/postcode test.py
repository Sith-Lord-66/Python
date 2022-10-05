postcode = input("Please enter in their postcode: ")
checkPost = False
while checkPost == False:
    for char in postcode[0:2]:
        if not char.isalpha():
            print("not a valid entry, please enter an approiate entry")
            postcode = input("Please enter in their postcode: ")
            checkPost = False
            
    if not postcode[2:5].isdigit():
        print("not a valid entry, please enter an approiate entry")
        number = input("Please enter in their postcode: ")
        checkPost = False

    for char in postcode[5:7]:
        if not char.isalpha():
            print("not a valid entry, please enter an approiate entry")
            postcode = input("Please enter in their postcode: ")
            checkPost = False
            
        else:
            checkPost = True

print("HELLO THERE")
