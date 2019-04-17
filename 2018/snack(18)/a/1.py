from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
left ,right = ['d','f'],['j','k']
for _ in xrange(int(cin())):
    store,ans = dict(),0
    for w in xrange(int(cin())):
        word = raw_input()
        if word in store:
            ans+= store[word]/2
        else:
            ans_ = 2
            for i in xrange(1,len(word)):
                first,second =False,False
                ans_+=2
                if word[i] in left: first = True
                if word[i-1] in left: second = True
                if first == second: ans_+=2
            store[word] = ans_
            ans+=ans_
    cout("%d\n"%(ans))
