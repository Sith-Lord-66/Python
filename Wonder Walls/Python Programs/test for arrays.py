file = open("Customer Details.csv", "r")
text = file.read()
length = len(open("Customer Details.csv").readlines())
print(length)

CustomerDetails = open('Customer Details.csv', 'r')
CustomerDetailsW = open('Customer Details.csv', 'w')

name = input("What is your full name")
number = int(input("What is your asigned number?"))
held =[number]
if name or number in CustomerDetails.readlines():
    print (CustomerDetails.readlines()[number])
    newData = input("ENTER DATA: ")
    print("We will now input your new data")
    
    
