with open("Customer Details.csv", "a") as csvFile:
        fieldnames = ["First Name","Last Name","Number"]
        csvReader = csv.DictReader(csvFile, lineterminator ="\n", fieldnames=fieldnames, delimiter = ",")
