"""
Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

"""
player1 = input("Please enter your name player one: ")
player2 = input("Please enter your name player two: ")
game = input("Do you want to play rock, paper, scissors(y/n)? ").lower()
while True:
    if game == 'n':
        break
    else:
        first_input = input(
            "What is your choice? Rock, paper, or Scissors? ").lower()
        second_input = input(
            "What is your choice? Rock, paper, or Scissors? ").lower()
        if first_input == 'rock' and second_input == 'scissors' or \
                first_input == 'scissors' and second_input == 'paper' or \
                first_input == 'paper' and second_input == 'rock':
            print("Player1 won")
        else:
            print("Player2 won")
        game = input(
            "Do you want to play rock, paper, scissors(y/n)? ").lower()
