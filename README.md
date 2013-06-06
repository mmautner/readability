Readability
====================

A collection of functions that measure the readability of a given body of text. I'd
recommend checking out the wikipedia articles below--most of the metrics estimate 
the grade level required to comprehend a given block of text and may return odd results
on small snippets of text.

To get up and running you'll need [NLTK](http://nltk.org/) and will need the punkt
data set:

    shell$ pip install nltk
    shell$ python
    >>import nltk
    >>nltk.download('punkt')

Demo:

    shell$ python readability.py
    Test text:
    "We are close to wrapping up our 10 week Rails Course. This week we will cover a handful of topics commonly encountered in Rails projects. We then wrap up with part 2 of our Reddit on Rails exercise!  By now you should be hard at work on your personal projects. The students in the course just presented in front of the class with some live demos and a brief intro to to the problems their app were solving. Maybe set aside some time this week to show someone your progress, block off 5 minutes and describe what goal you are working towards, the current state of the project (is it almost done, just getting started, needs UI, etc.), and then show them a quick demo of the app. Explain what type of feedback you are looking for (conceptual, design, usability, etc.) and see what they have to say.  As we are wrapping up the course you need to be focused on learning as much as you can, but also making sure you have the tools to succeed after the class is over."

    ARI:  7.2164516129
    FleschReadingEase:  88.9553
    FleschKincaidGradeLevel:  5.3235
    GunningFogIndex:  9.1355
    SMOGIndex:  8.19615242271
    ColemanLiauIndex:  6.7804
    LIX:  35.2666666667
    RIX:  3.1

The following readability metrics are included in readability.py:

1. http://en.wikipedia.org/wiki/Automated_Readability_Index
2. http://en.wikipedia.org/wiki/SMOG
3. http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_Grade_Level#Flesch.E2.80.93Kincaid_Grade_Level
4. http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test#Flesch_Reading_Ease
5. http://en.wikipedia.org/wiki/Coleman-Liau_Index
6. http://en.wikipedia.org/wiki/Gunning-Fog_Index

Largely lifted from:

    https://github.com/nltk/nltk_contrib/tree/master/nltk_contrib/readability

SMOG index appears to perform most accurately.
