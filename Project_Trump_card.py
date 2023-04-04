import requests
import random

#step 1 - generate a random number between 1 and 151 as pokID

def pok_number1():
    pok = random.randint(1,151)
    return pok

#step2 - using the pokemon API - get pokemon based on its ID

pokemon_number = pok_number1()
url = 'http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()

#Step 3 - Generate a dictionary that contain the retuned
#pok name, ID, weight and height

print('Name of the pokemon is:',pokemon['name'])
print('height of the pokemon is:',pokemon['height'])
print('weight of the pokemon is:',pokemon['weight'])

player_dict1 = {'Name':pokemon['name'],'ID':pokemon_number,'Height':pokemon['height'],'Weight':pokemon['weight']}

print(player_dict1)

#Step 4 - Create another recursive random number generator function
def pok_number2():
    pok2 = random.randint(1,151)
    if pok2 == pokemon_number:
        pok2 = pok_number2()
    return pok2

pokemon_number2 = pok_number2()
url2 = 'http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number2)

response2 = requests.get(url2)
print(response2)

pokemon2 = response2.json()

# Step 5 - Generate dictionary that contain the retuned parameters for the 2nd player
#pok name, ID, weight and height

print('Name of the pokemon is:',pokemon2['name'])
print('height of the pokemon is:',pokemon2['height'])
print('weight of the pokemon is:',pokemon2['weight'])

player_dict2 = {'Name':pokemon2['name'],'ID':pokemon_number2,'Height':pokemon2['height'],'Weight':pokemon2['weight']}

print(player_dict2)

#Step 6 - Pick a stat to compare

parameter = input('Which feature to compare? ')

#Step 7 - Define the function to compare the picked parameter to decide which player won th game

def game(dict1,dict2,parameter):
    if dict1[parameter]>dict2[parameter]:
        result = 'Player 1 won'
    else:
        result = 'Player 2 won'
    return result

#Step 8 - Print the results

print('The result of the game is :',game(player_dict1,player_dict2,parameter))


