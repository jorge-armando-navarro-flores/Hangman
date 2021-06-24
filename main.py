import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
lives = 6
for letter in chosen_word:
  display.append('_')

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()


  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = guess
    
  if guess not in display:
    lives -= 1

  print(' '.join(display))
  print(stages[lives])

  if '_' not in display:
    end_of_game = True
    print("You win")
  if lives == 0:
    end_of_game = True
    print("You lose")
  
  
