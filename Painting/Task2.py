while True:
    print("Welcome, Please enter the following details: ")

    customerId = input("Customer Id: ")
    estimateDate = input("Date of estimate: ")
    roomAmount = int(input("Rooms needed to be painted: "))
    roomInfo = []
    wallInfo = []
    totalArea = float()
    totalCost = float()

    for i in range(roomAmount):
        roomInfo.append([input(f"Room {i+1} name: "), int(input("Amount of walls: ")), input("Remove wallpaper? Y or N: ").upper()])
        if roomInfo[-1] == "Y":
            totalCost += 70

        for x in range(roomInfo[i][1]):
            width = int(input(f"Wall {x+1} Width (m): "))
            height = int(input(f"Wall {x+1} Height (m): "))
            
            wallInfo.append([i, width, height])
            totalArea += width * height

    totalCost += 250 if input("What type of employee would to like to hire? Apprentice or Fully Qualifed?").upper() == "FQ" else 100

    totalCost += (totalArea * 15)

    print("\nEstimated Total exc VAT : ", totalCost)
    print("Estimated Total inc VAT : ", totalCost * 1.2, "\n")

    if input("Calculate another price? Y or N").upper() != "Y":
        print("Exiting...")
        break
