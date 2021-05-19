print("Employee Details")

while True:
    EmpID = input("Enter employee ID > ")
    name = input("Enter name > ")
    phone = input("Enter phone number > ")
    while True:
        qualif = input("Enter qualification : AP for Apprentice, FQ for Fully Qualified > ").upper()

        if qualif == 'AP':
            qualif = "Apprentice"
            break
        elif qualif == 'FQ':
            qualif = "Fully Qulified"
            break
        else:
            print("Invalid Try again")
        

    print("{}\n{}\n{}\n{}\n".format(EmpID, name, phone, qualif))

    right = input("Are your details correct? Y or N > ").upper()

    if right == "Y":
        break

    if right == "N":
        print("\nPlease re enter details\n")
