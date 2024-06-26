
# Secret Santa:
# Given a list of players:
# each player gives gift once
# each player receives gift once
# player can not give or receive for themselves
# selection must be random


# Example input=["a","b","c","d","e"]
# Examples output=[["a","c"],["b","d"]]






import random

def go(players):
    # Ensure each player is unique
    players = list(set(players))
    
    # Make sure no one gives or receives a gift to/from themselves
    givers = players[:]
    receivers = players[:]
    
    random.shuffle(givers)
    random.shuffle(receivers)
    
    # Ensure no player gives a gift to themselves
    while any(g == r for g, r in zip(givers, receivers)):
        random.shuffle(receivers)
    
    return list(zip(givers, receivers))

player = ["nilam", "pooja", "aarti", "nikita"]

series = go(player)
print(series)
