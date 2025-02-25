import random

global num_players
global target_werewolf


# create the parameter function for the game (werewolves game)
def set_parameters():
    # Create a dictionary to store the parameters
    global num_players
    parameters = {}
    pseudo = {}
    num_players = int(input("Enter the number of players (between 6 and 18): "))
    # Set the number of players
    while num_players < 6 or num_players > 18:
        if num_players < 6:
            print("The number of players is too low.")
            num_players = int(input("Enter the number of players (between 6 and 18): "))
        if num_players > 8:
            print("The number of players is too high.")
            num_players = int(input("Enter the number of players (between 6 and 18): "))
    parameters["num_players"] = num_players

    # Set pseudo names
    for i in range(num_players):
        pseudo[i] = input(f"Enter the pseudo of player {i+1}: ")
    parameters["pseudo"] = pseudo

    # Set the number of werewolves
    parameters["roles"] = []
    if num_players < 9:
        num_werewolves = 2
    elif num_players < 13:
        num_werewolves = 3
    else:
        num_werewolves = 4
    parameters["num_werewolves"] = num_werewolves
    for i in range(num_werewolves):
        parameters["roles"].append("werewolf")

    # Set the number of special villagers
    num_special_villagers = 0
    witch = 0
    seer = 0
    hunter = 0
    cupid = 0
    thief = 0
    little_girl = 0
    if num_players <= 10:
        num_special_villagers = 3
        witch = 1
        parameters["roles"].append("witch")
        seer = 1
        parameters["roles"].append("seer")
        hunter = 1
        parameters["roles"].append("hunter")
    if 10 < num_players <= 13:
        num_special_villagers = 5
        cupid = 1
        parameters["roles"].append("cupid")
        thief = 1
        parameters["roles"].append("thief")
    if 13 < num_players <= 18:
        num_special_villagers = 6
        little_girl = 1
        parameters["roles"].append("little_girl")
    parameters["num_special_villagers"] = num_special_villagers
    parameters["witch"] = witch
    parameters["seer"] = seer
    parameters["hunter"] = hunter
    parameters["cupid"] = cupid
    parameters["thief"] = thief
    parameters["little_girl"] = little_girl

    # Set the number of villagers
    num_villagers = num_players - num_werewolves - num_special_villagers
    for i in range(num_villagers):
        parameters["roles"].append("villager")
    parameters["num_villagers"] = num_villagers

    return parameters


#  Function to set the roles of the players
def set_roles(parameters):
    roles = parameters["roles"]
    # assign the roles to the players randomly
    player_status = {}
    # shuffle the roles
    random.shuffle(roles)
    for i in range(num_players):
        player_status[parameters["pseudo"][i]] = roles[i]
    return player_status


def run_game(parameters, player_status):
    global target_werewolf, witch_choice, target_witch
    witch_choice = [1, 1]
    print("The game has started.")
    # Night 1
    print("The night has fallen.")
    for player in player_status:
        if player_status[player] == "werewolf":
            print("Werewolves, open your eyes.")
            print("Werewolves, choose a player to kill.")
            target_werewolf = ""
            while target_werewolf not in parameters["pseudo"]:
                target_werewolf = input("Enter the pseudo of the player you want to kill: ")
            print("Werewolves, close your eyes.")
        if player_status[player] == "witch":
            print("Witch, open your eyes.")
            print("Witch, this is the player who was killed by the werewolves.")
            print(target_werewolf)
            print("Witch, what do you want to do?")
            print("1. Save the player.\n2. Do nothing.\n3. Kill a player.")
            choice = input("Enter your choice: ")
            while choice not in [1, 2, 3]:
                choice = int(input("Enter your choice: "))
            if choice == 1 and witch_choice[0] == 1:
                print("Witch, you have chosen to save the player.")
                print("You chose to save the player", target_werewolf)
                witch_choice[0] -= 1
            if choice == 3 and witch_choice[1] == 1:
                print("Witch, who do you want to kill?")
                target_witch = ""
                while target_witch not in parameters["pseudo"]:
                    target_witch = input("Enter the pseudo of the player you want to kill: ")
                witch_choice[1] -= 1
            if choice == 2:
                print("Witch, you have chosen to do nothing.")
            print("Witch, close your eyes.")

        if player_status[player] == "seer":
            print("Seer, open your eyes.")
            print("Seer, choose a player to see.")
            target_seer = ""
            while target_seer not in parameters["pseudo"]:
                target_seer = input("Enter the pseudo of the player you want to see: ")
            print("Seer, this is the role of the player you chose.")
            print(player_status[target_seer])
            print("Seer, close your eyes.")

        if player_status[player] == "cupid":
            print("Cupid, open your eyes.")
            print("Cupid, choose two players to make them fall in love.")
            lovers = []
            for i in range(2):
                lover = ""
                while lover not in parameters["pseudo"]:
                    lover = input(f"Enter the pseudo of the lover {i+1}: ")
                lovers.append(lover)
            print("Cupid, close your eyes.")

        if player_status[player] == "thief":
            print("Thief, open your eyes.")
            print("Thief, choose a player to exchange your role with.")
            target_thief = ""
            while target_thief not in parameters["pseudo"]:
                target_thief = input("Enter the pseudo of the player you want to exchange your role with: ")
            print("Thief, close your eyes.")
            temp = player_status[player]
            player_status[player] = player_status[target_thief]
            player_status[target_thief] = temp
    print("The night is over.")
    print("The day has come.")
    print("The players wake up.")



# Main function
def main():
    parameters = set_parameters()
    player_status = set_roles(parameters)
    print(player_status)


if __name__ == "__main__":
    main()
