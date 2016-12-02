__author__ = 'Yogita Shukla'

import re

def word_count(word , string):
    count = 0
    for i in re.finditer(word , string):
        count +=1
    if count > 0:
        print "Word " +word+ "  occured "+str(count)+ " times"
        string = re.sub(word, "", string)
        print "after removal of word"+string
        print "word append"+string+((" ")+word)*count
    else:
        print word+"does not exist in"+string

def main():

        word = raw_input("enter word ")
        string = raw_input("enter string ")
        if len(word) < 1 or len(string) <1:
            print ("  ")
        word_count(word=word, string=string.lower())


if __name__ =='__main__':
    main()