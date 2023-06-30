"""
5 players in a stack, stating that they want to play their preferred roles(1-5)
input 5 sets of numbers
then randomly assign each player to a role
end point should fill all the roles in the game(1, 2, 3, 4, 5)
"""
import random

def main():
    '''
    player_a = input("What roles does player A want?: ")
    player_b = input("What roles does player B want?: ")
    player_c = input("What roles does player C want?: ")
    player_d = input("What roles does player D want?: ")
    player_e = input("What roles does player E want?: ")
    '''
    player_a = {'name' : 'player_a', 'position' : ["pos1", "pos2"]}
    player_b = {'name' : 'player_b', 'position' : ["pos2", "pos3"]}
    player_c = {'name' : 'player_c', 'position' : ["pos4"]}
    player_d = {'name' : 'player_d', 'position' : ["pos2", "pos5"]}
    player_e = {'name' : 'player_e', 'position' : ["pos3", "pos4", "pos5"]}
    available_position = ["pos1", "pos2", "pos3", "pos4", "pos5"]
    
    print("This is a sample program of dota2 roles randomizer where there are predetermined preferred roles for each of the player.")
    print("In reality, player names and selected position have to come from somewhere else.")
    print("player_a prefer " + str(player_a['position']))
    print("player_b prefer " + str(player_b['position']))
    print("player_c prefer " + str(player_c['position']))
    print("player_d prefer " + str(player_d['position']))
    print("player_e prefer " + str(player_e['position']))
    print("\nResults:")
    
    
    '''
    check how many is the least pos, not 0
    check which ones have the least pos
    random 1 player out of that
    random 1 pos out of the player list
    remove the position from all others
    repeat 5 times
    '''
    available_player = [player_a, player_b, player_c, player_d, player_e]
    chosen_position = "none"
    
    for i in range (5):
        least_len = least_player_list(len(player_a['position']), len(player_b['position']), len(player_c['position']), len(player_d['position']), len(player_e['position']))
        while chosen_position == "none":
            chosen_player = random.choice(available_player)
            #print(chosen_player['name'])
            if len(chosen_player['position']) == least_len:
                chosen_position = random.choice(chosen_player['position'])
            else:
                if chosen_player['position'] == []:
                    chosen_position = random.choice(available_position)
                else:
                    chosen_position = "none"
            #print(chosen_position)
        print(chosen_player['name'] + ' selected position is ' + chosen_position)
        if str(chosen_position) in player_a['position']:
            player_a['position'].remove(str(chosen_position))
            #print(player_a['position'])
        if str(chosen_position) in player_b['position']:
            player_b['position'].remove(str(chosen_position))
            #print(player_b['position'])
        if str(chosen_position) in player_c['position']:
            player_c['position'].remove(str(chosen_position))
            #print(player_c['position'])
        if str(chosen_position) in player_d['position']:
            player_d['position'].remove(str(chosen_position))
            #print(player_d['position'])
        if str(chosen_position) in player_e['position']:
            player_e['position'].remove(str(chosen_position))
            #print(player_e['position'])
        available_player.remove(chosen_player)
        available_position.remove(str(chosen_position))
        chosen_position = "none"
        
      
       
def least_player_list(a, b, c, d, e):
    least_len = 5
    if least_len > a and a > 0:
        least_len = a
    if least_len > b and b > 0:
        least_len = b
    if least_len > c and c > 0:
        least_len = c
    if least_len > d and d > 0:
        least_len = d
    if least_len > e and e > 0:
        least_len = e
    return least_len
    
if __name__ == "__main__":
    main()
