import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
  display.append('_')
while '_' in display:
  guess = input("Guess a letter: ").lower()


  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = guess
  print(display)
