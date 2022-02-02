'''Rules-------------------------------
1.Player has 6 chance to guess the word or a letter(in or out)
2.After every in letter or guess, player has to guess which letter is out.
3.Player has to finish the game before the hanged man die.
Also: I got the hangman strings from net hehe.'''
from operator import index
import random
continuegame = 1
hangman = ['''
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
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra '.upper()).split()

alphabet = "Included letters: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

class Words:
    def __init__(self, word):
        self.word = [x for x in word]
        self.length = len(word)
        self.correctguessed = [" "]*self.length
    @staticmethod
    def show(randind): ###shows the hangman
        print(hangman[randind])
    @staticmethod
    def resetABC():
        alphabet = "In Game Letters: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
        return alphabet
    def showspaces(self):
        self.guessed = "The Word is: |"
        for a in range(self.length):
            self.guessed = self.guessed + self.correctguessed[a] + "|"
        self.spaces = [(" "*13)+" _"*self.length, self.guessed, (" "*13)+" ¯"*self.length]
        for x in self.spaces:
            print(x)
        for x in alphabet:
            print(x, " ", end="")
        print()

random.shuffle(words)
for lap in words:
    theword = Words(f"{lap}")
    chances = 6
    mod = 0 #0 = in, 1 = out
    while chances != 0:
        theword.show(6-chances)
        theword.showspaces()
        print(f"Chances: {chances}")
        if " " not in theword.correctguessed:
            theword.show(6-chances)
            theword.showspaces()
            print("YOU WIN! HELAL KEEKKKKEEEE")
            break
        if mod == 0:
            takeinput = str(input("Type a letter which you think the word --HAS--\n"))
        elif mod == 1:
            takeinput = str(input("Type a letter which you think the word --HAS NOT--\n"))
        try:
            assert takeinput in alphabet
            if mod == 0:
                if takeinput in theword.word:
                    indexes = [x for x in range(len(theword.word)) if theword.word[x] == takeinput]
                    alphabet.remove(takeinput)
                    for a in indexes:
                        theword.correctguessed[a] = takeinput
                    mod = 1 
                else:
                    alphabet.remove(takeinput)
                    chances = chances - 1
                    mod = 1 
                continue
            elif mod == 1:
                if takeinput not in theword.word:
                    alphabet.remove(takeinput)
                    mod = 0
                else:
                    chances = chances - 1
                    mod = 0
                    
        except AssertionError:
            print("Choose a correct letter in correct form (capital).")
            continue
    
    if chances == 0:
        theword.correctguessed = theword.word
        theword.show(6-chances)
        theword.showspaces()
        print(f"HAHA! You fucking loser. It was {theword.word}")
    A = input("Do you want to play again? (Yes / No)\n")
    if A == "No" or A == "no":
        break
    else:
        alphabet = Words.resetABC()
    
######### write guessing system
#everything works completely fine more test




