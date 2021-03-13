from collections import defaultdict

# lose = ['scissors', 'rock', 'paper', 'spock', 'spock', 'lizard', 'lizard', 'paper', 'scissors', 'scissors' 'lizard']

# wins = ['rock', 'paper', 'scissors', 'rock', 'paper', 'rock', 'spock', 'lizard', 'lizard', 'spock', 'spock']


wins = ['scissors', 'rock', 'paper', 'lizard', 'spock',
        'scissors', 'lizard', 'paper', 'spock', 'rock']
lose = ['paper', 'lizard', 'rock', 'spock', 'scissors',
        'lizard', 'paper', 'spock', 'rock', 'scissors']

dic = {}
for x, y in zip(wins, lose):
    dic.setdefault(x, []).append(y)

print(dic)
print(set(dic))
