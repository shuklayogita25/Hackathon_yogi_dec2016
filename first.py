__author__ = 'Yogita Shukla'
def word_count(word , string):
	count = 0
	lst = string.split()
	for i in lst:
		if i == word:
			count +=1
			lst.remove(i)
	if count > 0:
		print "number of times word occured :" +str(count)+ " times"
		print "after removal of word: "+" ".join(lst)
		lst.append(((" ")+word)*count)		
		print "word append: "+" ".join(lst)
	else:
		print word+"does not exist in "+string

def main():

        word = raw_input("enter word ")
        string = raw_input("enter string ")
        if len(word) < 1 or len(string) <1:
            print ("  ")
        word_count(word=word, string=string.lower())


if __name__ =='__main__':
    main()
