# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:11:24 2021
@author: Ainish
"""

import random

def getWordRepository():
    """Function that reads words from a repository and returns a list 
    of words"""
    
    Repository =  ['Jazz', 'Rock', 'Popular', 'Blues', 'Country']    
    return Repository

def getWordRepository2():
    File    = open('HangmanWords.txt','r')
    Words   = File.readlines()
    return Words
    
def RandomWord():
    #Repository = getWordRepository()
    Repository = getWordRepository2()
    return Repository[(random.randint(0, len(Repository)-1))].lower().strip('\n')

def AllowedCharacters():
    return set('abcdefghijklmnopqrstuvwxyz')

class Game():
    def __init__(self, Word=RandomWord()):
        self.GameWord = Word
        self.AllowedCharacters = AllowedCharacters()
        self.guesses = 8
        self.repeats = 8
        self.lettersguessed = []
        self.currentguess  = None
        self.result = 'in progress'
        
        return
    
    def setGuess(self, letter):
        self.currentguess = letter.lower()        
        return
    
    def checkGuess(self):
        if self.currentguess in self.lettersguessed:
            self.repeats += -1
            print('You have already guessed',self.currentguess)
            return
            
        if self.currentguess in self.GameWord:
            msg = 'Good Guess!'
        else:
            msg = self.currentguess + ' is not in the word, you lost a guess' 
            self.guesses += -1
        self.lettersguessed.append(self.currentguess)
        print(msg)
        
        
        
    def checkGame(self):
        for letter in self.GameWord:
            if letter not in self.lettersguessed:          
                if self.guesses == 0:
                    self.result = 'You Lost'        
                if self.repeats == 0:
                    self.result = 'Game Terminated'
                return
        self.result = 'You Won'
    
    def ShowAvailableLetters(self):
        characters = list(self.AllowedCharacters - set(self.lettersguessed))
        characters.sort()
        print(" ".join(characters))
        return

    def ShowProgress(self):
        gameString = ''
        for letter in self.GameWord:
            if letter in self.lettersguessed:
                gameString = gameString+" "+letter+" "
            else:
                gameString = gameString+' _ '
        print(gameString)






Hangman = Game()

print('\n-----Lets Play! The word you have to guess has', len(Hangman.GameWord), 'letters-----\n')
Hangman.ShowProgress() 

while Hangman.result == 'in progress':
       
    print('\n------------------------------------\nNumber of Guesses left', Hangman.guesses)    
    print('Make your guess')
    guess = input().lower()
    Hangman.setGuess(guess)
    Hangman.checkGuess()    
    Hangman.checkGame()
    Hangman.ShowProgress() 
    
    
print(Hangman.result, Hangman.GameWord)



