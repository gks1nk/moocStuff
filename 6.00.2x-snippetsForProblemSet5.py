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

#this snippet demonstrates looping a file, line by line
with open('t.ini') as f:
   for line in f:
       print line
       if 'str' in line:
          break
       
#this is the simple depth first example from the lecture
#this will need to be modified to work with problem set 5-3
def DFS(graph, start, end, path = []):
   # Assumes graph is a Digraph
   # Assumes start and end are nodes in graph
   path = path + [start]
   print 'Current dfs path:', printPath(path)
   if start == end:
      return path
   for node in graph.childrenOf(start):
      if node not in path: # Avoid cycles
         newPath = DFS(graph,node,end,path)
         if newPath != None:
            return newPath
   return None
