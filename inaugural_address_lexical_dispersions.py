#Canaan McKenzie
#NLTK practice - Lexical dispersion charts of Inaugural Address Corpus 1789 - 2009
#MIT license


from nltk.books import *
import nltk

#TODO: expand imports from nltk.books to any source

def main():
    map_keyword(userInputKeywords())
main()

def map_keyword(user_input_list):
    
    text4.dispersion_plot(user_input_list)
    
def userInputKeywords():
    return user_input = nltk.word_tokenize(input("Enter keywords: "))
    #returns str list
    
