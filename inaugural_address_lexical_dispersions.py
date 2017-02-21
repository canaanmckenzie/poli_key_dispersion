#Canaan McKenzie
#NLTK practice - Lexical dispersion charts of Inaugural Address Corpus 1789 - 2009
#MIT license

import nltk
from nltk.book import *

#TODO: expand imports from nltk.books to any source

def main():
    
    map_keyword(userInputKeywords())
    

def map_keyword(user_input_list):
    #create dispersion plot of keywords of interest
    text4.dispersion_plot(user_input_list)
    
def userInputKeywords():
    return nltk.word_tokenize(input("Enter keywords: "))
    #returns str list
    
main()
