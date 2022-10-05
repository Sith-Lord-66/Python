import csv

CustomerDetails = open('Customer Details.csv', 'r')
CustomerDetailsW = open('Customer Details.csv', 'a')

name = input("What is your full name")
number = int(input("What is your asigned number?"))
if number in CustomerDetails.readlines():
    print(CustomerDetails.readlines()[number])


