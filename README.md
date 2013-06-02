Readability
====================

A collection of functions that measure the readability of a given body of text.

To get up and running you'll need [NLTK](http://nltk.org/) and will need the punkt
data set:

    shell$ pip install nltk
    shell$ python
    >>import nltk
    >>nltk.download()
    {{And then proceed to download the punkt dataset}}

Demo:

    shell$ python readability.py

The following readability metrics are implemented in readability.py:

1. http://en.wikipedia.org/wiki/Automated_Readability_Index
2. http://en.wikipedia.org/wiki/SMOG
3. http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_Grade_Level#Flesch.E2.80.93Kincaid_Grade_Level
4. http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test#Flesch_Reading_Ease
5. http://en.wikipedia.org/wiki/Coleman-Liau_Index
6. http://en.wikipedia.org/wiki/Gunning-Fog_Index

Largely lifted from:

https://github.com/nltk/nltk_contrib/tree/master/nltk_contrib/readability

SMOG index appears to perform most accurately.
