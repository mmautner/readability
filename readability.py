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

def analyze_text(text):
    words = getWords(text)
    charCount = getCharacterCount(words)
    wordCount = len(words)
    sentenceCount = len(get_sentences(text))
    syllableCount = count_syllables(words)
    complexwordsCount = countComplexWords(text)
    averageWordsPerSentence = wordCount/sentenceCount
    
    analyzedVars = {
        'words': words,
        'charCount': float(charCount),
        'wordCount': float(wordCount),
        'sentenceCount': float(sentenceCount),
        'syllableCount': float(syllableCount),
        'complexwordCount': float(complexwordsCount),
        'averageWordsPerSentence': float(averageWordsPerSentence)
    }
    return analyzedVars

def ARI(text):
    analyzedVars = analyze_text(text)
    score = 4.71 * (analyzedVars['charCount'] / analyzedVars['wordCount']) + 0.5 * (analyzedVars['wordCount'] / analyzedVars['sentenceCount']) - 21.43
    return score
    
def FleschReadingEase(text):
    score = 0.0
    analyzedVars = analyze_text(text)
    score = 206.835 - (1.015 * (analyzedVars['averageWordsPerSentence'])) - (84.6 * (analyzedVars['syllableCount']/ analyzedVars['wordCount']))
    return round(score, 4)
    
def FleschKincaidGradeLevel(text):
    analyzedVars = analyze_text(text)
    score = 0.39 * (analyzedVars['averageWordsPerSentence']) + 11.8 * (analyzedVars['syllableCount']/ analyzedVars['wordCount']) - 15.59
    return round(score, 4)
    
def GunningFogIndex(text):
    analyzedVars = analyze_text(text)
    score = 0.4 * ((analyzedVars['averageWordsPerSentence']) + (100 * (analyzedVars['complexwordCount']/analyzedVars['wordCount'])))
    return round(score, 4)

def SMOGIndex(text):
    analyzedVars = analyze_text(text)
    score = (math.sqrt(analyzedVars['complexwordCount']*(30/analyzedVars['sentenceCount'])) + 3)
    return score

def ColemanLiauIndex(text):
    analyzedVars = analyze_text(text)
    score = (5.89*(analyzedVars['charCount']/analyzedVars['wordCount']))-(30*(analyzedVars['sentenceCount']/analyzedVars['wordCount']))-15.8
    return round(score, 4)

def LIX(text):
    analyzedVars = analyze_text(text)
    longwords = 0.0
    for word in analyzedVars['words']:
        if len(word) >= 7:
            longwords += 1.0
    score = analyzedVars['wordCount'] / analyzedVars['sentenceCount'] + float(100 * longwords) / analyzedVars['wordCount']
    return score

def RIX(text):
    analyzedVars = analyze_text(text)
    score = 0.0
    longwords = 0.0
    for word in analyzedVars['words']:
        if len(word) >= 7:
            longwords += 1.0
    score = longwords / analyzedVars['sentenceCount']
    return score
        

if __name__ == "__main__":
    text = """We are close to wrapping up our 10 week Rails Course. This week we will cover a handful of topics commonly encountered in Rails projects. We then wrap up with part 2 of our Reddit on Rails exercise!  By now you should be hard at work on your personal projects. The students in the course just presented in front of the class with some live demos and a brief intro to to the problems their app were solving. Maybe set aside some time this week to show someone your progress, block off 5 minutes and describe what goal you are working towards, the current state of the project (is it almost done, just getting started, needs UI, etc.), and then show them a quick demo of the app. Explain what type of feedback you are looking for (conceptual, design, usability, etc.) and see what they have to say.  As we are wrapping up the course you need to be focused on learning as much as you can, but also making sure you have the tools to succeed after the class is over."""

    print 'ARI: ', ARI(text)
    print 'FleschReadingEase: ', FleschReadingEase(text)
    print 'FleschKincaidGradeLevel: ', FleschKincaidGradeLevel(text)
    print 'GunningFogIndex: ', GunningFogIndex(text)
    print 'SMOGIndex: ', SMOGIndex(text)
    print 'ColemanLiauIndex: ', ColemanLiauIndex(text)
    print 'LIX: ', LIX(text)
    print 'RIX: ', RIX(text)

