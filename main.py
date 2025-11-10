HANGMAN_PICS = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
       |\\  |
           |
           |
    =========''','''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========''','''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========''','''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========='''
]


class HangmanGame:
    def __init__(self, secret_word):
        self.secret_word = secret_word.upper()
        self.lives = 6
        self.guessed_letters = set()
        self.word_letters = set(self.secret_word)


    def display(self):
        print(HANGMAN_PICS[6 - self.lives])
        print(self.guessed_letters - self.word_letters)
        display_word = [letter if letter in self.guessed_letters else '_' for letter in self.secret_word]
        print(' '.join(display_word))

    def make_guess(self, letter):
        letter = letter.upper()
        if len(letter) == 1:
            if letter not in self.guessed_letters:
                self.guessed_letters.add(letter)
                if letter not in self.word_letters:
                    self.lives -= 1
                else:
                    print("Вы отгадали букву")
            else:
                print("Вы уже назвали эту букву")
        else:
            print("Введите только 1 букву.")

    def is_won(self):
        return self.word_letters <= self.guessed_letters

    def is_lost(self):
        return self.lives == 0


secret = "Python"

game = HangmanGame(secret)

while True:
    game.display()

    if game.is_won():
        print("Поздравляю вы выиграли!")
        break
    if game.is_lost():
        print(f"Вы проиграли. Было загадано слово: {game.secret_word}")
        break


    user_letter = input("Введите букву: ")
    game.make_guess(user_letter)


