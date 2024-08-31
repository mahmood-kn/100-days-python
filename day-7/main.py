import random
from hangman_art import stages,logo
from hangman_words import word_list
import os
print(logo)
chosen_word=random.choice(word_list)
display=[]
guessed=[]
word_length=len(chosen_word)
for _ in range(word_length):
  display.append('_')
lives=6
end_of_game=False
while  not end_of_game:
  guess=input('Guess a letter: ').lower()
  os.system('clear')
  for i in range(word_length):
    letter=chosen_word[i] 
    if letter== guess:
      display[i]=guess
  if guess in guessed:
    print(f'You already guessed {guess}')
  if guess not in chosen_word and guess not in guessed: 
    guessed.append(guess)
    lives-=1
    print(f'You guessed {guess}, that is not in the word, you lose a life.')
    if lives==0:
      print(f'You lost, the word was {chosen_word}')
      end_of_game=True

  print(f'{' '.join(display)}')
  if '_' not in display:
    end_of_game=True
    print('You win')

  print(stages[lives])
  
    