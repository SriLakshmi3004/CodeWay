import random


# Define quiz questions and answers
quiz_questions = {
    "How many years old is the world’s oldest piece of chewing gum?": "Chewing gum",
    "What is the largest mammal in the world?": "Blue whale",
    "What’s the smallest country in the world?": "The Vatican",
    "What is the chemical symbol for water?": "H2O",
    "How many continents are there?": "7"
}

# Function to present quiz questions, evaluate user's answer, and provide feedback
def play_quiz(questions, players):
    for player in players:
        player.score = 0
    
    print("Welcome to the Quiz Game!")
    print("You will be asked {} questions.".format(len(questions)))
    print("Please type your answers in lowercase.\n")
    
    # Shuffle questions to make it more engaging
    shuffled_questions = list(questions.items())
    random.shuffle(shuffled_questions)
    
    for question, answer in shuffled_questions:
        print("\nQuestion: {}".format(question))
        for player in players:
            user_answer = input("{}'s answer: ".format(player.name))
            if user_answer.lower() == answer.lower():
                print("Correct!")
                player.score += 1
            else:
                print("Incorrect! The correct answer is: {}".format(answer))
    
    print("\nQuiz Complete!")
    print("Final Scores:")
    for player in players:
        print("{}: {}/{}".format(player.name, player.score, len(questions)))

# Function to ask user if they want to play again
def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ")
        if again.lower() == "yes":
            return True
        elif again.lower() == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

# Main function to run the quiz game
def main():
    players = []
    num_players = 3
    for i in range(num_players):
        name = input("Enter Player {}'s name: ".format(i+1))
        players.append(Player(name))
    
    while True:
        play_quiz(quiz_questions, players)
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

