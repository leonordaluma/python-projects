import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display += "_"
print(chosen_word)
print(display)
length = len(chosen_word)

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for letter in range(0, len(chosen_word)):
      if guess == chosen_word[letter]:
        display[letter] = guess
    print(display)

print("You win")
