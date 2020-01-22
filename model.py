##@Fiona Yonkman 2019
##Hangman class Model which generates a random word from text files based on
##difficulty and handles logic of entered letter by user

import random

class Model:
    #constructor
    def __init__(self):
        #string that holds error messages
        self.errortext=None
        #holds indices of correct letters in the generated word
        self.indices=[]
        #array of letters guessed that are in the generated word
        self.correctLetters=[]
        #integer that indicates part of hangman to be drawn
        self.gameState=0
        #letters guessed by user that are not in generated word
        self.wrongLetters=[]
        #randomly-generated word for user to guess in game
        self.word=''

    #generates the word based on the difficultly selected by user
    #chooses a text file based on length of words desired
    def generateWord(self,difficulty):
        self.word =random.choice(
                        open("words/{}.txt".format(difficulty)).read().split())
        while len(self.word)>12 or len(self.word)<3:
            self.word =random.choice(
                        open("words/{}.txt".format(difficulty)).read().split())
        self.numLetters = len(self.word)

    #updates Model's attributes based on inputted letter
    def testLetter(self,letter):
        letter = letter.lower()
        if len(letter) == 1:
            if letter.isalpha():
                #if the letter has not already been guessed
                if letter not in self.wrongLetters and (letter
                                            not in self.correctLetters):
                    self.errortext=None
                    word=self.word
                    if letter in word:
                        #find indices in word that guessed letter is at
                        for index, char in enumerate(word):
                            if char == letter:
                                self.indices.append(index)
                                self.correctLetters.append(char)
                    #letter is not in generated word
                    else:
                        self.gameState+=1
                        self.wrongLetters.append(letter)
                else:
                    self.errortext="Please guess a new letter."
            else:
                self.errortext="Please input an English letter."
        else:
            self.errortext="Please input a single character."
