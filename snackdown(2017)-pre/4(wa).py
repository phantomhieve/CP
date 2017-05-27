def answer(y_start,y_end,y1_start,y1_end,x_start,x_end,x1_start,x1_end):
    if(y_start==y1_start==y1_end):
        if(x_start<=x1_start and x1_start<=x_end): 
            print "yes"
        elif(x1_start<=x_start and x_start<=x1_end):
            print "yes"
        else:
            print "no"
    elif(y1_start==y1_end):
        print "no"
    else:
        if(x_start==x_end and x_start==x1_start):
            if(y_start>=y1_start and y_start<=y_end):
                print "yes"
            else:
                print "no"
        if(x_start==x1_start or x_end==x1_start):
            if(y1_start==y_start or y1_end==y_start):
                print "yes"
            else:
                "no"
        else:
            print "no"            
for _ in range(input()):
    x_start,y_start,x_end,y_end=map(int,raw_input().split())
    x1_start,y1_start,x1_end,y1_end=map(int,raw_input().split())
    x_start,x_end=min(x_start,x_end),max(x_start,x_end)
    x1_start,x1_end=min(x1_start,x1_end),max(x1_start,x1_end)
    y_start_y_end=min(y_start,y_end),max(y_start,y_end)
    y1_start,y1_end=min(y1_start,y1_end),max(y1_start,y1_end)
    if(y_start==y_end):
        answer(y_start,y_end,y1_start,y1_end,x_start,x_end,x1_start,x1_end)
    else:
        answer(x_start,x_end,x1_start,x1_end,y_start,y_end,y1_start,y1_end)
        
            
