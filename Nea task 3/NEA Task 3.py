# Reads the 2 files

fixtures = open('firesidefixtures.txt').read().splitlines()
results = open('firesideresults.txt').read().splitlines()


# Converts the files into 2D Array

def convert(file):
    x = list()
    for i in file:
        x.append(i.split(","))
    return x


fixtures = convert(fixtures)  # Converted to 2D Array
results = convert(results)


# Show menu

def menu():
    print("\nOption A - Search for a fixture")
    print("Option B - Outstanding Fixtures")
    print("Option C - Display leaderboard")
    print('Enter "Q" to Quit\n')


# Option A - Show Fixtures

def a():
    valid = False

    while not valid:
        num = int(input("Enter a valid fixture number > "))

        for i in fixtures:
            index = fixtures.index(i)

            if num == int(fixtures[index][0]):
                print("\nFixture Number - {}".format(fixtures[index][0]))
                print("Fixture Date - {}".format(fixtures[index][1]))
                print("Player 1 Nickname - {}".format(fixtures[index][3]))
                print("Player 2 Nickname - {}".format(fixtures[index][4]))
                print("Fixture Played - {}".format(fixtures[index][5]))
                print("Winner - {}".format(fixtures[index][6]))
                valid = True
                break

            elif num >= len(fixtures) - 1:
                print("Invalid Please Try again")
                break


# Option B - Outstanding fixtures

def b():
    for i in fixtures:
        index = fixtures.index(i)

        if fixtures[index][5].upper() != "Y":
            print("\nFixture Number - {}".format(fixtures[index][0]))
            print("Fixture Date - {}".format(fixtures[index][1]))
            print("Fixture Time - {}".format(fixtures[index][2]))
            print("Player 1 Nickname - {}".format(fixtures[index][3]))
            print("Player 2 Nickname - {}".format(fixtures[index][4]))


# Option C - Leaderboard

def c():
    WIN = 3 # Win Constant
    x = list()  # Stores points

    def sortConfig(val):  # Will sort players by points
        return int(val[0])

    for i in results:
        index = results.index(i)

        if int(results[index][2]) >= 1:
            x.append(
                f"{int(results[index][2]) * WIN}, {results[index][1]}, {results[index][2]}, {results[index][3]}, {results[index][0]}".split(
                    ","))   # Makes a list of elegible players
            x.sort(reverse=True, key=sortConfig)  # Sorts the list

    for i in x:
        index = x.index(i)

        print("\nPlayer Nickname - {}".format(x[index][4]))
        print("Matches Played - {}".format(x[index][1]))
        print("Matches Won - {}".format(x[index][2]))
        print("Matches Lost - {}".format(x[index][3]))
        print("Points - {}".format(x[index][0]))


while True:
    menu()
    choice = input("A B C Q - ").upper()

    if choice == "A":
        a()

    elif choice == "B":
        b()

    elif choice == "C":
        c()

    elif choice == "Q":
        break

    else:
        print("\nInvalid Selection. Try again \n")
