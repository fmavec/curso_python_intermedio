""" Final Challenge: Hangman Game """

# Game class
from game import Game
import os

def main():
    game = Game()
    word = game.get_random_word()
    lengh = len(word) - 1
    found = False
    hidden_word = ['_'] * lengh
    tries = 0

    print("Welcome to Hangman Game")

    while not found:
        print(hidden_word)

        if tries >= 7:
            print("YOU LOSE!!!")
            print(hidden_word)
            print(f'The word was: {word}')
            print(f'intentos: {tries}')
            break

        user_letter = input("Enter a letter: ")
        if len(user_letter) != 1:
            os.system('clear')
            continue

        result = Game.is_correct(user_letter, word)

        if result == '_':
            os.system('clear')
            tries += 1
            continue
        else:
            for index in result:
                hidden_word[index] = user_letter

        try:
            hidden_word.index('_')
            os.system('clear')
        except ValueError:
            print("YOU WIN!!!")
            print(hidden_word)
            print(f'The word is: {word}, adivinaste en {tries} intentos')
            found = True

        print(f'intentos: {tries}')


if __name__ == '__main__':
    main()
""" Game class with methods to help play Hangman """

# random to select random word
import random

class Game:

    def __init__(self):
        """ open file with words """
        self.words = []
        with open('./files/data.txt', mode='r', encoding='utf-8') as file:
            for word in file:
                self.words.append(word)


    def get_random_word(self):
        """ choose and return a random word """
        words_with_accents = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
        word = lambda words: random.choice(self.words)
        random_word = word(self.words)

        for letter in random_word:
            if letter in words_with_accents:
                new_letter = words_with_accents[letter]
                random_word = random_word.replace(letter, new_letter)

        return random_word


    @staticmethod
    def is_correct(user_letter, word):
        """ return indices where user_letter is in word """
        indices = [index for index, value in enumerate(word) if value == user_letter]

        if indices:
            return indices

        return '_'
