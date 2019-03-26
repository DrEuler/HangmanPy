from __future__ import print_function
import random

#hangList = ["cow", "rat", "animal", "pizza"]
def hangman_display(guessed, secret):
    """ This sets up the hangman display"""
    #guessed = letters guessed so far
    #secret = full secret word/phrase
    secret_list = list(secret)
    guess_list = list(guessed)
    new_list = []
    for i in secret_list:
        if i in guess_list:
            new_list.append(i)
        elif i == ' ':
            new_list.append(i)
        else:
            new_list.append(len(i)*"-")
    
    return "".join(new_list)
 

def hangman(): #our theme is Harry Potter
    """Executes the main function for the game """
    secret_words_list = ['voldemort', 'hogwarts', 'harry potter', 'hermione', 'ron weasley', 'albus dumbledore', 'muggle', 'butterbeer', 'hogsmeade', 'death eaters', 'gryffindor', 'ravenclaw', 'hufflepuff', 'slytherin', 'buckbeak', 'dementors', 'quidditch', 'animagus', 'malfoy', 'magic', 'sirius black', 'the boy who lived', 'house elf']  
    answer = random.choice(secret_words_list)
    first_display = ''
    display = ''
    last_display = ''
    print("Welcome to our Hangman game! Our theme is Harry Potter! Everytime you guess, make sure to only input one character, and only guess letters!")
    for char in answer:
        if char == ' ':
            first_display += char
        else:
            first_display += '-'
    print(first_display)
    lives = 6
    condition = True
    guessed = []
    win = 'not yet'
    while condition == True:
        while lives > 0:
            guess = raw_input('Write your guess here:')
            guess = guess.lower()
            if len(guess) > 1:
                print('Oops! Your guess can only be one letter!')
                continue
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("Whoops! You can't use that character!")
                continue
            last_display = display
            display = ''
            
            correct = False
            for char in answer:
                if char in last_display:
                    display += char
                elif char in guess:
                    display += char
                    correct = True
                else:
                    if char == ' ':
                        display += ' '
                    else:
                        display += '-'

            if not correct:
                if guess in display:
                    print('Whoops! You already guessed this letter!')
                    print(' ')
                elif guess in guessed:
                    print('Whoops! You already guessed this letter!')
                    print(' ')
                else:
                    lives -= 1
                    guessed.append(guess)
            print('lives left:', lives)
            print('This is what you have guessed wrong:', guessed)
            print(display)
            if display == answer:
                win = 'You win!'
                print(win)
                break
        if win == 'You win!':
            condition = False
        else:
            print('You lose! The answer was:', answer)
            condition = False

hangman()#calls the function