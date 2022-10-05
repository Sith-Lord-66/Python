import csv
with open("Customer Details.csv", "a") as csvWrite:
                fieldnames = ["First Name","Last Name","Number","Postcode", "Gender", "Phone Number", "Email Address", "Reaction Test 1", "Reaction Test 2", "Reaction Test 3", "Eiffel Tower Climb", "SkyScraper Climb", "Slemish Climb"]
                csvWriter = csv.writer(csvWrite, lineterminator ="\n", delimiter = ",")
                csvWriter.writerow(fieldnames)
