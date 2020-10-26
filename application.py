import constants
import copy
import pdb

#Extracts PLAYERS data and stores it in a new varaiable
players_copy = copy.deepcopy(constants.PLAYERS)

#Stores essential data for the panthers team
panthers = []
exp_panthers = []
inexp_panthers = []
panthers_heights = []
panthers_guardians = []

#Stores essential data for the bandits team
bandits = []
exp_bandits = []
inexp_bandits = []
bandits_heights = []
bandits_guardians = []

#Stores essential data for the warriors team
warriors = []
exp_warriors = []
inexp_warriors = []
warriors_heights = []
warriors_guardians = []


#Converts players height(string) data into an integer, and converts players experiences from YES and NO strings to
#True and False boolean statemnts
def clean_data(players_copy):
    for players in players_copy:
        height_as_str = players["height"][0:2]
        height_as_int = int(height_as_str)
        players["height"] = height_as_int
        experience = players["experience"][0]
        if "Y" in experience:
            players["experience"] = True
        elif "N" in experience:
            players["experience"] = False
    return players_copy


#Utilizes the updated players data from the clean_data function
#In order to balance teams evenly while storing(appending) essential data
#From each team into different lists
def balance_team():
    for players in clean_data(players_copy):
            if players["experience"] == True or players["experience"] == False:
                if players["experience"] == True and len(exp_panthers) < 3:
                    panthers.append(players)
                    guardian = players["guardians"]
                    panthers_guardians.append(guardian)
                    exp_panthers.append(players["experience"])
                    panthers_heights.append(players["height"])
                elif players["experience"] == False and len(inexp_panthers) < 3:
                    panthers.append(players)
                    guardian = players["guardians"]
                    panthers_guardians.append(guardian)
                    inexp_panthers.append(players["experience"])
                    panthers_heights.append(players["height"])
                elif players["experience"] == True and len(exp_bandits) < 3:
                    bandits.append(players)
                    guardian = players["guardians"]
                    bandits_guardians.append(guardian)
                    exp_bandits.append(players["experience"])
                    bandits_heights.append(players["height"])
                elif players["experience"] == False and len(inexp_bandits) < 3:
                    bandits.append(players)
                    guardian = players["guardians"]
                    bandits_guardians.append(guardian)
                    inexp_bandits.append(players["experience"])
                    bandits_heights.append(players["height"])
                elif players["experience"] == True and len(exp_warriors) < 3:
                    warriors.append(players)
                    guardian = players["guardians"]
                    warriors_guardians.append(guardian)
                    exp_warriors.append(players["experience"])
                    warriors_heights.append(players["height"])
                elif players["experience"] == False and len(inexp_warriors) < 3:
                    warriors.append(players)
                    guardian = players["guardians"]
                    warriors_guardians.append(guardian)
                    inexp_warriors.append(players["experience"])
                    warriors_heights.append(players["height"])


#Intended to utilize teams data from various lists in order to display team stats
def print_stats(team_name, team, exp_players, inexp_players, height,  guardians):
    print("Team: {} Stats".format(team_name))
    print("-" * 20)
    print("Total players: ", len(team))
    print("Total experienced: {}".format(len(exp_players)))
    print("Total inexperienced: {}".format(len(inexp_players)))
    height_sum = sum(height)
    team_list_len = len(height)
    average_height = height_sum / team_list_len
    average_height = round(average_height, 1)
    print("Average height: {}".format(average_height))
    print("\n")
    team_players = []
    for players in team:
        name = players["name"]
        team_players.append(name)
    print("Players on Team: {}".format(", ".join(team_players)))
    print("\n")
    # For loop splits the guardian names and then stores it in a list
    # Which then is combined by using join
    split_team_guardians = []
    for guardian in guardians:
        splitted = guardian.split("and")
        joined = ",".join(splitted)
        split_team_guardians.append(joined)
    print("Guardians: {} \n".format(", ".join(split_team_guardians)))
    print("\n")


if __name__ == "__main__":
    #Balances teams by calling balance_team function
    balance_team()
    #Asks user a question based on users respose that response is then checked if it is valid or invalid and when verified
    #Program will either, raise errors, display a paticular teams stats, or end the program
    #Lastly upon the program completing user will be redirected to the main menu were user can continue checking
    #Team stats or finally quit or end the program
    while True:
        print(" " * 44, "BASKETBALL TEAM STATS TOOL", "\n")
        print("-" * 53, "MENU", "-" * 55, "\n")
        try:
            select_team = int(input("""Please select what you would like to do by entering 1 or 2:
            \n (1). Display Team Stats \n (2). Quit \n >>> """))
            if select_team >= 3 or select_team < 1:
                raise Exception("ERROR! You choose a number that is neither 1 or 2")
        except ValueError:
            print("ERROR! Invalid entry what you entered is not a number")
        except Exception as err:
            print(err)
        else:
            #Checks user input and sees if it is ethier a 1 or 2
            #If input is a 1 the user is then able to choose which team stats he/she will like to view
            #As long as they are valid options
            if select_team == 1:
                try:
                    team = int(input("""Please select one of the 3 teams available:
                    \n (1). Panthers \n (2). Bandits \n (3). Warriors \n >>> """))
                    if team >= 4 or team < 1:
                        raise Exception("ERROR! You choose a number that is neither 1, 2, or 3")
                except ValueError:
                    print("ERROR! Invalid entry what you entered is not a number")
                except Exception as err:
                    print(err)
                else:
                    if team == 1:
                        print_stats('Panthers', panthers, exp_panthers, inexp_panthers, panthers_heights, panthers_guardians)
                        # Redirects user to main menu
                        want_continue = input("Press ENTER to continue.....")
                        if want_continue == "":
                            continue
                    elif team == 2:
                        print_stats('Bandits', bandits, exp_bandits, inexp_bandits, bandits_heights, bandits_guardians)
                        # Redirects user to main menu
                        want_continue = input("Press ENTER to continue.....")
                        if want_continue == "":
                            continue
                    elif team == 3:
                        print_stats('Warriors', warriors, exp_warriors, inexp_warriors, warriors_heights, warriors_guardians)
                        # Redirects user to main menu
                        want_continue = input("Press ENTER to continue.....")
                        if want_continue == "":
                            continue
            #Checks user input and sees if it is ethier a 1 or 2
            #If input is 2 user will end the program and be accompanied with a closing message
            elif select_team == 2:
                print("Closing stats tool, see you next time!")
                break
