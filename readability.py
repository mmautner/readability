#!/usr/bin/env python

import math
import nltk
from nltk.tokenize import RegexpTokenizer
import syllables_en

TOKENIZER = RegexpTokenizer('(?u)\W+|\$[\d\.]+|\S+')
SPECIAL_CHARS = ['.', ',', '!', '?']

def getCharacterCount(words):
    characters = 0
    for word in words:
        characters += len(word.decode("utf-8"))
    return characters
    
def getWords(text=''):
    words = []
    words = TOKENIZER.tokenize(text)
    filtered_words = []
    for word in words:
        if word in SPECIAL_CHARS or word == " ":
            pass
        else:
            new_word = word.replace(",","").replace(".","")
            new_word = new_word.replace("!","").replace("?","")
            filtered_words.append(new_word)
    return filtered_words

def get_sentences(text=''):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences

def count_syllables(words):
    syllableCount = 0
    for word in words:
        syllableCount += syllables_en.count(word)
    return syllableCount

#This method must be enhanced. At the moment it only
#considers the number of syllables in a word.
#This often results in that too many complex words are detected.
def countComplexWords(text=''):
    words = getWords(text)
    sentences = get_sentences(text)
    complex_words = 0
    found = False
    cur_word = []
    
    for word in words:          
        cur_word.append(word)
        if count_syllables(cur_word)>= 3:
            
            #Checking proper nouns. If a word starts with a capital letter
            #and is NOT at the beginning of a sentence we don't add it
            #as a complex word.
            if not(word[0].isupper()):
                complex_words += 1
            else:
                for sentence in sentences:
                    if str(sentence).startswith(word):
                        found = True
                        break
                if found: 
                    complex_words += 1
                    found = False
                
        cur_word.remove(word)
    return complex_words


class Readability:
    analyzedVars = {}

    def __init__(self, text):
        self.analyze_text(text)

    def analyze_text(self, text):
        words = getWords(text)
        charCount = getCharacterCount(words)
        wordCount = len(words)
        sentenceCount = len(get_sentences(text))
        syllableCount = count_syllables(words)
        complexwordsCount = countComplexWords(text)
        averageWordsPerSentence = wordCount/sentenceCount
        
        self.analyzedVars = {
            'words': words,
            'charCount': float(charCount),
            'wordCount': float(wordCount),
            'sentenceCount': float(sentenceCount),
            'syllableCount': float(syllableCount),
            'complexwordCount': float(complexwordsCount),
            'averageWordsPerSentence': float(averageWordsPerSentence)
        }

    def ARI(self):
        score = 4.71 * (self.analyzedVars['charCount'] / self.analyzedVars['wordCount']) + 0.5 * (self.analyzedVars['wordCount'] / self.analyzedVars['sentenceCount']) - 21.43
        return score
        
    def FleschReadingEase(self):
        score = 0.0
        score = 206.835 - (1.015 * (self.analyzedVars['averageWordsPerSentence'])) - (84.6 * (self.analyzedVars['syllableCount']/ self.analyzedVars['wordCount']))
        return round(score, 4)
        
    def FleschKincaidGradeLevel(self):
        score = 0.39 * (self.analyzedVars['averageWordsPerSentence']) + 11.8 * (self.analyzedVars['syllableCount']/ self.analyzedVars['wordCount']) - 15.59
        return round(score, 4)
        
    def GunningFogIndex(self):
        score = 0.4 * ((self.analyzedVars['averageWordsPerSentence']) + (100 * (self.analyzedVars['complexwordCount']/self.analyzedVars['wordCount'])))
        return round(score, 4)

    def SMOGIndex(self):
        score = (math.sqrt(self.analyzedVars['complexwordCount']*(30/self.analyzedVars['sentenceCount'])) + 3)
        return score

    def ColemanLiauIndex(self):
        score = (5.89*(self.analyzedVars['charCount']/self.analyzedVars['wordCount']))-(30*(self.analyzedVars['sentenceCount']/self.analyzedVars['wordCount']))-15.8
        return round(score, 4)

    def LIX(self):
        longwords = 0.0
        for word in self.analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = self.analyzedVars['wordCount'] / self.analyzedVars['sentenceCount'] + float(100 * longwords) / self.analyzedVars['wordCount']
        return score

    def RIX(self):
        score = 0.0
        longwords = 0.0
        for word in self.analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = longwords / self.analyzedVars['sentenceCount']
        return score
        

if __name__ == "__main__":
    text = """We are close to wrapping up our 10 week Rails Course. This week we will cover a handful of topics commonly encountered in Rails projects. We then wrap up with part 2 of our Reddit on Rails exercise!  By now you should be hard at work on your personal projects. The students in the course just presented in front of the class with some live demos and a brief intro to to the problems their app were solving. Maybe set aside some time this week to show someone your progress, block off 5 minutes and describe what goal you are working towards, the current state of the project (is it almost done, just getting started, needs UI, etc.), and then show them a quick demo of the app. Explain what type of feedback you are looking for (conceptual, design, usability, etc.) and see what they have to say.  As we are wrapping up the course you need to be focused on learning as much as you can, but also making sure you have the tools to succeed after the class is over."""

    rd = Readability(text)
    print 'ARI: ', rd.ARI()
    print 'FleschReadingEase: ', rd.FleschReadingEase()
    print 'FleschKincaidGradeLevel: ', rd.FleschKincaidGradeLevel()
    print 'GunningFogIndex: ', rd.GunningFogIndex()
    print 'SMOGIndex: ', rd.SMOGIndex()
    print 'ColemanLiauIndex: ', rd.ColemanLiauIndex()
    print 'LIX: ', rd.LIX()
    print 'RIX: ', rd.RIX()

