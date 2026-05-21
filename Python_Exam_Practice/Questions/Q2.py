import random

def Character_Generator():
    
    dic = {"Char_ID":"", "Char_ATK":"", "Char_DEF":"", "Char_SPD":""}

    # Variables
    new_ATK = random.randint(0,10)
    new_DEF = random.randint(0,10)
    new_SPD = random.randint(0,10)
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Random ID
    new_ID = []
    while True:
        randLetter = letters[random.randint(0,25)]
        new_ID.append(randLetter)

        if len(new_ID) == 8:
            break
        
    new_ID = "".join(new_ID)

    # Add to dictionary
    dic["Char_ID"] = new_ID
    dic["Char_ATK"] = new_ATK
    dic["Char_DEF"] = new_DEF
    dic["Char_SPD"] = new_SPD
    
    return dic

print(Character_Generator())

def Team_Builder(team_size):
    newTeam = []
    
    # Create team
    while True:
        character = Character_Generator()
        Char_IDs = [character.values()[0]]
        newTeam.append(character)
        if len(newTeam) == int(team_size):
            break
    
    for i in range(len(newTeam)):
        if character.values()[0] == Char_IDs[-1]:
            continue

    return newTeam

print(Team_Builder(4))