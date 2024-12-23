locations = {
    'Villain Cave': {'South': 'Extended Desert', 'Enemy': 'Bookkeeper'},
    'Extended Desert': {'North': 'Villain Cave', 'South': 'Home', 'Enemy': 'Thirst'},
    'Home': {'North': 'Extended Desert', 'South': 'Violet Forest', 'East': 'Emerald Cave', 'West': 'Storm Ripper'},
    'Violet Forest': {'North': 'Home', 'East': 'Rushing River', 'West': 'Mysterious Cabin', 'Item': 'Wine Skin'},
    'Widows Peak': {'South': 'Emerald Cave', 'Item': 'Crusty Armor'},
    'Emerald Cave': {'North': 'Widows Peak', 'South': 'Rushing River', 'West': 'Home', 'Item': 'Shimmering Sword'},
    'Rushing River': {'North': 'Emerald Cave', 'West': 'Violet Forest', 'Item': 'Wine Barrel'},
    'Hellfire Island': {'South': 'Storm Ripper', 'Item': 'Dragon Horn'},
    'Storm Ripper': {'East': 'Home', 'North': 'Hellfire Island', 'Enemy': 'Squid'},
    'Mysterious Cabin': {'East': 'Violet Forest', 'Item': 'Runed Ring'}
}  # dictionary of rooms to visit

inventory = []
visited = False
visited1 = False
visited2 = False
current_room = 'Home'  # starting room
permittedDirections = ['North', 'East', 'South', 'West']


def move(direction):
    global inventory
    if direction in locations[current_room]:
        next_room = locations[current_room][direction]
        print("You have moved to", next_room)
        if 'Item' in locations[next_room]:
            if 'Item' not in inventory:
                print("You see an item:", locations[next_room]['Item'])
            else:
                print("You already have this item")
        print("Permitted directions in this room:", list(locations[next_room].keys()))  # print permitted directions
        print(inventory)  # Prints current inventory
        return next_room
    else:
        print("Not a valid direction.")
        return current_room


def roomHandlerVillainCave():
    print("The Bookkeeper is entertained by your presence, 'So you have come to destroy me"
          " with your toothpick and old armor'")
    if 'Dragon Horn' in inventory:
        print("You blow the horn and your old friend the ancient dragon arrives")
        print("The Bookkeeper intends to run but the dragon grabs him with his tail"
              " and launches him far into the air, the dragon opens it's maw and swallows the bookkeeper whole")
        print("You have saved the kingdom with the help of the dragon and have brought peace. You will be rewarded "
              "greatly...")
        return "win"
    else:
        print("You make a run for the Bookkeeper but he puts his hand up and stops you in your tracks")
        print("He takes your sword and stabs you in the gut, you fall and feel cold.")
        print("The kingdom falls into disarray and no one is there to stop it...")
        return "death"


def roomHandlerHellfireIsland():
    global visited1
    if visited1:
        print('You see the dragon in the distance')
        return
    visited1 = True
    if 'Runed Ring' in inventory:
        print("An ancient dragon approaches...")
        print("You hear the dragon ask, 'Why do you disturb my slumber?'")
        print("You remain silent but the dragon can read your thoughts...")
        print("I will help you on your quest, take my horn and use it sparingly...")
        print(" ")
        print("The dragon leaves")
    else:
        print("An ancient dragon approaches...")
        print("The ancient dragon crushes your bones and feasts on your soul")
        return "death"


def roomHandlerStormRipper():
    global visited
    if visited:
        print("The Kraken is no longer here, the waters are calm.")
        return
    print("The Kraken, a fabulous monster from the deep, extends is piercing tentacles at you")
    visited = True
    if 'Shimmering Sword' and 'Crusty Armor' in inventory:
        print("You hurdle yourself at the monster and slit one of the tentacles!")
        print("The beast recoils and swims away, healing to fight another day")
    else:
        print("You hurdle yourself at the beast, attempting to save your fellow sailors")
        print("The beast throws you like a ragdoll into the sea and sinks the ship")
        return "death"


def roomHandlerMysteriousCabin():
    global visited2
    if not visited2:
        print("You come across a cabin in the woods")
        print("There is an ancient aura around this place and you would like to leave as soon as possible")
        visited2 = True
    else:
        print(" ")


def roomHandlerExtendedDesert():
    print("The sweltering heat makes you thirsty, you need something to drink to move on")
    if 'Wine Skin' and 'Wine Barrel' in inventory:
        print("You drink your wine skin and move on to your destination")
    else:
        print("You fall into a fit of hysteria and fall asleep...")
        return "death"


def roomHandlerRushingRiver():
     if 'Wine Skin' in inventory:
        print("You see a barrel of wine and finally have something to hold it!")
     else:
        print("You see a barrel with wine but have nothing to hold it")


def handleRoom(): # Makes it easier to see how each room is its own function
    switcher = {
        'Villain Cave': roomHandlerVillainCave,
        'Hellfire Island': roomHandlerHellfireIsland,
        'Storm Ripper': roomHandlerStormRipper,
        'Mysterious Cabin': roomHandlerMysteriousCabin,
        'Extended Desert': roomHandlerExtendedDesert,
        'Rushing River': roomHandlerRushingRiver,
    }
    room_function = switcher.get(current_room, lambda: None)
    if room_function:
        return room_function()
    else:
        print("You are at", current_room)



def handleInput():
    global current_room
    global inventory
    command = input("Enter what you would like to do: ").lower().split()

    if len(command) == 2 and command[0] == 'go' and any(d in command[1].capitalize() for d in permittedDirections):
        current_room = move(command[1].capitalize())  # eliminates issues with format from inputs
    elif command[0] == 'exit':  # gives player option to exit the game if desired
        print("You have opted to end the game")
        return "exit"
    elif command[0] == 'get':
        if 'Item' in locations[current_room]:
            room_item = locations[current_room]['Item'].lower()
            entered_item = ' '.join(command[1:]).lower()  # Join all words after 'get' into a single string
            if entered_item in room_item:
                item = locations[current_room]['Item']
                if item not in inventory:
                    print("You retrieved", item)
                    inventory.append(item)
                    print(item, "added to your inventory.")
                else:
                    print("You already have", item, "in your inventory.")
            else:
                print("There is no such item in this room.")
        else:
            print("There is no item to pick up in this room.")
    else:
        print("Not a valid input")


def loop():  # Main Game loop
    while True:
        result = handleRoom()
        if result == "death" or result == "win":
            break
        result = handleInput()
        if result == "exit":
            break


def main():
    introMessage()  # start off the player with a warm welcome
    loop()  # run the game
    print("Game over")
    input("Press Enter to end this session")


def introMessage():
    print("Welcome to the Adventures of Aleen!")
    print("The land is on the brink of war. A mastermind by the name of the Bookkeeper has infiltrated the minds of "
          "three of our most powerful kings. Only with the help of the ancient dragon can peace be kept.")
    print("But a warning to you fair traveller...")
    print(" ")
    print("There will be treachery along the way. they say a ferocious beast stalks the waters, and the desert is "
          "no place for life...")
    print("Please enter 'go [North, East, South, West]' in order to move. "
          "When the location contains an item, you will be able to type 'get [Item] to add it to your inventory.")
    print("Good Luck! And my the odds be in your favor...")
    print("You are at", current_room)


if __name__ == "__main__":
    main()
