"""
premier test sur la notion de tuples:
"""

tuple = 45, #initialisation exemple 1 pouvant etre ecrit tuple = (45,)
print(tuple)

list = ["teste", 23, "essaie"]

for tuples in enumerate(list):
    print(tuples) #retourne (index,value)

"""
autres utilisations

"""
def get_player_position():
    x = 45
    y = 54
    return x,y

# initialisation position
cordx = 0
cordy = 0

print("cordonnées de départ x: {} et y: {}".format(cordx,cordy))

(cordx,cordy) = get_player_position()

print("cordonnées  x: {} et y: {}".format(cordx,cordy))



print(get_player_position()[0]) # type de lecture par index