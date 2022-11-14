import csv

FILENAME = "world_cup_champions.txt"

def read_cups():
    #Create a dictionary for won_cups
    won_cups = {}
    #Try-Except for file validation
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line.replace("'", "")
                row = line.split(",")
                won_cups[row[0]] = row[1]
            return won_cups
    #Exception handler for missing file
    except FileNotFoundError:
            print("Error! Missing ""world_cup_champions.txt"" file.")
            print("Please place the file in the same folder as this program and try again.")
            print("Bye!")
            exit()

def list_cups(won_cups):
    del won_cups["Year"]
    team = list(won_cups.values())
    years = list(won_cups.keys())
    #Lists for overall and country specific cups to be appended
    cups = []
    arg_cups = []
    bra_cups = []
    eng_cups = []
    fra_cups = []
    ger_cups = []
    ita_cups = []
    spa_cups = []
    uru_cups = []

    for count in range(0, len(won_cups)):
        year = [team[count], years[count]]
        cups.append(year)
        count += count

    #For-Elif-Else loop for accounting every occurance of each countries name in CSV
    count = 0
    for i in cups:
        if 'Argentina' in cups[count]:
            arg_cups.append(int(cups[count][1]))
            count+=1
        elif 'Brazil' in cups[count]:
            bra_cups.append(int(cups[count][1]))
            count += 1
        elif 'England' in cups[count]:
            eng_cups.append(int(cups[count][1]))
            count += 1
        elif 'France' in cups[count]:
            fra_cups.append(int(cups[count][1]))
            count += 1
        elif 'Germany' in cups[count]:
            ger_cups.append(int(cups[count][1]))
            count += 1
        elif 'Italy' in cups[count]:
            ita_cups.append(int(cups[count][1]))
            count += 1
        elif 'Spain' in cups[count]:
            spa_cups.append(int(cups[count][1]))
            count += 1
        elif 'Uruguay' in cups[count]:
            uru_cups.append(int(cups[count][1]))
            count += 1

    #Alphabetized dictionary for the win count
    won_cups = {"Argentina": arg_cups, "Brazil": bra_cups, "England": eng_cups, "France": fra_cups,
                "Germany": ger_cups, "Italy": ita_cups, "Spain": spa_cups, "Uruguay": uru_cups}
    return won_cups
    

def show_cups(won_cups):
    count = 0
    #Variables that can be called to a list
    teams = list(won_cups.keys())
    cup_years = list(won_cups.values())
    #Formatting for text menu
    print("{:14} {:7} {:6}".format(" Country", "Wins", "Years"))
    print("{:14} {:7} {:6}".format(" =======", "====","====="))
    #Loop that increments country wins by year it occured
    while count < len(teams):
        country = str(teams[count])
        wins = str(len(cup_years[count]))
        years = str(cup_years[count])
        print("", country.ljust(16), wins.ljust(5), years.strip("[]"))
        count += 1
    
    
#Top of hierarchy
def main():
    print(" FIFA World Cup Winners")
    print()
    choice = "y"
    while choice.lower() == "y":
        won_cups = read_cups()
        won_cups = list_cups(won_cups)
        show_cups(won_cups)
        choice = input("Restart the program? (Y/N): ")

if __name__ == "__main__":
    main()
