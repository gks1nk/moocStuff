def loadWords2():
2.     try:
3.         inFile = open(PATH_TO_FILE, 'r', 0)
4.     except IOError:
5.         print "The wordlist doesn't exist; using some fruits for now"
6.         return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
7.     line = inFile.readline()
8.     wordlist = string.split(line)
9.     print "  ", len(wordlist), "words loaded."
10.    return wordlist
