for _ in range(input()):
    string=raw_input()
    s,m,s_total,m_total=False,False,0,0
    for i in string:
        if(i=='s'):
            s_total+=1
            s=True
        else:
            m_total+=1
            m=True
        if(s and m):
            s_total-=1
            m=False;s=False
    if(s_total<m_total):
        print "mongooses"
    elif(s_total>m_total):
        print "snakes"
    else:
        print "tie"
        
            
            
        
