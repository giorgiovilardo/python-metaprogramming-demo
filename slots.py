import csv


def make_MedicName_slot():
    print("1. Building the MedicName slot")


def make_NurseName_slot():
    print("2a. Building the NurseName slot.")
    print("2b. I read my data from a CSV. Do that in JSON :)")
    with open("NurseNameData.csv") as nurse_data:
        reader = csv.reader(nurse_data)
        # Skips header line
        next(reader)
        for row in reader:
            print(", ".join(row))
