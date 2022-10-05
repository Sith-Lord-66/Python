x = 0
Name=input("whats your name")
DOB=input("Whats your date of birth?")
House=input("Wher do you live")
Details = (Name + ", " + DOB + ", " + House)
print(Details)
file = open("Name.csv", "a")
file.write(Details)
file = open("Name.csv", "r")
print (file.readlines())
x +=1 
if x == 1:
    lines = open("Name.csv", 'r').readlines()
    lines = text
    out = open("Name.csv", 'w')
    out.writelines(lines)
    out.close()
    CustomerDetails = open("Name.csv", "r")
    print(CustomerDetails.readlines())

