
def AddCustomer(): 
    adding = True
    while (adding == True):
        file = open("Customer Details.csv", "r")
        text = file.read()
        length = len(open("Customer Details.csv").readlines())
        print(length)
        #reads line length to find number
        CustomerDetails= open('Customer Details.csv', 'a')
        customerName = input("To add a customer please enter their name: ")
        #asks for name
        customerNum = length
        if length == 1:
            CustomerDetails.write(customerName + ", " + str("%03d"%customerNum))
        else:
            CustomerDetails.write("\n" + customerName + ", " + str("%03d"%customerNum))
        #prints into file name and number
        CustomerDetails = open('Customer Details.csv', 'r')
        print(CustomerDetails.readlines())
        CustomerDetails.close()
        continues = input("Do you want to add another person? Yes or No\n")
        if continues == "Yes":
            adding = True
        elif continues == "No":
            adding = False
        else:
            print("Not a valid entry")
            continues = input("Do you want to add another person? Yes or No\n")
        #asks if you want to add another person


AddCustomer()
