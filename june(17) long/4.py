for _ in range(input()):
    l=input()
    array=list(map(int,raw_input().split()))
    minus,m_sum,size=[],0,0
    for i in range(l):
        if(array[i]>=0):
            m_sum+=array[i];size+=1
        else:
            minus.append(array[i])
    minus.sort(reverse=True)
    ans,t_sum=m_sum*size,0
    for i in range(len(minus)):
        t_sum+=minus[i]
        if((t_sum+m_sum)*(size+1)>=ans):
            size+=1;ans=(t_sum+m_sum)*size
        else:
            ans+=sum(minus[i:])
            break
    print ans
        
