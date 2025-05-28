
#CREATE

#Initialize
action=0
import random
parks = ["yosemite","sequoia","bigbend","acadia","redwood","nationalparks"]
foundParks = []
parksRow1 = ["D","N","E","B","G","I"]
parksRow2 = ["A","P","L","I","T","B"]
parksRow3 = ["R","A","O","W","O","A"]
parksRow4 = ["K","N","E","D","O","N"]
parksRow5 = ["S","R","A","I","D","Y"]
parksRow6 = ["C","A","D","U","E","O"]
parksRow7 = ["A","I","O","Q","T","S"]
parksRow8 = ["A","S","E","I","M","E"]


games = ["battleship", "catan", "limbo", "poker", "sorry", "charades", "partygames"]
foundGames = []
gamesRow1=["O","R","R","Y","C","A"]
gamesRow2=["S","I","L","N","A","T"]
gamesRow3=["M","G","A","M","E","S"]
gamesRow4=["B","Y","P","S","E","L"]
gamesRow5=["O","T","P","I","H","T"]
gamesRow6=["P","R","O","B","A","T"]
gamesRow7=["S","A","K","E","R","C"]
gamesRow8=["E","D","A","R","A","H"]

planets = ["mars", "mercury", "jupiter", "venus", "earth", "neptune", "uranus", "planets"]
foundPlanets = []
planetsRow1=["T","R","A","E","A","R"]
planetsRow2=["H","J","S","U","N","U"]
planetsRow3=["I","U","R","C","R","Y"]
planetsRow4=["T","P","E","U","L","P"]
planetsRow5=["E","R","M","A","N","E"]
planetsRow6=["S","E","N","S","U","V"]
planetsRow7=["T","N","E","P","T","E"]
planetsRow8=["S","R","A","M","U","N"]


completedPuzzles =[]


#Functions

def nationalParksAesthetics():
    print("Look for words around a common theme in the grid (letters can be connected upwards, downwards, or diagonally and they do not have to be in a straight line).")
    print("HINT: PRESERVES")
    print(parksRow1)
    print(parksRow2)
    print(parksRow3)
    print(parksRow4)
    print(parksRow5)
    print(parksRow6)
    print(parksRow7)
    print(parksRow8)

def nationalParksCode():
    global y
    while True:
        guess = input("Enter a word you found in the grid or press x to quit.")
        if guess.lower() in parks:
            for i in range (len(parks)):
                    if guess.lower() == parks[i]:
                        print("Congrats! You found " + guess + "!")
                        foundParks.append(parks[i])
                        print("So far you have found: ")
                        print(foundParks)
                        y=parks.index(guess.lower())
                        parks[i]=[" "]
        elif guess.lower() in foundParks and parks[y]==[" "]:
            print("Already guessed, try again.")
        elif guess.lower() not in parks and guess.lower() != "x":
            print("INCORRECT")
        foundParks.sort()
        if foundParks==["acadia", "bigbend", "nationalparks", "redwood", "sequoia", "yosemite"]:
            print("Congratulations! You finished DuckStrands Puzzle 1: PRESERVES!")
            if "PRESERVES" not in completedPuzzles:
                completedPuzzles.append("PRESERVES")
            break
        if guess.lower() == "x":
            print("Goodbye!")
            break

def gamesAesthetics():
    print("Look for words around a common theme in the grid (letters can be connected upwards, downwards, or diagnonally and they do not have to be in a straight line).")
    print("HINT: FESTIVE")
    print(gamesRow1)
    print(gamesRow2)
    print(gamesRow3)
    print(gamesRow4)
    print(gamesRow5)
    print(gamesRow6)
    print(gamesRow7)
    print(gamesRow8)

def gamesCode():
    global y
    while True:
        guess = input("Enter a word you found in the grid or press x to quit.")
        if guess.lower() in games:
            for i in range (len(games)):
                    if guess.lower() == games[i]:
                        print("Congrats! You found " + guess + "!")
                        foundGames.append(games[i])
                        print("So far you have found: ") #displays list of already found words
                        print(foundGames)
                        y=games.index(guess.lower())
                        games[i]=[" "]
        elif guess.lower() in foundGames and games[y]==[" "]:
            print("Already guessed, try again.") #So they can't guess the same thing twice
        elif guess.lower() not in games and guess.lower() != "x":
            print("INCORRECT")
        foundGames.sort()
        if foundGames==["battleship", "catan", "charades", "limbo", "partygames", "poker", "sorry"]:
            print("Congratulations! You finished DuckStrands Puzzle 2: FESTIVE!")
            if "FESTIVE" not in completedPuzzles:
                completedPuzzles.append("FESTIVE")
            break
        if guess.lower() == "x":
            print("Goodbye!")
            break

def planetsAesthetics():
    print("Look for words around a common theme in the grid (letters can be connected upwards, downwards, or diagnonally and they do not have to be in a straight line).")
    print("HINT: UNIVERSAL")
    print(planetsRow1)
    print(planetsRow2)
    print(planetsRow3)
    print(planetsRow4)
    print(planetsRow5)
    print(planetsRow6)
    print(planetsRow7)
    print(planetsRow8)

def planetsCode():
    global y
    while True:
        guess = input("Enter a word you found in the grid or press x to quit.")
        if guess.lower() in planets:
            for i in range (len(planets)):
                    if guess.lower() == planets[i]:
                        print("Congrats! You found " + guess + "!")
                        foundPlanets.append(planets[i])
                        print("So far you have found: ") #displays list of already found words
                        print(foundPlanets)
                        y=planets.index(guess.lower())
                        planets[i]=[" "]
        elif guess.lower() in foundPlanets and planets[y]==[" "]:
            print("Already guessed, try again.") #So they can't guess the same thing twice
        elif guess.lower() not in planets and guess.lower() != "x":
            print("INCORRECT")
        foundPlanets.sort()
        if foundPlanets==["earth", "jupiter", "mars", "mercury", "neptune", "planets", "uranus", "venus"]:
            print("Congratulations! You finished DuckStrands Puzzle 3: UNIVERSAL!")
            if "UNIVERSAL" not in completedPuzzles:
                completedPuzzles.append("UNIVERSAL")
            break
        if guess.lower() == "x":
            print("Goodbye!")
            break

def menuAction (option):
    global action
    global y
    if option=="1":
        while True:
            print("Here are the options for themes. Choose your favorite to play: ")
            print("1. PRESERVES \n2. FESTIVE \n3. UNIVERSAL\n4. Back to menu")
            theme=str(input("Enter a number 1-4: "))
            if theme=="1":
                nationalParksAesthetics()
                nationalParksCode()
            if theme=="2":
                gamesAesthetics()
                gamesCode()
            if theme == "3":
                planetsAesthetics()
                planetsCode()
            if theme == "4":
                print("Back to menu")
                break
    if option=="2":
        p = random.randint(1, 3)
        if p==1:
            nationalParksAesthetics()
            nationalParksCode()
        if p==2:
            gamesAesthetics()
            gamesCode()
        if p==3:
            planetsAesthetics()
            planetsCode()
    if option == "3":
        print("You have completed " + str(len(completedPuzzles)) + " out of 3 puzzles! Completed puzzles: ")
        print(completedPuzzles)
    if option == "4":
        action=4
    else:
        print("Please enter a number 1-4")

def duckStrandsGame():
    global y
    global action
    print("Welcome to DuckStrands!")
    while True:
        print("1. Choose from theme options\n2. Solve a random puzzle\n3. Display scorecard \n4. Quit the game")
        menuAction(str(input("Please choose what you would like to do from the menu")))
        if action == 4:
            print("Goodbye!")
            break




#Main
duckStrandsGame()
