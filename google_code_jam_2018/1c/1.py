from sys import stdin,stdout
from collections import defaultdict
class Trie:
    def __init__(self):
        self.root = defaultdict()
        self.ans = ""

    def insert(self,word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter,{})
        current.setdefault("_end")
    def find(self,start,size,level):
        if level ==size:
            return False
        for i in table[level]:
            if i not in start:
                self.ans+=i
                return True
        for j in start:
            self.ans+=j
            if not self.find(start[j],size,level+1):
                self.ans = self.ans[:-1]
            else:
                return True
            
    def find_start(self,size):
        for i in table[0]:
            self.ans = i
            if self.find(self.root[i],size,1):
                curr_size = len(self.ans)
                if curr_size!=size:
                    for j in xrange(curr_size,size):
                        self.ans+=table[j].keys()[0]
                return self.ans
        return "-"
for _ in xrange(int(stdin.readline())):
    n,l = map(int,stdin.readline().split())
    mytrie = Trie()
    table = [defaultdict() for i in xrange(l)]
    for i in xrange(n):
        word = stdin.readline()[:-1]
        mytrie.insert(word)
        for j in xrange(l):
            table[j].setdefault(word[j],None)
    ans = mytrie.find_start(l)
    stdout.write("Case #%d: %s\n"%(_+1,ans))
